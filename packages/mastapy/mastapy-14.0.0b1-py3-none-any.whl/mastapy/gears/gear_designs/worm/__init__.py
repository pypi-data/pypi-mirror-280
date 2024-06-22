"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.gear_designs.worm._980 import WormDesign
    from mastapy._private.gears.gear_designs.worm._981 import WormGearDesign
    from mastapy._private.gears.gear_designs.worm._982 import WormGearMeshDesign
    from mastapy._private.gears.gear_designs.worm._983 import WormGearSetDesign
    from mastapy._private.gears.gear_designs.worm._984 import WormWheelDesign
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.gear_designs.worm._980": ["WormDesign"],
        "_private.gears.gear_designs.worm._981": ["WormGearDesign"],
        "_private.gears.gear_designs.worm._982": ["WormGearMeshDesign"],
        "_private.gears.gear_designs.worm._983": ["WormGearSetDesign"],
        "_private.gears.gear_designs.worm._984": ["WormWheelDesign"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "WormDesign",
    "WormGearDesign",
    "WormGearMeshDesign",
    "WormGearSetDesign",
    "WormWheelDesign",
)
