#!/usr/bin/env python3

import datetime
import warnings

from mmengine import DefaultScope


def register_all_modules(init_default_scope: bool = True) -> None:
    """Register all modules in blette into the registries.

    Args:
        init_default_scope (bool): Whether initialize the blette default scope.
            When `init_default_scope=True`, the global default scope will be
            set to `blette`, and all registries will build modules from blette's
            registry node. To understand more about the registry, please refer
            to https://github.com/open-mmlab/mmengine/blob/main/docs/en/tutorials/registry.md
            Defaults to True.
    """  # noqa
    import blette.datasets  # noqa: F401,F403
    import blette.engine  # noqa: F401,F403
    import blette.evaluation  # noqa: F401,F403
    import blette.models  # noqa: F401,F403
    import blette.structures  # noqa: F401,F403

    if init_default_scope:
        never_created = (
            DefaultScope.get_current_instance() is None
            or not DefaultScope.check_instance_created("blette")
        )
        if never_created:
            DefaultScope.get_instance("blette", scope_name="blette")
            return
        current_scope = DefaultScope.get_current_instance()
        if current_scope.scope_name != "blette":
            warnings.warn(
                "The current default scope "
                f'"{current_scope.scope_name}" is not "blette", '
                "`register_all_modules` will force the current"
                'default scope to be "blette". If this is not '
                "expected, please set `init_default_scope=False`."
            )
            # avoid name conflict
            new_instance_name = f"blette-{datetime.datetime.now()}"
            DefaultScope.get_instance(new_instance_name, scope_name="blette")
