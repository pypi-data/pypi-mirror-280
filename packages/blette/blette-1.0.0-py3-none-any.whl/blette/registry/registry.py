#!/usr/bin/env python3

"""MMSegmentation provides 21 registry nodes to support using modules across
projects. Each node is a child of the root registry in MMEngine.

More details can be found at
https://mmengine.readthedocs.io/en/latest/advanced_tutorials/registry.html.
"""

from mmengine.registry import DATA_SAMPLERS as MMENGINE_DATA_SAMPLERS
from mmengine.registry import DATASETS as MMENGINE_DATASETS
from mmengine.registry import HOOKS as MMENGINE_HOOKS
from mmengine.registry import INFERENCERS as MMENGINE_INFERENCERS
from mmengine.registry import LOG_PROCESSORS as MMENGINE_LOG_PROCESSORS
from mmengine.registry import LOOPS as MMENGINE_LOOPS
from mmengine.registry import RUNNER_CONSTRUCTORS as MMENGINE_RUNNER_CONSTRUCTORS
from mmengine.registry import RUNNERS as MMENGINE_RUNNERS
from mmengine.registry import WEIGHT_INITIALIZERS as MMENGINE_WEIGHT_INITIALIZERS
from mmengine.registry import Registry

from mmseg.registry import MODELS as MMSEG_MODELS
from mmseg.registry import MODEL_WRAPPERS as MMSEG_MODEL_WRAPPERS
from mmseg.registry import TRANSFORMS as MMSEG_TRANSFORMS
from mmseg.registry import OPTIMIZERS as MMSEG_OPTIMIZERS
from mmseg.registry import OPTIM_WRAPPERS as MMSEG_OPTIM_WRAPPERS
from mmseg.registry import (
    OPTIM_WRAPPER_CONSTRUCTORS as MMSEG_OPTIM_WRAPPER_CONSTRUCTORS,
)
from mmseg.registry import PARAM_SCHEDULERS as MMSEG_PARAM_SCHEDULERS
from mmseg.registry import METRICS as MMSEG_METRICS
from mmseg.registry import EVALUATOR as MMSEG_EVALUATOR
from mmseg.registry import TASK_UTILS as MMSEG_TASK_UTILS
from mmseg.registry import VISBACKENDS as MMSEG_VISBACKENDS
from mmseg.registry import VISUALIZERS as MMSEG_VISUALIZER

# manage all kinds of runners like `EpochBasedRunner` and `IterBasedRunner`
RUNNERS = Registry("runner", parent=MMENGINE_RUNNERS)
# manage runner constructors that define how to initialize runners
RUNNER_CONSTRUCTORS = Registry(
    "runner constructor", parent=MMENGINE_RUNNER_CONSTRUCTORS
)
# manage all kinds of loops like `EpochBasedTrainLoop`
LOOPS = Registry("loop", parent=MMENGINE_LOOPS)
# manage all kinds of hooks like `CheckpointHook`
HOOKS = Registry("hook", parent=MMENGINE_HOOKS, locations=["blette.engine.hooks"])

# manage data-related modules
DATASETS = Registry("dataset", parent=MMENGINE_DATASETS, locations=["blette.datasets"])
DATA_SAMPLERS = Registry("data sampler", parent=MMENGINE_DATA_SAMPLERS)
TRANSFORMS = Registry(
    "transform", parent=MMSEG_TRANSFORMS, locations=["blette.datasets.transforms"]
)

# mangage all kinds of modules inheriting `nn.Module`
MODELS = Registry("model", parent=MMSEG_MODELS, locations=["blette.models"])
# mangage all kinds of model wrappers like 'MMDistributedDataParallel'
MODEL_WRAPPERS = Registry(
    "model_wrapper", parent=MMSEG_MODEL_WRAPPERS, locations=["blette.models"]
)
# mangage all kinds of weight initialization modules like `Uniform`
WEIGHT_INITIALIZERS = Registry(
    "weight initializer",
    parent=MMENGINE_WEIGHT_INITIALIZERS,
    locations=["blette.models"],
)

# mangage all kinds of optimizers like `SGD` and `Adam`
OPTIMIZERS = Registry(
    "optimizer", parent=MMSEG_OPTIMIZERS, locations=["blette.engine.optimizers"]
)
# manage optimizer wrapper
OPTIM_WRAPPERS = Registry(
    "optim_wrapper", parent=MMSEG_OPTIM_WRAPPERS, locations=["blette.engine.optimizers"]
)
# manage constructors that customize the optimization hyperparameters.
OPTIM_WRAPPER_CONSTRUCTORS = Registry(
    "optimizer wrapper constructor",
    parent=MMSEG_OPTIM_WRAPPER_CONSTRUCTORS,
    locations=["blette.engine.optimizers"],
)
# mangage all kinds of parameter schedulers like `MultiStepLR`
PARAM_SCHEDULERS = Registry("parameter scheduler", parent=MMSEG_PARAM_SCHEDULERS)

# manage all kinds of metrics
METRICS = Registry("metric", parent=MMSEG_METRICS, locations=["blette.evaluation"])
# manage evaluator
EVALUATOR = Registry(
    "evaluator", parent=MMSEG_EVALUATOR, locations=["blette.evaluation"]
)

# manage task-specific modules like ohem pixel sampler
TASK_UTILS = Registry("task util", parent=MMSEG_TASK_UTILS, locations=["blette.models"])

# manage visualizer
VISUALIZERS = Registry(
    "visualizer", parent=MMSEG_VISUALIZER, locations=["blette.visualization"]
)
# manage visualizer backend
VISBACKENDS = Registry(
    "vis_backend", parent=MMSEG_VISBACKENDS, locations=["blette.visualization"]
)

# manage logprocessor
LOG_PROCESSORS = Registry(
    "log_processor", parent=MMENGINE_LOG_PROCESSORS, locations=["blette.visualization"]
)

# manage inferencer
INFERENCERS = Registry("inferencer", parent=MMENGINE_INFERENCERS)
