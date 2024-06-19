# pylint: disable=all
# Copyright (c) Facebook, Inc. and its affiliates.
import torch
from torch import nn
from torch.nn import functional as F
import torch.distributed as dist

def get_world_size() -> int:
    if not dist.is_available():
        return 1
    if not dist.is_initialized():
        return 1
    return dist.get_world_size()

class FrozenBatchNorm2d(nn.Module):
    """
    BatchNorm2d where the batch statistics and the affine parameters are fixed.

    It contains non-trainable buffers called
    "weight" and "bias", "running_mean", "running_var",
    initialized to perform identity transformation.

    The pre-trained backbone models from Caffe2 only contain "weight" and "bias",
    which are computed from the original four parameters of BN.
    The affine transform `x * weight + bias` will perform the equivalent
    computation of `(x - running_mean) / sqrt(running_var) * weight + bias`.
    When loading a backbone model from Caffe2, "running_mean" and "running_var"
    will be left unchanged as identity transformation.

    Other pre-trained backbone models may contain all 4 parameters.

    The forward is implemented by `F.batch_norm(..., training=False)`.
    """

    _version = 3

    def __init__(self, num_features, eps=1e-5):
        super().__init__()
        self.num_features = num_features
        self.eps = eps
        self.register_buffer("weight", torch.ones(num_features))
        self.register_buffer("bias", torch.zeros(num_features))
        self.register_buffer("running_mean", torch.zeros(num_features))
        self.register_buffer("running_var", torch.ones(num_features) - eps)
        self.register_buffer("num_batches_tracked", None)

    def forward(self, x):
        if x.requires_grad:
            # When gradients are needed, F.batch_norm will use extra memory
            # because its backward op computes gradients for weight/bias as well.
            scale = self.weight * (self.running_var + self.eps).rsqrt()
            bias = self.bias - self.running_mean * scale
            scale = scale.reshape(1, -1, 1, 1)
            bias = bias.reshape(1, -1, 1, 1)
            out_dtype = x.dtype  # may be half
            return x * scale.to(out_dtype) + bias.to(out_dtype)
        else:
            # When gradients are not needed, F.batch_norm is a single fused op
            # and provide more optimization opportunities.
            return F.batch_norm(
                x,
                self.running_mean,
                self.running_var,
                self.weight,
                self.bias,
                training=False,
                eps=self.eps,
            )

    def _load_from_state_dict(
        self,
        state_dict,
        prefix,
        local_metadata,
        strict,
        missing_keys,
        unexpected_keys,
        error_msgs,
    ):
        version = local_metadata.get("version", None)

        if version is None or version < 2:
            # No running_mean/var in early versions
            # This will silent the warnings
            if prefix + "running_mean" not in state_dict:
                state_dict[prefix + "running_mean"] = torch.zeros_like(self.running_mean)
            if prefix + "running_var" not in state_dict:
                state_dict[prefix + "running_var"] = torch.ones_like(self.running_var)

        super()._load_from_state_dict(
            state_dict,
            prefix,
            local_metadata,
            strict,
            missing_keys,
            unexpected_keys,
            error_msgs,
        )

    def __repr__(self):
        return "FrozenBatchNorm2d(num_features={}, eps={})".format(self.num_features, self.eps)

    @classmethod
    def convert_frozen_batchnorm(cls, module):
        """
        Convert all BatchNorm/SyncBatchNorm in module into FrozenBatchNorm.

        Args:
            module (torch.nn.Module):

        Returns:
            If module is BatchNorm/SyncBatchNorm, returns a new module.
            Otherwise, in-place convert module and return it.

        Similar to convert_sync_batchnorm in
        https://github.com/pytorch/pytorch/blob/master/torch/nn/modules/batchnorm.py
        """
        bn_module = nn.modules.batchnorm
        bn_module = (bn_module.BatchNorm2d, bn_module.SyncBatchNorm)
        res = module
        if isinstance(module, bn_module):
            res = cls(module.num_features)
            if module.affine:
                res.weight.data = module.weight.data.clone().detach()
                res.bias.data = module.bias.data.clone().detach()
            res.running_mean.data = module.running_mean.data
            res.running_var.data = module.running_var.data
            res.eps = module.eps
            res.num_batches_tracked = module.num_batches_tracked
        else:
            for name, child in module.named_children():
                new_child = cls.convert_frozen_batchnorm(child)
                if new_child is not child:
                    res.add_module(name, new_child)
        return res

    @classmethod
    def convert_frozenbatchnorm2d_to_batchnorm2d(cls, module: nn.Module) -> nn.Module:
        """
        Convert all FrozenBatchNorm2d to BatchNorm2d

        Args:
            module (torch.nn.Module):

        Returns:
            If module is FrozenBatchNorm2d, returns a new module.
            Otherwise, in-place convert module and return it.

        This is needed for quantization:
            https://fb.workplace.com/groups/1043663463248667/permalink/1296330057982005/
        """

        res = module
        if isinstance(module, FrozenBatchNorm2d):
            res = torch.nn.BatchNorm2d(module.num_features, module.eps)

            res.weight.data = module.weight.data.clone().detach()
            res.bias.data = module.bias.data.clone().detach()
            res.running_mean.data = module.running_mean.data.clone().detach()
            res.running_var.data = module.running_var.data.clone().detach()
            res.eps = module.eps
            res.num_batches_tracked = module.num_batches_tracked
        else:
            for name, child in module.named_children():
                new_child = cls.convert_frozenbatchnorm2d_to_batchnorm2d(child)
                if new_child is not child:
                    res.add_module(name, new_child)
        return res


