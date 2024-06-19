#!/usr/bin/env python3

import os.path as osp

import numpy as np


def apply_mask(image: np.ndarray, mask: np.ndarray, color: np.ndarray):
    """Apply the given mask to the image."""
    for c in range(3):
        image[:, :, c] = np.where(mask == 1, image[:, :, c] + color[c], image[:, :, c])
    return image


def beautify_multilabel_edge(
    edges: np.ndarray,  # not batched (but has multiple classes)
    palette=None,
    beautify_threshold: float = 0.5,
) -> np.ndarray:
    """Colorize multi-label edge map."""
    n, h, w = edges.shape
    is_binary = n == 1

    if is_binary:
        raise ValueError("beautify cannot be applied in binary mode")

    if palette is None:
        # Get random state before set seed,
        # and restore random state later.
        # It will prevent loss of randomness, as the palette
        # may be different in each iteration if not specified.
        # See: https://github.com/open-mmlab/mmdetection/issues/5844
        state = np.random.get_state()
        np.random.seed(42)
        # random palette
        palette = np.random.randint(0, 255, size=(n, 3))
        np.random.set_state(state)
    palette = np.array(palette)
    assert palette.shape[0] == len(n)
    assert palette.shape[1] == 3
    assert len(palette.shape) == 2
    assert 0 < beautify_threshold < 1

    out = np.zeros((h, w, 3))
    edges = np.where(edges >= beautify_threshold, 1, 0).astype(bool)
    edge_sum = np.zeros((h, w))

    for i in range(n):
        color = palette[i]
        edge = edges[i, :, :]
        edge_sum = edge_sum + edge
        masked_out = apply_mask(out, edge, color)

    edge_sum = np.array([edge_sum, edge_sum, edge_sum])
    edge_sum = np.transpose(edge_sum, (1, 2, 0))
    idx = edge_sum > 0
    masked_out[idx] = masked_out[idx] / edge_sum[idx]
    masked_out[~idx] = 255

    out = masked_out.astype(np.uint8)

    return out
