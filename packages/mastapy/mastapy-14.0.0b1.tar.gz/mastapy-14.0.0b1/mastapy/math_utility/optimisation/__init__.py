"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.math_utility.optimisation._1585 import AbstractOptimisable
    from mastapy._private.math_utility.optimisation._1586 import (
        DesignSpaceSearchStrategyDatabase,
    )
    from mastapy._private.math_utility.optimisation._1587 import InputSetter
    from mastapy._private.math_utility.optimisation._1588 import Optimisable
    from mastapy._private.math_utility.optimisation._1589 import OptimisationHistory
    from mastapy._private.math_utility.optimisation._1590 import OptimizationInput
    from mastapy._private.math_utility.optimisation._1591 import OptimizationVariable
    from mastapy._private.math_utility.optimisation._1592 import (
        ParetoOptimisationFilter,
    )
    from mastapy._private.math_utility.optimisation._1593 import ParetoOptimisationInput
    from mastapy._private.math_utility.optimisation._1594 import (
        ParetoOptimisationOutput,
    )
    from mastapy._private.math_utility.optimisation._1595 import (
        ParetoOptimisationStrategy,
    )
    from mastapy._private.math_utility.optimisation._1596 import (
        ParetoOptimisationStrategyBars,
    )
    from mastapy._private.math_utility.optimisation._1597 import (
        ParetoOptimisationStrategyChartInformation,
    )
    from mastapy._private.math_utility.optimisation._1598 import (
        ParetoOptimisationStrategyDatabase,
    )
    from mastapy._private.math_utility.optimisation._1599 import (
        ParetoOptimisationVariable,
    )
    from mastapy._private.math_utility.optimisation._1600 import (
        ParetoOptimisationVariableBase,
    )
    from mastapy._private.math_utility.optimisation._1601 import (
        PropertyTargetForDominantCandidateSearch,
    )
    from mastapy._private.math_utility.optimisation._1602 import (
        ReportingOptimizationInput,
    )
    from mastapy._private.math_utility.optimisation._1603 import (
        SpecifyOptimisationInputAs,
    )
    from mastapy._private.math_utility.optimisation._1604 import TargetingPropertyTo
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.math_utility.optimisation._1585": ["AbstractOptimisable"],
        "_private.math_utility.optimisation._1586": [
            "DesignSpaceSearchStrategyDatabase"
        ],
        "_private.math_utility.optimisation._1587": ["InputSetter"],
        "_private.math_utility.optimisation._1588": ["Optimisable"],
        "_private.math_utility.optimisation._1589": ["OptimisationHistory"],
        "_private.math_utility.optimisation._1590": ["OptimizationInput"],
        "_private.math_utility.optimisation._1591": ["OptimizationVariable"],
        "_private.math_utility.optimisation._1592": ["ParetoOptimisationFilter"],
        "_private.math_utility.optimisation._1593": ["ParetoOptimisationInput"],
        "_private.math_utility.optimisation._1594": ["ParetoOptimisationOutput"],
        "_private.math_utility.optimisation._1595": ["ParetoOptimisationStrategy"],
        "_private.math_utility.optimisation._1596": ["ParetoOptimisationStrategyBars"],
        "_private.math_utility.optimisation._1597": [
            "ParetoOptimisationStrategyChartInformation"
        ],
        "_private.math_utility.optimisation._1598": [
            "ParetoOptimisationStrategyDatabase"
        ],
        "_private.math_utility.optimisation._1599": ["ParetoOptimisationVariable"],
        "_private.math_utility.optimisation._1600": ["ParetoOptimisationVariableBase"],
        "_private.math_utility.optimisation._1601": [
            "PropertyTargetForDominantCandidateSearch"
        ],
        "_private.math_utility.optimisation._1602": ["ReportingOptimizationInput"],
        "_private.math_utility.optimisation._1603": ["SpecifyOptimisationInputAs"],
        "_private.math_utility.optimisation._1604": ["TargetingPropertyTo"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractOptimisable",
    "DesignSpaceSearchStrategyDatabase",
    "InputSetter",
    "Optimisable",
    "OptimisationHistory",
    "OptimizationInput",
    "OptimizationVariable",
    "ParetoOptimisationFilter",
    "ParetoOptimisationInput",
    "ParetoOptimisationOutput",
    "ParetoOptimisationStrategy",
    "ParetoOptimisationStrategyBars",
    "ParetoOptimisationStrategyChartInformation",
    "ParetoOptimisationStrategyDatabase",
    "ParetoOptimisationVariable",
    "ParetoOptimisationVariableBase",
    "PropertyTargetForDominantCandidateSearch",
    "ReportingOptimizationInput",
    "SpecifyOptimisationInputAs",
    "TargetingPropertyTo",
)
