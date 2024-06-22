"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.optimization._2279 import (
        ConicalGearOptimisationStrategy,
    )
    from mastapy._private.system_model.optimization._2280 import (
        ConicalGearOptimizationStep,
    )
    from mastapy._private.system_model.optimization._2281 import (
        ConicalGearOptimizationStrategyDatabase,
    )
    from mastapy._private.system_model.optimization._2282 import (
        CylindricalGearOptimisationStrategy,
    )
    from mastapy._private.system_model.optimization._2283 import (
        CylindricalGearOptimizationStep,
    )
    from mastapy._private.system_model.optimization._2284 import (
        MeasuredAndFactorViewModel,
    )
    from mastapy._private.system_model.optimization._2285 import (
        MicroGeometryOptimisationTarget,
    )
    from mastapy._private.system_model.optimization._2286 import OptimizationStep
    from mastapy._private.system_model.optimization._2287 import OptimizationStrategy
    from mastapy._private.system_model.optimization._2288 import (
        OptimizationStrategyBase,
    )
    from mastapy._private.system_model.optimization._2289 import (
        OptimizationStrategyDatabase,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.optimization._2279": ["ConicalGearOptimisationStrategy"],
        "_private.system_model.optimization._2280": ["ConicalGearOptimizationStep"],
        "_private.system_model.optimization._2281": [
            "ConicalGearOptimizationStrategyDatabase"
        ],
        "_private.system_model.optimization._2282": [
            "CylindricalGearOptimisationStrategy"
        ],
        "_private.system_model.optimization._2283": ["CylindricalGearOptimizationStep"],
        "_private.system_model.optimization._2284": ["MeasuredAndFactorViewModel"],
        "_private.system_model.optimization._2285": ["MicroGeometryOptimisationTarget"],
        "_private.system_model.optimization._2286": ["OptimizationStep"],
        "_private.system_model.optimization._2287": ["OptimizationStrategy"],
        "_private.system_model.optimization._2288": ["OptimizationStrategyBase"],
        "_private.system_model.optimization._2289": ["OptimizationStrategyDatabase"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ConicalGearOptimisationStrategy",
    "ConicalGearOptimizationStep",
    "ConicalGearOptimizationStrategyDatabase",
    "CylindricalGearOptimisationStrategy",
    "CylindricalGearOptimizationStep",
    "MeasuredAndFactorViewModel",
    "MicroGeometryOptimisationTarget",
    "OptimizationStep",
    "OptimizationStrategy",
    "OptimizationStrategyBase",
    "OptimizationStrategyDatabase",
)
