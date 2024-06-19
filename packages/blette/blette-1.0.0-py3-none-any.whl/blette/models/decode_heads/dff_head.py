#!/usr/bin/env python3

"""Implementation of DFF

https://github.com/Lavender105/DFF/blob/master/exps/models/dff.py

- mod bias: only Bias in the last conv of the side conv

| DFF           | mF    |
| ---           | ---   |
| All False     | 66.50 |
| mod bias      | 68.65 |
| act           | 68.67 |
| ", mod bias   | 69.34 |
| sig           | 69.30 |
| “, mod bias   | 68.76 |
| act sig       | 69.04 |
| “, mod bias   | 68.57 |
"""

import torch.nn as nn

from blette.registry import MODELS
from .base_decode_head import BaseEdgeDecodeHead
from ..utils import (
    LocationAdaptiveLearner,
    GeneralizedLocationAdaptiveLearner,
    SideConv,
    OGSideConv,
)


@MODELS.register_module()
class DFFHead(BaseEdgeDecodeHead):
    def __init__(
        self,
        pred_key="fuse",
        log_keys=("fuse", "last"),
        loss_decode=dict(
            mlbl=dict(
                fuse=dict(type="MultiLabelEdgeLoss", loss_weight=1.0),
                last=dict(type="MultiLabelEdgeLoss", loss_weight=1.0),
            ),
        ),
        resize_index=-1,
        use_pre_act=True,
        use_sigmoid=False,
        **kwargs,
    ) -> None:
        """DFF Head for various backbones.

        In the original implementation,
        - `use_pre_act` is set to False
        - `use_sigmoid` is set to False
        """
        super().__init__(
            input_transform="multiple_select",
            pred_key=pred_key,
            log_keys=log_keys,
            loss_decode=loss_decode,
            **kwargs,
        )

        self.resize_index = resize_index

        _interp = "bilinear"  # nearest
        _weight_bias = False
        _side_bias = False
        _last_bias = True

        # bias should not be turn on when some of the sides are not supervised

        sides = []
        for i in range(len(self.in_channels) - 1):
            sides.append(
                SideConv(
                    in_channels=self.in_channels[i],
                    out_channels=1,
                    conv_cfg=self.conv_cfg,
                    norm_cfg=self.norm_cfg,
                    bias=_side_bias,
                    act_cfg=self.act_cfg,
                    interpolation=_interp,
                    align_corners=self.align_corners,
                )
            )

        # last side is semantic
        sides.append(
            SideConv(
                in_channels=self.in_channels[-1],
                out_channels=self.num_classes,
                conv_cfg=self.conv_cfg,
                norm_cfg=self.norm_cfg,
                bias=_last_bias,
                act_cfg=self.act_cfg,
                interpolation=_interp,
                align_corners=self.align_corners,
            )
        )

        self.sides = nn.ModuleList(sides)

        self.side_w = SideConv(
            in_channels=self.in_channels[-1],
            out_channels=self.num_classes * 4,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            bias=_weight_bias,
            act_cfg=self.act_cfg,
            interpolation=_interp,
            align_corners=self.align_corners,
        )

        self.ada_learner = GeneralizedLocationAdaptiveLearner(
            num_sides=len(sides),
            in_channels=self.num_classes * 4,
            out_channels=self.num_classes * 4,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            act_cfg=self.act_cfg,
            use_pre_act=use_pre_act,
            use_sigmoid=use_sigmoid,
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

        last = side_outs[-1]

        side_outs.append(self.side_w(x[-1], resize_to))
        fuse = self.ada_learner(side_outs)

        return dict(fuse=fuse, last=last)


@MODELS.register_module()
class OGDFFHead(BaseEdgeDecodeHead):
    def __init__(
        self,
        pred_key="fuse",
        log_keys=("fuse", "last"),
        loss_decode=dict(
            mlbl=dict(
                fuse=dict(type="MultiLabelEdgeLoss", loss_weight=1.0),
                last=dict(type="MultiLabelEdgeLoss", loss_weight=1.0),
            ),
        ),
        **kwargs,
    ) -> None:
        super().__init__(
            input_transform="multiple_select",
            pred_key=pred_key,
            log_keys=log_keys,
            loss_decode=loss_decode,
            **kwargs,
        )

        assert not self.pass_input_image

        # Sides 1, 2, 3, 5 and Side 5 Weight
        self.side1 = OGSideConv(
            in_channels=self.in_channels[0],
            out_channels=1,
            rate=1,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            act_cfg=self.act_cfg,
        )
        self.side2 = OGSideConv(
            in_channels=self.in_channels[1],
            out_channels=1,
            rate=4,
            bias=True,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            act_cfg=self.act_cfg,
        )
        self.side3 = OGSideConv(
            in_channels=self.in_channels[2],
            out_channels=1,
            rate=8,
            bias=True,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            act_cfg=self.act_cfg,
        )
        self.side5 = OGSideConv(
            in_channels=self.in_channels[4],
            out_channels=self.num_classes,
            rate=16,
            bias=True,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            act_cfg=self.act_cfg,
        )
        self.side5_w = OGSideConv(
            in_channels=self.in_channels[4],
            out_channels=self.num_classes * 4,
            rate=16,
            bias=True,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            act_cfg=self.act_cfg,
        )

        self.ada_learner = LocationAdaptiveLearner(
            in_channels=self.num_classes * 4,
            out_channels=self.num_classes * 4,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            act_cfg=self.act_cfg,
            use_pre_act=False,
            use_sigmoid=False,
        )

    def forward(self, inputs):
        x = self._transform_inputs(inputs)
        assert len(x) == 4, f"Expect 4 inputs, got {len(x)}"

        side1 = self.side1(x[0])  # (B, 1, H, W)
        side2 = self.side2(x[1])  # (B, 1, H, W)
        side3 = self.side3(x[2])  # (B, 1, H, W)
        side5 = self.side5(x[3])  # (B, 19, H, W)
        side5_w = self.side5_w(x[3])  # (B, 19*4, H, W)

        fuse = self.ada_learner([side1, side2, side3, side5, side5_w])

        return dict(fuse=fuse, last=side5)
