"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.face._456 import FaceGearDutyCycleRating
    from mastapy._private.gears.rating.face._457 import FaceGearMeshDutyCycleRating
    from mastapy._private.gears.rating.face._458 import FaceGearMeshRating
    from mastapy._private.gears.rating.face._459 import FaceGearRating
    from mastapy._private.gears.rating.face._460 import FaceGearSetDutyCycleRating
    from mastapy._private.gears.rating.face._461 import FaceGearSetRating
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.face._456": ["FaceGearDutyCycleRating"],
        "_private.gears.rating.face._457": ["FaceGearMeshDutyCycleRating"],
        "_private.gears.rating.face._458": ["FaceGearMeshRating"],
        "_private.gears.rating.face._459": ["FaceGearRating"],
        "_private.gears.rating.face._460": ["FaceGearSetDutyCycleRating"],
        "_private.gears.rating.face._461": ["FaceGearSetRating"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "FaceGearDutyCycleRating",
    "FaceGearMeshDutyCycleRating",
    "FaceGearMeshRating",
    "FaceGearRating",
    "FaceGearSetDutyCycleRating",
    "FaceGearSetRating",
)
