# Copyright (c) OpenMMLab. All rights reserved.

import math

import torch
import torch.nn as nn

from torch.nn.functional import pad

from mmcv.cnn import build_activation_layer, build_conv_layer, build_norm_layer
from mmcv.cnn.bricks.transformer import build_dropout
from mmengine.model import BaseModule, ModuleList, Sequential
from mmseg.models.backbones.hrnet import Bottleneck, HRModule, HRNet
from mmseg.models.backbones.swin import WindowMSA
from mmseg.models.utils import nchw_to_nlc, nlc2nchw2nlc, nlc_to_nchw

from blette.registry import MODELS
from .hrnet import ModHRNet


class LocalWindowSelfAttention(BaseModule):
    """Local-window Self Attention (LSA) module with relative position bias.

    This module is the short-range self-attention module in the
    Interlaced Sparse Self-Attention <https://arxiv.org/abs/1907.12273>`_.

    Args:
        embed_dims (int): Number of input channels.
        num_heads (int): Number of attention heads.
        window_size (tuple[int] | int): The height and width of the window.
        qkv_bias (bool):  If True, add a learnable bias to q, k, v.
            Default: True.
        qk_scale (float | None, optional): Override default qk scale of
            head_dim ** -0.5 if set. Default: None.
        attn_drop_rate (float): Dropout ratio of attention weight.
            Default: 0.0
        proj_drop_rate (float): Dropout ratio of output. Default: 0.
        with_pad_mask (bool): If True, mask out the padded tokens in
            the attention process. Default: False.
        init_cfg (dict | None, optional): The Config for initialization.
            Default: None.
    """

    def __init__(
        self,
        embed_dims,
        num_heads,
        window_size,
        qkv_bias=True,
        qk_scale=None,
        attn_drop_rate=0.0,
        proj_drop_rate=0.0,
        with_pad_mask=False,
        init_cfg=None,
    ):
        super().__init__(init_cfg=init_cfg)
        if isinstance(window_size, int):
            window_size = (window_size, window_size)
        self.window_size = window_size
        self.with_pad_mask = with_pad_mask
        self.attn = WindowMSA(
            embed_dims=embed_dims,
            num_heads=num_heads,
            window_size=window_size,
            qkv_bias=qkv_bias,
            qk_scale=qk_scale,
            attn_drop_rate=attn_drop_rate,
            proj_drop_rate=proj_drop_rate,
            init_cfg=init_cfg,
        )

    def forward(self, x, H, W, **kwargs):
        """Forward function.

        Args:
            x: (torch.Tensor): The input tensor with shape [B, N, C].
            H: (int): The height of the original 4D feature map.
            W: (int): The width of the original 4D feature map.
            **kwargs: Other arguments input to the forward function
                of `WindowMSA`
        Returns:
            torch.Tensor: The output tensor with shape [B, N, C]
        """

        B, N, C = x.shape
        x = x.view(B, H, W, C)
        Wh, Ww = self.window_size

        # center-pad the feature on H and W axes
        pad_h = math.ceil(H / Wh) * Wh - H
        pad_w = math.ceil(W / Ww) * Ww - W
        x = pad(
            x, (0, 0, pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2)
        )

        # permute
        x = x.view(B, math.ceil(H / Wh), Wh, math.ceil(W / Ww), Ww, C)
        x = x.permute(0, 1, 3, 2, 4, 5)
        x = x.reshape(-1, Wh * Ww, C)  # (B*num_window, Wh*Ww, C)

        # attention
        if self.with_pad_mask and pad_h > 0 and pad_w > 0:
            pad_mask = x.new_zeros(1, H, W, 1)
            pad_mask = pad(
                pad_mask,
                [0, 0, pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2],
                value=-float("inf"),
            )
            pad_mask = pad_mask.view(1, math.ceil(H / Wh), Wh, math.ceil(W / Ww), Ww, 1)
            pad_mask = pad_mask.permute(0, 1, 3, 2, 4, 5)
            pad_mask = pad_mask.reshape(-1, Wh * Ww)
            pad_mask = pad_mask[:, None, :].expand([-1, Wh * Ww, -1])
            out = self.attn(x, pad_mask, **kwargs)
        else:
            out = self.attn(x, **kwargs)

        # reverse permutation
        out = out.reshape(B, math.ceil(H / Wh), math.ceil(W / Ww), Wh, Ww, C)
        out = out.permute(0, 1, 3, 2, 4, 5)
        out = out.reshape(B, H + pad_h, W + pad_w, C)

        # de-pad
        out = out[:, pad_h // 2 : H + pad_h // 2, pad_w // 2 : W + pad_w // 2]
        return out.reshape(B, N, C)


class CrossFFN(BaseModule):
    """FFN with Depthwise Conv of HRFormer.

    Args:
        in_channels (int): The number of input channels.
        hidden_channels (int): The hidden channel of FFNs.
            Defaults: The same as in_features.
        out_channels (int): The number of output channels
        act_cfg (dict): Config of activation layer.
            Default: dict(type='GELU').
        dw_act_cfg (dict): Config of activation layer appended
            right after depth-wise Conv. Default: dict(type='GELU').
        norm_cfg (dict): Config of norm layer.
            Default: dict(type='SyncBN').
        init_cfg (dict | list | None, optional): The init config.
            Default: None.
    """

    def __init__(
        self,
        in_channels,
        hidden_channels=None,
        out_channels=None,
        act_cfg=dict(type="GELU"),
        dw_act_cfg=dict(type="GELU"),
        norm_cfg=dict(type="BN2d", requires_grad=True),
        init_cfg=None,
    ):
        super().__init__(init_cfg=init_cfg)
        out_channels = out_channels or in_channels
        hidden_channels = hidden_channels or in_channels
        self.layers = Sequential(
            build_conv_layer(
                dict(type="Conv2d"),
                in_channels=in_channels,
                out_channels=hidden_channels,
                kernel_size=1,
            ),
            build_norm_layer(norm_cfg, hidden_channels)[1],
            build_activation_layer(act_cfg),
            build_conv_layer(
                dict(type="Conv2d"),
                in_channels=hidden_channels,
                out_channels=hidden_channels,
                kernel_size=3,
                stride=1,
                padding=1,
                groups=hidden_channels,
            ),
            build_norm_layer(norm_cfg, hidden_channels)[1],
            build_activation_layer(dw_act_cfg),
            build_conv_layer(
                dict(type="Conv2d"),
                in_channels=hidden_channels,
                out_channels=out_channels,
                kernel_size=1,
            ),
            build_norm_layer(norm_cfg, out_channels)[1],
            build_activation_layer(act_cfg),
        )

    def forward(self, x, H, W):
        """Forward function.

        Args:
            x: (torch.Tensor): The input tensor with shape [B, N, C].
            H: (int): The height of the original 4D feature map.
            W: (int): The width of the original 4D feature map.

        Returns:
            torch.Tensor: The output tensor with shape [B, N, C]
        """

        x = nlc2nchw2nlc(self.layers, x, (H, W))
        return x


class HRFormerBlock(BaseModule):
    """High-Resolution Block for HRFormer.

    Args:
        in_channels (int): The input number of channels.
        out_channels (int): The output number of channels.
        num_heads (int): The number of head within each LSA.
        window_size (int): The window size for the LSA.
            Default: 7
        drop_path (float): The drop path rate of HRFomer.
            Default: 0.0
        mlp_ratio (int): The expansion ration of FFN.
            Default: 4
        act_cfg (dict): Config of activation layer.
            Default: dict(type='GELU').
        norm_cfg (dict): Config of norm layer.
            Default: dict(type='SyncBN').
        transformer_norm_cfg (dict): Config of transformer norm
            layer. Default: dict(type='LN', eps=1e-6).
        init_cfg (dict | list | None, optional): The init config.
            Default: None.
    """

    expansion = 1

    def __init__(
        self,
        in_channels,
        out_channels,
        num_heads,
        window_size=7,
        mlp_ratio=4,
        drop_path=0.0,
        act_cfg=dict(type="GELU"),
        norm_cfg=dict(type="BN2d"),
        transformer_norm_cfg=dict(type="LN", eps=1e-6),
        init_cfg=None,
        **kwargs,
    ):
        super(HRFormerBlock, self).__init__(init_cfg=init_cfg)
        self.num_heads = num_heads
        self.window_size = window_size
        self.mlp_ratio = mlp_ratio

        self.norm1 = build_norm_layer(transformer_norm_cfg, in_channels)[1]
        self.attn = LocalWindowSelfAttention(
            in_channels,
            num_heads=num_heads,
            window_size=window_size,
            init_cfg=None,
            **kwargs,
        )

        self.norm2 = build_norm_layer(transformer_norm_cfg, out_channels)[1]
        self.ffn = CrossFFN(
            in_channels=in_channels,
            hidden_channels=int(in_channels * mlp_ratio),
            out_channels=out_channels,
            norm_cfg=norm_cfg,
            act_cfg=act_cfg,
            dw_act_cfg=act_cfg,
            init_cfg=None,
        )

        self.drop_path = (
            build_dropout(dict(type="DropPath", drop_prob=drop_path))
            if drop_path > 0.0
            else nn.Identity()
        )

    def forward(self, x):
        """Forward function."""
        B, C, H, W = x.size()
        # Attention
        x = nchw_to_nlc(x)
        x = x + self.drop_path(self.attn(self.norm1(x), H, W))
        # FFN
        x = x + self.drop_path(self.ffn(self.norm2(x), H, W))
        x = nlc_to_nchw(x, (H, W))
        return x

    def extra_repr(self):
        """(Optional) Set the extra information about this module."""
        return "num_heads={}, window_size={}, mlp_ratio={}".format(
            self.num_heads, self.window_size, self.mlp_ratio
        )


class HRFormerModule(HRModule):
    """High-Resolution Module for HRFormer.

    Args:
        num_branches (int): The number of branches in the HRFormerModule.
        block (nn.Module): The building block of HRFormer.
            The block should be the HRFormerBlock.
        num_blocks (tuple): The number of blocks in each branch.
            The length must be equal to num_branches.
        num_inchannels (tuple): The number of input channels in each branch.
            The length must be equal to num_branches.
        num_channels (tuple): The number of channels in each branch.
            The length must be equal to num_branches.
        num_heads (tuple): The number of heads within the LSAs.
        num_window_sizes (tuple): The window size for the LSAs.
        num_mlp_ratios (tuple): The expansion ratio for the FFNs.
        multiscale_output (bool): Whether to output multi-level
            features produced by multiple branches. If False, only the first
            level feature will be output. Default: True.
        drop_paths (list): The drop path rate of HRFomer.
            Default: [0.0]
        with_pad_mask (bool): Whether to mask out padded pixels when
            computing the attention. Default: False
        conv_cfg (dict, optional): Config of the conv layers.
            Default: None.
        norm_cfg (dict): Config of the norm layers appended
            right after conv. Default: dict(type='SyncBN', requires_grad=True)
        transformer_norm_cfg (dict): Config of the norm layers.
            Default: dict(type='LN', eps=1e-6)
        with_cp (bool): Use checkpoint or not. Using checkpoint will save some
            memory while slowing down the training speed. Default: False
    """

    def __init__(
        self,
        num_branches,
        block,
        num_blocks,
        num_inchannels,
        num_channels,
        num_heads,
        num_window_sizes,
        num_mlp_ratios,
        multiscale_output=True,
        drop_paths=[0.0],
        with_pad_mask=False,
        conv_cfg=None,
        norm_cfg=dict(type="BN", requires_grad=True),
        transformer_norm_cfg=dict(type="LN", eps=1e-6),
        with_cp=False,
    ):
        self.transformer_norm_cfg = transformer_norm_cfg
        self.drop_paths = drop_paths
        self.num_heads = num_heads
        self.num_window_sizes = num_window_sizes
        self.num_mlp_ratios = num_mlp_ratios
        self.with_pad_mask = with_pad_mask

        super().__init__(
            num_branches,
            block,
            num_blocks,
            num_inchannels,
            num_channels,
            multiscale_output,
            with_cp,
            conv_cfg,
            norm_cfg,
        )

    def _make_one_branch(self, branch_index, block, num_blocks, num_channels, stride=1):
        """Build one branch."""
        # HRFormerBlock does not support down sample layer yet.
        assert (
            stride == 1 and self.in_channels[branch_index] == num_channels[branch_index]
        )
        layers = []
        layers.append(
            block(
                self.in_channels[branch_index],
                num_channels[branch_index],
                num_heads=self.num_heads[branch_index],
                window_size=self.num_window_sizes[branch_index],
                mlp_ratio=self.num_mlp_ratios[branch_index],
                drop_path=self.drop_paths[0],
                norm_cfg=self.norm_cfg,
                transformer_norm_cfg=self.transformer_norm_cfg,
                init_cfg=None,
                with_pad_mask=self.with_pad_mask,
            )
        )

        self.in_channels[branch_index] = (
            self.in_channels[branch_index] * block.expansion
        )
        for i in range(1, num_blocks[branch_index]):
            layers.append(
                block(
                    self.in_channels[branch_index],
                    num_channels[branch_index],
                    num_heads=self.num_heads[branch_index],
                    window_size=self.num_window_sizes[branch_index],
                    mlp_ratio=self.num_mlp_ratios[branch_index],
                    drop_path=self.drop_paths[i],
                    norm_cfg=self.norm_cfg,
                    transformer_norm_cfg=self.transformer_norm_cfg,
                    init_cfg=None,
                    with_pad_mask=self.with_pad_mask,
                )
            )
        return Sequential(*layers)

    def _make_fuse_layers(self):
        """Build fuse layers."""
        if self.num_branches == 1:
            return None
        num_branches = self.num_branches
        num_inchannels = self.in_channels
        fuse_layers = []
        for i in range(num_branches if self.multiscale_output else 1):
            fuse_layer = []
            for j in range(num_branches):
                if j > i:
                    fuse_layer.append(
                        Sequential(
                            build_conv_layer(
                                self.conv_cfg,
                                num_inchannels[j],
                                num_inchannels[i],
                                kernel_size=1,
                                stride=1,
                                bias=False,
                            ),
                            build_norm_layer(self.norm_cfg, num_inchannels[i])[1],
                        )
                    )
                elif j == i:
                    fuse_layer.append(None)
                else:
                    conv3x3s = []
                    for k in range(i - j):
                        if k == i - j - 1:
                            num_outchannels_conv3x3 = num_inchannels[i]
                            with_out_act = False
                        else:
                            num_outchannels_conv3x3 = num_inchannels[j]
                            with_out_act = True
                        sub_modules = [
                            build_conv_layer(
                                self.conv_cfg,
                                num_inchannels[j],
                                num_inchannels[j],
                                kernel_size=3,
                                stride=2,
                                padding=1,
                                groups=num_inchannels[j],
                                bias=False,
                            ),
                            build_norm_layer(self.norm_cfg, num_inchannels[j])[1],
                            build_conv_layer(
                                self.conv_cfg,
                                num_inchannels[j],
                                num_outchannels_conv3x3,
                                kernel_size=1,
                                stride=1,
                                bias=False,
                            ),
                            build_norm_layer(self.norm_cfg, num_outchannels_conv3x3)[1],
                        ]
                        if with_out_act:
                            sub_modules.append(nn.ReLU(False))
                        conv3x3s.append(Sequential(*sub_modules))
                    fuse_layer.append(Sequential(*conv3x3s))
            fuse_layers.append(ModuleList(fuse_layer))

        return ModuleList(fuse_layers)


class ModHRFormerModule(HRFormerModule):
    def __init__(self, down_strides=(2, 2, 2), **kwargs):
        self.down_strides = down_strides
        super().__init__(**kwargs)

    def _make_fuse_layers(self):
        """Build fuse layers."""
        if self.num_branches == 1:
            return None
        num_branches = self.num_branches
        num_inchannels = self.in_channels
        fuse_layers = []
        for i in range(num_branches if self.multiscale_output else 1):
            fuse_layer = []
            for j in range(num_branches):
                if j > i:
                    fuse_layer.append(
                        Sequential(
                            build_conv_layer(
                                self.conv_cfg,
                                num_inchannels[j],
                                num_inchannels[i],
                                kernel_size=1,
                                stride=1,
                                bias=False,
                            ),
                            build_norm_layer(self.norm_cfg, num_inchannels[i])[1],
                        )
                    )
                elif j == i:
                    fuse_layer.append(None)
                else:
                    conv3x3s = []
                    for k in range(i - j):
                        if k == i - j - 1:
                            num_outchannels_conv3x3 = num_inchannels[i]
                            with_out_act = False
                        else:
                            num_outchannels_conv3x3 = num_inchannels[j]
                            with_out_act = True
                        sub_modules = [
                            build_conv_layer(
                                self.conv_cfg,
                                num_inchannels[j],
                                num_inchannels[j],
                                kernel_size=3,
                                stride=self.down_strides[j + k],
                                padding=1,
                                groups=num_inchannels[j],
                                bias=False,
                            ),
                            build_norm_layer(self.norm_cfg, num_inchannels[j])[1],
                            build_conv_layer(
                                self.conv_cfg,
                                num_inchannels[j],
                                num_outchannels_conv3x3,
                                kernel_size=1,
                                stride=1,
                                bias=False,
                            ),
                            build_norm_layer(self.norm_cfg, num_outchannels_conv3x3)[1],
                        ]
                        if with_out_act:
                            sub_modules.append(nn.ReLU(False))
                        conv3x3s.append(Sequential(*sub_modules))
                    fuse_layer.append(Sequential(*conv3x3s))
            fuse_layers.append(ModuleList(fuse_layer))

        return ModuleList(fuse_layers)


@MODELS.register_module()
class HRFormer(HRNet):
    """HRFormer backbone.

    This backbone is the implementation of `HRFormer:
    High-Resolution Transformer for Dense Prediction.
    <https://arxiv.org/abs/2110.09408>`_.

    Args:
        extra (dict): Detailed configuration for each stage of HRNet.
            There must be 4 stages, the configuration for each stage must have
            5 keys:
                - num_modules (int): The number of HRModule in this stage.
                - num_branches (int): The number of branches in the HRModule.
                - block (str): The type of block.
                - num_blocks (tuple): The number of blocks in each branch.
                    The length must be equal to num_branches.
                - num_channels (tuple): The number of channels in each branch.
                    The length must be equal to num_branches.
        in_channels (int): Number of input image channels. Normally 3.
        conv_cfg (dict, optional): Dictionary to construct and config conv
            layer. Default: None.
        norm_cfg (dict): Config of norm layer.
            Use `SyncBN` by default.
        transformer_norm_cfg (dict): Config of transformer norm layer.
            Use `LN` by default.
        norm_eval (bool): Whether to set norm layers to eval mode, namely,
            freeze running stats (mean and var). Note: Effect on Batch Norm
            and its variants only. Default: False.
        with_cp (bool): Use checkpoint in ``HRFomerModule`` or not. Using
            checkpoint will save some memory while slowing down the training
            speed. Default: False
        multiscale_output (bool): Whether to output multi-level features
            produced by multiple branches. If False, only the first level
            feature will be output. Default: True.
        drop_path_rate (float): Stochastic depth rate. Default 0.0.
        zero_init_residual (bool): Whether to use zero init for last norm layer
            in resblocks to let them behave as identity. Default: False.
        frozen_stages (int): Stages to be frozen (stop grad and set eval mode).
            -1 means not freezing any parameters. Default: -1.
        pretrained (str, optional): Model pretrained path. Default: None.
        init_cfg (dict or list[dict], optional): Initialization config dict.
            Default: None.
    Example:
        >>> from mmseg.models import HRFormer
        >>> import torch
        >>> extra = dict(
        >>>     stage1=dict(
        >>>         num_modules=1,
        >>>         num_branches=1,
        >>>         block='BOTTLENECK',
        >>>         num_blocks=(2, ),
        >>>         num_channels=(64, )),
        >>>     stage2=dict(
        >>>         num_modules=1,
        >>>         num_branches=2,
        >>>         block='HRFORMER',
        >>>         window_sizes=(7, 7),
        >>>         num_heads=(1, 2),
        >>>         mlp_ratios=(4, 4),
        >>>         num_blocks=(2, 2),
        >>>         num_channels=(32, 64)),
        >>>     stage3=dict(
        >>>         num_modules=4,
        >>>         num_branches=3,
        >>>         block='HRFORMER',
        >>>         window_sizes=(7, 7, 7),
        >>>         num_heads=(1, 2, 4),
        >>>         mlp_ratios=(4, 4, 4),
        >>>         num_blocks=(2, 2, 2),
        >>>         num_channels=(32, 64, 128)),
        >>>     stage4=dict(
        >>>         num_modules=2,
        >>>         num_branches=4,
        >>>         block='HRFORMER',
        >>>         window_sizes=(7, 7, 7, 7),
        >>>         num_heads=(1, 2, 4, 8),
        >>>         mlp_ratios=(4, 4, 4, 4),
        >>>         num_blocks=(2, 2, 2, 2),
        >>>         num_channels=(32, 64, 128, 256)))
        >>> self = HRFormer(extra, in_channels=1)
        >>> self.eval()
        >>> inputs = torch.rand(1, 1, 32, 32)
        >>> level_outputs = self.forward(inputs)
        >>> for level_out in level_outputs:
        ...     print(tuple(level_out.shape))
        (1, 32, 8, 8)
        (1, 64, 4, 4)
        (1, 128, 2, 2)
        (1, 256, 1, 1)
    """

    blocks_dict = {"BOTTLENECK": Bottleneck, "HRFORMERBLOCK": HRFormerBlock}

    def __init__(
        self,
        extra,
        in_channels=3,
        conv_cfg=None,
        norm_cfg=dict(type="BN2d", requires_grad=True),
        transformer_norm_cfg=dict(type="LN", eps=1e-6),
        norm_eval=False,
        with_cp=False,
        multiscale_output=True,
        drop_path_rate=0.0,
        zero_init_residual=False,
        frozen_stages=-1,
        pretrained=None,
        init_cfg=None,
    ):
        # stochastic depth
        depths = [
            extra[stage]["num_blocks"][0] * extra[stage]["num_modules"]
            for stage in ["stage2", "stage3", "stage4"]
        ]
        depth_s2, depth_s3, _ = depths
        drop_path_rate = drop_path_rate
        dpr = [x.item() for x in torch.linspace(0, drop_path_rate, sum(depths))]
        extra["stage2"]["drop_path_rates"] = dpr[0:depth_s2]
        extra["stage3"]["drop_path_rates"] = dpr[depth_s2 : depth_s2 + depth_s3]
        extra["stage4"]["drop_path_rates"] = dpr[depth_s2 + depth_s3 :]

        self.transformer_norm_cfg = transformer_norm_cfg
        self.with_pad_mask = extra.get("with_pad_mask", False)

        super().__init__(
            extra=extra,
            in_channels=in_channels,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            norm_eval=norm_eval,
            with_cp=with_cp,
            zero_init_residual=zero_init_residual,
            frozen_stages=frozen_stages,
            multiscale_output=multiscale_output,
            pretrained=pretrained,
            init_cfg=init_cfg,
        )

    def _make_stage(self, layer_config, num_inchannels, multiscale_output=True):
        """Make each stage."""
        num_modules = layer_config["num_modules"]
        num_branches = layer_config["num_branches"]
        num_blocks = layer_config["num_blocks"]
        num_channels = layer_config["num_channels"]
        block = self.blocks_dict[layer_config["block"]]
        num_heads = layer_config["num_heads"]
        num_window_sizes = layer_config["window_sizes"]
        num_mlp_ratios = layer_config["mlp_ratios"]
        drop_path_rates = layer_config["drop_path_rates"]

        modules = []
        for i in range(num_modules):
            # multiscale_output is only used at the last module
            if not multiscale_output and i == num_modules - 1:
                reset_multiscale_output = False
            else:
                reset_multiscale_output = True

            modules.append(
                HRFormerModule(
                    num_branches,
                    block,
                    num_blocks,
                    num_inchannels,
                    num_channels,
                    num_heads,
                    num_window_sizes,
                    num_mlp_ratios,
                    reset_multiscale_output,
                    drop_paths=drop_path_rates[
                        num_blocks[0] * i : num_blocks[0] * (i + 1)
                    ],
                    with_pad_mask=self.with_pad_mask,
                    conv_cfg=self.conv_cfg,
                    norm_cfg=self.norm_cfg,
                    transformer_norm_cfg=self.transformer_norm_cfg,
                    with_cp=self.with_cp,
                )
            )
            num_inchannels = modules[-1].in_channels

        return Sequential(*modules), num_inchannels


@MODELS.register_module()
class ModHRFormer(ModHRNet):
    blocks_dict = {"BOTTLENECK": Bottleneck, "HRFORMERBLOCK": HRFormerBlock}

    def __init__(
        self,
        extra,
        in_channels=3,
        conv_cfg=None,
        norm_cfg=dict(type="BN2d", requires_grad=True),
        transformer_norm_cfg=dict(type="LN", eps=1e-6),
        norm_eval=False,
        with_cp=False,
        multiscale_output=True,
        drop_path_rate=0.0,
        zero_init_residual=False,
        frozen_stages=-1,
        pretrained=None,
        init_cfg=None,
        **kwargs,
    ):
        # stochastic depth
        depths = [
            extra[stage]["num_blocks"][0] * extra[stage]["num_modules"]
            for stage in ["stage2", "stage3", "stage4"]
        ]
        depth_s2, depth_s3, _ = depths
        drop_path_rate = drop_path_rate
        dpr = [x.item() for x in torch.linspace(0, drop_path_rate, sum(depths))]
        extra["stage2"]["drop_path_rates"] = dpr[0:depth_s2]
        extra["stage3"]["drop_path_rates"] = dpr[depth_s2 : depth_s2 + depth_s3]
        extra["stage4"]["drop_path_rates"] = dpr[depth_s2 + depth_s3 :]

        self.transformer_norm_cfg = transformer_norm_cfg
        self.with_pad_mask = extra.get("with_pad_mask", False)

        super().__init__(
            extra=extra,
            in_channels=in_channels,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            norm_eval=norm_eval,
            with_cp=with_cp,
            zero_init_residual=zero_init_residual,
            frozen_stages=frozen_stages,
            multiscale_output=multiscale_output,
            pretrained=pretrained,
            init_cfg=init_cfg,
            **kwargs,
        )

    def _make_stage(
        self,
        layer_config,
        num_inchannels,
        multiscale_output=True,
        down_strides=(2, 2, 2),
    ):
        """Make each stage."""
        num_modules = layer_config["num_modules"]
        num_branches = layer_config["num_branches"]
        num_blocks = layer_config["num_blocks"]
        num_channels = layer_config["num_channels"]
        block = self.blocks_dict[layer_config["block"]]
        num_heads = layer_config["num_heads"]
        num_window_sizes = layer_config["window_sizes"]
        num_mlp_ratios = layer_config["mlp_ratios"]
        drop_path_rates = layer_config["drop_path_rates"]

        modules = []
        for i in range(num_modules):
            # multiscale_output is only used at the last module
            if not multiscale_output and i == num_modules - 1:
                reset_multiscale_output = False
            else:
                reset_multiscale_output = True

            modules.append(
                ModHRFormerModule(
                    num_branches=num_branches,
                    block=block,
                    num_blocks=num_blocks,
                    num_inchannels=num_inchannels,
                    num_channels=num_channels,
                    num_heads=num_heads,
                    num_window_sizes=num_window_sizes,
                    num_mlp_ratios=num_mlp_ratios,
                    multiscale_output=reset_multiscale_output,
                    down_strides=down_strides,
                    drop_paths=drop_path_rates[
                        num_blocks[0] * i : num_blocks[0] * (i + 1)
                    ],
                    with_pad_mask=self.with_pad_mask,
                    conv_cfg=self.conv_cfg,
                    norm_cfg=self.norm_cfg,
                    transformer_norm_cfg=self.transformer_norm_cfg,
                    with_cp=self.with_cp,
                )
            )
            num_inchannels = modules[-1].in_channels

        return Sequential(*modules), num_inchannels
