#!/usr/bin/env python3

from blette.registry import DATASETS
from .base_edge_dataset import BinaryEdgeDataset


@DATASETS.register_module()
class BSDS500Dataset(BinaryEdgeDataset):
    METAINFO = dict(
        classes=("edge",),
        palette=[[102, 255, 0]],
    )

    def __init__(
        self,
        img_suffix: str = ".jpg",
        bin_edge_suffix: str = ".png",
        **kwargs,
    ) -> None:
        super().__init__(
            img_suffix=img_suffix,
            bin_edge_suffix=bin_edge_suffix,
            **kwargs,
        )