def get_norm(norm, out_channels):
    """
    Args:
        norm (str or callable): either one of BN, SyncBN, FrozenBN, GN;
            or a callable that takes a channel number and returns
            the normalization layer as a nn.Module.

    Returns:
        nn.Module or None: the normalization layer
    """
    if norm is None:
        return None
    if isinstance(norm, str):
        if len(norm) == 0:
            return None
        norm = {
            "BN": nn.BatchNorm2d,
            # Fixed in https://github.com/pytorch/pytorch/pull/36382
            "SyncBN": nn.SyncBatchNorm,
            "FrozenBN": FrozenBatchNorm2d,
            "GN": lambda channels: nn.GroupNorm(32, channels),
            # for debugging:
            "nnSyncBN": nn.SyncBatchNorm,
            "LN": lambda channels: LayerNorm(channels),
        }[norm]
    return norm(out_channels)

class CycleBatchNormList(nn.ModuleList):
    """
    Implement domain-specific BatchNorm by cycling.

    When a BatchNorm layer is used for multiple input domains or input
    features, it might need to maintain a separate test-time statistics
    for each domain. See Sec 5.2 in :paper:`rethinking-batchnorm`.

    This module implements it by using N separate BN layers
    and it cycles through them every time a forward() is called.

    NOTE: The caller of this module MUST guarantee to always call
    this module by multiple of N times. Otherwise its test-time statistics
    will be incorrect.
    """

    def __init__(self, length: int, bn_class=nn.BatchNorm2d, **kwargs):
        """
        Args:
            length: number of BatchNorm layers to cycle.
            bn_class: the BatchNorm class to use
            kwargs: arguments of the BatchNorm class, such as num_features.
        """
        self._affine = kwargs.pop("affine", True)
        super().__init__([bn_class(**kwargs, affine=False) for k in range(length)])
        if self._affine:
            # shared affine, domain-specific BN
            channels = self[0].num_features
            self.weight = nn.Parameter(torch.ones(channels))
            self.bias = nn.Parameter(torch.zeros(channels))
        self._pos = 0

    def forward(self, x):
        ret = self[self._pos](x)
        self._pos = (self._pos + 1) % len(self)

        if self._affine:
            w = self.weight.reshape(1, -1, 1, 1)
            b = self.bias.reshape(1, -1, 1, 1)
            return ret * w + b
        else:
            return ret

    def extra_repr(self):
        return f"affine={self._affine}"


class LayerNorm(nn.Module):
    """
    A LayerNorm variant, popularized by Transformers, that performs point-wise mean and
    variance normalization over the channel dimension for inputs that have shape
    (batch_size, channels, height, width).
    https://github.com/facebookresearch/ConvNeXt/blob/d1fa8f6fef0a165b27399986cc2bdacc92777e40/models/convnext.py#L119  # noqa B950
    """

    def __init__(self, normalized_shape, eps=1e-6):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(normalized_shape))
        self.bias = nn.Parameter(torch.zeros(normalized_shape))
        self.eps = eps
        self.normalized_shape = (normalized_shape,)

    def forward(self, x):
        u = x.mean(1, keepdim=True)
        s = (x - u).pow(2).mean(1, keepdim=True)
        x = (x - u) / torch.sqrt(s + self.eps)
        x = self.weight[:, None, None] * x + self.bias[:, None, None]
        return x
