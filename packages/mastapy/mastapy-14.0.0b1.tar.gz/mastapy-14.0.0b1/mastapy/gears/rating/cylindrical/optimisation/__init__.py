"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.cylindrical.optimisation._512 import (
        CylindricalGearSetRatingOptimisationHelper,
    )
    from mastapy._private.gears.rating.cylindrical.optimisation._513 import (
        OptimisationResultsPair,
    )
    from mastapy._private.gears.rating.cylindrical.optimisation._514 import (
        SafetyFactorOptimisationResults,
    )
    from mastapy._private.gears.rating.cylindrical.optimisation._515 import (
        SafetyFactorOptimisationStepResult,
    )
    from mastapy._private.gears.rating.cylindrical.optimisation._516 import (
        SafetyFactorOptimisationStepResultAngle,
    )
    from mastapy._private.gears.rating.cylindrical.optimisation._517 import (
        SafetyFactorOptimisationStepResultNumber,
    )
    from mastapy._private.gears.rating.cylindrical.optimisation._518 import (
        SafetyFactorOptimisationStepResultShortLength,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.cylindrical.optimisation._512": [
            "CylindricalGearSetRatingOptimisationHelper"
        ],
        "_private.gears.rating.cylindrical.optimisation._513": [
            "OptimisationResultsPair"
        ],
        "_private.gears.rating.cylindrical.optimisation._514": [
            "SafetyFactorOptimisationResults"
        ],
        "_private.gears.rating.cylindrical.optimisation._515": [
            "SafetyFactorOptimisationStepResult"
        ],
        "_private.gears.rating.cylindrical.optimisation._516": [
            "SafetyFactorOptimisationStepResultAngle"
        ],
        "_private.gears.rating.cylindrical.optimisation._517": [
            "SafetyFactorOptimisationStepResultNumber"
        ],
        "_private.gears.rating.cylindrical.optimisation._518": [
            "SafetyFactorOptimisationStepResultShortLength"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "CylindricalGearSetRatingOptimisationHelper",
    "OptimisationResultsPair",
    "SafetyFactorOptimisationResults",
    "SafetyFactorOptimisationStepResult",
    "SafetyFactorOptimisationStepResultAngle",
    "SafetyFactorOptimisationStepResultNumber",
    "SafetyFactorOptimisationStepResultShortLength",
)
