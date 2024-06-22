"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.system_model.part_model._2487 import Assembly
    from mastapy._private.system_model.part_model._2488 import AbstractAssembly
    from mastapy._private.system_model.part_model._2489 import AbstractShaft
    from mastapy._private.system_model.part_model._2490 import AbstractShaftOrHousing
    from mastapy._private.system_model.part_model._2491 import (
        AGMALoadSharingTableApplicationLevel,
    )
    from mastapy._private.system_model.part_model._2492 import (
        AxialInternalClearanceTolerance,
    )
    from mastapy._private.system_model.part_model._2493 import Bearing
    from mastapy._private.system_model.part_model._2494 import BearingF0InputMethod
    from mastapy._private.system_model.part_model._2495 import (
        BearingRaceMountingOptions,
    )
    from mastapy._private.system_model.part_model._2496 import Bolt
    from mastapy._private.system_model.part_model._2497 import BoltedJoint
    from mastapy._private.system_model.part_model._2498 import Component
    from mastapy._private.system_model.part_model._2499 import ComponentsConnectedResult
    from mastapy._private.system_model.part_model._2500 import ConnectedSockets
    from mastapy._private.system_model.part_model._2501 import Connector
    from mastapy._private.system_model.part_model._2502 import Datum
    from mastapy._private.system_model.part_model._2503 import (
        ElectricMachineSearchRegionSpecificationMethod,
    )
    from mastapy._private.system_model.part_model._2504 import EnginePartLoad
    from mastapy._private.system_model.part_model._2505 import EngineSpeed
    from mastapy._private.system_model.part_model._2506 import ExternalCADModel
    from mastapy._private.system_model.part_model._2507 import FEPart
    from mastapy._private.system_model.part_model._2508 import FlexiblePinAssembly
    from mastapy._private.system_model.part_model._2509 import GuideDxfModel
    from mastapy._private.system_model.part_model._2510 import GuideImage
    from mastapy._private.system_model.part_model._2511 import GuideModelUsage
    from mastapy._private.system_model.part_model._2512 import (
        InnerBearingRaceMountingOptions,
    )
    from mastapy._private.system_model.part_model._2513 import (
        InternalClearanceTolerance,
    )
    from mastapy._private.system_model.part_model._2514 import LoadSharingModes
    from mastapy._private.system_model.part_model._2515 import LoadSharingSettings
    from mastapy._private.system_model.part_model._2516 import MassDisc
    from mastapy._private.system_model.part_model._2517 import MeasurementComponent
    from mastapy._private.system_model.part_model._2518 import Microphone
    from mastapy._private.system_model.part_model._2519 import MicrophoneArray
    from mastapy._private.system_model.part_model._2520 import MountableComponent
    from mastapy._private.system_model.part_model._2521 import OilLevelSpecification
    from mastapy._private.system_model.part_model._2522 import OilSeal
    from mastapy._private.system_model.part_model._2523 import (
        OuterBearingRaceMountingOptions,
    )
    from mastapy._private.system_model.part_model._2524 import Part
    from mastapy._private.system_model.part_model._2525 import PlanetCarrier
    from mastapy._private.system_model.part_model._2526 import PlanetCarrierSettings
    from mastapy._private.system_model.part_model._2527 import PointLoad
    from mastapy._private.system_model.part_model._2528 import PowerLoad
    from mastapy._private.system_model.part_model._2529 import (
        RadialInternalClearanceTolerance,
    )
    from mastapy._private.system_model.part_model._2530 import RootAssembly
    from mastapy._private.system_model.part_model._2531 import (
        ShaftDiameterModificationDueToRollingBearingRing,
    )
    from mastapy._private.system_model.part_model._2532 import SpecialisedAssembly
    from mastapy._private.system_model.part_model._2533 import UnbalancedMass
    from mastapy._private.system_model.part_model._2534 import (
        UnbalancedMassInclusionOption,
    )
    from mastapy._private.system_model.part_model._2535 import VirtualComponent
    from mastapy._private.system_model.part_model._2536 import (
        WindTurbineBladeModeDetails,
    )
    from mastapy._private.system_model.part_model._2537 import (
        WindTurbineSingleBladeDetails,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model._2487": ["Assembly"],
        "_private.system_model.part_model._2488": ["AbstractAssembly"],
        "_private.system_model.part_model._2489": ["AbstractShaft"],
        "_private.system_model.part_model._2490": ["AbstractShaftOrHousing"],
        "_private.system_model.part_model._2491": [
            "AGMALoadSharingTableApplicationLevel"
        ],
        "_private.system_model.part_model._2492": ["AxialInternalClearanceTolerance"],
        "_private.system_model.part_model._2493": ["Bearing"],
        "_private.system_model.part_model._2494": ["BearingF0InputMethod"],
        "_private.system_model.part_model._2495": ["BearingRaceMountingOptions"],
        "_private.system_model.part_model._2496": ["Bolt"],
        "_private.system_model.part_model._2497": ["BoltedJoint"],
        "_private.system_model.part_model._2498": ["Component"],
        "_private.system_model.part_model._2499": ["ComponentsConnectedResult"],
        "_private.system_model.part_model._2500": ["ConnectedSockets"],
        "_private.system_model.part_model._2501": ["Connector"],
        "_private.system_model.part_model._2502": ["Datum"],
        "_private.system_model.part_model._2503": [
            "ElectricMachineSearchRegionSpecificationMethod"
        ],
        "_private.system_model.part_model._2504": ["EnginePartLoad"],
        "_private.system_model.part_model._2505": ["EngineSpeed"],
        "_private.system_model.part_model._2506": ["ExternalCADModel"],
        "_private.system_model.part_model._2507": ["FEPart"],
        "_private.system_model.part_model._2508": ["FlexiblePinAssembly"],
        "_private.system_model.part_model._2509": ["GuideDxfModel"],
        "_private.system_model.part_model._2510": ["GuideImage"],
        "_private.system_model.part_model._2511": ["GuideModelUsage"],
        "_private.system_model.part_model._2512": ["InnerBearingRaceMountingOptions"],
        "_private.system_model.part_model._2513": ["InternalClearanceTolerance"],
        "_private.system_model.part_model._2514": ["LoadSharingModes"],
        "_private.system_model.part_model._2515": ["LoadSharingSettings"],
        "_private.system_model.part_model._2516": ["MassDisc"],
        "_private.system_model.part_model._2517": ["MeasurementComponent"],
        "_private.system_model.part_model._2518": ["Microphone"],
        "_private.system_model.part_model._2519": ["MicrophoneArray"],
        "_private.system_model.part_model._2520": ["MountableComponent"],
        "_private.system_model.part_model._2521": ["OilLevelSpecification"],
        "_private.system_model.part_model._2522": ["OilSeal"],
        "_private.system_model.part_model._2523": ["OuterBearingRaceMountingOptions"],
        "_private.system_model.part_model._2524": ["Part"],
        "_private.system_model.part_model._2525": ["PlanetCarrier"],
        "_private.system_model.part_model._2526": ["PlanetCarrierSettings"],
        "_private.system_model.part_model._2527": ["PointLoad"],
        "_private.system_model.part_model._2528": ["PowerLoad"],
        "_private.system_model.part_model._2529": ["RadialInternalClearanceTolerance"],
        "_private.system_model.part_model._2530": ["RootAssembly"],
        "_private.system_model.part_model._2531": [
            "ShaftDiameterModificationDueToRollingBearingRing"
        ],
        "_private.system_model.part_model._2532": ["SpecialisedAssembly"],
        "_private.system_model.part_model._2533": ["UnbalancedMass"],
        "_private.system_model.part_model._2534": ["UnbalancedMassInclusionOption"],
        "_private.system_model.part_model._2535": ["VirtualComponent"],
        "_private.system_model.part_model._2536": ["WindTurbineBladeModeDetails"],
        "_private.system_model.part_model._2537": ["WindTurbineSingleBladeDetails"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "Assembly",
    "AbstractAssembly",
    "AbstractShaft",
    "AbstractShaftOrHousing",
    "AGMALoadSharingTableApplicationLevel",
    "AxialInternalClearanceTolerance",
    "Bearing",
    "BearingF0InputMethod",
    "BearingRaceMountingOptions",
    "Bolt",
    "BoltedJoint",
    "Component",
    "ComponentsConnectedResult",
    "ConnectedSockets",
    "Connector",
    "Datum",
    "ElectricMachineSearchRegionSpecificationMethod",
    "EnginePartLoad",
    "EngineSpeed",
    "ExternalCADModel",
    "FEPart",
    "FlexiblePinAssembly",
    "GuideDxfModel",
    "GuideImage",
    "GuideModelUsage",
    "InnerBearingRaceMountingOptions",
    "InternalClearanceTolerance",
    "LoadSharingModes",
    "LoadSharingSettings",
    "MassDisc",
    "MeasurementComponent",
    "Microphone",
    "MicrophoneArray",
    "MountableComponent",
    "OilLevelSpecification",
    "OilSeal",
    "OuterBearingRaceMountingOptions",
    "Part",
    "PlanetCarrier",
    "PlanetCarrierSettings",
    "PointLoad",
    "PowerLoad",
    "RadialInternalClearanceTolerance",
    "RootAssembly",
    "ShaftDiameterModificationDueToRollingBearingRing",
    "SpecialisedAssembly",
    "UnbalancedMass",
    "UnbalancedMassInclusionOption",
    "VirtualComponent",
    "WindTurbineBladeModeDetails",
    "WindTurbineSingleBladeDetails",
)
