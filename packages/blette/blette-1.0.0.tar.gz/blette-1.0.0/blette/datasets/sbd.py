#!/usr/bin/env python3

from typing import Dict, Optional, Sequence

from pyEdgeEval.datasets.sbd_attributes import (
    SBD_inst_labelIds,
    SBD_labelIds,
    SBD_label2trainId,
)

from blette.registry import DATASETS
from .base_edge_dataset import (
    MultiLabelEdgeDataset,
    OTFEdgeDataset,
)

SBD_CLASSES = (
    "aeroplane",
    "bicycle",
    "bird",
    "boat",
    "bottle",
    "bus",
    "car",
    "cat",
    "chair",
    "cow",
    "dining table",
    "dog",
    "horse",
    "motor bike",
    "person",
    "potted plant",
    "sheep",
    "sofa",
    "train",
    "tv/monitor",
)
SBD_PALETTE = [
    # [0, 0, 0],  # background
    [128, 0, 0],
    [0, 128, 0],
    [128, 128, 0],
    [0, 0, 128],
    [128, 0, 128],
    [0, 128, 128],
    [128, 128, 128],
    [64, 0, 0],
    [192, 0, 0],
    [64, 128, 0],
    [192, 128, 0],
    [64, 0, 128],
    [192, 0, 128],
    [64, 128, 128],
    [192, 128, 128],
    [0, 64, 0],
    [128, 64, 0],
    [0, 192, 0],
    [128, 192, 0],
    [0, 64, 128],
]
ignore_ids = [21]  # boundary pixels


@DATASETS.register_module()
class SBDDataset(MultiLabelEdgeDataset):
    METAINFO = dict(
        classes=SBD_CLASSES,
        palette=SBD_PALETTE,
    )

    def __init__(
        self,
        img_suffix: str = ".jpg",
        mlbl_edge_suffix: str = "_raw_edge.png",
        inst_sensitive: bool = True,
        thin: bool = False,
        reanno: bool = False,
        **kwargs,
    ) -> None:
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

        if reanno:
            mlbl_edge_suffix = "_reanno" + mlbl_edge_suffix
            kwargs["ann_file"] = "reanno_val.txt"

        super().__init__(
            img_suffix=img_suffix,
            mlbl_edge_suffix=mlbl_edge_suffix,
            **kwargs,
        )


@DATASETS.register_module()
class OTFSBDDataset(OTFEdgeDataset):
    METAINFO = dict(
        classes=SBD_CLASSES,
        palette=SBD_PALETTE,
    )

    def __init__(
        self,
        img_suffix: str = ".jpg",
        seg_map_suffix: str = "_labelIds.png",
        inst_map_suffix: str = "_instanceIds.png",
        labelIds: Optional[Sequence] = SBD_labelIds,
        inst_labelIds: Optional[Sequence] = SBD_inst_labelIds,
        ignore_indices: Optional[Sequence] = ignore_ids,
        label2trainId: Optional[Dict] = SBD_label2trainId,
        **kwargs,
    ) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            inst_map_suffix=inst_map_suffix,
            labelIds=labelIds,
            inst_labelIds=inst_labelIds,
            ignore_indices=ignore_indices,
            label2trainId=label2trainId,
            **kwargs,
        )
