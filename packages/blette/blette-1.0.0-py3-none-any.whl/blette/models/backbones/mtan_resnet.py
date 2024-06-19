#!/usr/bin/env python3

"""Two-task MTAN Backbone

- supports multiple versions of ResNet (not just R50)
"""

from copy import deepcopy

import torch
import torch.nn as nn

from mmengine.model import BaseModule, ModuleList, Sequential
from mmcv.cnn import build_conv_layer, build_norm_layer
from mmseg.models.backbones.resnet import Bottleneck

from blette.registry import MODELS
from .resnet import ResNet


def _unwrap_reslayer(reslayer):
    """Unwrap ResLayer

    ResLayer(Sequential) subclasses nn.Sequential -> changes __class__ to ResLayer
    resulting in Sequential to not be sliced correctly.
    """
    layers = []
    for i in range(len(reslayer)):
        layers.append(deepcopy(reslayer[i]))
    return layers


@MODELS.register_module()
class MTANResNet(BaseModule):
    """Two-task MTAN Backbone

    - supports multiple versions of ResNet (not just R50)
    - uses x1.5~ more memory than ResNet (more if you increase the number of tasks)
    """

    tasks = ("seg", "bin_edge", "ml_edge")

    def __init__(
        self,
        tasks=("bin_edge", "ml_edge"),
        init_cfg=None,
        mtan_init_cfg=None,
        **kwargs,
    ):
        super().__init__()
        self.tasks = tasks
        self.init_cfg = mtan_init_cfg

        resnet = ResNet(init_cfg=init_cfg, **kwargs)
        resnet.init_weights()

        # transfer attributes
        self.deep_stem = resnet.deep_stem
        self.conv_cfg = deepcopy(resnet.conv_cfg)
        self.norm_cfg = deepcopy(resnet.norm_cfg)
        self.return_stem = resnet.return_stem

        if self.deep_stem:
            self.stem = deepcopy(resnet.stem)
        else:
            self.conv1 = deepcopy(resnet.conv1)
            self.norm1 = deepcopy(resnet.norm1)
            self.relu = deepcopy(resnet.relu)
        self.maxpool = deepcopy(resnet.maxpool)

        # get input channels
        ch = [resnet.base_channels]
        for i in range(4):
            planes = resnet.base_channels * 2**i
            inplanes = planes * getattr(resnet, f"layer{i+1}")[0].expansion
            ch.append(inplanes)

        # unwrap ResLayer
        layer1 = _unwrap_reslayer(resnet.layer1)
        self.layer1_b = Sequential(*layer1[:-1])
        self.layer1_t = layer1[-1]
        layer2 = _unwrap_reslayer(resnet.layer2)
        self.layer2_b = Sequential(*layer2[:-1])
        self.layer2_t = layer2[-1]
        layer3 = _unwrap_reslayer(resnet.layer3)
        self.layer3_b = Sequential(*layer3[:-1])
        self.layer3_t = layer3[-1]
        layer4 = _unwrap_reslayer(resnet.layer4)
        self.layer4_b = Sequential(*layer4[:-1])
        self.layer4_t = layer4[-1]

        del resnet

        # Define task specific attention modules using a similar bottleneck design in residual block
        # (to avoid large computations)
        self.encoder_att_1 = ModuleList(
            [self.att_layer(ch[1], ch[1] // 4, ch[1]) for _ in self.tasks],
            init_cfg=self.init_cfg,
        )
        self.encoder_att_2 = ModuleList(
            [self.att_layer(2 * ch[2], ch[2] // 4, ch[2]) for _ in self.tasks],
            init_cfg=self.init_cfg,
        )
        self.encoder_att_3 = ModuleList(
            [self.att_layer(2 * ch[3], ch[3] // 4, ch[3]) for _ in self.tasks],
            init_cfg=self.init_cfg,
        )
        self.encoder_att_4 = ModuleList(
            [self.att_layer(2 * ch[4], ch[4] // 4, ch[4]) for _ in self.tasks],
            init_cfg=self.init_cfg,
        )

        # Define task shared attention encoders using residual bottleneck layers
        # We do not apply shared attention encoders at the last layer,
        # so the attended features will be directly fed into the task-specific decoders.
        self.encoder_block_att_1 = self.conv_layer(ch[1], ch[2] // 4)
        self.encoder_block_att_2 = self.conv_layer(ch[2], ch[3] // 4)
        self.encoder_block_att_3 = self.conv_layer(ch[3], ch[4] // 4)

        self.down_sampling = nn.MaxPool2d(kernel_size=2, stride=2)

    def init_weights(self):
        # TODO: better way to initialize weights
        pass

    def att_layer(self, in_channel, intermediate_channel, out_channel):
        return Sequential(
            build_conv_layer(
                self.conv_cfg,
                in_channels=in_channel,
                out_channels=intermediate_channel,
                kernel_size=1,
                padding=0,
            ),
            build_norm_layer(self.norm_cfg, intermediate_channel)[1],
            nn.ReLU(inplace=True),
            build_conv_layer(
                self.conv_cfg,
                in_channels=intermediate_channel,
                out_channels=out_channel,
                kernel_size=1,
                padding=0,
            ),
            build_norm_layer(self.norm_cfg, out_channel)[1],
            nn.Sigmoid(),
            # init_cfg=self.init_cfg,
        )

    def conv_layer(self, in_channel, out_channel):
        downsample = nn.Sequential(
            build_conv_layer(
                self.conv_cfg,
                in_channels=in_channel,
                out_channels=4 * out_channel,
                kernel_size=1,
                stride=1,
            ),
            build_norm_layer(self.norm_cfg, 4 * out_channel)[1],
        )
        return Bottleneck(
            inplanes=in_channel,
            planes=out_channel,
            downsample=downsample,
            conv_cfg=self.conv_cfg,
            norm_cfg=self.norm_cfg,
            init_cfg=self.init_cfg,
        )

    def forward(self, x):
        """Forward function."""

        if self.deep_stem:
            x = self.stem(x)
        else:
            x = self.conv1(x)
            x = self.norm1(x)
            x = self.relu(x)

        # before maxpool
        if self.return_stem:
            outs = [x]
        else:
            outs = []

        x = self.maxpool(x)

        # Shared ResNet block 1
        u1_b = self.layer1_b(x)
        u1_t = self.layer1_t(u1_b)

        # Shared ResNet block 2
        u2_b = self.layer2_b(u1_t)
        u2_t = self.layer2_t(u2_b)

        # Shared ResNet block 3
        u3_b = self.layer3_b(u2_t)
        u3_t = self.layer3_t(u3_b)

        # Shared ResNet block 4
        u4_b = self.layer4_b(u3_t)
        u4_t = self.layer4_t(u4_b)

        # Attention block 1 -> Apply attention over last residual block
        # Generate task specific attention map
        a1_mask = [att_i(u1_b) for att_i in self.encoder_att_1]
        # Apply task specific attention map to shared features
        a1 = [a1_mask_i * u1_t for a1_mask_i in a1_mask]
        outs.append(a1)
        a1 = [self.down_sampling(self.encoder_block_att_1(a1_i)) for a1_i in a1]

        # Attention block 2 -> Apply attention over last residual block
        a2_mask = [
            att_i(torch.cat((u2_b, a1_i), dim=1))
            for a1_i, att_i in zip(a1, self.encoder_att_2)
        ]
        a2 = [a2_mask_i * u2_t for a2_mask_i in a2_mask]
        outs.append(a2)
        a2 = [self.encoder_block_att_2(a2_i) for a2_i in a2]
        # a2 = [self.down_sampling(self.encoder_block_att_2(a2_i)) for a2_i in a2]

        # Attention block 3 -> Apply attention over last residual block
        a3_mask = [
            att_i(torch.cat((u3_b, a2_i), dim=1))
            for a2_i, att_i in zip(a2, self.encoder_att_3)
        ]
        a3 = [a3_mask_i * u3_t for a3_mask_i in a3_mask]
        outs.append(a3)
        a3 = [self.encoder_block_att_3(a3_i) for a3_i in a3]

        # Attention block 4 -> Apply attention over last residual block (without final encoder)
        a4_mask = [
            att_i(torch.cat((u4_b, a3_i), dim=1))
            for a3_i, att_i in zip(a3, self.encoder_att_4)
        ]
        a4 = [a4_mask_i * u4_t for a4_mask_i in a4_mask]
        outs.append(a4)

        return tuple(outs)
