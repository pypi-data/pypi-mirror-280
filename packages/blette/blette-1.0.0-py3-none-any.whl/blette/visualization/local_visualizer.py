#!/usr/bin/env python3

from typing import Dict, List, Optional

import mmcv
import numpy as np
from mmengine.dist import master_only
from mmengine.structures import PixelData
from mmengine.visualization import Visualizer

from blette.registry import VISUALIZERS
from blette.structures import BasicEdgeDataSample
from blette.utils import get_classes, get_palette
from blette.visualization.vis_edge import beautify_multilabel_edge


@VISUALIZERS.register_module()
class EdgeLocalVisualizer(Visualizer):
    """Edge Local Visualizer.

    Args:
        name (str): Name of the instance. Defaults to 'visualizer'.
        image (np.ndarray, optional): the origin image to draw. The format
            should be RGB. Defaults to None.
        vis_backends (list, optional): Visual backend config list.
            Defaults to None.
        save_dir (str, optional): Save file dir for all storage backends.
            If it is None, the backend storage will not save any data.
        classes (list, optional): Input classes for result rendering, as the
            prediction of edge detectiib model is a edge map with label
            indices, `classes` is a list which includes items responding to the
            label indices. If classes is not defined, visualizer will take
            `cityscapes` classes by default. Defaults to None.
        palette (list, optional): Input palette for result rendering, which is
            a list of color palette responding to the classes. Defaults to None.
        dataset_name (str, optional): `Dataset name or alias
            visualizer will use the meta information of the dataset i.e. classes
            and palette, but the `classes` and `palette` have higher priority.
            Defaults to None.
        vis_image (bool, optional): Whether to visualize the input image.
            Defaults to True.
        threshold (float, optional): The threshold to beautify the multi-label edge.
            Defaults to 0.7.
    """  # noqa

    def __init__(
        self,
        name: str = "visualizer",
        image: Optional[np.ndarray] = None,
        vis_backends: Optional[Dict] = None,
        save_dir: Optional[str] = None,
        classes: Optional[List] = None,
        palette: Optional[List] = None,
        dataset_name: Optional[str] = None,
        vis_image: bool = True,
        threshold: float = 0.7,
        **kwargs
    ) -> None:
        super().__init__(name, image, vis_backends, save_dir, **kwargs)
        self.set_dataset_meta(palette, classes, dataset_name)

        self.vis_image = vis_image
        self.threshold = threshold

    def _draw_bin_edge(
        self,
        bin_edge: PixelData,
    ) -> np.ndarray:
        """Draw semantic seg of GT or prediction.

        Args:
            bin_edge (:obj:`PixelData`): Data structure for pixel-level
                annotations or predictions.

        Returns:
            np.ndarray: the drawn image which channel is RGB.
        """
        bin_edge = bin_edge.cpu().data

        if bin_edge.ndim == 3:
            bin_edge = bin_edge.squeeze(0)

        bin_edge = bin_edge.numpy()

        # colorize
        # I want to shade the edge with the color
        # the intensity of the color is proportional to the edge value
        # the edge value is between 0 and 1
        # the color is between 0 and 255

        # bin_edge (H, W)
        out_img = 255 * bin_edge
        out_img = out_img.astype(np.uint8)
        # make it 3 channels
        out_img = np.stack([out_img] * 3, axis=2)
        return out_img

    def _draw_mlbl_edge(
        self,
        mlbl_edge: PixelData,
        palette: Optional[List],
    ) -> np.ndarray:
        """Draw multi-label edge of GT or prediction.

        Args:
            mlbl_edge (:obj:`PixelData`): Data structure for pixel-level
                annotations or predictions.
            palette (list, optional): Input palette for result rendering, which
                is a list of color palette responding to the classes.
                Defaults to None.

        Returns:
            np.ndarray: the drawn image which channel is RGB.
        """
        # mlbl_edge (Class, H, W)
        mlbl_edge = mlbl_edge.cpu().data.numpy()
        out = beautify_multilabel_edge(
            mlbl_edge, palette, beautify_threshold=self.threshold
        )
        return out

    def set_dataset_meta(
        self,
        classes: Optional[List] = None,
        palette: Optional[List] = None,
        dataset_name: Optional[str] = None,
    ) -> None:
        """Set meta information to visualizer.

        Args:
            classes (list, optional): Input classes for result rendering, as
                the prediction of edge detection model is an edge map with
                label indices, `classes` is a list which includes items
                responding to the label indices. If classes is not defined,
                visualizer will take `cityscapes` classes by default.
                Defaults to None.
            palette (list, optional): Input palette for result rendering, which
                is a list of color palette responding to the classes.
                Defaults to None.
            dataset_name (str, optional): `Dataset name or alias
                visulizer will use the meta information of the dataset i.e.
                classes and palette, but the `classes` and `palette` have
                higher priority. Defaults to None.
        """  # noqa
        # Set default value. When calling
        # `MultiEdgeLocalVisualizer().dataset_meta=xxx`,
        # it will override the default value.
        if dataset_name is None:
            dataset_name = "cityscapes"
        classes = classes if classes else get_classes(dataset_name)
        palette = palette if palette else get_palette(dataset_name)
        assert len(classes) == len(
            palette
        ), "The length of classes should be equal to palette"
        self.dataset_meta: dict = {"classes": classes, "palette": palette}

    @master_only
    def add_datasample(
        self,
        name: str,
        image: np.ndarray,
        data_sample: Optional[BasicEdgeDataSample] = None,
        draw_gt: bool = True,
        draw_pred: bool = True,
        show: bool = False,
        wait_time: float = 0,
        # TODO: Supported in mmengine's Viusalizer.
        out_file: Optional[str] = None,
        step: int = 0,
    ) -> None:
        """Draw datasample and save to all backends.

        - If GT and prediction are plotted at the same time, they are
        displayed in a stitched image where the left image is the
        ground truth and the right image is the prediction.
        - If ``show`` is True, all storage backends are ignored, and
        the images will be displayed in a local window.
        - If ``out_file`` is specified, the drawn image will be
        saved to ``out_file``. it is usually used when the display
        is not available.

        Args:
            name (str): The image identifier.
            image (np.ndarray): The image to draw.
            gt_sample (:obj:`BasicEdgeDataSample`, optional): GT BasicEdgeDataSample.
                Defaults to None.
            pred_sample (:obj:`BasicEdgeDataSample`, optional): Prediction
                BasicEdgeDataSample. Defaults to None.
            draw_gt (bool): Whether to draw GT BasicEdgeDataSample. Default to True.
            draw_pred (bool): Whether to draw Prediction BasicEdgeDataSample.
                Defaults to True.
            show (bool): Whether to display the drawn image. Default to False.
            wait_time (float): The interval of show (s). Defaults to 0.
            out_file (str): Path to output file. Defaults to None.
            step (int): Global step value to record. Defaults to 0.
        """
        classes = self.dataset_meta.get("classes", None)
        palette = self.dataset_meta.get("palette", None)
        num_classes = len(classes)

        gt_img_data = None
        pred_img_data = None

        # Plan:
        # Concat Image, GT, and Prediction
        # I'm assuming that the image and outputs are all
        # same size.

        if draw_gt and data_sample is not None:
            assert classes is not None, (
                "class information is " "not provided when " "visualizing results."
            )
            if num_classes > 1:
                assert "gt_mlbl_edge" in data_sample
                gt_img_data = self._draw_mlbl_edge(data_sample.gt_mlbl_edge, palette)
            else:
                assert "gt_bin_edge" in data_sample
                gt_img_data = self._draw_bin_edge(data_sample.gt_bin_edge)

        if draw_pred and data_sample is not None and "pred_edge" in data_sample:
            assert classes is not None, (
                "class information is " "not provided when " "visualizing results."
            )
            if num_classes > 1:
                pred_img_data = self._draw_mlbl_edge(data_sample.pred_edge, palette)
            else:
                pred_img_data = self._draw_bin_edge(data_sample.pred_edge)

        concat_list = []

        if self.vis_image:
            concat_list.append(image)

        if gt_img_data is not None:
            concat_list.append(gt_img_data)

        if pred_img_data is not None:
            concat_list.append(pred_img_data)

        if len(concat_list) > 0:
            drawn_img = np.concatenate(concat_list, axis=1)
        else:
            drawn_img = concat_list[0]

        if show:
            self.show(drawn_img, win_name=name, wait_time=wait_time)

        if out_file is not None:
            mmcv.imwrite(mmcv.bgr2rgb(drawn_img), out_file)
        else:
            self.add_image(name, drawn_img, step)
