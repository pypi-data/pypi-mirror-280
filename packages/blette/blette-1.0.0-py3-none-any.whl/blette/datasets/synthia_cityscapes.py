#!/usr/bin/env python3

from typing import Dict, Optional, Sequence

from blette.registry import DATASETS
from .base_edge_dataset import (
    MultiLabelEdgeDataset,
    OTFEdgeDataset,
)
from .cityscapes import CITYSCAPES_CLASSES, CITYSCAPES_PALETTE

SYNTHIA_labelIds = list(range(20))
SYNTHIA_label2trainId = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    15: 15,
    16: 16,
    17: 17,
    18: 18,
}
SYNTHIA_inst_labelIds = [
    11,  # pedestrian
    12,  # rider
    13,  # car
    14,  # truck
    15,  # bus
    16,  # train
    17,  # motorcycle
    18,  # bicycle
]


@DATASETS.register_module()
class SynthiaDataset(MultiLabelEdgeDataset):
    METAINFO = dict(
        classes=CITYSCAPES_CLASSES,
        palette=CITYSCAPES_PALETTE,
    )

    def __init__(
        self,
        img_suffix: str = ".png",
        mlbl_edge_suffix: str = "_raw_edge.png",
        inst_sensitive: bool = True,
        thin: bool = False,
        test_mode: bool = False,
        **kwargs,
    ) -> None:
        if test_mode:
            if inst_sensitive:
                if thin:
                    mlbl_edge_suffix = "_thin_isedge.png"
                else:
                    mlbl_edge_suffix = "_raw_isedge.png"
            else:
                if thin:
                    mlbl_edge_suffix = "_thin_edge.png"
                else:
                    mlbl_edge_suffix = "_raw_edge.png"
        else:
            if inst_sensitive:
                mlbl_edge_suffix = "_isedge.png"
            else:
                mlbl_edge_suffix = "_edge.png"

        super().__init__(
            img_suffix=img_suffix,
            mlbl_edge_suffix=mlbl_edge_suffix,
            test_mode=test_mode,
            **kwargs,
        )


@DATASETS.register_module()
class OTFSynthiaDataset(OTFEdgeDataset):
    METAINFO = dict(
        classes=CITYSCAPES_CLASSES,
        palette=CITYSCAPES_PALETTE,
    )

    def __init__(
        self,
        img_suffix: str = ".png",
        seg_map_suffix: str = "_labelIds.png",
        inst_map_suffix: str = "_instanceIds.png",
        labelIds: Optional[Sequence] = SYNTHIA_labelIds,
        inst_labelIds: Optional[Sequence] = SYNTHIA_inst_labelIds,
        ignore_indicies: Optional[Sequence] = [],
        label2trainId: Optional[Dict] = SYNTHIA_label2trainId,
        **kwargs,
    ) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            inst_map_suffix=inst_map_suffix,
            labelIds=labelIds,
            inst_labelIds=inst_labelIds,
            ignore_indices=ignore_indicies,
            label2trainId=label2trainId,
            **kwargs,
        )
