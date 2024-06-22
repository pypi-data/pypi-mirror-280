"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.worm._383 import WormGearDutyCycleRating
    from mastapy._private.gears.rating.worm._384 import WormGearMeshRating
    from mastapy._private.gears.rating.worm._385 import WormGearRating
    from mastapy._private.gears.rating.worm._386 import WormGearSetDutyCycleRating
    from mastapy._private.gears.rating.worm._387 import WormGearSetRating
    from mastapy._private.gears.rating.worm._388 import WormMeshDutyCycleRating
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.worm._383": ["WormGearDutyCycleRating"],
        "_private.gears.rating.worm._384": ["WormGearMeshRating"],
        "_private.gears.rating.worm._385": ["WormGearRating"],
        "_private.gears.rating.worm._386": ["WormGearSetDutyCycleRating"],
        "_private.gears.rating.worm._387": ["WormGearSetRating"],
        "_private.gears.rating.worm._388": ["WormMeshDutyCycleRating"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "WormGearDutyCycleRating",
    "WormGearMeshRating",
    "WormGearRating",
    "WormGearSetDutyCycleRating",
    "WormGearSetRating",
    "WormMeshDutyCycleRating",
)
