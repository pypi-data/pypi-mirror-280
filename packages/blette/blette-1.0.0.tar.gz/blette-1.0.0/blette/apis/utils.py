#!/usr/bin/env python3

import os.path as osp
from copy import deepcopy

import numpy as np
from PIL import Image

from mmengine.utils import mkdir_or_exist


def format_results_for_pyEdgeEval(
    edges: np.ndarray,
    out_dir: str,
    out_prefix: str,
) -> None:

    if edges.ndim == 2:
        is_binary = True
    elif edges.ndim == 3:
        if edges.shape[0] == 1:
            edges = edges.squeeze(0)
            is_binary = True
        else:
            is_binary = False
    elif edges.ndim == 4:
        assert edges.shape[0] == 1, "Only support one image at a time"
        edges = edges.squeeze(0)
    else:
        raise ValueError(f"Unsupported shape {edges.shape}")

    if is_binary:
        # we can try to save in a directory that is easy to see
        # but classes can have spaces, which makes it complicated for
        # pyEdgeEval
        out_file = osp.join(
            out_dir,
            out_prefix + ".png",
        )

        mkdir_or_exist(osp.dirname(out_file))

        # assuming edge is 0 ~ 1
        edges = (edges * 255).astype(np.uint8)

        out = Image.fromarray(edges)
        out.save(out_file)
    else:
        num_classes, h, w = edges.shape
        for c in range(num_classes):

            # we can try to save in a directory that is easy to see
            # but classes can have spaces, which makes it complicated for
            # pyEdgeEval
            # out_file = osp.join(
            #     out_dir,
            #     f"class_{c + 1}",  # NOTE: start from 1
            #     out_prefix + ".png",
            # )
            # NOTE: requires zfill filepath
            out_file = osp.join(
                out_dir,
                f"class_{str(c + 1).zfill(3)}",
                out_prefix + ".png",
            )

            mkdir_or_exist(osp.dirname(out_file))

            edge = deepcopy(edges[c])

            # assuming edge is 0 ~ 1
            edge = (edge * 255).astype(np.uint8)

            out = Image.fromarray(edge)
            out.save(out_file)
