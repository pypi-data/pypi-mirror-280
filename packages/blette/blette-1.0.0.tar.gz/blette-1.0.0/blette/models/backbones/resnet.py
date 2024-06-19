#!/usr/bin/env python3

"""Blette ResNet

difference:
- added `return_stem`
- added configurable conv for stem
"""

from collections import OrderedDict

import torch
import torch.nn as nn

from mmcv.cnn import build_conv_layer, build_norm_layer
from mmseg.models.backbones.resnet import (
    ResNet as MMSEG_ResNet,
)

from blette.registry import MODELS


@MODELS.register_module(force=True)
class ResNet(MMSEG_ResNet):
    def __init__(
        self,
        stem_kernel_size=7,
        stem_stride_size=2,
        stem_padding_size=3,
        return_stem=False,
        **kwargs,
    ):
        self.stem_kwargs = dict(
            kernel_size=stem_kernel_size,
            stride_size=stem_stride_size,
            padding_size=stem_padding_size,
        )
        self.return_stem = return_stem
        super(ResNet, self).__init__(**kwargs)

    def _make_stem_layer(
        self,
        in_channels,
        stem_channels,
    ):
        """Make stem layer for ResNet."""

        # currently only changes non-deep stem
        kernel_size = self.stem_kwargs["kernel_size"]
        stride_size = self.stem_kwargs["stride_size"]
        padding_size = self.stem_kwargs["padding_size"]

        if self.deep_stem:
            self.stem = nn.Sequential(
                build_conv_layer(
                    self.conv_cfg,
                    in_channels,
                    stem_channels // 2,
                    kernel_size=3,
                    stride=stride_size,  # modified here!
                    padding=1,
                    bias=False,
                ),
                build_norm_layer(self.norm_cfg, stem_channels // 2)[1],
                nn.ReLU(inplace=True),
                build_conv_layer(
                    self.conv_cfg,
                    stem_channels // 2,
                    stem_channels // 2,
                    kernel_size=3,
                    stride=1,
                    padding=1,
                    bias=False,
                ),
                build_norm_layer(self.norm_cfg, stem_channels // 2)[1],
                nn.ReLU(inplace=True),
                build_conv_layer(
                    self.conv_cfg,
                    stem_channels // 2,
                    stem_channels,
                    kernel_size=3,
                    stride=1,
                    padding=1,
                    bias=False,
                ),
                build_norm_layer(self.norm_cfg, stem_channels)[1],
                nn.ReLU(inplace=True),
            )
        else:
            self.conv1 = build_conv_layer(
                self.conv_cfg,
                in_channels,
                stem_channels,
                kernel_size=kernel_size,
                stride=stride_size,
                padding=padding_size,
                bias=False,
            )
            self.norm1_name, norm1 = build_norm_layer(
                self.norm_cfg, stem_channels, postfix=1
            )
            self.add_module(self.norm1_name, norm1)
            self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        """Forward function."""
        if self.deep_stem:
            x = self.stem(x)
        else:
            x = self.conv1(x)
            x = self.norm1(x)
            x = self.relu(x)

        if self.return_stem:
            outs = [x]  # before pooling
        else:
            outs = []

        x = self.maxpool(x)

        for i, layer_name in enumerate(self.res_layers):
            res_layer = getattr(self, layer_name)
            x = res_layer(x)
            if i in self.out_indices:
                outs.append(x)
        return tuple(outs)


@MODELS.register_module(force=True)
class ResNetV1c(ResNet):
    """ResNetV1c variant described in [1]_.

    Compared with default ResNet(ResNetV1b), ResNetV1c replaces the 7x7 conv in
    the input stem with three 3x3 convs. For more details please refer to `Bag
    of Tricks for Image Classification with Convolutional Neural Networks
    <https://arxiv.org/abs/1812.01187>`_.
    """

    def __init__(self, **kwargs):
        super(ResNetV1c, self).__init__(deep_stem=True, avg_down=False, **kwargs)


@MODELS.register_module(force=True)
class ResNetV1d(ResNet):
    """ResNetV1d variant described in [1]_.

    Compared with default ResNet(ResNetV1b), ResNetV1d replaces the 7x7 conv in
    the input stem with three 3x3 convs. And in the downsampling block, a 2x2
    avg_pool with stride 2 is added before conv, whose stride is changed to 1.
    """

    def __init__(self, **kwargs):
        super(ResNetV1d, self).__init__(deep_stem=True, avg_down=True, **kwargs)


@MODELS.register_module()
class RCFResNet(ResNet):
    def forward(self, x):
        selected_out = OrderedDict()

        def _forward_hook(name):
            def hook(module, input, output):
                # activate after bn or conv
                selected_out[name] = torch.relu(output)

            return hook

        fhooks = []

        if self.deep_stem:
            for i, layer in enumerate(self.stem):
                hook = layer.register_forward_hook(_forward_hook("0_" + i))
                fhooks.append(hook)
        else:
            hook = self.conv1.register_forward_hook(_forward_hook("0_0"))
            fhooks.append(hook)

        for layer_name in self.res_layers:
            layer_num = layer_name.replace("layer", "")
            res_layer = getattr(self, layer_name)
            for i, sub_layer in enumerate(res_layer):
                for sub_name, l in sub_layer.named_modules():
                    # only return direct output of convolutions
                    # batch norm might be better since we're going to add
                    # another conv layer after this
                    # print(layer_name, sub_name)
                    if "bn" in sub_name:
                        hook = l.register_forward_hook(
                            _forward_hook(layer_num + "_" + str(i))
                        )
                        fhooks.append(hook)

        _ = super().forward(x)

        for hook in fhooks:
            hook.remove()

        return tuple([selected_out])


@MODELS.register_module()
class RCFResNetV1c(RCFResNet):
    def __init__(self, **kwargs):
        super(RCFResNetV1c, self).__init__(deep_stem=True, avg_down=False, **kwargs)


@MODELS.register_module()
class RCFResNetV1d(RCFResNet):
    def __init__(self, **kwargs):
        super(RCFResNetV1d, self).__init__(deep_stem=True, avg_down=True, **kwargs)
