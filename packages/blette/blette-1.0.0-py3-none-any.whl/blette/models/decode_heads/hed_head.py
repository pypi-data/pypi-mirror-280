#!/usr/bin/env python3

"""HED

https://github.com/s9xie/hed
"""

import torch
import torch.nn as nn

from mmcv.cnn import ConvModule
from mmseg.models.utils import resize

from blette.registry import MODELS
from .base_decode_head import BaseEdgeDecodeHead


class HEDSideConv(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        conv_cfg=None,
        norm_cfg=None,
        act_cfg=None,
        interpolation="bilinear",
        align_corners=False,
    ) -> None:
        super().__init__()
        self.pre_resize = ConvModule(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=1,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            act_cfg=act_cfg,
        )
        self._interp = interpolation
        self._align_corners = align_corners

    def forward(self, x, size):
        x = resize(  # (B, out_channels, H, W)
            self.pre_resize(x),
            size=size,
            mode=self._interp,
            align_corners=self._align_corners,
        )
        return x


@MODELS.register_module()
class HEDHead(BaseEdgeDecodeHead):
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
        resize_index=-1,
        **kwargs,
    ) -> None:
        super().__init__(
            input_transform="multiple_select",
            pred_key=pred_key,
            log_keys=log_keys,
            loss_decode=loss_decode,
            **kwargs,
        )

        self.resize_index = resize_index

        _interp = "bilinear"  # nearest

        sides = []
        for i in range(len(self.in_channels)):
            sides.append(
                HEDSideConv(
                    in_channels=self.in_channels[i],
                    out_channels=1,
                    conv_cfg=self.conv_cfg,
                    norm_cfg=None,
                    act_cfg=None,
                    interpolation=_interp,
                    align_corners=self.align_corners,
                )
            )

        self.sides = nn.ModuleList(sides)
        self.score_final = ConvModule(
            in_channels=len(self.in_channels),
            out_channels=1,
            kernel_size=1,
            conv_cfg=self.conv_cfg,
            norm_cfg=None,
            act_cfg=None,
        )

    def forward(self, inputs):
        x = self._transform_inputs(inputs)

        if self.pass_input_image:
            h, w = x[self.resize_index].shape[2:]
            _ = x.pop()  # remove image if exists
            resize_to = (h, w)
        else:
            h, w = x[self.resize_index].shape[2:]
            resize_to = (h, w)

        side_outs = []
        for i, layer in enumerate(self.sides):
            side_outs.append(layer(x[i], resize_to))

        fuse_cat = torch.cat(side_outs, dim=1)
        fuse = self.score_final(fuse_cat)

        outs = dict(fuse=fuse)
        for i, side_out in enumerate(side_outs):
            outs[f"side{i + 1}"] = side_out

        return outs
