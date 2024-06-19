#!/usr/bin/env python3

from typing import List, Optional, Union

import numpy as np
import torch
import torch.nn.functional as F

from .typing_utils import SampleList


def stack_batch(
    inputs: List[torch.Tensor],
    data_samples: Optional[SampleList] = None,
    size: Optional[tuple] = None,
    size_divisor: Optional[int] = None,
    pad_val: Union[int, float] = 0,
    edge_pad_val: Union[int, float] = 0,
) -> torch.Tensor:
    """Stack multiple inputs to form a batch and pad the images and gt_bin_edge
    and gt_mlbl_edge to the max shape use the right bottom padding mode.

    Args:
        inputs (List[Tensor]): The input multiple tensors. each is a
            CHW 3D-tensor.
        data_samples (list[:obj:`BasicEdgeDataSample`]): The list of data samples.
            It usually includes information such as `gt_bin_edge`.
        size (tuple, optional): Fixed padding size.
        size_divisor (int, optional): The divisor of padded size.
        pad_val (int, float): The padding value. Defaults to 0
        edge_pad_val (int, float): The padding value. Defaults to 0

    Returns:
        Tensor: The 4D-tensor.
        List[:obj:`BasicEdgeDataSample`]: After the padding of the gt_edges.
    """
    assert isinstance(
        inputs, list
    ), f"Expected input type to be list, but got {type(inputs)}"
    assert len({tensor.ndim for tensor in inputs}) == 1, (
        f"Expected the dimensions of all inputs must be the same, "
        f"but got {[tensor.ndim for tensor in inputs]}"
    )
    assert inputs[0].ndim == 3, (
        f"Expected tensor dimension to be 3, " f"but got {inputs[0].ndim}"
    )
    assert len({tensor.shape[0] for tensor in inputs}) == 1, (
        f"Expected the channels of all inputs must be the same, "
        f"but got {[tensor.shape[0] for tensor in inputs]}"
    )

    # only one of size and size_divisor should be valid
    assert (size is not None) ^ (
        size_divisor is not None
    ), "only one of size and size_divisor should be valid"

    padded_inputs = []
    padded_samples = []
    inputs_sizes = [(img.shape[-2], img.shape[-1]) for img in inputs]
    max_size = np.stack(inputs_sizes).max(0)
    if size_divisor is not None and size_divisor > 1:
        # the last two dims are H,W, both subject to divisibility requirement
        max_size = (max_size + (size_divisor - 1)) // size_divisor * size_divisor

    for i in range(len(inputs)):
        tensor = inputs[i]
        if size is not None:
            width = max(size[-1] - tensor.shape[-1], 0)
            height = max(size[-2] - tensor.shape[-2], 0)
            # (padding_left, padding_right, padding_top, padding_bottom)
            padding_size = (0, width, 0, height)
        elif size_divisor is not None:
            width = max(max_size[-1] - tensor.shape[-1], 0)
            height = max(max_size[-2] - tensor.shape[-2], 0)
            padding_size = (0, width, 0, height)
        else:
            padding_size = [0, 0, 0, 0]

        # pad img
        pad_img = F.pad(tensor, padding_size, value=pad_val)
        padded_inputs.append(pad_img)

        # pad gt_edges
        if data_samples is not None:
            data_sample = data_samples[i]
            if "gt_bin_edge" in data_sample:
                gt_bin_edge = data_sample.gt_bin_edge.data
                del data_sample.gt_bin_edge.data
                data_sample.gt_bin_edge.data = F.pad(
                    gt_bin_edge, padding_size, value=edge_pad_val
                )
            if "gt_mlbl_edge" in data_sample:
                gt_mlbl_edge = data_sample.gt_mlbl_edge.data
                del data_sample.gt_mlbl_edge.data
                data_sample.gt_mlbl_edge.data = F.pad(
                    gt_mlbl_edge, padding_size, value=edge_pad_val
                )

            data_sample.set_metainfo(
                {
                    "img_shape": tensor.shape[-2:],
                    "pad_shape": pad_img.shape,  # use the same size as the transforms
                    "padding_size": padding_size,
                }
            )
            padded_samples.append(data_sample)
        else:
            padded_samples.append(
                dict(img_padding_size=padding_size, pad_shape=pad_img.shape[-2:])
            )

    return torch.stack(padded_inputs, dim=0), padded_samples
