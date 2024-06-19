#!/usr/bin/env python3

"""General evaluation protocols for Synthia Semantic Boundary Benchmark

- should work because Synthia is based on cityscapes labels

TODO: make half evaluation
"""

import argparse
import os.path as osp
import time

from pyEdgeEval.evaluators import CityscapesEvaluator
from pyEdgeEval.utils import get_root_logger, mkdir_or_exist, print_log


class SynthiaEvaluator(CityscapesEvaluator):
    GT_DIR = "gtEval"

    RAW_EDGE_SUFFIX = "_raw_edge.png"
    THIN_EDGE_SUFFIX = "_thin_edge.png"
    RAW_ISEDGE_SUFFIX = "_raw_isedge.png"
    THIN_ISEDGE_SUFFIX = "_thin_isedge.png"

    SEG_SUFFIX = "_trainIds.png"
    PRED_SUFFIX = ".png"

    def __init__(
        self,
        dataset_root: str,
        pred_root: str,
        split: str = "val",
        thin: bool = False,
        gt_dir=None,
        pred_suffix=None,
        **kwargs,
    ):
        self.dataset_root = dataset_root
        self.pred_root = pred_root

        assert split in ("val", "test")
        self.split = split
        self.thin = thin
        if self.thin:
            print_log(
                "Using `thin` mode; setting the suffix respectively",
                logger=self._logger,
            )
            self.EDGE_SUFFIX = self.THIN_EDGE_SUFFIX
            self.ISEDGE_SUFFIX = self.THIN_ISEDGE_SUFFIX
        else:
            print_log(
                "Using `raw` mode; setting the suffix respectively",
                logger=self._logger,
            )
            self.EDGE_SUFFIX = self.RAW_EDGE_SUFFIX
            self.ISEDGE_SUFFIX = self.RAW_ISEDGE_SUFFIX

        # change dataset directory and suffix
        if gt_dir:
            print_log(f"changing GT_DIR to {gt_dir}", logger=self._logger)
            self.GT_DIR = gt_dir
        if pred_suffix:
            print_log(f"changing PRED_SUFFIX to {pred_suffix}", logger=self._logger)
            self.PRED_SUFFIX = pred_suffix

        # set parameters
        self.gtEval_root = osp.join(self.dataset_root, self.GT_DIR)

        # we can try to load some sample names
        try:
            self.set_sample_names()
        except Exception:
            print_log(
                "Tried to set sample_names, but couldn't",
                logger=self._logger,
            )

    def set_sample_names(self, sample_names=None, split_file=None):
        """priortizes `sample_names` more than `split_file`"""
        if sample_names is None:
            # load sample_names from split file
            if split_file is None:
                split_file = osp.join(self.dataset_root, f"splits/{self.split}.txt")

            assert osp.exists(split_file), f"ERR: {split_file} does not exist!"

            print_log(f"Loading samples from {split_file}", logger=self._logger)
            with open(split_file, "r") as f:
                sample_names = f.read().splitlines()

        assert isinstance(
            sample_names, list
        ), f"ERR: sample_names should be a list but got {type(sample_names)}"
        assert len(sample_names) > 0, "ERR: sample_names is empty"
        self._sample_names = (
            sample_names  # setting new object to potentially mutable attribute
        )

    def _before_evaluation(self):
        assert (
            self._sample_names is not None
        ), "ERR: no samples yet. load them before evaluation"
        assert osp.exists(self.dataset_root), f"ERR: {self.dataset_root} does not exist"
        assert osp.exists(self.gtEval_root), f"ERR: {self.gtEval_root} does not exist"
        assert osp.exists(self.pred_root), f"ERR: {self.pred_root} does not exist"


def parse_args():
    parser = argparse.ArgumentParser("Synthia evaluation parser")
    parser.add_argument(
        "synthia_path",
        type=str,
        help="the root path of the Synthia dataset",
    )
    parser.add_argument(
        "pred_path",
        type=str,
        help="the root path of the predictions",
    )
    parser.add_argument(
        "--output-path",
        type=str,
        help="the root path of where the results are populated",
    )
    parser.add_argument(
        "--categories",
        type=str,
        help="the category number to evaluate; can be multiple values'[1, 14]'",
    )
    parser.add_argument(
        "--split",
        type=str,
        default="val",
        help="(val, test)",
    )
    parser.add_argument(
        "--pre-seal",
        action="store_true",
        help="prior to SEAL, the evaluations were not as strict",
    )
    parser.add_argument(
        "--nonIS",
        action="store_true",
        help="non instance sensitive evaluation",
    )
    parser.add_argument(
        "--max-dist",
        type=float,
        default=0.0035,
        help="tolerance distance (default: 0.0035)",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=1.0,
        help="scale of the data for evaluations",
    )
    parser.add_argument(
        "--thresholds",
        type=str,
        default="99",
        help="the number of thresholds (could be a list of floats); use 99 for eval",
    )
    parser.add_argument(
        "--thin",
        action="store_true",
        help="Use thin evaluation protocol",
    )
    parser.add_argument(
        "--apply-nms",
        action="store_true",
        help="applies NMS before evaluation",
    )
    parser.add_argument(
        "--nproc",
        type=int,
        default=4,
        help="the number of parallel threads",
    )
    return parser.parse_args()


