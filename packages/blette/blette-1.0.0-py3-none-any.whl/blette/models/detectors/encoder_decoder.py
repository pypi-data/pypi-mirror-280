#!/usr/bin/env python3

from typing import List, Optional

import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor

from mmseg.utils import add_prefix

from blette.registry import MODELS
from blette.utils import (
    ConfigType,
    OptConfigType,
    OptMultiConfig,
    OptSampleList,
    SampleList,
)
from .base import BaseEdgeDetector


@MODELS.register_module()
class EdgeEncoderDecoder(BaseEdgeDetector):
    """Encoder Decoder for edge detection.

    Args:
        backbone (ConfigType): The config for the backbone of detector.
        decode_head (ConfigType): The config for the decode head of detector.
        neck (OptConfigType): The config for the neck of detector
            Defaults to None.
        auxiliary_head (OptConfigType): The config for the auxiliary head of
            detector. Defaults to None.
        train_cfg (OptConfigType): The config for training. Defaults to None.
        test_cfg (OptConfigType): The config for testing. Defaults to None.
        data_preprocessor (dict, optional): The pre-process config of
            :class:`BaseDataPreprocessor`.
        pretrained (str, optional): The path for pretrained model.
            Defaults to None.
        init_cfg (dict, optional): The weight initialized config for
            :class:`BaseModule`.
        pass_input_image (bool): Whether to pass input image to decode head.
    """  # noqa: E501

    def __init__(
        self,
        backbone: ConfigType,
        decode_head: ConfigType,
        neck: OptConfigType = None,
        auxiliary_head: OptConfigType = None,
        train_cfg: OptConfigType = None,
        test_cfg: OptConfigType = None,
        data_preprocessor: OptConfigType = None,
        pretrained: Optional[str] = None,
        init_cfg: OptMultiConfig = None,
        pass_input_image: bool = False,
    ) -> None:
        self.pass_input_image = pass_input_image

        super().__init__(data_preprocessor=data_preprocessor, init_cfg=init_cfg)
        if pretrained is not None:
            assert (
                backbone.get("pretrained") is None
            ), "both backbone and detector set pretrained weight"
            backbone.pretrained = pretrained
        self.backbone = MODELS.build(backbone)
        if neck is not None:
            self.neck = MODELS.build(neck)
        self._init_decode_head(decode_head)
        self._init_auxiliary_head(auxiliary_head)

        self.train_cfg = train_cfg
        self.test_cfg = test_cfg

        assert self.with_decode_head

    def _init_decode_head(self, decode_head: ConfigType) -> None:
        """Initialize ``decode_head``"""
        if self.pass_input_image:
            # HACK: force `pass_input_image` argument to be True
            decode_head["pass_input_image"] = True

        self.decode_head = MODELS.build(decode_head)
        self.align_corners = self.decode_head.align_corners
        self.num_classes = self.decode_head.num_classes

    def _init_auxiliary_head(self, auxiliary_head: ConfigType) -> None:
        """Initialize ``auxiliary_head``"""
        if auxiliary_head is not None:
            if isinstance(auxiliary_head, list):
                self.auxiliary_head = nn.ModuleList()
                for head_cfg in auxiliary_head:
                    self.auxiliary_head.append(MODELS.build(head_cfg))
            else:
                self.auxiliary_head = MODELS.build(auxiliary_head)

    def extract_feat(self, inputs: Tensor) -> List[Tensor]:
        """Extract features from images."""
        x = self.backbone(inputs)
        if self.with_neck:
            x = self.neck(x)

        if self.pass_input_image:
            # HACK: append input
            x = (*x, inputs)

        return x

    def encode_decode(self, inputs: Tensor, batch_img_metas: List[dict]) -> Tensor:
        """Encode images with backbone and decode into an edge
        map of the same size as input."""
        x = self.extract_feat(inputs)
        edge_logits = self.decode_head.predict(x, batch_img_metas, self.test_cfg)

        return edge_logits

    def _decode_head_forward_train(
        self, inputs: List[Tensor], data_samples: SampleList
    ) -> dict:
        """Run forward function and calculate loss for decode head in
        training."""
        losses = dict()
        loss_decode = self.decode_head.loss(inputs, data_samples, self.train_cfg)

        losses.update(add_prefix(loss_decode, "decode"))
        return losses

    def _auxiliary_head_forward_train(
        self, inputs: List[Tensor], data_samples: SampleList
    ) -> dict:
        """Run forward function and calculate loss for auxiliary head in
        training."""
        losses = dict()
        if isinstance(self.auxiliary_head, nn.ModuleList):
            for idx, aux_head in enumerate(self.auxiliary_head):
                loss_aux = aux_head.loss(inputs, data_samples, self.train_cfg)
                losses.update(add_prefix(loss_aux, f"aux_{idx}"))
        else:
            loss_aux = self.auxiliary_head.loss(inputs, data_samples, self.train_cfg)
            losses.update(add_prefix(loss_aux, "aux"))

        return losses

    def loss(self, inputs: Tensor, data_samples: SampleList) -> dict:
        """Calculate losses from a batch of inputs and data samples.

        Args:
            inputs (Tensor): Input images.
            data_samples (list[:obj:`BasicEdgeDataSample`]): The edge data samples.
                It usually includes information such as `metainfo` and
                `gt_bin_edge`.

        Returns:
            dict[str, Tensor]: a dictionary of loss components
        """

        x = self.extract_feat(inputs)

        losses = dict()

        loss_decode = self._decode_head_forward_train(x, data_samples)
        losses.update(loss_decode)

        if self.with_auxiliary_head:
            loss_aux = self._auxiliary_head_forward_train(x, data_samples)
            losses.update(loss_aux)

        return losses

    def predict(self, inputs: Tensor, data_samples: OptSampleList = None) -> SampleList:
        """Predict results from a batch of inputs and data samples with post-
        processing.

        Args:
            inputs (Tensor): Inputs with shape (N, C, H, W).
            data_samples (List[:obj:`BasicEdgeDataSample`], optional): The edge data
                samples. It usually includes information such as `metainfo`
                and `gt_bin_edge`.

        Returns:
            list[:obj:`BasicEdgeDataSample`]: Edge results of the
            input images. Each BasicEdgeDataSample usually contain:

            - ``pred_edge``(PixelData): Prediction of edge.
            - ``edge_logits``(PixelData): Predicted logits of edge
                before normalization.
        """
        if data_samples is not None:
            batch_img_metas = [data_sample.metainfo for data_sample in data_samples]
        else:
            batch_img_metas = [
                dict(
                    ori_shape=inputs.shape[2:],
                    img_shape=inputs.shape[2:],
                    pad_shape=inputs.shape[2:],
                    padding_size=[0, 0, 0, 0],
                )
            ] * inputs.shape[0]

        edge_logits = self.inference(inputs, batch_img_metas)

        return self.postprocess_result(edge_logits, data_samples)

    def _forward(self, inputs: Tensor, data_samples: OptSampleList = None) -> Tensor:
        """Network forward process.

        Args:
            inputs (Tensor): Inputs with shape (N, C, H, W).
            data_samples (List[:obj:`BasicEdgeDataSample`]): The edge
                data samples. It usually includes information such
                as `metainfo` and `gt_bin_edge`.

        Returns:
            Tensor: Forward output of model without any post-processes.
        """
        x = self.extract_feat(inputs)
        return self.decode_head.forward(x)

    def slide_inference(self, inputs: Tensor, batch_img_metas: List[dict]) -> Tensor:
        """Inference by sliding-window with overlap.

        If h_crop > h_img or w_crop > w_img, the small patch will be used to
        decode without padding.

        Args:
            inputs (tensor): the tensor should have a shape NxCxHxW,
                which contains all images in the batch.
            batch_img_metas (List[dict]): List of image metainfo where each may
                also contain: 'img_shape', 'scale_factor', 'flip', 'img_path',
                'ori_shape', and 'pad_shape'.
                For details on the values of these keys see
                `blette/datasets/pipelines/formatting.py:PackEdgeInputs`.

        Returns:
            Tensor: The edge results, edge_logits from model of each
                input image.
        """

        h_stride, w_stride = self.test_cfg.stride
        h_crop, w_crop = self.test_cfg.crop_size
        batch_size, _, h_img, w_img = inputs.size()
        num_classes = self.num_classes
        h_grids = max(h_img - h_crop + h_stride - 1, 0) // h_stride + 1
        w_grids = max(w_img - w_crop + w_stride - 1, 0) // w_stride + 1
        preds = inputs.new_zeros((batch_size, num_classes, h_img, w_img))
        count_mat = inputs.new_zeros((batch_size, 1, h_img, w_img))
        for h_idx in range(h_grids):
            for w_idx in range(w_grids):
                y1 = h_idx * h_stride
                x1 = w_idx * w_stride
                y2 = min(y1 + h_crop, h_img)
                x2 = min(x1 + w_crop, w_img)
                y1 = max(y2 - h_crop, 0)
                x1 = max(x2 - w_crop, 0)
                crop_img = inputs[:, :, y1:y2, x1:x2]
                # change the image shape to patch shape
                batch_img_metas[0]["img_shape"] = crop_img.shape[2:]
                # the output of encode_decode is edge logits tensor map
                # with shape [N, C, H, W]
                crop_edge_logit = self.encode_decode(crop_img, batch_img_metas)
                preds += F.pad(
                    crop_edge_logit,
                    (
                        int(x1),
                        int(preds.shape[3] - x2),
                        int(y1),
                        int(preds.shape[2] - y2),
                    ),
                )

                count_mat[:, :, y1:y2, x1:x2] += 1
        assert (count_mat == 0).sum() == 0
        edge_logits = preds / count_mat

        return edge_logits

    def whole_inference(self, inputs: Tensor, batch_img_metas: List[dict]) -> Tensor:
        """Inference with full image.

        Args:
            inputs (Tensor): The tensor should have a shape NxCxHxW, which
                contains all images in the batch.
            batch_img_metas (List[dict]): List of image metainfo where each may
                also contain: 'img_shape', 'scale_factor', 'flip', 'img_path',
                'ori_shape', and 'pad_shape'.
                For details on the values of these keys see
                `blette/datasets/pipelines/formatting.py:PackEdgeInputs`.

        Returns:
            Tensor: The edge results, edge_logits from model of each
                input image.
        """

        edge_logits = self.encode_decode(inputs, batch_img_metas)

        return edge_logits

    def inference(self, inputs: Tensor, batch_img_metas: List[dict]) -> Tensor:
        """Inference with slide/whole style.

        Args:
            inputs (Tensor): The input image of shape (N, 3, H, W).
            batch_img_metas (List[dict]): List of image metainfo where each may
                also contain: 'img_shape', 'scale_factor', 'flip', 'img_path',
                'ori_shape', 'pad_shape', and 'padding_size'.
                For details on the values of these keys see
                `blette/datasets/pipelines/formatting.py:PackEdgeInputs`.

        Returns:
            Tensor: The edge results, edge_logits from model of each
                input image.
        """

        assert self.test_cfg.mode in ["slide", "whole"]
        ori_shape = batch_img_metas[0]["ori_shape"]
        assert all(_["ori_shape"] == ori_shape for _ in batch_img_metas)
        if self.test_cfg.mode == "slide":
            edge_logit = self.slide_inference(inputs, batch_img_metas)
        else:
            edge_logit = self.whole_inference(inputs, batch_img_metas)

        return edge_logit

    def aug_test(self, inputs, batch_img_metas, rescale=True):
        """Test with augmentations.

        Only rescale=True is supported.
        """
        # aug_test rescale all imgs back to ori_shape for now
        assert rescale
        # to save memory, we get augmented edge logit inplace
        edge_logit = self.inference(inputs[0], batch_img_metas[0], rescale)
        for i in range(1, len(inputs)):
            cur_edge_logit = self.inference(inputs[i], batch_img_metas[i], rescale)
            edge_logit += cur_edge_logit
        edge_logit /= len(inputs)

        # sigmoid instead of argmax
        edge_pred = edge_logit.sigmoid()
        # unravel batch dim
        edge_pred = list(edge_pred)
        return edge_pred
