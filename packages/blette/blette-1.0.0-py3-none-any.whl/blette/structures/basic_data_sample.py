#!/usr/bin/env python3

from mmengine.structures import BaseDataElement, PixelData


class BasicEdgeDataSample(BaseDataElement):
    """A data structure interface for edges.

    They are used as interfaces between different components.

    The attributes in ``BasicEdgeDataSample`` are divided into several parts:

        - ``gt_bin_edge``(PixelData): Ground truth binary edge.
        - ``gt_mlbl_edge``(PixelData): Ground truth multi-label (mlbl) edge.
        - ``pred_edge``(PixelData): Prediction of edge.
        - ``edge_logits``(PixelData): Predicted logits of edges.
    """

    @property
    def gt_bin_edge(self) -> PixelData:
        return self._gt_bin_edge

    @gt_bin_edge.setter
    def gt_bin_edge(self, value: PixelData) -> None:
        self.set_field(value, "_gt_bin_edge", dtype=PixelData)

    @gt_bin_edge.deleter
    def gt_bin_edge(self) -> None:
        del self._gt_bin_edge

    @property
    def gt_mlbl_edge(self) -> PixelData:
        return self._gt_mlbl_edge

    @gt_mlbl_edge.setter
    def gt_mlbl_edge(self, value: PixelData) -> None:
        self.set_field(value, "_gt_mlbl_edge", dtype=PixelData)

    @gt_mlbl_edge.deleter
    def gt_mlbl_edge(self) -> None:
        del self._gt_mlbl_edge

    @property
    def pred_edge(self) -> PixelData:
        return self._pred_edge

    @pred_edge.setter
    def pred_edge(self, value: PixelData) -> None:
        self.set_field(value, "_pred_edge", dtype=PixelData)

    @pred_edge.deleter
    def pred_edge(self) -> None:
        del self._pred_edge

    @property
    def edge_logits(self) -> PixelData:
        return self._edge_logits

    @edge_logits.setter
    def edge_logits(self, value: PixelData) -> None:
        self.set_field(value, "_edge_logits", dtype=PixelData)

    @edge_logits.deleter
    def bin_logits(self) -> None:
        del self._edge_logits
