#!/usr/bin/env python3

"""Precision Recall.

This metric module is also being used to save the results for
pyEdgeEval with `format_only=True`
"""

import os.path as osp
from collections import OrderedDict
from typing import Dict, List, Optional, Sequence

import numpy as np
import torch
from mmengine.dist import is_main_process
from mmengine.evaluator import BaseMetric
from mmengine.logging import MMLogger, print_log
from mmengine.utils import mkdir_or_exist
from prettytable import PrettyTable

from blette.registry import METRICS
from blette.apis.utils import format_results_for_pyEdgeEval


@METRICS.register_module()
class PrecisionRecallMetric(BaseMetric):
    """Precision and Recall evaluation metric.

    Args:
        ignore_index (int): Index that will be ignored in evaluation.
            Default: 255.
        metrics (list[str] | str): ["mFscore]
        nan_to_num (int, optional): If specified, NaN values will be replaced
            by the numbers defined by the user. Default: None.
        collect_device (str): Device name used for collecting results from
            different ranks during distributed training. Must be 'cpu' or
            'gpu'. Defaults to 'cpu'.
        output_dir (str): The directory for output prediction. Defaults to
            None.
        format_only (bool): Only format result for results commit without
            perform evaluation. It is useful when you want to save the result
            to a specific format and submit it to the test server.
            Defaults to False.
        prefix (str, optional): The prefix that will be added in the metric
            names to disambiguate homonymous metrics of different evaluators.
            If prefix is not provided in the argument, self.default_prefix
            will be used instead. Defaults to None.
    """

    def __init__(
        self,
        ignore_index: int = 255,
        binary: bool = False,
        threshold: float = 0.7,
        metrics: List[str] = ["mFscore"],
        nan_to_num: Optional[int] = None,
        collect_device: str = "cpu",
        output_dir: Optional[str] = None,
        format_only: bool = False,
        prefix: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(collect_device=collect_device, prefix=prefix)

        self.ignore_index = ignore_index
        self.binary = binary
        self.threshold = threshold
        self.metrics = metrics
        self.nan_to_num = nan_to_num
        self.output_dir = output_dir
        if self.output_dir and is_main_process():
            mkdir_or_exist(self.output_dir)
        self.format_only = format_only

    def process(self, data_batch: dict, data_samples: Sequence[dict]) -> None:
        """Process one batch of data and data_samples.

        The processed results should be stored in ``self.results``, which will
        be used to compute the metrics when all batches have been processed.

        Args:
            data_batch (dict): A batch of data from the dataloader.
            data_samples (Sequence[dict]): A batch of outputs from the model.
        """
        num_classes = len(self.dataset_meta["classes"])
        for data_sample in data_samples:

            edge_prob = data_sample["pred_edge"]["data"].squeeze()

            # format_only always for test dataset without ground truth
            if not self.format_only:
                if self.binary:
                    label = data_sample["gt_bin_edge"]["data"].squeeze().to(edge_prob)
                    self.results.append(
                        self.pre_calc(edge_prob, label, 1, self.threshold)
                    )
                else:
                    label = data_sample["gt_mlbl_edge"]["data"].squeeze().to(edge_prob)
                    self.results.append(
                        self.pre_calc(edge_prob, label, num_classes, self.threshold)
                    )

            # format_result
            if self.output_dir is not None:
                basename = osp.splitext(osp.basename(data_sample["img_path"]))[0]
                edge_prob = edge_prob.cpu().numpy()

                format_results_for_pyEdgeEval(
                    edge_prob,
                    out_dir=self.output_dir,
                    out_prefix=basename,
                )

    def compute_metrics(self, results: list) -> Dict[str, float]:
        """Compute the metrics from processed results.

        Args:
            results (list): The processed results of each batch.

        Returns:
            Dict[str, float]: The computed metrics. The keys are the names of
                the metrics, and the values are corresponding results. The key
                mainly includes aAcc, mIoU, mAcc, mDice, mFscore, mPrecision,
                mRecall.
        """
        logger: MMLogger = MMLogger.get_current_instance()
        if self.format_only:
            logger.info(f"results are saved to {osp.dirname(self.output_dir)}")
            return OrderedDict()

        # convert list of tuples to tuple of lists, e.g.
        # [(A_1, B_1, C_1, D_1), ...,  (A_n, B_n, C_n, D_n)] to
        # ([A_1, ..., A_n], ..., [D_1, ..., D_n])

        pre_eval_results = tuple(zip(*results))
        assert len(pre_eval_results) == 4
        all_tp = sum(pre_eval_results[0])
        all_preds = sum(pre_eval_results[1])
        all_targets = sum(pre_eval_results[2])
        all_acc = sum(pre_eval_results[3]) / len(pre_eval_results[3])

        ret_metrics = self.pre_eval_to_metrics(
            all_tp,
            all_preds,
            all_targets,
            all_acc,
            self.metrics,
            self.nan_to_num,
        )

        class_names = self.dataset_meta["classes"]

        # summary table
        ret_metrics_summary = OrderedDict(
            {
                ret_metric: np.round(np.nanmean(ret_metric_value) * 100, 2)
                for ret_metric, ret_metric_value in ret_metrics.items()
            }
        )
        metrics = dict()
        for key, val in ret_metrics_summary.items():
            if key == "aAcc":
                metrics[key] = val
            else:
                metrics["m" + key] = val

        # each class table
        ret_metrics.pop("aAcc", None)
        ret_metrics_class = OrderedDict(
            {
                ret_metric: np.round(ret_metric_value * 100, 2)
                for ret_metric, ret_metric_value in ret_metrics.items()
            }
        )
        ret_metrics_class.update({"Class": class_names})
        ret_metrics_class.move_to_end("Class", last=False)
        class_table_data = PrettyTable()
        for key, val in ret_metrics_class.items():
            class_table_data.add_column(key, val)

        print_log("per class results:", logger)
        print_log("\n" + class_table_data.get_string(), logger=logger)

        return metrics

    @staticmethod
    def pre_calc(
        pred: torch.Tensor,
        label: torch.Tensor,
        num_classes: int,
        thresh: float = 0.7,
    ):
        tp = torch.zeros((num_classes,), dtype=torch.float64)
        preds = torch.zeros((num_classes,), dtype=torch.float64)
        targets = torch.zeros((num_classes,), dtype=torch.float64)
        acc = torch.zeros((num_classes,), dtype=torch.float64)

        # pred = torch.from_numpy(result)
        # label = torch.from_numpy(gt_edge_map)

        # FIXME: very ugly
        if num_classes == 1:
            if pred.ndim == 2:
                pred = pred.unsqueeze(0)
            if label.ndim == 2:
                label = label.unsqueeze(0)

        assert pred.shape == label.shape
        assert pred.ndim == 3

        # print('pred', pred.shape)
        # print('label', label.shape)

        # threshold
        t_pred = pred > thresh
        t_label = label > thresh

        for i in range(num_classes):
            _pred = t_pred[i]
            _label = t_label[i]

            tp[i] = _pred[_pred == _label].sum()
            preds[i] = _pred.sum()
            targets[i] = _label.sum()
            acc[i] = _pred.eq(_label).sum() / _label.numel()
            # print(_label.numel(), acc[i])

        return (tp, preds, targets, acc)

    @staticmethod
    def pre_eval_to_metrics(
        all_tp,
        all_preds,
        all_targets,
        all_acc,
        metrics=["mFscore"],
        nan_to_num: Optional[int] = None,
    ):
        def f_score(precision, recall, beta=1):
            """calculate the f-score value.

            Args:
                precision (float | torch.Tensor): The precision value.
                recall (float | torch.Tensor): The recall value.
                beta (int): Determines the weight of recall in the combined
                    score. Default: 1.

            Returns:
                [torch.tensor]: The f-score value.
            """
            score = (
                (1 + beta**2) * (precision * recall) / ((beta**2 * precision) + recall)
            )
            return score

        num_classes = len(all_acc)

        # organize metrics that we should return
        g_acc = all_acc.sum() / num_classes
        ret_metrics = OrderedDict({"aAcc": g_acc})
        for metric in metrics:
            if metric == "mFscore":
                # ret_metrics["Acc"] = all_acc

                prec = all_tp / all_preds
                rec = all_tp / all_targets
                f1 = 2 * (prec * rec) / (prec + rec)

                # f_value = torch.tensor([f_score(x[0], x[1]) for x in zip(prec, rec)])

                ret_metrics["Precision"] = prec
                ret_metrics["Recall"] = rec
                ret_metrics["Fscore"] = f1

        ret_metrics = {metric: value.numpy() for metric, value in ret_metrics.items()}

        if nan_to_num is not None:
            ret_metrics = OrderedDict(
                {
                    metric: np.nan_to_num(metric_value, nan=nan_to_num)
                    for metric, metric_value in ret_metrics.items()
                }
            )

        return ret_metrics
