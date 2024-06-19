#!/usr/bin/env python3

import torch.nn as nn

from mmcv.cnn import ConvModule
from mmseg.models.backbones.resnet import BasicBlock
from mmseg.models.utils import resize


class OGSideConv(nn.Module):
    """Original Side Upsample

    Weird choices in the original paper:
    - no activations after conv when there is a tranpose layer
    - bias + BN
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        rate,
        bias=False,
        conv_cfg=None,
        norm_cfg=None,
        act_cfg=dict(type="ReLU"),
    ):
        super().__init__()
        if rate == 1:
            # keeps the same size
            self.side = ConvModule(
                in_channels=in_channels,
                out_channels=out_channels,
                kernel_size=1,
                bias=False,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=None,
            )
        else:
            assert rate % 4 == 0
            self.side = nn.Sequential(
                ConvModule(
                    in_channels=in_channels,
                    out_channels=out_channels,
                    kernel_size=1,
                    bias=bias,
                    conv_cfg=conv_cfg,
                    norm_cfg=norm_cfg,
                    act_cfg=None,
                ),
                nn.ConvTranspose2d(
                    in_channels=out_channels,
                    out_channels=out_channels,
                    kernel_size=rate,
                    stride=rate // 2,
                    padding=rate // 4,
                    bias=False,
                ),
            )

    def forward(self, x):
        return self.side(x)


class SideConv(nn.Module):
    """'Improved' Basic Side Convolution

    instead of deconv, we use
    upsample -> 3x3conv

    https://distill.pub/2016/deconv-checkerboard/
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        conv_cfg=None,
        norm_cfg=None,
        bias=False,
        act_cfg=dict(type="ReLU"),
        interpolation="bilinear",
        align_corners=False,
    ):
        super().__init__()
        self.conv_reduce = ConvModule(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=1,
            bias=False,  # NOTE: worse results
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            act_cfg=act_cfg,
        )
        self.post_resize = nn.Sequential(
            nn.ReflectionPad2d(1),
            ConvModule(
                in_channels=out_channels,
                out_channels=out_channels,
                kernel_size=3,
                stride=1,
                padding=0,
                conv_cfg=conv_cfg,
                norm_cfg=None,  # no bn
                bias=bias,
                act_cfg=None,  # no activation -> edge logit
            ),
        )
        self._interp = interpolation
        self._align_corners = align_corners

    def forward(self, x, size):
        x = resize(  # (B, out_channels, H, W)
            self.conv_reduce(x),
            size=size,
            mode=self._interp,
            align_corners=self._align_corners,
        )
        x = self.post_resize(x)
        return x


