"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.part_model.gears._2566 import (
        ActiveCylindricalGearSetDesignSelection,
    )
    from mastapy._private.system_model.part_model.gears._2567 import (
        ActiveGearSetDesignSelection,
    )
    from mastapy._private.system_model.part_model.gears._2568 import (
        ActiveGearSetDesignSelectionGroup,
    )
    from mastapy._private.system_model.part_model.gears._2569 import (
        AGMAGleasonConicalGear,
    )
    from mastapy._private.system_model.part_model.gears._2570 import (
        AGMAGleasonConicalGearSet,
    )
    from mastapy._private.system_model.part_model.gears._2571 import (
        BevelDifferentialGear,
    )
    from mastapy._private.system_model.part_model.gears._2572 import (
        BevelDifferentialGearSet,
    )
    from mastapy._private.system_model.part_model.gears._2573 import (
        BevelDifferentialPlanetGear,
    )
    from mastapy._private.system_model.part_model.gears._2574 import (
        BevelDifferentialSunGear,
    )
    from mastapy._private.system_model.part_model.gears._2575 import BevelGear
    from mastapy._private.system_model.part_model.gears._2576 import BevelGearSet
    from mastapy._private.system_model.part_model.gears._2577 import ConceptGear
    from mastapy._private.system_model.part_model.gears._2578 import ConceptGearSet
    from mastapy._private.system_model.part_model.gears._2579 import ConicalGear
    from mastapy._private.system_model.part_model.gears._2580 import ConicalGearSet
    from mastapy._private.system_model.part_model.gears._2581 import CylindricalGear
    from mastapy._private.system_model.part_model.gears._2582 import CylindricalGearSet
    from mastapy._private.system_model.part_model.gears._2583 import (
        CylindricalPlanetGear,
    )
    from mastapy._private.system_model.part_model.gears._2584 import FaceGear
    from mastapy._private.system_model.part_model.gears._2585 import FaceGearSet
    from mastapy._private.system_model.part_model.gears._2586 import Gear
    from mastapy._private.system_model.part_model.gears._2587 import GearOrientations
    from mastapy._private.system_model.part_model.gears._2588 import GearSet
    from mastapy._private.system_model.part_model.gears._2589 import (
        GearSetConfiguration,
    )
    from mastapy._private.system_model.part_model.gears._2590 import HypoidGear
    from mastapy._private.system_model.part_model.gears._2591 import HypoidGearSet
    from mastapy._private.system_model.part_model.gears._2592 import (
        KlingelnbergCycloPalloidConicalGear,
    )
    from mastapy._private.system_model.part_model.gears._2593 import (
        KlingelnbergCycloPalloidConicalGearSet,
    )
    from mastapy._private.system_model.part_model.gears._2594 import (
        KlingelnbergCycloPalloidHypoidGear,
    )
    from mastapy._private.system_model.part_model.gears._2595 import (
        KlingelnbergCycloPalloidHypoidGearSet,
    )
    from mastapy._private.system_model.part_model.gears._2596 import (
        KlingelnbergCycloPalloidSpiralBevelGear,
    )
    from mastapy._private.system_model.part_model.gears._2597 import (
        KlingelnbergCycloPalloidSpiralBevelGearSet,
    )
    from mastapy._private.system_model.part_model.gears._2598 import PlanetaryGearSet
    from mastapy._private.system_model.part_model.gears._2599 import SpiralBevelGear
    from mastapy._private.system_model.part_model.gears._2600 import SpiralBevelGearSet
    from mastapy._private.system_model.part_model.gears._2601 import (
        StraightBevelDiffGear,
    )
    from mastapy._private.system_model.part_model.gears._2602 import (
        StraightBevelDiffGearSet,
    )
    from mastapy._private.system_model.part_model.gears._2603 import StraightBevelGear
    from mastapy._private.system_model.part_model.gears._2604 import (
        StraightBevelGearSet,
    )
    from mastapy._private.system_model.part_model.gears._2605 import (
        StraightBevelPlanetGear,
    )
    from mastapy._private.system_model.part_model.gears._2606 import (
        StraightBevelSunGear,
    )
    from mastapy._private.system_model.part_model.gears._2607 import WormGear
    from mastapy._private.system_model.part_model.gears._2608 import WormGearSet
    from mastapy._private.system_model.part_model.gears._2609 import ZerolBevelGear
    from mastapy._private.system_model.part_model.gears._2610 import ZerolBevelGearSet
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.gears._2566": [
            "ActiveCylindricalGearSetDesignSelection"
        ],
        "_private.system_model.part_model.gears._2567": [
            "ActiveGearSetDesignSelection"
        ],
        "_private.system_model.part_model.gears._2568": [
            "ActiveGearSetDesignSelectionGroup"
        ],
        "_private.system_model.part_model.gears._2569": ["AGMAGleasonConicalGear"],
        "_private.system_model.part_model.gears._2570": ["AGMAGleasonConicalGearSet"],
        "_private.system_model.part_model.gears._2571": ["BevelDifferentialGear"],
        "_private.system_model.part_model.gears._2572": ["BevelDifferentialGearSet"],
        "_private.system_model.part_model.gears._2573": ["BevelDifferentialPlanetGear"],
        "_private.system_model.part_model.gears._2574": ["BevelDifferentialSunGear"],
        "_private.system_model.part_model.gears._2575": ["BevelGear"],
        "_private.system_model.part_model.gears._2576": ["BevelGearSet"],
        "_private.system_model.part_model.gears._2577": ["ConceptGear"],
        "_private.system_model.part_model.gears._2578": ["ConceptGearSet"],
        "_private.system_model.part_model.gears._2579": ["ConicalGear"],
        "_private.system_model.part_model.gears._2580": ["ConicalGearSet"],
        "_private.system_model.part_model.gears._2581": ["CylindricalGear"],
        "_private.system_model.part_model.gears._2582": ["CylindricalGearSet"],
        "_private.system_model.part_model.gears._2583": ["CylindricalPlanetGear"],
        "_private.system_model.part_model.gears._2584": ["FaceGear"],
        "_private.system_model.part_model.gears._2585": ["FaceGearSet"],
        "_private.system_model.part_model.gears._2586": ["Gear"],
        "_private.system_model.part_model.gears._2587": ["GearOrientations"],
        "_private.system_model.part_model.gears._2588": ["GearSet"],
        "_private.system_model.part_model.gears._2589": ["GearSetConfiguration"],
        "_private.system_model.part_model.gears._2590": ["HypoidGear"],
        "_private.system_model.part_model.gears._2591": ["HypoidGearSet"],
        "_private.system_model.part_model.gears._2592": [
            "KlingelnbergCycloPalloidConicalGear"
        ],
        "_private.system_model.part_model.gears._2593": [
            "KlingelnbergCycloPalloidConicalGearSet"
        ],
        "_private.system_model.part_model.gears._2594": [
            "KlingelnbergCycloPalloidHypoidGear"
        ],
        "_private.system_model.part_model.gears._2595": [
            "KlingelnbergCycloPalloidHypoidGearSet"
        ],
        "_private.system_model.part_model.gears._2596": [
            "KlingelnbergCycloPalloidSpiralBevelGear"
        ],
        "_private.system_model.part_model.gears._2597": [
            "KlingelnbergCycloPalloidSpiralBevelGearSet"
        ],
        "_private.system_model.part_model.gears._2598": ["PlanetaryGearSet"],
        "_private.system_model.part_model.gears._2599": ["SpiralBevelGear"],
        "_private.system_model.part_model.gears._2600": ["SpiralBevelGearSet"],
        "_private.system_model.part_model.gears._2601": ["StraightBevelDiffGear"],
        "_private.system_model.part_model.gears._2602": ["StraightBevelDiffGearSet"],
        "_private.system_model.part_model.gears._2603": ["StraightBevelGear"],
        "_private.system_model.part_model.gears._2604": ["StraightBevelGearSet"],
        "_private.system_model.part_model.gears._2605": ["StraightBevelPlanetGear"],
        "_private.system_model.part_model.gears._2606": ["StraightBevelSunGear"],
        "_private.system_model.part_model.gears._2607": ["WormGear"],
        "_private.system_model.part_model.gears._2608": ["WormGearSet"],
        "_private.system_model.part_model.gears._2609": ["ZerolBevelGear"],
        "_private.system_model.part_model.gears._2610": ["ZerolBevelGearSet"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ActiveCylindricalGearSetDesignSelection",
    "ActiveGearSetDesignSelection",
    "ActiveGearSetDesignSelectionGroup",
    "AGMAGleasonConicalGear",
    "AGMAGleasonConicalGearSet",
    "BevelDifferentialGear",
    "BevelDifferentialGearSet",
    "BevelDifferentialPlanetGear",
    "BevelDifferentialSunGear",
    "BevelGear",
    "BevelGearSet",
    "ConceptGear",
    "ConceptGearSet",
    "ConicalGear",
    "ConicalGearSet",
    "CylindricalGear",
    "CylindricalGearSet",
    "CylindricalPlanetGear",
    "FaceGear",
    "FaceGearSet",
    "Gear",
    "GearOrientations",
    "GearSet",
    "GearSetConfiguration",
    "HypoidGear",
    "HypoidGearSet",
    "KlingelnbergCycloPalloidConicalGear",
    "KlingelnbergCycloPalloidConicalGearSet",
    "KlingelnbergCycloPalloidHypoidGear",
    "KlingelnbergCycloPalloidHypoidGearSet",
    "KlingelnbergCycloPalloidSpiralBevelGear",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
    "PlanetaryGearSet",
    "SpiralBevelGear",
    "SpiralBevelGearSet",
    "StraightBevelDiffGear",
    "StraightBevelDiffGearSet",
    "StraightBevelGear",
    "StraightBevelGearSet",
    "StraightBevelPlanetGear",
    "StraightBevelSunGear",
    "WormGear",
    "WormGearSet",
    "ZerolBevelGear",
    "ZerolBevelGearSet",
)
