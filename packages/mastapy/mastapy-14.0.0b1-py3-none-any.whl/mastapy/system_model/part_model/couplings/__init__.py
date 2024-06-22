"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.part_model.couplings._2633 import BeltDrive
    from mastapy._private.system_model.part_model.couplings._2634 import BeltDriveType
    from mastapy._private.system_model.part_model.couplings._2635 import Clutch
    from mastapy._private.system_model.part_model.couplings._2636 import ClutchHalf
    from mastapy._private.system_model.part_model.couplings._2637 import ClutchType
    from mastapy._private.system_model.part_model.couplings._2638 import ConceptCoupling
    from mastapy._private.system_model.part_model.couplings._2639 import (
        ConceptCouplingHalf,
    )
    from mastapy._private.system_model.part_model.couplings._2640 import (
        ConceptCouplingHalfPositioning,
    )
    from mastapy._private.system_model.part_model.couplings._2641 import Coupling
    from mastapy._private.system_model.part_model.couplings._2642 import CouplingHalf
    from mastapy._private.system_model.part_model.couplings._2643 import (
        CrowningSpecification,
    )
    from mastapy._private.system_model.part_model.couplings._2644 import CVT
    from mastapy._private.system_model.part_model.couplings._2645 import CVTPulley
    from mastapy._private.system_model.part_model.couplings._2646 import (
        PartToPartShearCoupling,
    )
    from mastapy._private.system_model.part_model.couplings._2647 import (
        PartToPartShearCouplingHalf,
    )
    from mastapy._private.system_model.part_model.couplings._2648 import (
        PitchErrorFlankOptions,
    )
    from mastapy._private.system_model.part_model.couplings._2649 import Pulley
    from mastapy._private.system_model.part_model.couplings._2650 import (
        RigidConnectorStiffnessType,
    )
    from mastapy._private.system_model.part_model.couplings._2651 import (
        RigidConnectorTiltStiffnessTypes,
    )
    from mastapy._private.system_model.part_model.couplings._2652 import (
        RigidConnectorToothLocation,
    )
    from mastapy._private.system_model.part_model.couplings._2653 import (
        RigidConnectorToothSpacingType,
    )
    from mastapy._private.system_model.part_model.couplings._2654 import (
        RigidConnectorTypes,
    )
    from mastapy._private.system_model.part_model.couplings._2655 import RollingRing
    from mastapy._private.system_model.part_model.couplings._2656 import (
        RollingRingAssembly,
    )
    from mastapy._private.system_model.part_model.couplings._2657 import (
        ShaftHubConnection,
    )
    from mastapy._private.system_model.part_model.couplings._2658 import (
        SplineFitOptions,
    )
    from mastapy._private.system_model.part_model.couplings._2659 import (
        SplineLeadRelief,
    )
    from mastapy._private.system_model.part_model.couplings._2660 import (
        SplinePitchErrorInputType,
    )
    from mastapy._private.system_model.part_model.couplings._2661 import (
        SplinePitchErrorOptions,
    )
    from mastapy._private.system_model.part_model.couplings._2662 import SpringDamper
    from mastapy._private.system_model.part_model.couplings._2663 import (
        SpringDamperHalf,
    )
    from mastapy._private.system_model.part_model.couplings._2664 import Synchroniser
    from mastapy._private.system_model.part_model.couplings._2665 import (
        SynchroniserCone,
    )
    from mastapy._private.system_model.part_model.couplings._2666 import (
        SynchroniserHalf,
    )
    from mastapy._private.system_model.part_model.couplings._2667 import (
        SynchroniserPart,
    )
    from mastapy._private.system_model.part_model.couplings._2668 import (
        SynchroniserSleeve,
    )
    from mastapy._private.system_model.part_model.couplings._2669 import TorqueConverter
    from mastapy._private.system_model.part_model.couplings._2670 import (
        TorqueConverterPump,
    )
    from mastapy._private.system_model.part_model.couplings._2671 import (
        TorqueConverterSpeedRatio,
    )
    from mastapy._private.system_model.part_model.couplings._2672 import (
        TorqueConverterTurbine,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.couplings._2633": ["BeltDrive"],
        "_private.system_model.part_model.couplings._2634": ["BeltDriveType"],
        "_private.system_model.part_model.couplings._2635": ["Clutch"],
        "_private.system_model.part_model.couplings._2636": ["ClutchHalf"],
        "_private.system_model.part_model.couplings._2637": ["ClutchType"],
        "_private.system_model.part_model.couplings._2638": ["ConceptCoupling"],
        "_private.system_model.part_model.couplings._2639": ["ConceptCouplingHalf"],
        "_private.system_model.part_model.couplings._2640": [
            "ConceptCouplingHalfPositioning"
        ],
        "_private.system_model.part_model.couplings._2641": ["Coupling"],
        "_private.system_model.part_model.couplings._2642": ["CouplingHalf"],
        "_private.system_model.part_model.couplings._2643": ["CrowningSpecification"],
        "_private.system_model.part_model.couplings._2644": ["CVT"],
        "_private.system_model.part_model.couplings._2645": ["CVTPulley"],
        "_private.system_model.part_model.couplings._2646": ["PartToPartShearCoupling"],
        "_private.system_model.part_model.couplings._2647": [
            "PartToPartShearCouplingHalf"
        ],
        "_private.system_model.part_model.couplings._2648": ["PitchErrorFlankOptions"],
        "_private.system_model.part_model.couplings._2649": ["Pulley"],
        "_private.system_model.part_model.couplings._2650": [
            "RigidConnectorStiffnessType"
        ],
        "_private.system_model.part_model.couplings._2651": [
            "RigidConnectorTiltStiffnessTypes"
        ],
        "_private.system_model.part_model.couplings._2652": [
            "RigidConnectorToothLocation"
        ],
        "_private.system_model.part_model.couplings._2653": [
            "RigidConnectorToothSpacingType"
        ],
        "_private.system_model.part_model.couplings._2654": ["RigidConnectorTypes"],
        "_private.system_model.part_model.couplings._2655": ["RollingRing"],
        "_private.system_model.part_model.couplings._2656": ["RollingRingAssembly"],
        "_private.system_model.part_model.couplings._2657": ["ShaftHubConnection"],
        "_private.system_model.part_model.couplings._2658": ["SplineFitOptions"],
        "_private.system_model.part_model.couplings._2659": ["SplineLeadRelief"],
        "_private.system_model.part_model.couplings._2660": [
            "SplinePitchErrorInputType"
        ],
        "_private.system_model.part_model.couplings._2661": ["SplinePitchErrorOptions"],
        "_private.system_model.part_model.couplings._2662": ["SpringDamper"],
        "_private.system_model.part_model.couplings._2663": ["SpringDamperHalf"],
        "_private.system_model.part_model.couplings._2664": ["Synchroniser"],
        "_private.system_model.part_model.couplings._2665": ["SynchroniserCone"],
        "_private.system_model.part_model.couplings._2666": ["SynchroniserHalf"],
        "_private.system_model.part_model.couplings._2667": ["SynchroniserPart"],
        "_private.system_model.part_model.couplings._2668": ["SynchroniserSleeve"],
        "_private.system_model.part_model.couplings._2669": ["TorqueConverter"],
        "_private.system_model.part_model.couplings._2670": ["TorqueConverterPump"],
        "_private.system_model.part_model.couplings._2671": [
            "TorqueConverterSpeedRatio"
        ],
        "_private.system_model.part_model.couplings._2672": ["TorqueConverterTurbine"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BeltDrive",
    "BeltDriveType",
    "Clutch",
    "ClutchHalf",
    "ClutchType",
    "ConceptCoupling",
    "ConceptCouplingHalf",
    "ConceptCouplingHalfPositioning",
    "Coupling",
    "CouplingHalf",
    "CrowningSpecification",
    "CVT",
    "CVTPulley",
    "PartToPartShearCoupling",
    "PartToPartShearCouplingHalf",
    "PitchErrorFlankOptions",
    "Pulley",
    "RigidConnectorStiffnessType",
    "RigidConnectorTiltStiffnessTypes",
    "RigidConnectorToothLocation",
    "RigidConnectorToothSpacingType",
    "RigidConnectorTypes",
    "RollingRing",
    "RollingRingAssembly",
    "ShaftHubConnection",
    "SplineFitOptions",
    "SplineLeadRelief",
    "SplinePitchErrorInputType",
    "SplinePitchErrorOptions",
    "SpringDamper",
    "SpringDamperHalf",
    "Synchroniser",
    "SynchroniserCone",
    "SynchroniserHalf",
    "SynchroniserPart",
    "SynchroniserSleeve",
    "TorqueConverter",
    "TorqueConverterPump",
    "TorqueConverterSpeedRatio",
    "TorqueConverterTurbine",
)
