"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.conical._549 import ConicalGearDutyCycleRating
    from mastapy._private.gears.rating.conical._550 import ConicalGearMeshRating
    from mastapy._private.gears.rating.conical._551 import ConicalGearRating
    from mastapy._private.gears.rating.conical._552 import ConicalGearSetDutyCycleRating
    from mastapy._private.gears.rating.conical._553 import ConicalGearSetRating
    from mastapy._private.gears.rating.conical._554 import ConicalGearSingleFlankRating
    from mastapy._private.gears.rating.conical._555 import ConicalMeshDutyCycleRating
    from mastapy._private.gears.rating.conical._556 import ConicalMeshedGearRating
    from mastapy._private.gears.rating.conical._557 import ConicalMeshSingleFlankRating
    from mastapy._private.gears.rating.conical._558 import ConicalRateableMesh
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.conical._549": ["ConicalGearDutyCycleRating"],
        "_private.gears.rating.conical._550": ["ConicalGearMeshRating"],
        "_private.gears.rating.conical._551": ["ConicalGearRating"],
        "_private.gears.rating.conical._552": ["ConicalGearSetDutyCycleRating"],
        "_private.gears.rating.conical._553": ["ConicalGearSetRating"],
        "_private.gears.rating.conical._554": ["ConicalGearSingleFlankRating"],
        "_private.gears.rating.conical._555": ["ConicalMeshDutyCycleRating"],
        "_private.gears.rating.conical._556": ["ConicalMeshedGearRating"],
        "_private.gears.rating.conical._557": ["ConicalMeshSingleFlankRating"],
        "_private.gears.rating.conical._558": ["ConicalRateableMesh"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ConicalGearDutyCycleRating",
    "ConicalGearMeshRating",
    "ConicalGearRating",
    "ConicalGearSetDutyCycleRating",
    "ConicalGearSetRating",
    "ConicalGearSingleFlankRating",
    "ConicalMeshDutyCycleRating",
    "ConicalMeshedGearRating",
    "ConicalMeshSingleFlankRating",
    "ConicalRateableMesh",
)