class BasicBlockSideConv(nn.Module):
    """Side Convolution with Basic Block

    Better 'information converter'
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        num_blocks=2,
        return_block_output=False,
        dilations=None,
        conv_cfg=None,
        norm_cfg=None,
        bias=False,
        act_cfg=dict(type="ReLU"),
        interpolation="bilinear",
        align_corners=False,
    ):
        super().__init__()

        assert num_blocks > 0
        self.block = self._build_block(
            num_blocks=num_blocks,
            in_channels=in_channels,
            dilations=dilations,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
        )
        self.side_conv = SideConv(
            in_channels=in_channels,
            out_channels=out_channels,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            bias=bias,
            act_cfg=act_cfg,
            interpolation=interpolation,
            align_corners=align_corners,
        )
        self.return_block_output = return_block_output

    def _build_block(
        self,
        num_blocks,
        in_channels,
        dilations,
        conv_cfg,
        norm_cfg,
    ):
        if dilations is None:
            # default is 1
            dilations = tuple([1] * num_blocks)
        assert num_blocks == len(dilations)
        modules = []
        for d in dilations:
            modules.append(
                BasicBlock(
                    inplanes=in_channels,
                    planes=in_channels,
                    stride=1,
                    dilation=d,
                    downsample=None,
                    conv_cfg=conv_cfg,
                    norm_cfg=norm_cfg,
                )
            )
        return nn.Sequential(*modules)

    def forward(self, x, size):
        x = self.block(x)
        s = self.side_conv(x, size)
        if self.return_block_output:
            return s, x
        else:
            return s


class CBAMBlockSideConv(BasicBlockSideConv):
    def _build_block(self, num_blocks, in_channels, dilations, conv_cfg, norm_cfg):
        from blette.models.backbones.cbam_resnet import CBAMBasicBlock

        if dilations is None:
            # default is 1
            dilations = tuple([1] * num_blocks)
        assert num_blocks == len(dilations)
        modules = []
        for d in dilations:
            modules.append(
                CBAMBasicBlock(
                    inplanes=in_channels,
                    planes=in_channels,
                    stride=1,
                    dilation=d,
                    downsample=None,
                    conv_cfg=conv_cfg,
                    norm_cfg=norm_cfg,
                )
            )
        return nn.Sequential(*modules)


class BatchReduceChannel(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        conv_cfg=None,
        norm_cfg=None,
        act_cfg=dict(type="ReLU"),
    ):
        super().__init__()

        assert isinstance(in_channels, (list, tuple))
        assert isinstance(out_channels, (list, tuple))
        assert len(in_channels) == len(out_channels)

        self.conv_cfg = conv_cfg
        self.norm_cfg = norm_cfg
        self.act_cfg = act_cfg

        # initialize layers
        modules = []
        for in_c, out_c in zip(in_channels, out_channels):
            modules.append(self._build_reduce(in_c, out_c))

        self.reduces = nn.ModuleList(modules)

    def _build_reduce(self, in_channels, out_channels):
        return ConvModule(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=1,
            bias=False,  # NOTE: worse results
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            act_cfg=self.act_cfg,
        )

    def forward(self, xs):
        assert isinstance(xs, (tuple, list)) and len(xs) == len(self.reduces)

        outs = []
        for x, reduce in zip(xs, self.reduces):
            outs.append(reduce(x))

        return outs


class BatchBasicBlockReduce(BatchReduceChannel):
    def __init__(
        self,
        in_channels,
        out_channels,
        num_blocks=2,
        dilations=None,
        return_block_output=False,
        **kwargs,
    ):
        super().__init__(
            in_channels=in_channels,
            out_channels=out_channels,
            **kwargs,
        )

        assert num_blocks > 0
        self.return_block_output = return_block_output

        modules = []
        for in_c in in_channels:
            modules.append(
                self._build_block(
                    num_blocks=num_blocks,
                    in_channels=in_c,
                    dilations=dilations,
                )
            )

        self.blocks = nn.ModuleList(modules)

    def _build_block(self, in_channels, num_blocks, dilations):
        if dilations is None:
            # default is 1
            dilations = tuple([1] * num_blocks)
        assert num_blocks == len(dilations)
        modules = []
        for d in dilations:
            modules.append(
                BasicBlock(
                    inplanes=in_channels,
                    planes=in_channels,
                    stride=1,
                    dilation=d,
                    downsample=None,
                    conv_cfg=self.conv_cfg,
                    norm_cfg=self.norm_cfg,
                )
            )
        return nn.Sequential(*modules)

    def forward(self, xs):
        assert isinstance(xs, (tuple, list)) and len(xs) == len(self.reduces)

        outs = []
        for x, block, reduce in zip(xs, self.blocks, self.reduces):
            x = block(x)
            x = reduce(x)
            outs.append(x)

        return outs


class BatchUpsample(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        interpolation="bilinear",
        align_corners=False,
        conv_cfg=None,
        norm_cfg=None,
        act_cfg=dict(type="ReLU"),
    ):
        super().__init__()
        assert isinstance(in_channels, (list, tuple))
        assert isinstance(out_channels, (list, tuple))
        assert len(in_channels) == len(out_channels)

        self.conv_cfg = conv_cfg
        self.norm_cfg = norm_cfg
        self.act_cfg = act_cfg
        self._interp = interpolation
        self._align_corners = align_corners

        modules = []
        for in_c, out_c in zip(in_channels, out_channels):
            modules.append(self._build_post(in_c, out_c))

        self.posts = nn.ModuleList(modules)

    def _build_post(self, in_channels, out_channels):
        return nn.Sequential(
            nn.ReflectionPad2d(1),
            ConvModule(
                in_channels=in_channels,
                out_channels=out_channels,
                kernel_size=3,
                stride=1,
                padding=0,
                conv_cfg=self.conv_cfg,
                norm_cfg=None,  # no bn
                bias=False,
                act_cfg=None,  # no activation -> edge logit
            ),
        )

    def _resize(self, x, size):
        return resize(
            x,
            size=size,
            mode=self._interp,
            align_corners=self._align_corners,
        )

    def forward(self, xs, size):
        assert isinstance(xs, (tuple, list)) and len(xs) == len(self.posts)

        outs = []
        for x, post in zip(xs, self.posts):
            x = self._resize(x, size)
            x = post(x)
            outs.append(x)

        return outs
