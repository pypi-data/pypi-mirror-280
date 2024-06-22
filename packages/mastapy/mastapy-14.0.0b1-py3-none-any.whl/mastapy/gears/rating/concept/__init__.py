"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.concept._559 import ConceptGearDutyCycleRating
    from mastapy._private.gears.rating.concept._560 import (
        ConceptGearMeshDutyCycleRating,
    )
    from mastapy._private.gears.rating.concept._561 import ConceptGearMeshRating
    from mastapy._private.gears.rating.concept._562 import ConceptGearRating
    from mastapy._private.gears.rating.concept._563 import ConceptGearSetDutyCycleRating
    from mastapy._private.gears.rating.concept._564 import ConceptGearSetRating
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.concept._559": ["ConceptGearDutyCycleRating"],
        "_private.gears.rating.concept._560": ["ConceptGearMeshDutyCycleRating"],
        "_private.gears.rating.concept._561": ["ConceptGearMeshRating"],
        "_private.gears.rating.concept._562": ["ConceptGearRating"],
        "_private.gears.rating.concept._563": ["ConceptGearSetDutyCycleRating"],
        "_private.gears.rating.concept._564": ["ConceptGearSetRating"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ConceptGearDutyCycleRating",
    "ConceptGearMeshDutyCycleRating",
    "ConceptGearMeshRating",
    "ConceptGearRating",
    "ConceptGearSetDutyCycleRating",
    "ConceptGearSetRating",
)
