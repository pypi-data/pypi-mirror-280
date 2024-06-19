#!/usr/bin/env python3

import torch
import torch.nn as nn
import torch.nn.functional as F
from mmseg.structures.sampler.base_pixel_sampler import BasePixelSampler

from blette.registry import TASK_UTILS


@TASK_UTILS.register_module()
class OHEMEdgePixelSampler(BasePixelSampler):
    """Online Hard Example Mining Sampler for edge detection.

    Args:
        context (nn.Module): The context of sampler, subclass of
            :obj:`BaseDecodeHead`.
        thresh (float, optional): The threshold for hard example selection.
            Below which, are prediction with low confidence. If not
            specified, the hard examples will be pixels of top ``min_kept``
            loss. Default: None.
        min_kept (int, optional): The minimum number of predictions to keep.
            Default: 100000.
    """

    def __init__(self, context, thresh=None, min_kept=100000):
        super().__init__()
        self.context = context
        assert min_kept > 1
        self.thresh = thresh
        self.min_kept = min_kept

    def sample(self, edge_logit, edge_label):
        """Sample pixels that have high loss or with low prediction confidence.

        Args:
            edge_logit (torch.Tensor): edge logits, shape (N, C, H, W)
            edge_label (torch.Tensor): edge label, shape (N, 1, H, W)

        Returns:
            torch.Tensor: edge weight, shape (N, H, W)
        """
        with torch.no_grad():
            assert edge_logit.shape[2:] == edge_label.shape[2:]
            assert edge_label.shape[1] == 1
            edge_label = edge_label.squeeze(1).long()
            batch_kept = self.min_kept * edge_label.size(0)
            valid_mask = edge_label != self.context.ignore_index
            edge_weight = edge_logit.new_zeros(size=edge_label.size())
            valid_edge_weight = edge_weight[valid_mask]
            if self.thresh is not None:
                edge_prob = F.softmax(edge_logit, dim=1)

                tmp_edge_label = edge_label.clone().unsqueeze(1)
                tmp_edge_label[tmp_edge_label == self.context.ignore_index] = 0
                edge_prob = edge_prob.gather(1, tmp_edge_label).squeeze(1)
                sort_prob, sort_indices = edge_prob[valid_mask].sort()

                if sort_prob.numel() > 0:
                    min_threshold = sort_prob[min(batch_kept, sort_prob.numel() - 1)]
                else:
                    min_threshold = 0.0
                threshold = max(min_threshold, self.thresh)
                valid_edge_weight[edge_prob[valid_mask] < threshold] = 1.0
            else:
                if not isinstance(self.context.loss_decode, nn.ModuleList):
                    losses_decode = [self.context.loss_decode]
                else:
                    losses_decode = self.context.loss_decode
                losses = 0.0
                for loss_module in losses_decode:
                    losses += loss_module(
                        edge_logit,
                        edge_label,
                        weight=None,
                        ignore_index=self.context.ignore_index,
                        reduction_override="none",
                    )

                # faster than topk according to https://github.com/pytorch/pytorch/issues/22812  # noqa
                _, sort_indices = losses[valid_mask].sort(descending=True)
                valid_edge_weight[sort_indices[:batch_kept]] = 1.0

            edge_weight[valid_mask] = valid_edge_weight

            return edge_weight