def evaluate(
    gt_dir: str,
    synthia_path: str,
    pred_path: str,
    output_path: str,
    categories: str,
    split: str,
    thin: bool,
    pre_seal: bool,
    nonIS: bool,
    max_dist: float,
    scale: float,
    apply_thinning: bool,
    apply_nms: bool,
    thresholds: str,
    nproc: int,
):
    """Evaluate Synthia"""

    if categories is None:
        print("use all categories")
        categories = list(range(1, len(SynthiaEvaluator.CLASSES) + 1))
    else:
        # string evaluation for categories
        categories = categories.strip()
        try:
            categories = [int(categories)]
        except ValueError:
            try:
                if categories.startswith("[") and categories.endswith("]"):
                    categories = categories[1:-1]
                    categories = [int(cat.strip()) for cat in categories.split(",")]
                else:
                    print(
                        "Bad categories format; should be a python list of floats (`[a, b, c]`)"
                    )
                    return
            except ValueError:
                print(
                    "Bad categories format; should be a python list of ints (`[a, b, c]`)"
                )
                return

    for cat in categories:
        assert 0 < cat < 20, f"category needs to be between 1 ~ 19, but got {cat}"

    # string evaluation for thresholds
    thresholds = thresholds.strip()
    try:
        n_thresholds = int(thresholds)
        thresholds = n_thresholds
    except ValueError:
        try:
            if thresholds.startswith("[") and thresholds.endswith("]"):
                thresholds = thresholds[1:-1]
                thresholds = [float(t.strip()) for t in thresholds.split(",")]
            else:
                print(
                    "Bad threshold format; should be a python list of floats (`[a, b, c]`)"
                )
                return
        except ValueError:
            print("Bad threshold format; should be a python list of ints (`[a, b, c]`)")
            return

    # generate output_path if given None
    if output_path is None:
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        output_path = osp.join(osp.normpath(pred_path), f"edge_results_{timestamp}")

    mkdir_or_exist(output_path)

    # setup logger
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    log_file = osp.join(output_path, f"{timestamp}.log")
    logger = get_root_logger(log_file=log_file, log_level="INFO")
    logger.info("Running Synthia Evaluation")
    logger.info(f"categories:         \t{categories}")
    logger.info(f"thresholds:         \t{thresholds}")
    logger.info(f"scale:              \t{scale}")
    logger.info(f"pre-seal:           \t{pre_seal}")
    logger.info(f"thinned GTs:        \t{thin}")
    logger.info(f"thinning:           \t{apply_thinning}")
    logger.info(f"nms:                \t{apply_nms}")
    logger.info(f"nonIS:              \t{nonIS}")
    logger.info(f"GT directory:       \t{gt_dir}")
    logger.info(f"split:              \t{split}")
    print("\n\n")

    # initialize evaluator
    evaluator = SynthiaEvaluator(
        dataset_root=synthia_path,
        pred_root=pred_path,
        thin=thin,
        gt_dir=gt_dir,  # NOTE: we can change the directory where the preprocessed GTs are
        split=split,
    )
    evaluator.gtEval_root = osp.join(evaluator.dataset_root, evaluator.GT_DIR)
    if evaluator.sample_names is None:
        evaluator.set_sample_names()

    # set parameters
    # evaluator.set_pred_suffix("_leftImg8bit.png")  # potato save them using .png
    eval_mode = "pre-seal" if pre_seal else "post-seal"
    instance_sensitive = not nonIS
    evaluator.set_eval_params(
        eval_mode=eval_mode,
        scale=scale,
        apply_thinning=apply_thinning,
        apply_nms=apply_nms,
        max_dist=max_dist,
        instance_sensitive=instance_sensitive,
    )

    # evaluate
    evaluator.evaluate(
        categories=categories,
        thresholds=thresholds,
        nproc=nproc,
        save_dir=output_path,
    )
