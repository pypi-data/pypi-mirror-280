#!/usr/bin/env python3

import warnings

import mmcv
import mmengine
import mmseg
import pyEdgeEval
from packaging.version import parse

from .version import __version__, version_info

"""Version managing for dependencies:

Depends on:
- ``mmcv``
- ``mmengine``
- ``mmsegmentation``
- ``pyEdgeEval``
"""

MMCV_MIN = "2.0.0rc4"
MMCV_MAX = "2.1.0"

MMENGINE_MIN = "0.5.0"
MMENGINE_MAX = "1.0.0"

MMSEG_MIN = "1.0.0rc4"
MMSEG_MAX = "2.0.0"

EDGEEVAL_MIN = "0.2.7"
EDGEEVAL_MAX = "0.3.0"


def digit_version(version_str: str, length: int = 4):
    """Convert a version string into a tuple of integers.
    This method is usually used for comparing two versions. For pre-release
    versions: alpha < beta < rc.
    Args:
        version_str (str): The version string.
        length (int): The maximum number of version levels. Default: 4.
    Returns:
        tuple[int]: The version info in digits (integers).
    """
    version = parse(version_str)
    assert version.release, f"failed to parse version {version_str}"
    release = list(version.release)
    release = release[:length]
    if len(release) < length:
        release = release + [0] * (length - len(release))
    if version.is_prerelease:
        mapping = {"a": -3, "b": -2, "rc": -1}
        val = -4
        # version.pre can be None
        if version.pre:
            if version.pre[0] not in mapping:
                warnings.warn(
                    f"unknown prerelease version {version.pre[0]}, "
                    "version checking may go wrong"
                )
            else:
                val = mapping[version.pre[0]]
            release.extend([val, version.pre[-1]])
        else:
            release.extend([val, 0])

    elif version.is_postrelease:
        release.extend([1, version.post])
    else:
        release.extend([0, 0])
    return tuple(release)


mmcv_min_version = digit_version(MMCV_MIN)
mmcv_max_version = digit_version(MMCV_MAX)
mmcv_version = digit_version(mmcv.__version__)

assert mmcv_min_version <= mmcv_version < mmcv_max_version, (
    f"MMCV=={mmcv.__version__} is used but incompatible. "
    f"Please install mmcv>={MMCV_MIN}, <{MMCV_MAX}."
)

mmengine_min_version = digit_version(MMENGINE_MIN)
mmengine_max_version = digit_version(MMENGINE_MAX)
mmengine_version = digit_version(mmengine.__version__)

assert mmengine_min_version <= mmengine_version < mmengine_max_version, (
    f"MMEngine=={mmengine.__version__} is used but incompatible. "
    f"Please install mmengine>={mmengine_min_version}, "
    f"<{mmengine_max_version}."
)


mmseg_min_version = digit_version(MMSEG_MIN)
mmseg_max_version = digit_version(MMSEG_MAX)
mmseg_version = digit_version(mmseg.__version__)

assert mmseg_min_version <= mmseg_version < mmseg_max_version, (
    f"MMSeg=={mmseg.__version__} is used but incompatible. "
    f"Please install mmseg>={MMSEG_MIN}, <{MMSEG_MAX}."
)

edgeeval_min_version = digit_version(EDGEEVAL_MIN)
edgeeval_max_version = digit_version(EDGEEVAL_MAX)
edgeeval_version = digit_version(pyEdgeEval.__version__)

assert edgeeval_min_version <= edgeeval_version < edgeeval_max_version, (
    f"pyEdgeEval=={pyEdgeEval.__version__} is used but incompatible. "
    f"Please install pyEdgeEval>={EDGEEVAL_MIN}, <{EDGEEVAL_MAX}."
)


__all__ = ["__version__", "version_info", "digit_version"]
