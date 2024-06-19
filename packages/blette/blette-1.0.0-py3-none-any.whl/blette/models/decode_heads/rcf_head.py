#!/usr/bin/env python3

"""Richer Convolutional Features

https://github.com/yun-liu/RCF
https://github.com/balajiselvaraj1601/RCF_Pytorch_Updated
"""

from collections import defaultdict

import torch
import torch.nn as nn

from mmcv.cnn import ConvModule
from mmseg.models.utils import resize

from blette.registry import MODELS
from .base_decode_head import BaseEdgeDecodeHead


class SideLayer(nn.Module):
    def __init__(
        self,
        in_channels,
        in_layers,
        out_channels,
        mid_channels=21,
        conv_cfg=None,
        norm_cfg=None,
        act_cfg=None,
        interpolation="bilinear",
        align_corners=False,
    ) -> None:
        super().__init__()

        side_layers = []
        for _ in range(in_layers):
            side_layers.append(
                ConvModule(
                    in_channels=in_channels,
                    out_channels=mid_channels,
                    kernel_size=1,
                    conv_cfg=conv_cfg,
                    norm_cfg=norm_cfg,
                    act_cfg=act_cfg,
                )
            )
        self.side_layers = nn.ModuleList(side_layers)

        self.fuse = ConvModule(
            in_channels=mid_channels,
            out_channels=out_channels,
            kernel_size=1,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            act_cfg=act_cfg,
        )

        self._interp = interpolation
        self._align_corners = align_corners

    def forward(self, xs, size):
        assert len(xs) == len(self.side_layers)
        out = []
        for x, layer in zip(xs, self.side_layers):
            out.append(layer(x))

        # sum over all layers
        out = torch.stack(out, dim=0).sum(dim=0)

        out = resize(  # (B, out_channels, H, W)
            self.fuse(out),
            size=size,
            mode=self._interp,
            align_corners=self._align_corners,
        )
        return out


@MODELS.register_module()
class RCFHead(BaseEdgeDecodeHead):
    back_arch = {
        "vgg16": (2, 2, 3, 3, 3),
        "resnet50": (1, 3, 4, 6, 3),
        "resnet101": (1, 3, 4, 23, 3),
    }

    def __init__(
        self,
        pred_key="fuse",
        log_keys=("fuse", "side5"),
        loss_decode=dict(
            binary=dict(
                side1=dict(type="ConsensusBinaryEdgeLoss", loss_weight=0.6),
                side2=dict(type="ConsensusBinaryEdgeLoss", loss_weight=0.4),
                side3=dict(type="ConsensusBinaryEdgeLoss", loss_weight=0.6),
                side4=dict(type="ConsensusBinaryEdgeLoss", loss_weight=0.8),
                side5=dict(type="ConsensusBinaryEdgeLoss", loss_weight=1.0),
                fuse=dict(type="ConsensusBinaryEdgeLoss", loss_weight=1.0),
            ),
        ),
        back_arch="resnet101",
        mid_channels=21,
        **kwargs,
    ) -> None:
        super().__init__(
            input_transform="multiple_select",
            pred_key=pred_key,
            log_keys=log_keys,
            loss_decode=loss_decode,
            **kwargs,
        )

        _interp = "bilinear"  # nearest

        layers = []
        for i, num_layers in enumerate(self.back_arch[back_arch]):
            layers.append(
                SideLayer(
                    in_channels=self.in_channels[i],
                    in_layers=num_layers,
                    out_channels=1,
                    mid_channels=mid_channels,
                    conv_cfg=self.conv_cfg,
                    norm_cfg=None,
                    act_cfg=None,
                    interpolation=_interp,
                    align_corners=self.align_corners,
                )
            )
        self.side_layers = nn.ModuleList(layers)

        self.final = ConvModule(
            in_channels=5,
            out_channels=1,
            kernel_size=1,
            conv_cfg=self.conv_cfg,
            norm_cfg=None,
            act_cfg=None,
        )

    def forward(self, inputs):
        # [hooks, input_image]
        x = [i for i in inputs]

        assert self.pass_input_image
        assert isinstance(x, list)
        assert len(x) == 2

        bs, c, h, w = x[-1].shape
        resize_to = (h, w)

        # HACK: very ugly and only works for ResNet backbones...
        # sort hooks
        hooks = x[0]
        layer_out = defaultdict(list)
        for name, t in hooks.items():
            layer_num, conv_num = name.split("_")
            layer_out[int(layer_num)].append(t)

        side1 = self.side_layers[0](layer_out[0], resize_to)
        side2 = self.side_layers[1](layer_out[1], resize_to)
        side3 = self.side_layers[2](layer_out[2], resize_to)
        side4 = self.side_layers[3](layer_out[3], resize_to)
        side5 = self.side_layers[4](layer_out[4], resize_to)

        fuse = torch.cat([side1, side2, side3, side4, side5], dim=1)
        fuse = self.final(fuse)

        return dict(
            side1=side1,
            side2=side2,
            side3=side3,
            side4=side4,
            side5=side5,
            fuse=fuse,
        )
