"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.spiral_bevel._413 import (
        SpiralBevelGearMeshRating,
    )
    from mastapy._private.gears.rating.spiral_bevel._414 import SpiralBevelGearRating
    from mastapy._private.gears.rating.spiral_bevel._415 import SpiralBevelGearSetRating
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.spiral_bevel._413": ["SpiralBevelGearMeshRating"],
        "_private.gears.rating.spiral_bevel._414": ["SpiralBevelGearRating"],
        "_private.gears.rating.spiral_bevel._415": ["SpiralBevelGearSetRating"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "SpiralBevelGearMeshRating",
    "SpiralBevelGearRating",
    "SpiralBevelGearSetRating",
)
