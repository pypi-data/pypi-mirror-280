"""CompoundSystemDeflectionAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.analyses_and_results import _2702
from mastapy._private._internal.cast_exception import CastException

_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
)
_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingConnection"
)
_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)
_TORQUE_CONVERTER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterConnection",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "PartToPartShearCouplingConnection",
)
_CLUTCH_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ClutchConnection"
)
_ABSTRACT_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
)
_MICROPHONE = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Microphone")
_MICROPHONE_ARRAY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MicrophoneArray"
)
_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
)
_BEARING = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bearing")
_BOLT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bolt")
_BOLTED_JOINT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "BoltedJoint")
_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_CONNECTOR = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")
_DATUM = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Datum")
_EXTERNAL_CAD_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ExternalCADModel"
)
_FE_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "FEPart")
_FLEXIBLE_PIN_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "FlexiblePinAssembly"
)
_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Assembly")
_GUIDE_DXF_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "GuideDxfModel"
)
_MASS_DISC = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "MassDisc")
_MEASUREMENT_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MeasurementComponent"
)
_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)
_OIL_SEAL = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "OilSeal")
_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")
_PLANET_CARRIER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrier"
)
_POINT_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PointLoad")
_POWER_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")
_ROOT_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "RootAssembly")
_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)
_UNBALANCED_MASS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
)
_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)
_SHAFT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "Shaft")
_CONCEPT_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGear"
)
_CONCEPT_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
)
_FACE_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGear")
_FACE_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
)
_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)
_BEVEL_DIFFERENTIAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
)
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
)
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)
_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")
_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)
_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)
_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)
_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGear"
)
_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
)
_CYLINDRICAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalPlanetGear"
)
_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear")
_GEAR_SET = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet")
_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)
_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGear"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGear"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGear",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
)
_PLANETARY_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "PlanetaryGearSet"
)
_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGear"
)
_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGearSet"
)
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGear"
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)
_STRAIGHT_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGear"
)
_STRAIGHT_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGearSet"
)
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
)
_WORM_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGear")
_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)
_ZEROL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
)
_ZEROL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
)
_CYCLOIDAL_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
)
_CYCLOIDAL_DISC = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalDisc"
)
_RING_PINS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "RingPins"
)
_PART_TO_PART_SHEAR_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCoupling"
)
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCouplingHalf"
)
_BELT_DRIVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDrive"
)
_CLUTCH = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Clutch")
_CLUTCH_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
)
_CONCEPT_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
)
_CONCEPT_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalf"
)
_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
)
_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)
_CVT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVT")
_CVT_PULLEY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
)
_PULLEY = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Pulley")
_SHAFT_HUB_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ShaftHubConnection"
)
_ROLLING_RING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRing"
)
_ROLLING_RING_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRingAssembly"
)
_SPRING_DAMPER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamper"
)
_SPRING_DAMPER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamperHalf"
)
_SYNCHRONISER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Synchroniser"
)
_SYNCHRONISER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
)
_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)
_SYNCHRONISER_SLEEVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
)
_TORQUE_CONVERTER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverter"
)
_TORQUE_CONVERTER_PUMP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
)
_TORQUE_CONVERTER_TURBINE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterTurbine"
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "ShaftToMountableComponentConnection",
)
_CVT_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTBeltConnection"
)
_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BeltConnection"
)
_COAXIAL_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CoaxialConnection"
)
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)
_PLANETARY_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetaryConnection"
)
_ROLLING_RING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RollingRingConnection"
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "AbstractShaftToMountableComponentConnection",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelDifferentialGearMesh"
)
_CONCEPT_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearMesh"
)
_FACE_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "FaceGearMesh"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelDiffGearMesh"
)
_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)
_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)
_CYLINDRICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "CylindricalGearMesh"
)
_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidConicalGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidHypoidGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
)
_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "SpiralBevelGearMesh"
)
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelGearMesh"
)
_WORM_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "WormGearMesh"
)
_ZEROL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearMesh"
)
_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearMesh"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscCentralBearingConnection",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscPlanetaryBearingConnection",
)
_RING_PINS_TO_DISC_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "RingPinsToDiscConnection",
)
_COMPOUND_SYSTEM_DEFLECTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundSystemDeflectionAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, Iterable, TypeVar

    from mastapy._private.system_model.connections_and_sockets.couplings import (
        _2397,
        _2399,
        _2403,
        _2405,
        _2401,
        _2395,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2963,
        _2974,
        _3043,
        _3058,
        _2937,
        _3015,
        _3014,
        _2936,
        _2938,
        _2944,
        _2955,
        _2956,
        _2961,
        _2972,
        _2987,
        _2989,
        _2993,
        _2994,
        _2943,
        _2998,
        _3012,
        _3013,
        _3016,
        _3017,
        _3018,
        _3024,
        _3025,
        _3026,
        _3033,
        _3038,
        _3061,
        _3062,
        _3034,
        _2965,
        _2967,
        _2990,
        _2992,
        _2940,
        _2942,
        _2947,
        _2949,
        _2950,
        _2951,
        _2952,
        _2954,
        _2968,
        _2970,
        _2983,
        _2985,
        _2986,
        _2995,
        _2997,
        _2999,
        _3001,
        _3003,
        _3005,
        _3006,
        _3008,
        _3009,
        _3011,
        _3023,
        _3039,
        _3041,
        _3045,
        _3047,
        _3048,
        _3050,
        _3051,
        _3052,
        _3063,
        _3065,
        _3066,
        _3068,
        _2979,
        _2981,
        _3028,
        _3019,
        _3021,
        _2946,
        _2957,
        _2959,
        _2962,
        _2964,
        _2973,
        _2975,
        _2977,
        _2978,
        _3027,
        _3036,
        _3031,
        _3030,
        _3042,
        _3044,
        _3053,
        _3054,
        _3055,
        _3056,
        _3057,
        _3059,
        _3060,
        _3037,
        _2976,
        _2945,
        _2960,
        _2971,
        _3002,
        _3022,
        _3032,
        _2939,
        _2948,
        _2966,
        _2991,
        _3046,
        _2953,
        _2969,
        _2941,
        _2984,
        _3000,
        _3004,
        _3007,
        _3010,
        _3040,
        _3049,
        _3064,
        _3067,
        _2996,
        _2980,
        _2982,
        _3029,
        _3020,
        _2958,
    )
    from mastapy._private.system_model.part_model import (
        _2489,
        _2518,
        _2519,
        _2488,
        _2490,
        _2493,
        _2496,
        _2497,
        _2498,
        _2501,
        _2502,
        _2506,
        _2507,
        _2508,
        _2487,
        _2509,
        _2516,
        _2517,
        _2520,
        _2522,
        _2524,
        _2525,
        _2527,
        _2528,
        _2530,
        _2532,
        _2533,
        _2535,
    )
    from mastapy._private.system_model.part_model.shaft_model import _2538
    from mastapy._private.system_model.part_model.gears import (
        _2577,
        _2578,
        _2584,
        _2585,
        _2569,
        _2570,
        _2571,
        _2572,
        _2573,
        _2574,
        _2575,
        _2576,
        _2579,
        _2580,
        _2581,
        _2582,
        _2583,
        _2586,
        _2588,
        _2590,
        _2591,
        _2592,
        _2593,
        _2594,
        _2595,
        _2596,
        _2597,
        _2598,
        _2599,
        _2600,
        _2601,
        _2602,
        _2603,
        _2604,
        _2605,
        _2606,
        _2607,
        _2608,
        _2609,
        _2610,
    )
    from mastapy._private.system_model.part_model.cycloidal import _2624, _2625, _2626
    from mastapy._private.system_model.part_model.couplings import (
        _2646,
        _2647,
        _2633,
        _2635,
        _2636,
        _2638,
        _2639,
        _2641,
        _2642,
        _2644,
        _2645,
        _2649,
        _2657,
        _2655,
        _2656,
        _2662,
        _2663,
        _2664,
        _2666,
        _2667,
        _2668,
        _2669,
        _2670,
        _2672,
    )
    from mastapy._private.system_model.connections_and_sockets import (
        _2348,
        _2326,
        _2321,
        _2322,
        _2325,
        _2334,
        _2340,
        _2345,
        _2318,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2354,
        _2358,
        _2364,
        _2378,
        _2356,
        _2360,
        _2352,
        _2362,
        _2368,
        _2371,
        _2372,
        _2373,
        _2376,
        _2380,
        _2382,
        _2384,
        _2366,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import (
        _2388,
        _2391,
        _2394,
    )
    from mastapy._private import _7718

    Self = TypeVar("Self", bound="CompoundSystemDeflectionAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CompoundSystemDeflectionAnalysis._Cast_CompoundSystemDeflectionAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CompoundSystemDeflectionAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CompoundSystemDeflectionAnalysis:
    """Special nested class for casting CompoundSystemDeflectionAnalysis to subclasses."""

    __parent__: "CompoundSystemDeflectionAnalysis"

    @property
    def compound_analysis(self: "CastSelf") -> "_2702.CompoundAnalysis":
        return self.__parent__._cast(_2702.CompoundAnalysis)

    @property
    def marshal_by_ref_object_permanent(
        self: "CastSelf",
    ) -> "_7718.MarshalByRefObjectPermanent":
        from mastapy._private import _7718

        return self.__parent__._cast(_7718.MarshalByRefObjectPermanent)

    @property
    def compound_system_deflection_analysis(
        self: "CastSelf",
    ) -> "CompoundSystemDeflectionAnalysis":
        return self.__parent__

    def __getattr__(self: "CastSelf", name: str) -> "Any":
        try:
            return self.__getattribute__(name)
        except AttributeError:
            class_name = utility.camel(name)
            raise CastException(
                f'Detected an invalid cast. Cannot cast to type "{class_name}"'
            ) from None


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class CompoundSystemDeflectionAnalysis(_2702.CompoundAnalysis):
    """CompoundSystemDeflectionAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPOUND_SYSTEM_DEFLECTION_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: "Self", design_entity: "_2397.ConceptCouplingConnection"
    ) -> "Iterable[_2963.ConceptCouplingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConceptCouplingConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling_connection(
        self: "Self", design_entity: "_2399.CouplingConnection"
    ) -> "Iterable[_2974.CouplingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CouplingConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: "Self", design_entity: "_2403.SpringDamperConnection"
    ) -> "Iterable[_3043.SpringDamperConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SpringDamperConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection(
        self: "Self", design_entity: "_2405.TorqueConverterConnection"
    ) -> "Iterable[_3058.TorqueConverterConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.TorqueConverterConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft(
        self: "Self", design_entity: "_2489.AbstractShaft"
    ) -> "Iterable[_2937.AbstractShaftCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.AbstractShaftCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractShaft)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_microphone(
        self: "Self", design_entity: "_2518.Microphone"
    ) -> "Iterable[_3015.MicrophoneCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.MicrophoneCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.Microphone)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MICROPHONE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_microphone_array(
        self: "Self", design_entity: "_2519.MicrophoneArray"
    ) -> "Iterable[_3014.MicrophoneArrayCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.MicrophoneArrayCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.MicrophoneArray)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MICROPHONE_ARRAY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_assembly(
        self: "Self", design_entity: "_2488.AbstractAssembly"
    ) -> "Iterable[_2936.AbstractAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.AbstractAssemblyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing(
        self: "Self", design_entity: "_2490.AbstractShaftOrHousing"
    ) -> "Iterable[_2938.AbstractShaftOrHousingCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.AbstractShaftOrHousingCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractShaftOrHousing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bearing(
        self: "Self", design_entity: "_2493.Bearing"
    ) -> "Iterable[_2944.BearingCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BearingCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.Bearing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEARING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bolt(
        self: "Self", design_entity: "_2496.Bolt"
    ) -> "Iterable[_2955.BoltCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BoltCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.Bolt)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BOLT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bolted_joint(
        self: "Self", design_entity: "_2497.BoltedJoint"
    ) -> "Iterable[_2956.BoltedJointCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BoltedJointCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.BoltedJoint)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_component(
        self: "Self", design_entity: "_2498.Component"
    ) -> "Iterable[_2961.ComponentCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ComponentCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_connector(
        self: "Self", design_entity: "_2501.Connector"
    ) -> "Iterable[_2972.ConnectorCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConnectorCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.Connector)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONNECTOR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_datum(
        self: "Self", design_entity: "_2502.Datum"
    ) -> "Iterable[_2987.DatumCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.DatumCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.Datum)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_DATUM](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_external_cad_model(
        self: "Self", design_entity: "_2506.ExternalCADModel"
    ) -> "Iterable[_2989.ExternalCADModelCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ExternalCADModelCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.ExternalCADModel)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_fe_part(
        self: "Self", design_entity: "_2507.FEPart"
    ) -> "Iterable[_2993.FEPartCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.FEPartCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.FEPart)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FE_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly(
        self: "Self", design_entity: "_2508.FlexiblePinAssembly"
    ) -> "Iterable[_2994.FlexiblePinAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.FlexiblePinAssemblyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.FlexiblePinAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_assembly(
        self: "Self", design_entity: "_2487.Assembly"
    ) -> "Iterable[_2943.AssemblyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.AssemblyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.Assembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model(
        self: "Self", design_entity: "_2509.GuideDxfModel"
    ) -> "Iterable[_2998.GuideDxfModelCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.GuideDxfModelCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.GuideDxfModel)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_mass_disc(
        self: "Self", design_entity: "_2516.MassDisc"
    ) -> "Iterable[_3012.MassDiscCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.MassDiscCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.MassDisc)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MASS_DISC](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_measurement_component(
        self: "Self", design_entity: "_2517.MeasurementComponent"
    ) -> "Iterable[_3013.MeasurementComponentCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.MeasurementComponentCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.MeasurementComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_mountable_component(
        self: "Self", design_entity: "_2520.MountableComponent"
    ) -> "Iterable[_3016.MountableComponentCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.MountableComponentCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.MountableComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_oil_seal(
        self: "Self", design_entity: "_2522.OilSeal"
    ) -> "Iterable[_3017.OilSealCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.OilSealCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.OilSeal)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_OIL_SEAL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part(
        self: "Self", design_entity: "_2524.Part"
    ) -> "Iterable[_3018.PartCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PartCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_planet_carrier(
        self: "Self", design_entity: "_2525.PlanetCarrier"
    ) -> "Iterable[_3024.PlanetCarrierCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PlanetCarrierCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.PlanetCarrier)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_point_load(
        self: "Self", design_entity: "_2527.PointLoad"
    ) -> "Iterable[_3025.PointLoadCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PointLoadCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.PointLoad)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_POINT_LOAD](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_power_load(
        self: "Self", design_entity: "_2528.PowerLoad"
    ) -> "Iterable[_3026.PowerLoadCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PowerLoadCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.PowerLoad)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_POWER_LOAD](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_root_assembly(
        self: "Self", design_entity: "_2530.RootAssembly"
    ) -> "Iterable[_3033.RootAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.RootAssemblyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.RootAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_specialised_assembly(
        self: "Self", design_entity: "_2532.SpecialisedAssembly"
    ) -> "Iterable[_3038.SpecialisedAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SpecialisedAssemblyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.SpecialisedAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass(
        self: "Self", design_entity: "_2533.UnbalancedMass"
    ) -> "Iterable[_3061.UnbalancedMassCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.UnbalancedMassCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.UnbalancedMass)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_virtual_component(
        self: "Self", design_entity: "_2535.VirtualComponent"
    ) -> "Iterable[_3062.VirtualComponentCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.VirtualComponentCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.VirtualComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft(
        self: "Self", design_entity: "_2538.Shaft"
    ) -> "Iterable[_3034.ShaftCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ShaftCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.shaft_model.Shaft)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear(
        self: "Self", design_entity: "_2577.ConceptGear"
    ) -> "Iterable[_2965.ConceptGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConceptGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConceptGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear_set(
        self: "Self", design_entity: "_2578.ConceptGearSet"
    ) -> "Iterable[_2967.ConceptGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConceptGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConceptGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear(
        self: "Self", design_entity: "_2584.FaceGear"
    ) -> "Iterable[_2990.FaceGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.FaceGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.FaceGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear_set(
        self: "Self", design_entity: "_2585.FaceGearSet"
    ) -> "Iterable[_2992.FaceGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.FaceGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.FaceGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear(
        self: "Self", design_entity: "_2569.AGMAGleasonConicalGear"
    ) -> "Iterable[_2940.AGMAGleasonConicalGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.AGMAGleasonConicalGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set(
        self: "Self", design_entity: "_2570.AGMAGleasonConicalGearSet"
    ) -> "Iterable[_2942.AGMAGleasonConicalGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.AGMAGleasonConicalGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear(
        self: "Self", design_entity: "_2571.BevelDifferentialGear"
    ) -> "Iterable[_2947.BevelDifferentialGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set(
        self: "Self", design_entity: "_2572.BevelDifferentialGearSet"
    ) -> "Iterable[_2949.BevelDifferentialGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear(
        self: "Self", design_entity: "_2573.BevelDifferentialPlanetGear"
    ) -> "Iterable[_2950.BevelDifferentialPlanetGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialPlanetGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear(
        self: "Self", design_entity: "_2574.BevelDifferentialSunGear"
    ) -> "Iterable[_2951.BevelDifferentialSunGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialSunGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear(
        self: "Self", design_entity: "_2575.BevelGear"
    ) -> "Iterable[_2952.BevelGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BevelGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set(
        self: "Self", design_entity: "_2576.BevelGearSet"
    ) -> "Iterable[_2954.BevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BevelGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear(
        self: "Self", design_entity: "_2579.ConicalGear"
    ) -> "Iterable[_2968.ConicalGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConicalGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear_set(
        self: "Self", design_entity: "_2580.ConicalGearSet"
    ) -> "Iterable[_2970.ConicalGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConicalGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear(
        self: "Self", design_entity: "_2581.CylindricalGear"
    ) -> "Iterable[_2983.CylindricalGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CylindricalGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set(
        self: "Self", design_entity: "_2582.CylindricalGearSet"
    ) -> "Iterable[_2985.CylindricalGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CylindricalGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear(
        self: "Self", design_entity: "_2583.CylindricalPlanetGear"
    ) -> "Iterable[_2986.CylindricalPlanetGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CylindricalPlanetGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear(
        self: "Self", design_entity: "_2586.Gear"
    ) -> "Iterable[_2995.GearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.GearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.Gear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear_set(
        self: "Self", design_entity: "_2588.GearSet"
    ) -> "Iterable[_2997.GearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.GearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.GearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear(
        self: "Self", design_entity: "_2590.HypoidGear"
    ) -> "Iterable[_2999.HypoidGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.HypoidGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.HypoidGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set(
        self: "Self", design_entity: "_2591.HypoidGearSet"
    ) -> "Iterable[_3001.HypoidGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.HypoidGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.HypoidGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear(
        self: "Self", design_entity: "_2592.KlingelnbergCycloPalloidConicalGear"
    ) -> "Iterable[_3003.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: "Self", design_entity: "_2593.KlingelnbergCycloPalloidConicalGearSet"
    ) -> (
        "Iterable[_3005.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection]"
    ):
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: "Self", design_entity: "_2594.KlingelnbergCycloPalloidHypoidGear"
    ) -> "Iterable[_3006.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: "Self", design_entity: "_2595.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> (
        "Iterable[_3008.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]"
    ):
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "Self", design_entity: "_2596.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "Iterable[_3009.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: "Self", design_entity: "_2597.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "Iterable[_3011.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set(
        self: "Self", design_entity: "_2598.PlanetaryGearSet"
    ) -> "Iterable[_3023.PlanetaryGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PlanetaryGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.PlanetaryGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear(
        self: "Self", design_entity: "_2599.SpiralBevelGear"
    ) -> "Iterable[_3039.SpiralBevelGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SpiralBevelGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.SpiralBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set(
        self: "Self", design_entity: "_2600.SpiralBevelGearSet"
    ) -> "Iterable[_3041.SpiralBevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SpiralBevelGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.SpiralBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear(
        self: "Self", design_entity: "_2601.StraightBevelDiffGear"
    ) -> "Iterable[_3045.StraightBevelDiffGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelDiffGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set(
        self: "Self", design_entity: "_2602.StraightBevelDiffGearSet"
    ) -> "Iterable[_3047.StraightBevelDiffGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear(
        self: "Self", design_entity: "_2603.StraightBevelGear"
    ) -> "Iterable[_3048.StraightBevelGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.StraightBevelGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set(
        self: "Self", design_entity: "_2604.StraightBevelGearSet"
    ) -> "Iterable[_3050.StraightBevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.StraightBevelGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear(
        self: "Self", design_entity: "_2605.StraightBevelPlanetGear"
    ) -> "Iterable[_3051.StraightBevelPlanetGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.StraightBevelPlanetGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear(
        self: "Self", design_entity: "_2606.StraightBevelSunGear"
    ) -> "Iterable[_3052.StraightBevelSunGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.StraightBevelSunGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelSunGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear(
        self: "Self", design_entity: "_2607.WormGear"
    ) -> "Iterable[_3063.WormGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.WormGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.WormGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear_set(
        self: "Self", design_entity: "_2608.WormGearSet"
    ) -> "Iterable[_3065.WormGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.WormGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.WormGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear(
        self: "Self", design_entity: "_2609.ZerolBevelGear"
    ) -> "Iterable[_3066.ZerolBevelGearCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ZerolBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set(
        self: "Self", design_entity: "_2610.ZerolBevelGearSet"
    ) -> "Iterable[_3068.ZerolBevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearSetCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ZerolBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly(
        self: "Self", design_entity: "_2624.CycloidalAssembly"
    ) -> "Iterable[_2979.CycloidalAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CycloidalAssemblyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc(
        self: "Self", design_entity: "_2625.CycloidalDisc"
    ) -> "Iterable[_2981.CycloidalDiscCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CycloidalDiscCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.CycloidalDisc)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_ring_pins(
        self: "Self", design_entity: "_2626.RingPins"
    ) -> "Iterable[_3028.RingPinsCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.RingPinsCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.RingPins)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_RING_PINS](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling(
        self: "Self", design_entity: "_2646.PartToPartShearCoupling"
    ) -> "Iterable[_3019.PartToPartShearCouplingCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PartToPartShearCouplingCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half(
        self: "Self", design_entity: "_2647.PartToPartShearCouplingHalf"
    ) -> "Iterable[_3021.PartToPartShearCouplingHalfCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PartToPartShearCouplingHalfCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_belt_drive(
        self: "Self", design_entity: "_2633.BeltDrive"
    ) -> "Iterable[_2946.BeltDriveCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BeltDriveCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.BeltDrive)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch(
        self: "Self", design_entity: "_2635.Clutch"
    ) -> "Iterable[_2957.ClutchCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ClutchCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Clutch)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch_half(
        self: "Self", design_entity: "_2636.ClutchHalf"
    ) -> "Iterable[_2959.ClutchHalfCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ClutchHalfCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ClutchHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling(
        self: "Self", design_entity: "_2638.ConceptCoupling"
    ) -> "Iterable[_2962.ConceptCouplingCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConceptCouplingCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ConceptCoupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half(
        self: "Self", design_entity: "_2639.ConceptCouplingHalf"
    ) -> "Iterable[_2964.ConceptCouplingHalfCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConceptCouplingHalfCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling(
        self: "Self", design_entity: "_2641.Coupling"
    ) -> "Iterable[_2973.CouplingCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CouplingCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Coupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling_half(
        self: "Self", design_entity: "_2642.CouplingHalf"
    ) -> "Iterable[_2975.CouplingHalfCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CouplingHalfCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt(
        self: "Self", design_entity: "_2644.CVT"
    ) -> "Iterable[_2977.CVTCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CVTCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CVT)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt_pulley(
        self: "Self", design_entity: "_2645.CVTPulley"
    ) -> "Iterable[_2978.CVTPulleyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CVTPulleyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CVTPulley)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_pulley(
        self: "Self", design_entity: "_2649.Pulley"
    ) -> "Iterable[_3027.PulleyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PulleyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Pulley)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PULLEY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection(
        self: "Self", design_entity: "_2657.ShaftHubConnection"
    ) -> "Iterable[_3036.ShaftHubConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ShaftHubConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ShaftHubConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring(
        self: "Self", design_entity: "_2655.RollingRing"
    ) -> "Iterable[_3031.RollingRingCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.RollingRingCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.RollingRing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly(
        self: "Self", design_entity: "_2656.RollingRingAssembly"
    ) -> "Iterable[_3030.RollingRingAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.RollingRingAssemblyCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.RollingRingAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper(
        self: "Self", design_entity: "_2662.SpringDamper"
    ) -> "Iterable[_3042.SpringDamperCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SpringDamperCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SpringDamper)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper_half(
        self: "Self", design_entity: "_2663.SpringDamperHalf"
    ) -> "Iterable[_3044.SpringDamperHalfCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SpringDamperHalfCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SpringDamperHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser(
        self: "Self", design_entity: "_2664.Synchroniser"
    ) -> "Iterable[_3053.SynchroniserCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SynchroniserCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Synchroniser)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_half(
        self: "Self", design_entity: "_2666.SynchroniserHalf"
    ) -> "Iterable[_3054.SynchroniserHalfCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SynchroniserHalfCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_part(
        self: "Self", design_entity: "_2667.SynchroniserPart"
    ) -> "Iterable[_3055.SynchroniserPartCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SynchroniserPartCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserPart)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve(
        self: "Self", design_entity: "_2668.SynchroniserSleeve"
    ) -> "Iterable[_3056.SynchroniserSleeveCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SynchroniserSleeveCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserSleeve)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter(
        self: "Self", design_entity: "_2669.TorqueConverter"
    ) -> "Iterable[_3057.TorqueConverterCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.TorqueConverterCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverter)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump(
        self: "Self", design_entity: "_2670.TorqueConverterPump"
    ) -> "Iterable[_3059.TorqueConverterPumpCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.TorqueConverterPumpCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverterPump)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine(
        self: "Self", design_entity: "_2672.TorqueConverterTurbine"
    ) -> "Iterable[_3060.TorqueConverterTurbineCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.TorqueConverterTurbineCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection(
        self: "Self", design_entity: "_2348.ShaftToMountableComponentConnection"
    ) -> "Iterable[_3037.ShaftToMountableComponentConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ShaftToMountableComponentConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection(
        self: "Self", design_entity: "_2326.CVTBeltConnection"
    ) -> "Iterable[_2976.CVTBeltConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CVTBeltConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.CVTBeltConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_belt_connection(
        self: "Self", design_entity: "_2321.BeltConnection"
    ) -> "Iterable[_2945.BeltConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BeltConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.BeltConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coaxial_connection(
        self: "Self", design_entity: "_2322.CoaxialConnection"
    ) -> "Iterable[_2960.CoaxialConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CoaxialConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.CoaxialConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_connection(
        self: "Self", design_entity: "_2325.Connection"
    ) -> "Iterable[_2971.ConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.Connection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection(
        self: "Self", design_entity: "_2334.InterMountableComponentConnection"
    ) -> "Iterable[_3002.InterMountableComponentConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.InterMountableComponentConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_planetary_connection(
        self: "Self", design_entity: "_2340.PlanetaryConnection"
    ) -> "Iterable[_3022.PlanetaryConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PlanetaryConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.PlanetaryConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection(
        self: "Self", design_entity: "_2345.RollingRingConnection"
    ) -> "Iterable[_3032.RollingRingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.RollingRingConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.RollingRingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection(
        self: "Self", design_entity: "_2318.AbstractShaftToMountableComponentConnection"
    ) -> "Iterable[_2939.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh(
        self: "Self", design_entity: "_2354.BevelDifferentialGearMesh"
    ) -> "Iterable[_2948.BevelDifferentialGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh(
        self: "Self", design_entity: "_2358.ConceptGearMesh"
    ) -> "Iterable[_2966.ConceptGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConceptGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh(
        self: "Self", design_entity: "_2364.FaceGearMesh"
    ) -> "Iterable[_2991.FaceGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.FaceGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh(
        self: "Self", design_entity: "_2378.StraightBevelDiffGearMesh"
    ) -> "Iterable[_3046.StraightBevelDiffGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh(
        self: "Self", design_entity: "_2356.BevelGearMesh"
    ) -> "Iterable[_2953.BevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.BevelGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh(
        self: "Self", design_entity: "_2360.ConicalGearMesh"
    ) -> "Iterable[_2969.ConicalGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ConicalGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh(
        self: "Self", design_entity: "_2352.AGMAGleasonConicalGearMesh"
    ) -> "Iterable[_2941.AGMAGleasonConicalGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.AGMAGleasonConicalGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh(
        self: "Self", design_entity: "_2362.CylindricalGearMesh"
    ) -> "Iterable[_2984.CylindricalGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CylindricalGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh(
        self: "Self", design_entity: "_2368.HypoidGearMesh"
    ) -> "Iterable[_3000.HypoidGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.HypoidGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: "Self", design_entity: "_2371.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "Iterable[_3004.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: "Self", design_entity: "_2372.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> (
        "Iterable[_3007.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection]"
    ):
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: "Self", design_entity: "_2373.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "Iterable[_3010.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh(
        self: "Self", design_entity: "_2376.SpiralBevelGearMesh"
    ) -> "Iterable[_3040.SpiralBevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.SpiralBevelGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh(
        self: "Self", design_entity: "_2380.StraightBevelGearMesh"
    ) -> "Iterable[_3049.StraightBevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.StraightBevelGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh(
        self: "Self", design_entity: "_2382.WormGearMesh"
    ) -> "Iterable[_3064.WormGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.WormGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh(
        self: "Self", design_entity: "_2384.ZerolBevelGearMesh"
    ) -> "Iterable[_3067.ZerolBevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear_mesh(
        self: "Self", design_entity: "_2366.GearMesh"
    ) -> "Iterable[_2996.GearMeshCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.GearMeshCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.GearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection(
        self: "Self", design_entity: "_2388.CycloidalDiscCentralBearingConnection"
    ) -> (
        "Iterable[_2980.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection]"
    ):
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection(
        self: "Self", design_entity: "_2391.CycloidalDiscPlanetaryBearingConnection"
    ) -> "Iterable[_2982.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection(
        self: "Self", design_entity: "_2394.RingPinsToDiscConnection"
    ) -> "Iterable[_3029.RingPinsToDiscConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.RingPinsToDiscConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection(
        self: "Self", design_entity: "_2401.PartToPartShearCouplingConnection"
    ) -> "Iterable[_3020.PartToPartShearCouplingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.PartToPartShearCouplingConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch_connection(
        self: "Self", design_entity: "_2395.ClutchConnection"
    ) -> "Iterable[_2958.ClutchConnectionCompoundSystemDeflection]":
        """Iterable[mastapy._private.system_model.analyses_and_results.system_deflections.compound.ClutchConnectionCompoundSystemDeflection]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @property
    def cast_to(self: "Self") -> "_Cast_CompoundSystemDeflectionAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CompoundSystemDeflectionAnalysis
        """
        return _Cast_CompoundSystemDeflectionAnalysis(self)
