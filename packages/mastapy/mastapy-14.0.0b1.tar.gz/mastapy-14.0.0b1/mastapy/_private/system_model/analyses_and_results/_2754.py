"""CompoundModalAnalysis"""
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
_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundModalAnalysis"
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
    from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
        _4868,
        _4879,
        _4946,
        _4961,
        _4842,
        _4919,
        _4918,
        _4841,
        _4843,
        _4849,
        _4860,
        _4861,
        _4866,
        _4877,
        _4892,
        _4893,
        _4897,
        _4898,
        _4848,
        _4902,
        _4916,
        _4917,
        _4920,
        _4921,
        _4922,
        _4928,
        _4929,
        _4930,
        _4937,
        _4941,
        _4964,
        _4965,
        _4938,
        _4870,
        _4872,
        _4894,
        _4896,
        _4845,
        _4847,
        _4852,
        _4854,
        _4855,
        _4856,
        _4857,
        _4859,
        _4873,
        _4875,
        _4888,
        _4890,
        _4891,
        _4899,
        _4901,
        _4903,
        _4905,
        _4907,
        _4909,
        _4910,
        _4912,
        _4913,
        _4915,
        _4927,
        _4942,
        _4944,
        _4948,
        _4950,
        _4951,
        _4953,
        _4954,
        _4955,
        _4966,
        _4968,
        _4969,
        _4971,
        _4884,
        _4886,
        _4932,
        _4923,
        _4925,
        _4851,
        _4862,
        _4864,
        _4867,
        _4869,
        _4878,
        _4880,
        _4882,
        _4883,
        _4931,
        _4939,
        _4935,
        _4934,
        _4945,
        _4947,
        _4956,
        _4957,
        _4958,
        _4959,
        _4960,
        _4962,
        _4963,
        _4940,
        _4881,
        _4850,
        _4865,
        _4876,
        _4906,
        _4926,
        _4936,
        _4844,
        _4853,
        _4871,
        _4895,
        _4949,
        _4858,
        _4874,
        _4846,
        _4889,
        _4904,
        _4908,
        _4911,
        _4914,
        _4943,
        _4952,
        _4967,
        _4970,
        _4900,
        _4885,
        _4887,
        _4933,
        _4924,
        _4863,
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

    Self = TypeVar("Self", bound="CompoundModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="CompoundModalAnalysis._Cast_CompoundModalAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CompoundModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CompoundModalAnalysis:
    """Special nested class for casting CompoundModalAnalysis to subclasses."""

    __parent__: "CompoundModalAnalysis"

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
    def compound_modal_analysis(self: "CastSelf") -> "CompoundModalAnalysis":
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
class CompoundModalAnalysis(_2702.CompoundAnalysis):
    """CompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPOUND_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: "Self", design_entity: "_2397.ConceptCouplingConnection"
    ) -> "Iterable[_4868.ConceptCouplingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4879.CouplingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CouplingConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4946.SpringDamperConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpringDamperConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4961.TorqueConverterConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4842.AbstractShaftCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.AbstractShaftCompoundModalAnalysis]

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
    ) -> "Iterable[_4919.MicrophoneCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.MicrophoneCompoundModalAnalysis]

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
    ) -> "Iterable[_4918.MicrophoneArrayCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.MicrophoneArrayCompoundModalAnalysis]

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
    ) -> "Iterable[_4841.AbstractAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.AbstractAssemblyCompoundModalAnalysis]

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
    ) -> "Iterable[_4843.AbstractShaftOrHousingCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.AbstractShaftOrHousingCompoundModalAnalysis]

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
    ) -> "Iterable[_4849.BearingCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BearingCompoundModalAnalysis]

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
    ) -> "Iterable[_4860.BoltCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BoltCompoundModalAnalysis]

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
    ) -> "Iterable[_4861.BoltedJointCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BoltedJointCompoundModalAnalysis]

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
    ) -> "Iterable[_4866.ComponentCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ComponentCompoundModalAnalysis]

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
    ) -> "Iterable[_4877.ConnectorCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConnectorCompoundModalAnalysis]

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
    ) -> "Iterable[_4892.DatumCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.DatumCompoundModalAnalysis]

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
    ) -> "Iterable[_4893.ExternalCADModelCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ExternalCADModelCompoundModalAnalysis]

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
    ) -> "Iterable[_4897.FEPartCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.FEPartCompoundModalAnalysis]

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
    ) -> "Iterable[_4898.FlexiblePinAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.FlexiblePinAssemblyCompoundModalAnalysis]

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
    ) -> "Iterable[_4848.AssemblyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.AssemblyCompoundModalAnalysis]

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
    ) -> "Iterable[_4902.GuideDxfModelCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.GuideDxfModelCompoundModalAnalysis]

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
    ) -> "Iterable[_4916.MassDiscCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.MassDiscCompoundModalAnalysis]

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
    ) -> "Iterable[_4917.MeasurementComponentCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.MeasurementComponentCompoundModalAnalysis]

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
    ) -> "Iterable[_4920.MountableComponentCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.MountableComponentCompoundModalAnalysis]

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
    ) -> "Iterable[_4921.OilSealCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.OilSealCompoundModalAnalysis]

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
    ) -> "Iterable[_4922.PartCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PartCompoundModalAnalysis]

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
    ) -> "Iterable[_4928.PlanetCarrierCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PlanetCarrierCompoundModalAnalysis]

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
    ) -> "Iterable[_4929.PointLoadCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PointLoadCompoundModalAnalysis]

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
    ) -> "Iterable[_4930.PowerLoadCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PowerLoadCompoundModalAnalysis]

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
    ) -> "Iterable[_4937.RootAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.RootAssemblyCompoundModalAnalysis]

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
    ) -> "Iterable[_4941.SpecialisedAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpecialisedAssemblyCompoundModalAnalysis]

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
    ) -> "Iterable[_4964.UnbalancedMassCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.UnbalancedMassCompoundModalAnalysis]

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
    ) -> "Iterable[_4965.VirtualComponentCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.VirtualComponentCompoundModalAnalysis]

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
    ) -> "Iterable[_4938.ShaftCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ShaftCompoundModalAnalysis]

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
    ) -> "Iterable[_4870.ConceptGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConceptGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4872.ConceptGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConceptGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4894.FaceGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.FaceGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4896.FaceGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.FaceGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4845.AGMAGleasonConicalGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4847.AGMAGleasonConicalGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4852.BevelDifferentialGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4854.BevelDifferentialGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4855.BevelDifferentialPlanetGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialPlanetGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4856.BevelDifferentialSunGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialSunGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4857.BevelGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4859.BevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4873.ConicalGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConicalGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4875.ConicalGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConicalGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4888.CylindricalGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4890.CylindricalGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4891.CylindricalPlanetGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CylindricalPlanetGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4899.GearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.GearCompoundModalAnalysis]

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
    ) -> "Iterable[_4901.GearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.GearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4903.HypoidGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.HypoidGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4905.HypoidGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.HypoidGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4907.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4909.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4910.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4912.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4913.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4915.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4927.PlanetaryGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PlanetaryGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4942.SpiralBevelGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4944.SpiralBevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4948.StraightBevelDiffGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4950.StraightBevelDiffGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4951.StraightBevelGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4953.StraightBevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4954.StraightBevelPlanetGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelPlanetGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4955.StraightBevelSunGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelSunGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4966.WormGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.WormGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4968.WormGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.WormGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4969.ZerolBevelGearCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearCompoundModalAnalysis]

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
    ) -> "Iterable[_4971.ZerolBevelGearSetCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearSetCompoundModalAnalysis]

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
    ) -> "Iterable[_4884.CycloidalAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CycloidalAssemblyCompoundModalAnalysis]

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
    ) -> "Iterable[_4886.CycloidalDiscCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CycloidalDiscCompoundModalAnalysis]

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
    ) -> "Iterable[_4932.RingPinsCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.RingPinsCompoundModalAnalysis]

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
    ) -> "Iterable[_4923.PartToPartShearCouplingCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingCompoundModalAnalysis]

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
    ) -> "Iterable[_4925.PartToPartShearCouplingHalfCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingHalfCompoundModalAnalysis]

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
    ) -> "Iterable[_4851.BeltDriveCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BeltDriveCompoundModalAnalysis]

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
    ) -> "Iterable[_4862.ClutchCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ClutchCompoundModalAnalysis]

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
    ) -> "Iterable[_4864.ClutchHalfCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ClutchHalfCompoundModalAnalysis]

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
    ) -> "Iterable[_4867.ConceptCouplingCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingCompoundModalAnalysis]

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
    ) -> "Iterable[_4869.ConceptCouplingHalfCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingHalfCompoundModalAnalysis]

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
    ) -> "Iterable[_4878.CouplingCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CouplingCompoundModalAnalysis]

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
    ) -> "Iterable[_4880.CouplingHalfCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CouplingHalfCompoundModalAnalysis]

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
    ) -> "Iterable[_4882.CVTCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CVTCompoundModalAnalysis]

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
    ) -> "Iterable[_4883.CVTPulleyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CVTPulleyCompoundModalAnalysis]

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
    ) -> "Iterable[_4931.PulleyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PulleyCompoundModalAnalysis]

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
    ) -> "Iterable[_4939.ShaftHubConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ShaftHubConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4935.RollingRingCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.RollingRingCompoundModalAnalysis]

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
    ) -> "Iterable[_4934.RollingRingAssemblyCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.RollingRingAssemblyCompoundModalAnalysis]

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
    ) -> "Iterable[_4945.SpringDamperCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpringDamperCompoundModalAnalysis]

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
    ) -> "Iterable[_4947.SpringDamperHalfCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpringDamperHalfCompoundModalAnalysis]

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
    ) -> "Iterable[_4956.SynchroniserCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SynchroniserCompoundModalAnalysis]

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
    ) -> "Iterable[_4957.SynchroniserHalfCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SynchroniserHalfCompoundModalAnalysis]

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
    ) -> "Iterable[_4958.SynchroniserPartCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SynchroniserPartCompoundModalAnalysis]

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
    ) -> "Iterable[_4959.SynchroniserSleeveCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SynchroniserSleeveCompoundModalAnalysis]

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
    ) -> "Iterable[_4960.TorqueConverterCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterCompoundModalAnalysis]

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
    ) -> "Iterable[_4962.TorqueConverterPumpCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterPumpCompoundModalAnalysis]

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
    ) -> "Iterable[_4963.TorqueConverterTurbineCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterTurbineCompoundModalAnalysis]

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
    ) -> "Iterable[_4940.ShaftToMountableComponentConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ShaftToMountableComponentConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4881.CVTBeltConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CVTBeltConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4850.BeltConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BeltConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4865.CoaxialConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CoaxialConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4876.ConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4906.InterMountableComponentConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.InterMountableComponentConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4926.PlanetaryConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PlanetaryConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4936.RollingRingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.RollingRingConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4844.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4853.BevelDifferentialGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4871.ConceptGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConceptGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4895.FaceGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.FaceGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4949.StraightBevelDiffGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4858.BevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.BevelGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4874.ConicalGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ConicalGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4846.AGMAGleasonConicalGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4889.CylindricalGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4904.HypoidGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.HypoidGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4908.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4911.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4914.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4943.SpiralBevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4952.StraightBevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4967.WormGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.WormGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4970.ZerolBevelGearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4900.GearMeshCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.GearMeshCompoundModalAnalysis]

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
    ) -> "Iterable[_4885.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4887.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4933.RingPinsToDiscConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.RingPinsToDiscConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4924.PartToPartShearCouplingConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingConnectionCompoundModalAnalysis]

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
    ) -> "Iterable[_4863.ClutchConnectionCompoundModalAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.modal_analyses.compound.ClutchConnectionCompoundModalAnalysis]

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @property
    def cast_to(self: "Self") -> "_Cast_CompoundModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CompoundModalAnalysis
        """
        return _Cast_CompoundModalAnalysis(self)
