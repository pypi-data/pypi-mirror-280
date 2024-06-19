#!/usr/bin/env python3

import torch
import torch.nn as nn

from mmcv.cnn import ConvModule


class GroupedConvFuse(nn.Module):
    """Basic multi-layer side fusion used in CaseNet

    https://github.com/Lavender105/DFF/blob/master/exps/models/casenet.py

    Changes:
    - bias=False: no bias in the last layer
    - flexible: number of sides could channge (CASENet, DDS, etc...)
    """

    def __init__(
        self,
        num_classes,
        num_sides,
        conv_cfg=None,
        bias=True,
    ):
        super().__init__()

        self.num_sides = num_sides

        # fuse (grouped convolution)
        self.fuse = ConvModule(
            in_channels=num_classes * num_sides,
            out_channels=num_classes,
            kernel_size=1,
            groups=num_classes,
            conv_cfg=conv_cfg,
            norm_cfg=None,
            bias=bias,  # originally True
            act_cfg=None,
        )

    def forward(self, sides):
        assert isinstance(sides, list)
        assert len(sides) == self.num_sides, f"number of sides: {len(sides)}"

        # fixed inplace array
        side5 = sides[-1]
        sides = sides[:-1]

        slice5 = side5[:, 0:1, :, :]
        fuse = torch.cat((slice5, *sides), 1)
        for i in range(side5.size(1) - 1):
            slice5 = side5[:, i + 1 : i + 2, :, :]
            fuse = torch.cat((fuse, slice5, *sides), 1)

        fuse = self.fuse(fuse)

        return fuse


class GroupedConvFuseSide4(GroupedConvFuse):
    def forward(self, sides):
        assert isinstance(sides, list)
        assert len(sides) == self.num_sides, f"number of sides: {len(sides)}"

        side5 = sides[-1]
        side4 = sides[-2]
        sides = sides[:-2]

        slice5 = side5[:, 0:1, :, :]
        slice4 = side4[:, 0:1, :, :]
        fuse = torch.cat((slice5, slice4, *sides), 1)
        for i in range(side5.size(1) - 1):
            slice5 = side5[:, i + 1 : i + 2, :, :]
            slice4 = side4[:, i + 1 : i + 2, :, :]
            fuse = torch.cat((fuse, slice5, slice4, *sides), 1)

        fuse = self.fuse(fuse)

        return fuse


class LocationAdaptiveLearner(nn.Module):
    """LocationAdaptiveLearner

    https://github.com/Lavender105/DFF/blob/master/exps/models/dff.py
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        conv_cfg,
        norm_cfg=None,
        act_cfg=dict(type="ReLU"),
        use_pre_act=False,
        use_sigmoid=False,
    ):
        super().__init__()

        modules = []

        if use_pre_act:
            modules.append(nn.ReLU())

        modules = modules + [
            ConvModule(
                in_channels,
                out_channels,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=act_cfg,
            ),
            ConvModule(
                out_channels,
                out_channels,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=act_cfg,
            ),
            ConvModule(
                out_channels,
                out_channels,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=None,
            ),
        ]

        if use_sigmoid:
            modules.append(nn.Sigmoid())

        self.conv_layers = nn.Sequential(*modules)

    def forward(self, inputs):
        assert isinstance(inputs, (list, tuple))
        assert len(inputs) == 5

        side1, side2, side3, side5, side5_w = inputs
        num_backbone = 4
        num_classes = side5.size(1)

        slice5 = side5[:, 0:1, :, :]
        fuse = torch.cat((slice5, side1, side2, side3), 1)
        for i in range(side5.size(1) - 1):
            slice5 = side5[:, i + 1 : i + 2, :, :]
            fuse = torch.cat((fuse, slice5, side1, side2, side3), 1)

        # (N, 19*4, H, W)
        w = self.conv_layers(side5_w)
        # Reshape to (N, 19, 4, H, W)
        w = w.view(w.size(0), num_classes, num_backbone, w.size(2), w.size(3))
        fuse = fuse.view(fuse.size(0), num_classes, -1, fuse.size(2), fuse.size(3))

        # fuse = torch.mul(fuse, w)
        # fuse = torch.sum(fuse, 2)
        # fuse = fuse * torch.sigmoid(w)
        fuse = fuse * w
        fuse = torch.sum(fuse, 2)

        return fuse


class GeneralizedLocationAdaptiveLearner(nn.Module):
    def __init__(
        self,
        num_sides,
        in_channels,
        out_channels,
        conv_cfg,
        norm_cfg=None,
        act_cfg=dict(type="ReLU"),
        use_pre_act=False,
        use_sigmoid=False,
    ):
        super().__init__()

        self.num_sides = num_sides

        modules = []
        if use_pre_act:
            modules.append(nn.ReLU())

        modules = modules + [
            ConvModule(
                in_channels,
                out_channels,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=act_cfg,
            ),
            ConvModule(
                out_channels,
                out_channels,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=act_cfg,
            ),
            ConvModule(
                out_channels,
                out_channels,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=None,
            ),
        ]

        if use_sigmoid:
            modules.append(nn.Sigmoid())

        self.conv_layers = nn.Sequential(*modules)

    def forward(self, sides):
        assert isinstance(sides, list)
        assert len(sides) == self.num_sides + 1, f"number of sides: {len(sides)}"

        num_backbones = len(sides) - 1

        side_w = sides[-1]
        side_l = sides[-2]
        sides = sides[:-2]

        num_classes = side_l.size(1)

        slice_l = side_l[:, 0:1, :, :]
        fuse = torch.cat((slice_l, *sides), 1)
        for i in range(side_l.size(1) - 1):
            slice_l = side_l[:, i + 1 : i + 2, :, :]
            fuse = torch.cat((fuse, slice_l, *sides), 1)

        # (N, 19*4, H, W)
        w = self.conv_layers(side_w)
        # Reshape to (N, 19, 4, H, W)
        w = w.view(w.size(0), num_classes, num_backbones, w.size(2), w.size(3))
        fuse = fuse.view(fuse.size(0), num_classes, -1, fuse.size(2), fuse.size(3))

        # fuse = torch.mul(fuse, w)
        # fuse = torch.sum(fuse, 2)
        # fuse = fuse * torch.sigmoid(w)
        fuse = fuse * w
        fuse = torch.sum(fuse, 2)

        return fuse
