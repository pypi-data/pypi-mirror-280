#!/usr/bin/env python3

from functools import partial

from mmcv.transforms.base import BaseTransform

from blette.registry import TRANSFORMS

try:
    from imagecorruptions import corrupt
except ImportError:
    corrupt = None


@TRANSFORMS.register_module()
class ImageCorruptions(BaseTransform):
    """Image Corruptions."""

    def __init__(self, name, severity=1):
        assert (
            corrupt is not None
        ), "Please install imagecorruptions to use this transform."
        assert 0 < severity < 6, "Severity should be between 1 and 5."
        assert name in [
            "gaussian_noise",
            "shot_noise",
            "impulse_noise",
            "speckle_noise",
            "gaussian_blur",
            "defocus_blur",
            "motion_blur",
            "zoom_blur",
            "fog",
            "frost",
            "snow",
            "spatter",
            "contrast",
            "brightness",
            "saturate",
            "jpeg_compression",
            "pixelate",
            "elastic_transform",
        ]
        self.corruption_name = name
        self.severity = severity
        self._corrupt = partial(
            corrupt, severity=self.severity, corruption_name=self.corruption_name
        )

    def transform(self, results: dict) -> dict:
        results["img"] = self._corrupt(results["img"])
        return results

    def __repr__(self):
        repr_str = self.__class__.__name__
        repr_str += f"(name={self.corruption_name},"
        repr_str += f"severity={self.severity})"
        return repr_str
