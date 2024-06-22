"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.gears.rating.virtual_cylindrical_gears._389 import (
        BevelVirtualCylindricalGearISO10300MethodB2,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._390 import (
        BevelVirtualCylindricalGearSetISO10300MethodB1,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._391 import (
        BevelVirtualCylindricalGearSetISO10300MethodB2,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._392 import (
        HypoidVirtualCylindricalGearISO10300MethodB2,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._393 import (
        HypoidVirtualCylindricalGearSetISO10300MethodB1,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._394 import (
        HypoidVirtualCylindricalGearSetISO10300MethodB2,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._395 import (
        KlingelnbergHypoidVirtualCylindricalGear,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._396 import (
        KlingelnbergSpiralBevelVirtualCylindricalGear,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._397 import (
        KlingelnbergVirtualCylindricalGear,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._398 import (
        KlingelnbergVirtualCylindricalGearSet,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._399 import (
        VirtualCylindricalGear,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._400 import (
        VirtualCylindricalGearBasic,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._401 import (
        VirtualCylindricalGearISO10300MethodB1,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._402 import (
        VirtualCylindricalGearISO10300MethodB2,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._403 import (
        VirtualCylindricalGearSet,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._404 import (
        VirtualCylindricalGearSetISO10300MethodB1,
    )
    from mastapy._private.gears.rating.virtual_cylindrical_gears._405 import (
        VirtualCylindricalGearSetISO10300MethodB2,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.gears.rating.virtual_cylindrical_gears._389": [
            "BevelVirtualCylindricalGearISO10300MethodB2"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._390": [
            "BevelVirtualCylindricalGearSetISO10300MethodB1"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._391": [
            "BevelVirtualCylindricalGearSetISO10300MethodB2"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._392": [
            "HypoidVirtualCylindricalGearISO10300MethodB2"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._393": [
            "HypoidVirtualCylindricalGearSetISO10300MethodB1"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._394": [
            "HypoidVirtualCylindricalGearSetISO10300MethodB2"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._395": [
            "KlingelnbergHypoidVirtualCylindricalGear"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._396": [
            "KlingelnbergSpiralBevelVirtualCylindricalGear"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._397": [
            "KlingelnbergVirtualCylindricalGear"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._398": [
            "KlingelnbergVirtualCylindricalGearSet"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._399": [
            "VirtualCylindricalGear"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._400": [
            "VirtualCylindricalGearBasic"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._401": [
            "VirtualCylindricalGearISO10300MethodB1"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._402": [
            "VirtualCylindricalGearISO10300MethodB2"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._403": [
            "VirtualCylindricalGearSet"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._404": [
            "VirtualCylindricalGearSetISO10300MethodB1"
        ],
        "_private.gears.rating.virtual_cylindrical_gears._405": [
            "VirtualCylindricalGearSetISO10300MethodB2"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BevelVirtualCylindricalGearISO10300MethodB2",
    "BevelVirtualCylindricalGearSetISO10300MethodB1",
    "BevelVirtualCylindricalGearSetISO10300MethodB2",
    "HypoidVirtualCylindricalGearISO10300MethodB2",
    "HypoidVirtualCylindricalGearSetISO10300MethodB1",
    "HypoidVirtualCylindricalGearSetISO10300MethodB2",
    "KlingelnbergHypoidVirtualCylindricalGear",
    "KlingelnbergSpiralBevelVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGearSet",
    "VirtualCylindricalGear",
    "VirtualCylindricalGearBasic",
    "VirtualCylindricalGearISO10300MethodB1",
    "VirtualCylindricalGearISO10300MethodB2",
    "VirtualCylindricalGearSet",
    "VirtualCylindricalGearSetISO10300MethodB1",
    "VirtualCylindricalGearSetISO10300MethodB2",
)
