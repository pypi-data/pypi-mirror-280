#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from mmengine.model import BaseModel
from mmengine.structures import PixelData
from mmseg.models.utils import resize
from torch import Tensor

from blette.structures import BasicEdgeDataSample
from blette.utils import (
    ForwardResults,
    OptConfigType,
    OptMultiConfig,
    OptSampleList,
    SampleList,
)


class BaseEdgeDetector(BaseModel, metaclass=ABCMeta):
    def __init__(
        self, data_preprocessor: OptConfigType = None, init_cfg: OptMultiConfig = None
    ):
        super().__init__(data_preprocessor=data_preprocessor, init_cfg=init_cfg)

    @property
    def with_neck(self) -> bool:
        """bool: whether the detector has neck"""
        return hasattr(self, "neck") and self.neck is not None

    @property
    def with_auxiliary_head(self) -> bool:
        """bool: whether the detector has auxiliary head"""
        return hasattr(self, "auxiliary_head") and self.auxiliary_head is not None

    @property
    def with_decode_head(self) -> bool:
        """bool: whether the detector has decode head"""
        return hasattr(self, "decode_head") and self.decode_head is not None

    @abstractmethod
    def extract_feat(self, inputs: Tensor) -> bool:
        """Placeholder for extract features from images."""
        pass

    @abstractmethod
    def encode_decode(self, inputs: Tensor, batch_data_samples: SampleList):
        """Placeholder for encode images with backbone and decode into an
        edge map of the same size as input."""
        pass

    def forward(
        self, inputs: Tensor, data_samples: OptSampleList = None, mode: str = "tensor"
    ) -> ForwardResults:
        """The unified entry for a forward process in both training and test.

        The method should accept three modes: "tensor", "predict" and "loss":

        - "tensor": Forward the whole network and return tensor or tuple of
        tensor without any post-processing, same as a common nn.Module.
        - "predict": Forward and return the predictions, which are fully
        processed to a list of :obj:`SegDataSample`.
        - "loss": Forward and return a dict of losses according to the given
        inputs and data samples.

        Note that this method doesn't handle neither back propagation nor
        optimizer updating, which are done in the :meth:`train_step`.

        Args:
            inputs (torch.Tensor): The input tensor with shape (N, C, ...) in
                general.
            data_samples (list[:obj:`SegDataSample`]): The seg data samples.
                It usually includes information such as `metainfo` and
                `gt_sem_seg`. Default to None.
            mode (str): Return what kind of value. Defaults to 'tensor'.

        Returns:
            The return type depends on ``mode``.

            - If ``mode="tensor"``, return a tensor or a tuple of tensor.
            - If ``mode="predict"``, return a list of :obj:`DetDataSample`.
            - If ``mode="loss"``, return a dict of tensor.
        """
        if mode == "loss":
            return self.loss(inputs, data_samples)
        elif mode == "predict":
            return self.predict(inputs, data_samples)
        elif mode == "tensor":
            return self._forward(inputs, data_samples)
        else:
            raise RuntimeError(
                f'Invalid mode "{mode}". ' "Only supports loss, predict and tensor mode"
            )

    @abstractmethod
    def loss(self, inputs: Tensor, data_samples: SampleList) -> dict:
        """Calculate losses from a batch of inputs and data samples."""
        pass

    @abstractmethod
    def predict(self, inputs: Tensor, data_samples: OptSampleList = None) -> SampleList:
        """Predict results from a batch of inputs and data samples with post-
        processing."""
        pass

    @abstractmethod
    def _forward(
        self, inputs: Tensor, data_samples: OptSampleList = None
    ) -> Tuple[List[Tensor]]:
        """Network forward process.

        Usually includes backbone, neck and head forward without any post-
        processing.
        """
        pass

    def postprocess_result(
        self, edge_logits: Tensor, data_samples: OptSampleList = None
    ) -> SampleList:
        """Convert results list to `BasicEdgeDataSample`.
        Args:
            bin_edge_logits (Tensor): The edge results, edge_logits from
                model of each input image.
            data_samples (list[:obj:`BasicEdgeDataSample`]): The edge data samples.
                It usually includes information such as `metainfo` and
                `gt_bin_edge`. Default to None.
        Returns:
            list[:obj:`BasicEdgeDataSample`]: Edge results of the
            input images. Each BasicEdgeDataSample usually contain:

            - ``pred_bin_edge``(PixelData): Prediction of binary edge.
            - ``bin_edge_logits``(PixelData): Predicted logits of binary
                edge before normalization.
        """
        batch_size, C, H, W = edge_logits.shape

        if data_samples is None:
            data_samples = [BasicEdgeDataSample() for _ in range(batch_size)]
            only_prediction = True
        else:
            only_prediction = False

        for i in range(batch_size):
            if not only_prediction:
                img_meta = data_samples[i].metainfo
                # remove padding area
                if "img_padding_size" not in img_meta:
                    padding_size = img_meta.get("padding_size", [0] * 4)
                else:
                    padding_size = img_meta["img_padding_size"]
                padding_left, padding_right, padding_top, padding_bottom = padding_size
                # i_bin_edge_logits shape is 1, C, H, W after remove padding
                i_edge_logits = edge_logits[
                    i : i + 1,
                    :,
                    padding_top : H - padding_bottom,
                    padding_left : W - padding_right,
                ]

                flip = img_meta.get("flip", None)
                if flip:
                    flip_direction = img_meta.get("flip_direction", None)
                    assert flip_direction in ["horizontal", "vertical"]
                    if flip_direction == "horizontal":
                        i_edge_logits = i_edge_logits.flip(dims=(3,))
                    else:
                        i_edge_logits = i_edge_logits.flip(dims=(2,))

                # resize as original shape
                i_edge_logits = resize(
                    i_edge_logits,
                    size=img_meta["ori_shape"],
                    mode="bilinear",
                    align_corners=self.align_corners,
                    warning=False,
                ).squeeze(0)
            else:
                i_edge_logits = edge_logits[i]

            data_samples[i].set_data(
                {
                    "edge_logits": PixelData(**{"data": i_edge_logits}),
                    "pred_edge": PixelData(**{"data": i_edge_logits.sigmoid()}),
                }
            )

        return data_samples
