"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.micro_geometry._580 import BiasModification
    from mastapy._private.gears.micro_geometry._581 import FlankMicroGeometry
    from mastapy._private.gears.micro_geometry._582 import FlankSide
    from mastapy._private.gears.micro_geometry._583 import LeadModification
    from mastapy._private.gears.micro_geometry._584 import (
        LocationOfEvaluationLowerLimit,
    )
    from mastapy._private.gears.micro_geometry._585 import (
        LocationOfEvaluationUpperLimit,
    )
    from mastapy._private.gears.micro_geometry._586 import (
        LocationOfRootReliefEvaluation,
    )
    from mastapy._private.gears.micro_geometry._587 import LocationOfTipReliefEvaluation
    from mastapy._private.gears.micro_geometry._588 import (
        MainProfileReliefEndsAtTheStartOfRootReliefOption,
    )
    from mastapy._private.gears.micro_geometry._589 import (
        MainProfileReliefEndsAtTheStartOfTipReliefOption,
    )
    from mastapy._private.gears.micro_geometry._590 import Modification
    from mastapy._private.gears.micro_geometry._591 import (
        ParabolicRootReliefStartsTangentToMainProfileRelief,
    )
    from mastapy._private.gears.micro_geometry._592 import (
        ParabolicTipReliefStartsTangentToMainProfileRelief,
    )
    from mastapy._private.gears.micro_geometry._593 import ProfileModification
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.micro_geometry._580": ["BiasModification"],
        "_private.gears.micro_geometry._581": ["FlankMicroGeometry"],
        "_private.gears.micro_geometry._582": ["FlankSide"],
        "_private.gears.micro_geometry._583": ["LeadModification"],
        "_private.gears.micro_geometry._584": ["LocationOfEvaluationLowerLimit"],
        "_private.gears.micro_geometry._585": ["LocationOfEvaluationUpperLimit"],
        "_private.gears.micro_geometry._586": ["LocationOfRootReliefEvaluation"],
        "_private.gears.micro_geometry._587": ["LocationOfTipReliefEvaluation"],
        "_private.gears.micro_geometry._588": [
            "MainProfileReliefEndsAtTheStartOfRootReliefOption"
        ],
        "_private.gears.micro_geometry._589": [
            "MainProfileReliefEndsAtTheStartOfTipReliefOption"
        ],
        "_private.gears.micro_geometry._590": ["Modification"],
        "_private.gears.micro_geometry._591": [
            "ParabolicRootReliefStartsTangentToMainProfileRelief"
        ],
        "_private.gears.micro_geometry._592": [
            "ParabolicTipReliefStartsTangentToMainProfileRelief"
        ],
        "_private.gears.micro_geometry._593": ["ProfileModification"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BiasModification",
    "FlankMicroGeometry",
    "FlankSide",
    "LeadModification",
    "LocationOfEvaluationLowerLimit",
    "LocationOfEvaluationUpperLimit",
    "LocationOfRootReliefEvaluation",
    "LocationOfTipReliefEvaluation",
    "MainProfileReliefEndsAtTheStartOfRootReliefOption",
    "MainProfileReliefEndsAtTheStartOfTipReliefOption",
    "Modification",
    "ParabolicRootReliefStartsTangentToMainProfileRelief",
    "ParabolicTipReliefStartsTangentToMainProfileRelief",
    "ProfileModification",
)
