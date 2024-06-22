"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.optimization.system_optimiser._2290 import (
        DesignStateTargetRatio,
    )
    from mastapy._private.system_model.optimization.system_optimiser._2291 import (
        PlanetGearOptions,
    )
    from mastapy._private.system_model.optimization.system_optimiser._2292 import (
        SystemOptimiser,
    )
    from mastapy._private.system_model.optimization.system_optimiser._2293 import (
        SystemOptimiserDetails,
    )
    from mastapy._private.system_model.optimization.system_optimiser._2294 import (
        ToothNumberFinder,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.optimization.system_optimiser._2290": [
            "DesignStateTargetRatio"
        ],
        "_private.system_model.optimization.system_optimiser._2291": [
            "PlanetGearOptions"
        ],
        "_private.system_model.optimization.system_optimiser._2292": [
            "SystemOptimiser"
        ],
        "_private.system_model.optimization.system_optimiser._2293": [
            "SystemOptimiserDetails"
        ],
        "_private.system_model.optimization.system_optimiser._2294": [
            "ToothNumberFinder"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "DesignStateTargetRatio",
    "PlanetGearOptions",
    "SystemOptimiser",
    "SystemOptimiserDetails",
    "ToothNumberFinder",
)
