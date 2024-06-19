#!/usr/bin/env python3

from typing import Dict, Optional, Sequence

from blette.registry import DATASETS
from .base_edge_dataset import (
    MultiLabelEdgeDataset,
    OTFEdgeDataset,
)

BDD100K_CLASSES = (
    "road",
    "sidewalk",
    "building",
    "wall",
    "fence",
    "pole",
    "traffic light",
    "traffic sign",
    "vegetation",
    "terrain",
    "sky",
    "person",
    "rider",
    "car",
    "truck",
    "bus",
    "train",
    "motorcycle",
    "bicycle",
)
BDD100K_PALETTE = [
    [128, 64, 128],
    [244, 35, 232],
    [70, 70, 70],
    [102, 102, 156],
    [190, 153, 153],
    [153, 153, 153],
    [250, 170, 30],
    [220, 220, 0],
    [107, 142, 35],
    [152, 251, 152],
    [70, 130, 180],
    [220, 20, 60],
    [255, 0, 0],
    [0, 0, 142],
    [0, 0, 70],
    [0, 60, 100],
    [0, 80, 100],
    [0, 0, 230],
    [119, 11, 32],
]
ignore_ids = [19]  # border pixels (5px)
BDD100K_labelIds = list(range(20))  # adds border pixels
BDD100K_label2trainId = {
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
BDD100K_inst_labelIds = [
    11,  # "person"
    12,  # "rider"
    13,  # "car"
    14,  # "truck"
    15,  # "bus"
    16,  # "train"
    17,  # "motorcycle"
    18,  # "bicycle"
]


@DATASETS.register_module()
class BDD100KDataset(MultiLabelEdgeDataset):
    METAINFO = dict(
        classes=BDD100K_CLASSES,
        palette=BDD100K_PALETTE,
    )

    def __init__(
        self,
        img_suffix: str = ".jpg",
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
class OTFBDD100KDataset(OTFEdgeDataset):
    METAINFO = dict(
        classes=BDD100K_CLASSES,
        palette=BDD100K_PALETTE,
    )

    def __init__(
        self,
        img_suffix: str = ".jpg",
        seg_map_suffix: str = "_labelIds.png",
        inst_map_suffix: str = "_instanceIds.png",
        inst_sensitive: bool = True,  # default instance sensitive
        labelIds: Optional[Sequence] = BDD100K_labelIds,
        inst_labelIds: Optional[Sequence] = BDD100K_inst_labelIds,
        ignore_indicies: Optional[Sequence] = [19],
        label2trainId: Optional[Dict] = BDD100K_label2trainId,
        **kwargs,
    ) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            inst_map_suffix=inst_map_suffix,
            inst_sensitive=inst_sensitive,
            labelIds=labelIds,
            inst_labelIds=inst_labelIds,
            ignore_indices=ignore_indicies,
            label2trainId=label2trainId,
            **kwargs,
        )
