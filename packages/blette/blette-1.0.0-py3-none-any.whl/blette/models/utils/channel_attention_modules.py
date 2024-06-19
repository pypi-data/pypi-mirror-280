#!/usr/bin/env python3

import torch
import torch.nn as nn

from mmcv.cnn import ConvModule


class SELayer(nn.Module):
    def __init__(
        self,
        in_planes,
        ratio=16,
        norm_cfg=None,
        act_cfg=dict(type="ReLU"),
    ):
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            ConvModule(
                in_planes, in_planes // ratio, 1, norm_cfg=norm_cfg, act_cfg=act_cfg
            ),
            ConvModule(
                in_planes // ratio, in_planes, 1, norm_cfg=norm_cfg, act_cfg=None
            ),
            nn.Sigmoid(),
        )

    def forward(self, x):
        y = self.avg_pool(x)
        y = self.fc(y)
        return x * y.expand_as(x)


class _CAM(nn.Module):
    """MS-CAM introduced in doi.org/10.3390/app122111248

    `Image Semantic Segmentation Fusion of Edge Detection and AFF Attention Mechanism`
    """

    def __init__(
        self,
        in_planes,
        ratio=16,
        **kwargs,
    ):
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc1 = nn.Sequential(
            nn.Conv2d(in_planes, in_planes // ratio, 1, bias=False),
            nn.BatchNorm2d(in_planes // ratio),
            nn.ReLU(),
            nn.Conv2d(in_planes // ratio, in_planes, 1, bias=False),
            nn.BatchNorm2d(in_planes),
        )
        self.fc2 = nn.Sequential(
            nn.Conv2d(in_planes, in_planes // ratio, 1, bias=False),
            nn.BatchNorm2d(in_planes // ratio),
            nn.ReLU(),
            nn.Conv2d(in_planes // ratio, in_planes, 1, bias=False),
            nn.BatchNorm2d(in_planes),
        )

    def forward(self, x):
        avg_out = self.fc1(self.avg_pool(x)).expand(x.shape)
        shape_out = self.fc2(x)
        out = avg_out + shape_out
        return torch.sigmoid(out)


class CAM(nn.Module):
    """MS-CAM introduced in doi.org/10.3390/app122111248

    Paper: `Image Semantic Segmentation Fusion of Edge Detection and AFF Attention Mechanism`

    adding SyncBN reduces metrics by around 1% (although multitask architecture benefits from it)
    """

    def __init__(
        self,
        in_planes,
        ratio=16,
        conv_cfg=None,
        norm_cfg=dict(type="BN"),
        act_cfg=dict(type="ReLU"),
    ):
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc1 = nn.Sequential(
            ConvModule(
                in_planes,
                in_planes // ratio,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=act_cfg,
            ),
            ConvModule(
                in_planes // ratio,
                in_planes,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=None,
            ),
        )
        self.fc2 = nn.Sequential(
            ConvModule(
                in_planes,
                in_planes // ratio,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=act_cfg,
            ),
            ConvModule(
                in_planes // ratio,
                in_planes,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=None,
            ),
        )

    def forward(self, x):
        avg_out = self.fc1(self.avg_pool(x)).expand(x.shape)
        shape_out = self.fc2(x)
        out = avg_out + shape_out
        return torch.sigmoid(out)
