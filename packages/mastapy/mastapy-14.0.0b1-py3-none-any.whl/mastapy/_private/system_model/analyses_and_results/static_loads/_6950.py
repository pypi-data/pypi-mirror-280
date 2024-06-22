"""LoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable, enum_with_selected_value
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import (
    constructor,
    conversion,
    enum_with_selected_value_runtime,
    overridable_enum_runtime,
    utility,
)
from mastapy._private.bearings.bearing_results.rolling import _2025
from mastapy._private.system_model import _2267
from mastapy._private.gears import _347
from mastapy._private.nodal_analysis.nodal_entities import _131
from mastapy._private.bearings.bearing_results.rolling.iso_rating_results import _2162
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.analyses_and_results import _2733
from mastapy._private._internal.cast_exception import CastException

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
_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
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
_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "LoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import _2020, _2122
    from mastapy._private.system_model import _2262, _2277
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _6957,
        _7088,
        _7127,
        _6998,
        _7105,
        _7121,
        _6954,
        _7072,
        _7071,
        _6953,
        _6955,
        _6966,
        _6978,
        _6977,
        _6984,
        _6997,
        _7016,
        _7030,
        _7034,
        _7035,
        _6965,
        _7043,
        _7068,
        _7069,
        _7073,
        _7075,
        _7077,
        _7084,
        _7087,
        _7097,
        _7101,
        _7129,
        _7130,
        _7099,
        _6988,
        _6990,
        _7031,
        _7033,
        _6960,
        _6962,
        _6969,
        _6971,
        _6972,
        _6973,
        _6974,
        _6976,
        _6991,
        _6995,
        _7008,
        _7012,
        _7013,
        _7037,
        _7042,
        _7052,
        _7054,
        _7059,
        _7061,
        _7062,
        _7064,
        _7065,
        _7067,
        _7082,
        _7102,
        _7104,
        _7108,
        _7110,
        _7111,
        _7113,
        _7114,
        _7115,
        _7131,
        _7133,
        _7134,
        _7136,
        _7004,
        _7006,
        _7092,
        _7080,
        _7079,
        _6968,
        _6981,
        _6980,
        _6987,
        _6986,
        _7000,
        _6999,
        _7002,
        _7003,
        _7089,
        _7098,
        _7096,
        _7094,
        _7107,
        _7106,
        _7117,
        _7116,
        _7118,
        _7119,
        _7122,
        _7123,
        _7124,
        _7100,
        _7001,
        _6967,
        _6983,
        _6996,
        _7058,
        _7081,
        _7095,
        _6956,
        _6970,
        _6989,
        _7032,
        _7109,
        _6975,
        _6993,
        _6961,
        _7010,
        _7053,
        _7060,
        _7063,
        _7066,
        _7103,
        _7112,
        _7132,
        _7135,
        _7039,
        _7005,
        _7007,
        _7093,
        _7078,
        _6979,
        _6985,
        _6951,
        _6952,
        _6958,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4498,
        _4496,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings import (
        _2399,
        _2403,
        _2405,
        _2401,
        _2395,
        _2397,
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
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5900,
    )

    Self = TypeVar("Self", bound="LoadCase")
    CastSelf = TypeVar("CastSelf", bound="LoadCase._Cast_LoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("LoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadCase:
    """Special nested class for casting LoadCase to subclasses."""

    __parent__: "LoadCase"

    @property
    def context(self: "CastSelf") -> "_2733.Context":
        return self.__parent__._cast(_2733.Context)

    @property
    def parametric_study_static_load(
        self: "CastSelf",
    ) -> "_4496.ParametricStudyStaticLoad":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4496,
        )

        return self.__parent__._cast(_4496.ParametricStudyStaticLoad)

    @property
    def harmonic_analysis_with_varying_stiffness_static_load_case(
        self: "CastSelf",
    ) -> "_5900.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5900,
        )

        return self.__parent__._cast(
            _5900.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
        )

    @property
    def static_load_case(self: "CastSelf") -> "_6951.StaticLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6951,
        )

        return self.__parent__._cast(_6951.StaticLoadCase)

    @property
    def time_series_load_case(self: "CastSelf") -> "_6952.TimeSeriesLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6952,
        )

        return self.__parent__._cast(_6952.TimeSeriesLoadCase)

    @property
    def advanced_time_stepping_analysis_for_modulation_static_load_case(
        self: "CastSelf",
    ) -> "_6958.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6958,
        )

        return self.__parent__._cast(
            _6958.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
        )

    @property
    def load_case(self: "CastSelf") -> "LoadCase":
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
class LoadCase(_2733.Context):
    """LoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def air_density(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AirDensity

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @air_density.setter
    @enforce_parameter_types
    def air_density(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AirDensity = value

    @property
    def ball_bearing_contact_calculation(
        self: "Self",
    ) -> "_2020.BallBearingContactCalculation":
        """mastapy._private.bearings.bearing_results.rolling.BallBearingContactCalculation"""
        temp = self.wrapped.BallBearingContactCalculation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.BallBearingContactCalculation",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings.bearing_results.rolling._2020",
            "BallBearingContactCalculation",
        )(value)

    @ball_bearing_contact_calculation.setter
    @enforce_parameter_types
    def ball_bearing_contact_calculation(
        self: "Self", value: "_2020.BallBearingContactCalculation"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.BallBearingContactCalculation",
        )
        self.wrapped.BallBearingContactCalculation = value

    @property
    def ball_bearing_friction_model_for_gyroscopic_moment(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FrictionModelForGyroscopicMoment":
        """EnumWithSelectedValue[mastapy._private.bearings.bearing_results.rolling.FrictionModelForGyroscopicMoment]"""
        temp = self.wrapped.BallBearingFrictionModelForGyroscopicMoment

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FrictionModelForGyroscopicMoment.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @ball_bearing_friction_model_for_gyroscopic_moment.setter
    @enforce_parameter_types
    def ball_bearing_friction_model_for_gyroscopic_moment(
        self: "Self", value: "_2025.FrictionModelForGyroscopicMoment"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FrictionModelForGyroscopicMoment.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BallBearingFrictionModelForGyroscopicMoment = value

    @property
    def characteristic_specific_acoustic_impedance(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CharacteristicSpecificAcousticImpedance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @characteristic_specific_acoustic_impedance.setter
    @enforce_parameter_types
    def characteristic_specific_acoustic_impedance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CharacteristicSpecificAcousticImpedance = value

    @property
    def energy_convergence_absolute_tolerance(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EnergyConvergenceAbsoluteTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @energy_convergence_absolute_tolerance.setter
    @enforce_parameter_types
    def energy_convergence_absolute_tolerance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EnergyConvergenceAbsoluteTolerance = value

    @property
    def expand_grounded_nodes_for_thermal_effects(
        self: "Self",
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.ExpandGroundedNodesForThermalEffects

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @expand_grounded_nodes_for_thermal_effects.setter
    @enforce_parameter_types
    def expand_grounded_nodes_for_thermal_effects(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.ExpandGroundedNodesForThermalEffects = value

    @property
    def force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = self.wrapped.ForceMultipleMeshNodesForUnloadedCylindricalGearMeshes

        if temp is None:
            return False

        return temp

    @force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes.setter
    @enforce_parameter_types
    def force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.ForceMultipleMeshNodesForUnloadedCylindricalGearMeshes = (
            bool(value) if value is not None else False
        )

    @property
    def gear_mesh_nodes_per_unit_length_to_diameter_ratio(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.GearMeshNodesPerUnitLengthToDiameterRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @gear_mesh_nodes_per_unit_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def gear_mesh_nodes_per_unit_length_to_diameter_ratio(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.GearMeshNodesPerUnitLengthToDiameterRatio = value

    @property
    def grid_refinement_factor_contact_width(
        self: "Self",
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.GridRefinementFactorContactWidth

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @grid_refinement_factor_contact_width.setter
    @enforce_parameter_types
    def grid_refinement_factor_contact_width(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.GridRefinementFactorContactWidth = value

    @property
    def grid_refinement_factor_rib_height(
        self: "Self",
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.GridRefinementFactorRibHeight

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @grid_refinement_factor_rib_height.setter
    @enforce_parameter_types
    def grid_refinement_factor_rib_height(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.GridRefinementFactorRibHeight = value

    @property
    def hypoid_gear_wind_up_removal_method_for_misalignments(
        self: "Self",
    ) -> "_2262.HypoidWindUpRemovalMethod":
        """mastapy._private.system_model.HypoidWindUpRemovalMethod"""
        temp = self.wrapped.HypoidGearWindUpRemovalMethodForMisalignments

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.HypoidWindUpRemovalMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model._2262", "HypoidWindUpRemovalMethod"
        )(value)

    @hypoid_gear_wind_up_removal_method_for_misalignments.setter
    @enforce_parameter_types
    def hypoid_gear_wind_up_removal_method_for_misalignments(
        self: "Self", value: "_2262.HypoidWindUpRemovalMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.HypoidWindUpRemovalMethod"
        )
        self.wrapped.HypoidGearWindUpRemovalMethodForMisalignments = value

    @property
    def include_bearing_centrifugal_ring_expansion(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingCentrifugalRingExpansion

        if temp is None:
            return False

        return temp

    @include_bearing_centrifugal_ring_expansion.setter
    @enforce_parameter_types
    def include_bearing_centrifugal_ring_expansion(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeBearingCentrifugalRingExpansion = (
            bool(value) if value is not None else False
        )

    @property
    def include_bearing_centrifugal(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingCentrifugal

        if temp is None:
            return False

        return temp

    @include_bearing_centrifugal.setter
    @enforce_parameter_types
    def include_bearing_centrifugal(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeBearingCentrifugal = (
            bool(value) if value is not None else False
        )

    @property
    def include_fitting_effects(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeFittingEffects

        if temp is None:
            return False

        return temp

    @include_fitting_effects.setter
    @enforce_parameter_types
    def include_fitting_effects(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeFittingEffects = bool(value) if value is not None else False

    @property
    def include_gear_blank_elastic_distortion(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGearBlankElasticDistortion

        if temp is None:
            return False

        return temp

    @include_gear_blank_elastic_distortion.setter
    @enforce_parameter_types
    def include_gear_blank_elastic_distortion(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeGearBlankElasticDistortion = (
            bool(value) if value is not None else False
        )

    @property
    def include_gravity(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGravity

        if temp is None:
            return False

        return temp

    @include_gravity.setter
    @enforce_parameter_types
    def include_gravity(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeGravity = bool(value) if value is not None else False

    @property
    def include_inner_race_distortion_for_flexible_pin_spindle(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle

        if temp is None:
            return False

        return temp

    @include_inner_race_distortion_for_flexible_pin_spindle.setter
    @enforce_parameter_types
    def include_inner_race_distortion_for_flexible_pin_spindle(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle = (
            bool(value) if value is not None else False
        )

    @property
    def include_planetary_centrifugal(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludePlanetaryCentrifugal

        if temp is None:
            return False

        return temp

    @include_planetary_centrifugal.setter
    @enforce_parameter_types
    def include_planetary_centrifugal(self: "Self", value: "bool") -> None:
        self.wrapped.IncludePlanetaryCentrifugal = (
            bool(value) if value is not None else False
        )

    @property
    def include_profile_modifications_and_manufacturing_errors_during_cycloidal_analysis(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.IncludeProfileModificationsAndManufacturingErrorsDuringCycloidalAnalysis
        )

        if temp is None:
            return False

        return temp

    @include_profile_modifications_and_manufacturing_errors_during_cycloidal_analysis.setter
    @enforce_parameter_types
    def include_profile_modifications_and_manufacturing_errors_during_cycloidal_analysis(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.IncludeProfileModificationsAndManufacturingErrorsDuringCycloidalAnalysis = (
            bool(value) if value is not None else False
        )

    @property
    def include_rib_contact_analysis(self: "Self") -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.IncludeRibContactAnalysis

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @include_rib_contact_analysis.setter
    @enforce_parameter_types
    def include_rib_contact_analysis(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.IncludeRibContactAnalysis = value

    @property
    def include_ring_ovality(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeRingOvality

        if temp is None:
            return False

        return temp

    @include_ring_ovality.setter
    @enforce_parameter_types
    def include_ring_ovality(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeRingOvality = bool(value) if value is not None else False

    @property
    def include_thermal_expansion_effects(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeThermalExpansionEffects

        if temp is None:
            return False

        return temp

    @include_thermal_expansion_effects.setter
    @enforce_parameter_types
    def include_thermal_expansion_effects(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeThermalExpansionEffects = (
            bool(value) if value is not None else False
        )

    @property
    def include_tilt_stiffness_for_bevel_hypoid_gears(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeTiltStiffnessForBevelHypoidGears

        if temp is None:
            return False

        return temp

    @include_tilt_stiffness_for_bevel_hypoid_gears.setter
    @enforce_parameter_types
    def include_tilt_stiffness_for_bevel_hypoid_gears(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.IncludeTiltStiffnessForBevelHypoidGears = (
            bool(value) if value is not None else False
        )

    @property
    def maximum_shaft_section_cross_sectional_area_ratio(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumShaftSectionCrossSectionalAreaRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_shaft_section_cross_sectional_area_ratio.setter
    @enforce_parameter_types
    def maximum_shaft_section_cross_sectional_area_ratio(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.MaximumShaftSectionCrossSectionalAreaRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_shaft_section_length_to_diameter_ratio(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumShaftSectionLengthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_shaft_section_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def maximum_shaft_section_length_to_diameter_ratio(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.MaximumShaftSectionLengthToDiameterRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_shaft_section_polar_area_moment_of_inertia_ratio(
        self: "Self",
    ) -> "float":
        """float"""
        temp = self.wrapped.MaximumShaftSectionPolarAreaMomentOfInertiaRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_shaft_section_polar_area_moment_of_inertia_ratio.setter
    @enforce_parameter_types
    def maximum_shaft_section_polar_area_moment_of_inertia_ratio(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.MaximumShaftSectionPolarAreaMomentOfInertiaRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_translation_per_solver_step(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumTranslationPerSolverStep

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_translation_per_solver_step.setter
    @enforce_parameter_types
    def maximum_translation_per_solver_step(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumTranslationPerSolverStep = value

    @property
    def mesh_stiffness_model(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel":
        """EnumWithSelectedValue[mastapy._private.system_model.MeshStiffnessModel]"""
        temp = self.wrapped.MeshStiffnessModel

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @mesh_stiffness_model.setter
    @enforce_parameter_types
    def mesh_stiffness_model(self: "Self", value: "_2267.MeshStiffnessModel") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MeshStiffnessModel = value

    @property
    def micro_geometry_model_in_system_deflection(
        self: "Self",
    ) -> "overridable.Overridable_MicroGeometryModel":
        """Overridable[mastapy._private.gears.MicroGeometryModel]"""
        temp = self.wrapped.MicroGeometryModelInSystemDeflection

        if temp is None:
            return None

        value = overridable.Overridable_MicroGeometryModel.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @micro_geometry_model_in_system_deflection.setter
    @enforce_parameter_types
    def micro_geometry_model_in_system_deflection(
        self: "Self",
        value: "Union[_347.MicroGeometryModel, Tuple[_347.MicroGeometryModel, bool]]",
    ) -> None:
        wrapper_type = overridable.Overridable_MicroGeometryModel.wrapper_type()
        enclosed_type = overridable.Overridable_MicroGeometryModel.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.MicroGeometryModelInSystemDeflection = value

    @property
    def minimum_force_for_bearing_to_be_considered_loaded(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumForceForBearingToBeConsideredLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_force_for_bearing_to_be_considered_loaded.setter
    @enforce_parameter_types
    def minimum_force_for_bearing_to_be_considered_loaded(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumForceForBearingToBeConsideredLoaded = value

    @property
    def minimum_moment_for_bearing_to_be_considered_loaded(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumMomentForBearingToBeConsideredLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_moment_for_bearing_to_be_considered_loaded.setter
    @enforce_parameter_types
    def minimum_moment_for_bearing_to_be_considered_loaded(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumMomentForBearingToBeConsideredLoaded = value

    @property
    def minimum_number_of_gear_mesh_nodes(
        self: "Self",
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MinimumNumberOfGearMeshNodes

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @minimum_number_of_gear_mesh_nodes.setter
    @enforce_parameter_types
    def minimum_number_of_gear_mesh_nodes(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MinimumNumberOfGearMeshNodes = value

    @property
    def minimum_power_for_gear_mesh_to_be_loaded(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumPowerForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_power_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_power_for_gear_mesh_to_be_loaded(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumPowerForGearMeshToBeLoaded = value

    @property
    def minimum_torque_for_gear_mesh_to_be_loaded(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumTorqueForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_torque_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_torque_for_gear_mesh_to_be_loaded(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumTorqueForGearMeshToBeLoaded = value

    @property
    def model_bearing_mounting_clearances_automatically(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ModelBearingMountingClearancesAutomatically

        if temp is None:
            return False

        return temp

    @model_bearing_mounting_clearances_automatically.setter
    @enforce_parameter_types
    def model_bearing_mounting_clearances_automatically(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.ModelBearingMountingClearancesAutomatically = (
            bool(value) if value is not None else False
        )

    @property
    def number_of_grid_points_across_rib_contact_width(
        self: "Self",
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfGridPointsAcrossRibContactWidth

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_grid_points_across_rib_contact_width.setter
    @enforce_parameter_types
    def number_of_grid_points_across_rib_contact_width(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfGridPointsAcrossRibContactWidth = value

    @property
    def number_of_grid_points_across_rib_height(
        self: "Self",
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfGridPointsAcrossRibHeight

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_grid_points_across_rib_height.setter
    @enforce_parameter_types
    def number_of_grid_points_across_rib_height(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfGridPointsAcrossRibHeight = value

    @property
    def number_of_strips_for_roller_calculation(
        self: "Self",
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfStripsForRollerCalculation

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_strips_for_roller_calculation.setter
    @enforce_parameter_types
    def number_of_strips_for_roller_calculation(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfStripsForRollerCalculation = value

    @property
    def peak_load_factor_for_shafts(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PeakLoadFactorForShafts

        if temp is None:
            return 0.0

        return temp

    @peak_load_factor_for_shafts.setter
    @enforce_parameter_types
    def peak_load_factor_for_shafts(self: "Self", value: "float") -> None:
        self.wrapped.PeakLoadFactorForShafts = (
            float(value) if value is not None else 0.0
        )

    @property
    def refine_grid_around_contact_point(
        self: "Self",
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.RefineGridAroundContactPoint

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @refine_grid_around_contact_point.setter
    @enforce_parameter_types
    def refine_grid_around_contact_point(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.RefineGridAroundContactPoint = value

    @property
    def relative_tolerance_for_convergence(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RelativeToleranceForConvergence

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @relative_tolerance_for_convergence.setter
    @enforce_parameter_types
    def relative_tolerance_for_convergence(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RelativeToleranceForConvergence = value

    @property
    def ring_ovality_scaling(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RingOvalityScaling

        if temp is None:
            return 0.0

        return temp

    @ring_ovality_scaling.setter
    @enforce_parameter_types
    def ring_ovality_scaling(self: "Self", value: "float") -> None:
        self.wrapped.RingOvalityScaling = float(value) if value is not None else 0.0

    @property
    def roller_analysis_method(self: "Self") -> "_2122.RollerAnalysisMethod":
        """mastapy._private.bearings.bearing_results.rolling.RollerAnalysisMethod"""
        temp = self.wrapped.RollerAnalysisMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.Rolling.RollerAnalysisMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings.bearing_results.rolling._2122",
            "RollerAnalysisMethod",
        )(value)

    @roller_analysis_method.setter
    @enforce_parameter_types
    def roller_analysis_method(
        self: "Self", value: "_2122.RollerAnalysisMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.Rolling.RollerAnalysisMethod"
        )
        self.wrapped.RollerAnalysisMethod = value

    @property
    def set_first_element_angle_to_load_direction(
        self: "Self",
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.SetFirstElementAngleToLoadDirection

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @set_first_element_angle_to_load_direction.setter
    @enforce_parameter_types
    def set_first_element_angle_to_load_direction(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.SetFirstElementAngleToLoadDirection = value

    @property
    def shear_area_factor_method(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ShearAreaFactorMethod":
        """EnumWithSelectedValue[mastapy._private.nodal_analysis.nodal_entities.ShearAreaFactorMethod]"""
        temp = self.wrapped.ShearAreaFactorMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ShearAreaFactorMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @shear_area_factor_method.setter
    @enforce_parameter_types
    def shear_area_factor_method(
        self: "Self", value: "_131.ShearAreaFactorMethod"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ShearAreaFactorMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ShearAreaFactorMethod = value

    @property
    def speed_of_sound(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpeedOfSound

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @speed_of_sound.setter
    @enforce_parameter_types
    def speed_of_sound(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpeedOfSound = value

    @property
    def spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = (
            self.wrapped.SplineRigidBondDetailedConnectionNodesPerUnitLengthToDiameterRatio
        )

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SplineRigidBondDetailedConnectionNodesPerUnitLengthToDiameterRatio = (
            value
        )

    @property
    def stress_concentration_method_for_rating(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_StressConcentrationMethod":
        """EnumWithSelectedValue[mastapy._private.bearings.bearing_results.rolling.iso_rating_results.StressConcentrationMethod]"""
        temp = self.wrapped.StressConcentrationMethodForRating

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_StressConcentrationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @stress_concentration_method_for_rating.setter
    @enforce_parameter_types
    def stress_concentration_method_for_rating(
        self: "Self", value: "_2162.StressConcentrationMethod"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_StressConcentrationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.StressConcentrationMethodForRating = value

    @property
    def tolerance_factor_for_axial_internal_clearances(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ToleranceFactorForAxialInternalClearances

        if temp is None:
            return 0.0

        return temp

    @tolerance_factor_for_axial_internal_clearances.setter
    @enforce_parameter_types
    def tolerance_factor_for_axial_internal_clearances(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.ToleranceFactorForAxialInternalClearances = (
            float(value) if value is not None else 0.0
        )

    @property
    def tolerance_factor_for_inner_fit(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ToleranceFactorForInnerFit

        if temp is None:
            return 0.0

        return temp

    @tolerance_factor_for_inner_fit.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_fit(self: "Self", value: "float") -> None:
        self.wrapped.ToleranceFactorForInnerFit = (
            float(value) if value is not None else 0.0
        )

    @property
    def tolerance_factor_for_inner_mounting_sleeve_bore(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForInnerMountingSleeveBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_inner_mounting_sleeve_bore.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_mounting_sleeve_bore(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForInnerMountingSleeveBore = value

    @property
    def tolerance_factor_for_inner_mounting_sleeve_outer_diameter(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForInnerMountingSleeveOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_inner_mounting_sleeve_outer_diameter.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_mounting_sleeve_outer_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForInnerMountingSleeveOuterDiameter = value

    @property
    def tolerance_factor_for_inner_ring(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForInnerRing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_inner_ring.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_ring(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForInnerRing = value

    @property
    def tolerance_factor_for_inner_support(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForInnerSupport

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_inner_support.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_support(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForInnerSupport = value

    @property
    def tolerance_factor_for_outer_fit(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ToleranceFactorForOuterFit

        if temp is None:
            return 0.0

        return temp

    @tolerance_factor_for_outer_fit.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_fit(self: "Self", value: "float") -> None:
        self.wrapped.ToleranceFactorForOuterFit = (
            float(value) if value is not None else 0.0
        )

    @property
    def tolerance_factor_for_outer_mounting_sleeve_bore(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForOuterMountingSleeveBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_outer_mounting_sleeve_bore.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_mounting_sleeve_bore(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForOuterMountingSleeveBore = value

    @property
    def tolerance_factor_for_outer_mounting_sleeve_outer_diameter(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForOuterMountingSleeveOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_outer_mounting_sleeve_outer_diameter.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_mounting_sleeve_outer_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForOuterMountingSleeveOuterDiameter = value

    @property
    def tolerance_factor_for_outer_ring(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForOuterRing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_outer_ring.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_ring(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForOuterRing = value

    @property
    def tolerance_factor_for_outer_support(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForOuterSupport

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_outer_support.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_support(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForOuterSupport = value

    @property
    def tolerance_factor_for_radial_internal_clearances(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ToleranceFactorForRadialInternalClearances

        if temp is None:
            return 0.0

        return temp

    @tolerance_factor_for_radial_internal_clearances.setter
    @enforce_parameter_types
    def tolerance_factor_for_radial_internal_clearances(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.ToleranceFactorForRadialInternalClearances = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_default_temperatures(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseDefaultTemperatures

        if temp is None:
            return False

        return temp

    @use_default_temperatures.setter
    @enforce_parameter_types
    def use_default_temperatures(self: "Self", value: "bool") -> None:
        self.wrapped.UseDefaultTemperatures = (
            bool(value) if value is not None else False
        )

    @property
    def use_node_per_bearing_row_inner(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseNodePerBearingRowInner

        if temp is None:
            return False

        return temp

    @use_node_per_bearing_row_inner.setter
    @enforce_parameter_types
    def use_node_per_bearing_row_inner(self: "Self", value: "bool") -> None:
        self.wrapped.UseNodePerBearingRowInner = (
            bool(value) if value is not None else False
        )

    @property
    def use_node_per_bearing_row_outer(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseNodePerBearingRowOuter

        if temp is None:
            return False

        return temp

    @use_node_per_bearing_row_outer.setter
    @enforce_parameter_types
    def use_node_per_bearing_row_outer(self: "Self", value: "bool") -> None:
        self.wrapped.UseNodePerBearingRowOuter = (
            bool(value) if value is not None else False
        )

    @property
    def use_single_node_for_cylindrical_gear_meshes(
        self: "Self",
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.UseSingleNodeForCylindricalGearMeshes

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @use_single_node_for_cylindrical_gear_meshes.setter
    @enforce_parameter_types
    def use_single_node_for_cylindrical_gear_meshes(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.UseSingleNodeForCylindricalGearMeshes = value

    @property
    def use_single_node_for_spline_rigid_bond_detailed_connection_connections(
        self: "Self",
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.UseSingleNodeForSplineRigidBondDetailedConnectionConnections

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @use_single_node_for_spline_rigid_bond_detailed_connection_connections.setter
    @enforce_parameter_types
    def use_single_node_for_spline_rigid_bond_detailed_connection_connections(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.UseSingleNodeForSplineRigidBondDetailedConnectionConnections = (
            value
        )

    @property
    def additional_acceleration(self: "Self") -> "_6957.AdditionalAccelerationOptions":
        """mastapy._private.system_model.analyses_and_results.static_loads.AdditionalAccelerationOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdditionalAcceleration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def input_power_load(self: "Self") -> "_7088.PowerLoadLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputPowerLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def output_power_load(self: "Self") -> "_7088.PowerLoadLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OutputPowerLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_study_tool_options(
        self: "Self",
    ) -> "_4498.ParametricStudyToolOptions":
        """mastapy._private.system_model.analyses_and_results.parametric_study_tools.ParametricStudyToolOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyToolOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def temperatures(self: "Self") -> "_2277.TransmissionTemperatureSet":
        """mastapy._private.system_model.TransmissionTemperatureSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Temperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transmission_efficiency_settings(
        self: "Self",
    ) -> "_7127.TransmissionEfficiencySettings":
        """mastapy._private.system_model.analyses_and_results.static_loads.TransmissionEfficiencySettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionEfficiencySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_loads(self: "Self") -> "List[_7088.PowerLoadLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.PowerLoadLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def delete(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def inputs_for_coupling_connection(
        self: "Self", design_entity: "_2399.CouplingConnection"
    ) -> "_6998.CouplingConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spring_damper_connection(
        self: "Self", design_entity: "_2403.SpringDamperConnection"
    ) -> "_7105.SpringDamperConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPRING_DAMPER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_torque_converter_connection(
        self: "Self", design_entity: "_2405.TorqueConverterConnection"
    ) -> "_7121.TorqueConverterConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_abstract_shaft(
        self: "Self", design_entity: "_2489.AbstractShaft"
    ) -> "_6954.AbstractShaftLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AbstractShaftLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractShaft)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ABSTRACT_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_microphone(
        self: "Self", design_entity: "_2518.Microphone"
    ) -> "_7072.MicrophoneLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.MicrophoneLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.Microphone)
        """
        method_result = self.wrapped.InputsFor.Overloads[_MICROPHONE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_microphone_array(
        self: "Self", design_entity: "_2519.MicrophoneArray"
    ) -> "_7071.MicrophoneArrayLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.MicrophoneArrayLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.MicrophoneArray)
        """
        method_result = self.wrapped.InputsFor.Overloads[_MICROPHONE_ARRAY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_abstract_assembly(
        self: "Self", design_entity: "_2488.AbstractAssembly"
    ) -> "_6953.AbstractAssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ABSTRACT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_abstract_shaft_or_housing(
        self: "Self", design_entity: "_2490.AbstractShaftOrHousing"
    ) -> "_6955.AbstractShaftOrHousingLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractShaftOrHousing)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bearing(
        self: "Self", design_entity: "_2493.Bearing"
    ) -> "_6966.BearingLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BearingLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.Bearing)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEARING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bolt(
        self: "Self", design_entity: "_2496.Bolt"
    ) -> "_6978.BoltLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BoltLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.Bolt)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BOLT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bolted_joint(
        self: "Self", design_entity: "_2497.BoltedJoint"
    ) -> "_6977.BoltedJointLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.BoltedJoint)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BOLTED_JOINT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_component(
        self: "Self", design_entity: "_2498.Component"
    ) -> "_6984.ComponentLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ComponentLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_connector(
        self: "Self", design_entity: "_2501.Connector"
    ) -> "_6997.ConnectorLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConnectorLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.Connector)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONNECTOR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_datum(
        self: "Self", design_entity: "_2502.Datum"
    ) -> "_7016.DatumLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.DatumLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.Datum)
        """
        method_result = self.wrapped.InputsFor.Overloads[_DATUM](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_external_cad_model(
        self: "Self", design_entity: "_2506.ExternalCADModel"
    ) -> "_7030.ExternalCADModelLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.ExternalCADModel)
        """
        method_result = self.wrapped.InputsFor.Overloads[_EXTERNAL_CAD_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_fe_part(
        self: "Self", design_entity: "_2507.FEPart"
    ) -> "_7034.FEPartLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.FEPart)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FE_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_flexible_pin_assembly(
        self: "Self", design_entity: "_2508.FlexiblePinAssembly"
    ) -> "_7035.FlexiblePinAssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.FlexiblePinAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_assembly(
        self: "Self", design_entity: "_2487.Assembly"
    ) -> "_6965.AssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AssemblyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_guide_dxf_model(
        self: "Self", design_entity: "_2509.GuideDxfModel"
    ) -> "_7043.GuideDxfModelLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.GuideDxfModel)
        """
        method_result = self.wrapped.InputsFor.Overloads[_GUIDE_DXF_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_mass_disc(
        self: "Self", design_entity: "_2516.MassDisc"
    ) -> "_7068.MassDiscLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.MassDisc)
        """
        method_result = self.wrapped.InputsFor.Overloads[_MASS_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_measurement_component(
        self: "Self", design_entity: "_2517.MeasurementComponent"
    ) -> "_7069.MeasurementComponentLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.MeasurementComponent)
        """
        method_result = self.wrapped.InputsFor.Overloads[_MEASUREMENT_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_mountable_component(
        self: "Self", design_entity: "_2520.MountableComponent"
    ) -> "_7073.MountableComponentLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.MountableComponentLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.MountableComponent)
        """
        method_result = self.wrapped.InputsFor.Overloads[_MOUNTABLE_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_oil_seal(
        self: "Self", design_entity: "_2522.OilSeal"
    ) -> "_7075.OilSealLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.OilSeal)
        """
        method_result = self.wrapped.InputsFor.Overloads[_OIL_SEAL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_part(
        self: "Self", design_entity: "_2524.Part"
    ) -> "_7077.PartLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PartLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.Part)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_planet_carrier(
        self: "Self", design_entity: "_2525.PlanetCarrier"
    ) -> "_7084.PlanetCarrierLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.PlanetCarrier)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PLANET_CARRIER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_point_load(
        self: "Self", design_entity: "_2527.PointLoad"
    ) -> "_7087.PointLoadLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PointLoadLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.PointLoad)
        """
        method_result = self.wrapped.InputsFor.Overloads[_POINT_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_power_load(
        self: "Self", design_entity: "_2528.PowerLoad"
    ) -> "_7088.PowerLoadLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.PowerLoad)
        """
        method_result = self.wrapped.InputsFor.Overloads[_POWER_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_root_assembly(
        self: "Self", design_entity: "_2530.RootAssembly"
    ) -> "_7097.RootAssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.RootAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ROOT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_specialised_assembly(
        self: "Self", design_entity: "_2532.SpecialisedAssembly"
    ) -> "_7101.SpecialisedAssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.SpecialisedAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPECIALISED_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_unbalanced_mass(
        self: "Self", design_entity: "_2533.UnbalancedMass"
    ) -> "_7129.UnbalancedMassLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.UnbalancedMass)
        """
        method_result = self.wrapped.InputsFor.Overloads[_UNBALANCED_MASS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_virtual_component(
        self: "Self", design_entity: "_2535.VirtualComponent"
    ) -> "_7130.VirtualComponentLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.VirtualComponent)
        """
        method_result = self.wrapped.InputsFor.Overloads[_VIRTUAL_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_shaft(
        self: "Self", design_entity: "_2538.Shaft"
    ) -> "_7099.ShaftLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.shaft_model.Shaft)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_gear(
        self: "Self", design_entity: "_2577.ConceptGear"
    ) -> "_6988.ConceptGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConceptGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_gear_set(
        self: "Self", design_entity: "_2578.ConceptGearSet"
    ) -> "_6990.ConceptGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConceptGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_face_gear(
        self: "Self", design_entity: "_2584.FaceGear"
    ) -> "_7031.FaceGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.FaceGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FACE_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_face_gear_set(
        self: "Self", design_entity: "_2585.FaceGearSet"
    ) -> "_7033.FaceGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.FaceGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FACE_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_agma_gleason_conical_gear(
        self: "Self", design_entity: "_2569.AGMAGleasonConicalGear"
    ) -> "_6960.AGMAGleasonConicalGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_agma_gleason_conical_gear_set(
        self: "Self", design_entity: "_2570.AGMAGleasonConicalGearSet"
    ) -> "_6962.AGMAGleasonConicalGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_gear(
        self: "Self", design_entity: "_2571.BevelDifferentialGear"
    ) -> "_6969.BevelDifferentialGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_gear_set(
        self: "Self", design_entity: "_2572.BevelDifferentialGearSet"
    ) -> "_6971.BevelDifferentialGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_planet_gear(
        self: "Self", design_entity: "_2573.BevelDifferentialPlanetGear"
    ) -> "_6972.BevelDifferentialPlanetGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _BEVEL_DIFFERENTIAL_PLANET_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_sun_gear(
        self: "Self", design_entity: "_2574.BevelDifferentialSunGear"
    ) -> "_6973.BevelDifferentialSunGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_gear(
        self: "Self", design_entity: "_2575.BevelGear"
    ) -> "_6974.BevelGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BevelGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_gear_set(
        self: "Self", design_entity: "_2576.BevelGearSet"
    ) -> "_6976.BevelGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_conical_gear(
        self: "Self", design_entity: "_2579.ConicalGear"
    ) -> "_6991.ConicalGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConicalGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConicalGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_conical_gear_set(
        self: "Self", design_entity: "_2580.ConicalGearSet"
    ) -> "_6995.ConicalGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConicalGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cylindrical_gear(
        self: "Self", design_entity: "_2581.CylindricalGear"
    ) -> "_7008.CylindricalGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYLINDRICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cylindrical_gear_set(
        self: "Self", design_entity: "_2582.CylindricalGearSet"
    ) -> "_7012.CylindricalGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYLINDRICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cylindrical_planet_gear(
        self: "Self", design_entity: "_2583.CylindricalPlanetGear"
    ) -> "_7013.CylindricalPlanetGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalPlanetGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_gear(
        self: "Self", design_entity: "_2586.Gear"
    ) -> "_7037.GearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.GearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.Gear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_gear_set(
        self: "Self", design_entity: "_2588.GearSet"
    ) -> "_7042.GearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.GearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.GearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_hypoid_gear(
        self: "Self", design_entity: "_2590.HypoidGear"
    ) -> "_7052.HypoidGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.HypoidGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_HYPOID_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_hypoid_gear_set(
        self: "Self", design_entity: "_2591.HypoidGearSet"
    ) -> "_7054.HypoidGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.HypoidGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_HYPOID_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_conical_gear(
        self: "Self", design_entity: "_2592.KlingelnbergCycloPalloidConicalGear"
    ) -> "_7059.KlingelnbergCycloPalloidConicalGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: "Self", design_entity: "_2593.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "_7061.KlingelnbergCycloPalloidConicalGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: "Self", design_entity: "_2594.KlingelnbergCycloPalloidHypoidGear"
    ) -> "_7062.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: "Self", design_entity: "_2595.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "_7064.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "Self", design_entity: "_2596.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "_7065.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: "Self", design_entity: "_2597.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "_7067.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_planetary_gear_set(
        self: "Self", design_entity: "_2598.PlanetaryGearSet"
    ) -> "_7082.PlanetaryGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.PlanetaryGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PLANETARY_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spiral_bevel_gear(
        self: "Self", design_entity: "_2599.SpiralBevelGear"
    ) -> "_7102.SpiralBevelGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.SpiralBevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPIRAL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spiral_bevel_gear_set(
        self: "Self", design_entity: "_2600.SpiralBevelGearSet"
    ) -> "_7104.SpiralBevelGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.SpiralBevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_diff_gear(
        self: "Self", design_entity: "_2601.StraightBevelDiffGear"
    ) -> "_7108.StraightBevelDiffGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelDiffGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_diff_gear_set(
        self: "Self", design_entity: "_2602.StraightBevelDiffGearSet"
    ) -> "_7110.StraightBevelDiffGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_gear(
        self: "Self", design_entity: "_2603.StraightBevelGear"
    ) -> "_7111.StraightBevelGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_gear_set(
        self: "Self", design_entity: "_2604.StraightBevelGearSet"
    ) -> "_7113.StraightBevelGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_planet_gear(
        self: "Self", design_entity: "_2605.StraightBevelPlanetGear"
    ) -> "_7114.StraightBevelPlanetGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_sun_gear(
        self: "Self", design_entity: "_2606.StraightBevelSunGear"
    ) -> "_7115.StraightBevelSunGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelSunGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_worm_gear(
        self: "Self", design_entity: "_2607.WormGear"
    ) -> "_7131.WormGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.WormGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.WormGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_WORM_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_worm_gear_set(
        self: "Self", design_entity: "_2608.WormGearSet"
    ) -> "_7133.WormGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.WormGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_WORM_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_zerol_bevel_gear(
        self: "Self", design_entity: "_2609.ZerolBevelGear"
    ) -> "_7134.ZerolBevelGearLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ZerolBevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ZEROL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_zerol_bevel_gear_set(
        self: "Self", design_entity: "_2610.ZerolBevelGearSet"
    ) -> "_7136.ZerolBevelGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ZerolBevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cycloidal_assembly(
        self: "Self", design_entity: "_2624.CycloidalAssembly"
    ) -> "_7004.CycloidalAssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cycloidal_disc(
        self: "Self", design_entity: "_2625.CycloidalDisc"
    ) -> "_7006.CycloidalDiscLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.CycloidalDisc)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYCLOIDAL_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_ring_pins(
        self: "Self", design_entity: "_2626.RingPins"
    ) -> "_7092.RingPinsLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.RingPins)
        """
        method_result = self.wrapped.InputsFor.Overloads[_RING_PINS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_part_to_part_shear_coupling(
        self: "Self", design_entity: "_2646.PartToPartShearCoupling"
    ) -> "_7080.PartToPartShearCouplingLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_part_to_part_shear_coupling_half(
        self: "Self", design_entity: "_2647.PartToPartShearCouplingHalf"
    ) -> "_7079.PartToPartShearCouplingHalfLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_HALF
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_belt_drive(
        self: "Self", design_entity: "_2633.BeltDrive"
    ) -> "_6968.BeltDriveLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.BeltDrive)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BELT_DRIVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_clutch(
        self: "Self", design_entity: "_2635.Clutch"
    ) -> "_6981.ClutchLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Clutch)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CLUTCH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_clutch_half(
        self: "Self", design_entity: "_2636.ClutchHalf"
    ) -> "_6980.ClutchHalfLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ClutchHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CLUTCH_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_coupling(
        self: "Self", design_entity: "_2638.ConceptCoupling"
    ) -> "_6987.ConceptCouplingLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ConceptCoupling)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_coupling_half(
        self: "Self", design_entity: "_2639.ConceptCouplingHalf"
    ) -> "_6986.ConceptCouplingHalfLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_coupling(
        self: "Self", design_entity: "_2641.Coupling"
    ) -> "_7000.CouplingLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CouplingLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Coupling)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_coupling_half(
        self: "Self", design_entity: "_2642.CouplingHalf"
    ) -> "_6999.CouplingHalfLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CouplingHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cvt(self: "Self", design_entity: "_2644.CVT") -> "_7002.CVTLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CVTLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CVT)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CVT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cvt_pulley(
        self: "Self", design_entity: "_2645.CVTPulley"
    ) -> "_7003.CVTPulleyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CVTPulley)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CVT_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_pulley(
        self: "Self", design_entity: "_2649.Pulley"
    ) -> "_7089.PulleyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Pulley)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_shaft_hub_connection(
        self: "Self", design_entity: "_2657.ShaftHubConnection"
    ) -> "_7098.ShaftHubConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ShaftHubConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SHAFT_HUB_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_rolling_ring(
        self: "Self", design_entity: "_2655.RollingRing"
    ) -> "_7096.RollingRingLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.RollingRing)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ROLLING_RING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_rolling_ring_assembly(
        self: "Self", design_entity: "_2656.RollingRingAssembly"
    ) -> "_7094.RollingRingAssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.RollingRingAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ROLLING_RING_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spring_damper(
        self: "Self", design_entity: "_2662.SpringDamper"
    ) -> "_7107.SpringDamperLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SpringDamper)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPRING_DAMPER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spring_damper_half(
        self: "Self", design_entity: "_2663.SpringDamperHalf"
    ) -> "_7106.SpringDamperHalfLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SpringDamperHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPRING_DAMPER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_synchroniser(
        self: "Self", design_entity: "_2664.Synchroniser"
    ) -> "_7117.SynchroniserLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Synchroniser)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SYNCHRONISER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_synchroniser_half(
        self: "Self", design_entity: "_2666.SynchroniserHalf"
    ) -> "_7116.SynchroniserHalfLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SYNCHRONISER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_synchroniser_part(
        self: "Self", design_entity: "_2667.SynchroniserPart"
    ) -> "_7118.SynchroniserPartLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserPart)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SYNCHRONISER_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_synchroniser_sleeve(
        self: "Self", design_entity: "_2668.SynchroniserSleeve"
    ) -> "_7119.SynchroniserSleeveLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserSleeve)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SYNCHRONISER_SLEEVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_torque_converter(
        self: "Self", design_entity: "_2669.TorqueConverter"
    ) -> "_7122.TorqueConverterLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverter)
        """
        method_result = self.wrapped.InputsFor.Overloads[_TORQUE_CONVERTER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_torque_converter_pump(
        self: "Self", design_entity: "_2670.TorqueConverterPump"
    ) -> "_7123.TorqueConverterPumpLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverterPump)
        """
        method_result = self.wrapped.InputsFor.Overloads[_TORQUE_CONVERTER_PUMP](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_torque_converter_turbine(
        self: "Self", design_entity: "_2672.TorqueConverterTurbine"
    ) -> "_7124.TorqueConverterTurbineLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        method_result = self.wrapped.InputsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_shaft_to_mountable_component_connection(
        self: "Self", design_entity: "_2348.ShaftToMountableComponentConnection"
    ) -> "_7100.ShaftToMountableComponentConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cvt_belt_connection(
        self: "Self", design_entity: "_2326.CVTBeltConnection"
    ) -> "_7001.CVTBeltConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.CVTBeltConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CVT_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_belt_connection(
        self: "Self", design_entity: "_2321.BeltConnection"
    ) -> "_6967.BeltConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.BeltConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_coaxial_connection(
        self: "Self", design_entity: "_2322.CoaxialConnection"
    ) -> "_6983.CoaxialConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.CoaxialConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COAXIAL_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_connection(
        self: "Self", design_entity: "_2325.Connection"
    ) -> "_6996.ConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_inter_mountable_component_connection(
        self: "Self", design_entity: "_2334.InterMountableComponentConnection"
    ) -> "_7058.InterMountableComponentConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _INTER_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_planetary_connection(
        self: "Self", design_entity: "_2340.PlanetaryConnection"
    ) -> "_7081.PlanetaryConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.PlanetaryConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PLANETARY_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_rolling_ring_connection(
        self: "Self", design_entity: "_2345.RollingRingConnection"
    ) -> "_7095.RollingRingConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.RollingRingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ROLLING_RING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_abstract_shaft_to_mountable_component_connection(
        self: "Self", design_entity: "_2318.AbstractShaftToMountableComponentConnection"
    ) -> "_6956.AbstractShaftToMountableComponentConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AbstractShaftToMountableComponentConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_gear_mesh(
        self: "Self", design_entity: "_2354.BevelDifferentialGearMesh"
    ) -> "_6970.BevelDifferentialGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_gear_mesh(
        self: "Self", design_entity: "_2358.ConceptGearMesh"
    ) -> "_6989.ConceptGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_face_gear_mesh(
        self: "Self", design_entity: "_2364.FaceGearMesh"
    ) -> "_7032.FaceGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FACE_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_diff_gear_mesh(
        self: "Self", design_entity: "_2378.StraightBevelDiffGearMesh"
    ) -> "_7109.StraightBevelDiffGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_gear_mesh(
        self: "Self", design_entity: "_2356.BevelGearMesh"
    ) -> "_6975.BevelGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_conical_gear_mesh(
        self: "Self", design_entity: "_2360.ConicalGearMesh"
    ) -> "_6993.ConicalGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_agma_gleason_conical_gear_mesh(
        self: "Self", design_entity: "_2352.AGMAGleasonConicalGearMesh"
    ) -> "_6961.AGMAGleasonConicalGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cylindrical_gear_mesh(
        self: "Self", design_entity: "_2362.CylindricalGearMesh"
    ) -> "_7010.CylindricalGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_hypoid_gear_mesh(
        self: "Self", design_entity: "_2368.HypoidGearMesh"
    ) -> "_7053.HypoidGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_HYPOID_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: "Self", design_entity: "_2371.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "_7060.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: "Self", design_entity: "_2372.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "_7063.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: "Self", design_entity: "_2373.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "_7066.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spiral_bevel_gear_mesh(
        self: "Self", design_entity: "_2376.SpiralBevelGearMesh"
    ) -> "_7103.SpiralBevelGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_gear_mesh(
        self: "Self", design_entity: "_2380.StraightBevelGearMesh"
    ) -> "_7112.StraightBevelGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_worm_gear_mesh(
        self: "Self", design_entity: "_2382.WormGearMesh"
    ) -> "_7132.WormGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_WORM_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_zerol_bevel_gear_mesh(
        self: "Self", design_entity: "_2384.ZerolBevelGearMesh"
    ) -> "_7135.ZerolBevelGearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_gear_mesh(
        self: "Self", design_entity: "_2366.GearMesh"
    ) -> "_7039.GearMeshLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.GearMeshLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.GearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cycloidal_disc_central_bearing_connection(
        self: "Self", design_entity: "_2388.CycloidalDiscCentralBearingConnection"
    ) -> "_7005.CycloidalDiscCentralBearingConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CycloidalDiscCentralBearingConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cycloidal_disc_planetary_bearing_connection(
        self: "Self", design_entity: "_2391.CycloidalDiscPlanetaryBearingConnection"
    ) -> "_7007.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_ring_pins_to_disc_connection(
        self: "Self", design_entity: "_2394.RingPinsToDiscConnection"
    ) -> "_7093.RingPinsToDiscConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_part_to_part_shear_coupling_connection(
        self: "Self", design_entity: "_2401.PartToPartShearCouplingConnection"
    ) -> "_7078.PartToPartShearCouplingConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_clutch_connection(
        self: "Self", design_entity: "_2395.ClutchConnection"
    ) -> "_6979.ClutchConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CLUTCH_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_coupling_connection(
        self: "Self", design_entity: "_2397.ConceptCouplingConnection"
    ) -> "_6985.ConceptCouplingConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_LoadCase":
        """Cast to another type.

        Returns:
            _Cast_LoadCase
        """
        return _Cast_LoadCase(self)
