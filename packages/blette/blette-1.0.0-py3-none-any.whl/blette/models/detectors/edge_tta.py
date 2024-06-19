#!/usr/bin/env python3

from typing import List

import torch
from mmengine.model import BaseTTAModel
from mmengine.structures import PixelData

from blette.registry import MODELS
from blette.structures import BasicEdgeDataSample
from blette.utils import SampleList


@MODELS.register_module()
class EdgeTTAModel(BaseTTAModel):
    def merge_preds(self, data_samples_list: List[SampleList]) -> SampleList:
        """Merge predictions of enhanced data to one prediction.

        Args:
            data_samples_list (List[SampleList]): List of predictions
                of all enhanced data.

        Returns:
            SampleList: Merged prediction.
        """
        predictions = []
        for data_samples in data_samples_list:
            edge_logits = data_samples[0].edge_logits.data

            logits = torch.zeros(edge_logits.shape).to(edge_logits)
            for data_sample in data_samples:
                edge_logit = data_sample.edge_logits.data

                # instead of argmax or softmax, just normalize
                logits += edge_logit.sigmoid()

            logits /= len(data_samples)

            if self.module.out_channels == 1:
                # binary
                edge_pred = (
                    (logits > self.module.decode_head.threshold).to(logits).squeeze(1)
                )
                # to (B, H, W)
                data_sample = BasicEdgeDataSample(
                    **{
                        "pred_edge": PixelData(data=edge_pred),
                        "edge_logits": PixelData(data=logits),
                        "gt_bin_edge": data_samples[0].gt_bin_edge,
                    }
                )
            else:
                # multi-label
                edge_pred = (logits > self.module.decode_head.threshold).to(logits)
                # to (B, C, H, W)
                data_sample = BasicEdgeDataSample(
                    **{
                        "pred_edge": PixelData(data=edge_pred),
                        "edge_logits": PixelData(data=logits),
                        "gt_mlbl_edge": data_samples[0].gt_mlbl_edge,
                    }
                )
            predictions.append(data_sample)

        return predictions
