"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.bevel.standards._568 import (
        AGMASpiralBevelGearSingleFlankRating,
    )
    from mastapy._private.gears.rating.bevel.standards._569 import (
        AGMASpiralBevelMeshSingleFlankRating,
    )
    from mastapy._private.gears.rating.bevel.standards._570 import (
        GleasonSpiralBevelGearSingleFlankRating,
    )
    from mastapy._private.gears.rating.bevel.standards._571 import (
        GleasonSpiralBevelMeshSingleFlankRating,
    )
    from mastapy._private.gears.rating.bevel.standards._572 import (
        SpiralBevelGearSingleFlankRating,
    )
    from mastapy._private.gears.rating.bevel.standards._573 import (
        SpiralBevelMeshSingleFlankRating,
    )
    from mastapy._private.gears.rating.bevel.standards._574 import (
        SpiralBevelRateableGear,
    )
    from mastapy._private.gears.rating.bevel.standards._575 import (
        SpiralBevelRateableMesh,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.bevel.standards._568": [
            "AGMASpiralBevelGearSingleFlankRating"
        ],
        "_private.gears.rating.bevel.standards._569": [
            "AGMASpiralBevelMeshSingleFlankRating"
        ],
        "_private.gears.rating.bevel.standards._570": [
            "GleasonSpiralBevelGearSingleFlankRating"
        ],
        "_private.gears.rating.bevel.standards._571": [
            "GleasonSpiralBevelMeshSingleFlankRating"
        ],
        "_private.gears.rating.bevel.standards._572": [
            "SpiralBevelGearSingleFlankRating"
        ],
        "_private.gears.rating.bevel.standards._573": [
            "SpiralBevelMeshSingleFlankRating"
        ],
        "_private.gears.rating.bevel.standards._574": ["SpiralBevelRateableGear"],
        "_private.gears.rating.bevel.standards._575": ["SpiralBevelRateableMesh"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AGMASpiralBevelGearSingleFlankRating",
    "AGMASpiralBevelMeshSingleFlankRating",
    "GleasonSpiralBevelGearSingleFlankRating",
    "GleasonSpiralBevelMeshSingleFlankRating",
    "SpiralBevelGearSingleFlankRating",
    "SpiralBevelMeshSingleFlankRating",
    "SpiralBevelRateableGear",
    "SpiralBevelRateableMesh",
)
