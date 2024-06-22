"""MultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.analyses_and_results import _2703
from mastapy._private._internal.cast_exception import CastException

_CONCEPT_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingConnectionLoadCase",
)
_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CouplingConnectionLoadCase",
)
_SPRING_DAMPER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperConnectionLoadCase",
)
_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterConnectionLoadCase",
)
_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelPlanetGearLoadCase",
)
_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelSunGearLoadCase",
)
_WORM_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearLoadCase"
)
_WORM_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearSetLoadCase"
)
_ZEROL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ZerolBevelGearLoadCase"
)
_ZEROL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ZerolBevelGearSetLoadCase",
)
_CYCLOIDAL_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalAssemblyLoadCase",
)
_CYCLOIDAL_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CycloidalDiscLoadCase"
)
_RING_PINS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RingPinsLoadCase"
)
_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingLoadCase",
)
_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingHalfLoadCase",
)
_BELT_DRIVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltDriveLoadCase"
)
_CLUTCH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchLoadCase"
)
_CLUTCH_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchHalfLoadCase"
)
_CONCEPT_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptCouplingLoadCase"
)
_CONCEPT_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingHalfLoadCase",
)
_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingLoadCase"
)
_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)
_CVT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTLoadCase"
)
_CVT_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTPulleyLoadCase"
)
_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PulleyLoadCase"
)
_SHAFT_HUB_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftHubConnectionLoadCase",
)
_ROLLING_RING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RollingRingLoadCase"
)
_ROLLING_RING_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingAssemblyLoadCase",
)
_SPRING_DAMPER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpringDamperLoadCase"
)
_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperHalfLoadCase",
)
_SYNCHRONISER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SynchroniserLoadCase"
)
_SYNCHRONISER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserHalfLoadCase",
)
_SYNCHRONISER_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserPartLoadCase",
)
_SYNCHRONISER_SLEEVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserSleeveLoadCase",
)
_TORQUE_CONVERTER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TorqueConverterLoadCase"
)
_TORQUE_CONVERTER_PUMP_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterPumpLoadCase",
)
_TORQUE_CONVERTER_TURBINE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterTurbineLoadCase",
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftToMountableComponentConnectionLoadCase",
)
_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CVTBeltConnectionLoadCase",
)
_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltConnectionLoadCase"
)
_COAXIAL_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CoaxialConnectionLoadCase",
)
_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)
_PLANETARY_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryConnectionLoadCase",
)
_ROLLING_RING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingConnectionLoadCase",
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftToMountableComponentConnectionLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearMeshLoadCase",
)
_CONCEPT_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearMeshLoadCase"
)
_FACE_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearMeshLoadCase"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearMeshLoadCase",
)
_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearMeshLoadCase"
)
_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearMeshLoadCase"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearMeshLoadCase",
)
_CYLINDRICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearMeshLoadCase",
)
_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearMeshLoadCase"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
)
_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearMeshLoadCase",
)
_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearMeshLoadCase",
)
_WORM_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearMeshLoadCase"
)
_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ZerolBevelGearMeshLoadCase",
)
_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearMeshLoadCase"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscCentralBearingConnectionLoadCase",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
)
_RING_PINS_TO_DISC_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RingPinsToDiscConnectionLoadCase",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingConnectionLoadCase",
)
_CLUTCH_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ClutchConnectionLoadCase",
)
_ABSTRACT_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AbstractShaftLoadCase"
)
_MICROPHONE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MicrophoneLoadCase"
)
_MICROPHONE_ARRAY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MicrophoneArrayLoadCase"
)
_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractAssemblyLoadCase",
)
_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftOrHousingLoadCase",
)
_BEARING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BearingLoadCase"
)
_BOLT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltLoadCase"
)
_BOLTED_JOINT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltedJointLoadCase"
)
_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)
_CONNECTOR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectorLoadCase"
)
_DATUM_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "DatumLoadCase"
)
_EXTERNAL_CAD_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ExternalCADModelLoadCase",
)
_FE_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FEPartLoadCase"
)
_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "FlexiblePinAssemblyLoadCase",
)
_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AssemblyLoadCase"
)
_GUIDE_DXF_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GuideDxfModelLoadCase"
)
_MASS_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MassDiscLoadCase"
)
_MEASUREMENT_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MeasurementComponentLoadCase",
)
_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MountableComponentLoadCase",
)
_OIL_SEAL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "OilSealLoadCase"
)
_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)
_PLANET_CARRIER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PlanetCarrierLoadCase"
)
_POINT_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PointLoadLoadCase"
)
_POWER_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PowerLoadLoadCase"
)
_ROOT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RootAssemblyLoadCase"
)
_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpecialisedAssemblyLoadCase",
)
_UNBALANCED_MASS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "UnbalancedMassLoadCase"
)
_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "VirtualComponentLoadCase",
)
_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ShaftLoadCase"
)
_CONCEPT_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearLoadCase"
)
_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearSetLoadCase"
)
_FACE_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearLoadCase"
)
_FACE_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearSetLoadCase"
)
_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)
_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearSetLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearSetLoadCase",
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialPlanetGearLoadCase",
)
_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialSunGearLoadCase",
)
_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearLoadCase"
)
_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearSetLoadCase"
)
_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearLoadCase"
)
_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearSetLoadCase"
)
_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CylindricalGearLoadCase"
)
_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearSetLoadCase",
)
_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalPlanetGearLoadCase",
)
_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearLoadCase"
)
_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearSetLoadCase"
)
_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearLoadCase"
)
_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearSetLoadCase"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
)
_PLANETARY_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryGearSetLoadCase",
)
_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpiralBevelGearLoadCase"
)
_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearSetLoadCase",
)
_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearLoadCase",
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearSetLoadCase",
)
_STRAIGHT_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearLoadCase",
)
_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearSetLoadCase",
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
_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
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
_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "MultibodyDynamicsAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _6985,
        _6998,
        _7105,
        _7121,
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
        _7088,
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
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
        _5529,
        _5540,
        _5620,
        _5635,
        _5629,
        _5630,
        _5645,
        _5646,
        _5648,
        _5649,
        _5546,
        _5548,
        _5603,
        _5596,
        _5595,
        _5512,
        _5525,
        _5524,
        _5531,
        _5530,
        _5542,
        _5541,
        _5544,
        _5545,
        _5602,
        _5611,
        _5607,
        _5605,
        _5622,
        _5621,
        _5632,
        _5631,
        _5633,
        _5634,
        _5637,
        _5638,
        _5640,
        _5613,
        _5543,
        _5511,
        _5527,
        _5538,
        _5573,
        _5597,
        _5606,
        _5502,
        _5513,
        _5532,
        _5556,
        _5623,
        _5518,
        _5535,
        _5503,
        _5550,
        _5566,
        _5574,
        _5577,
        _5580,
        _5616,
        _5626,
        _5644,
        _5647,
        _5561,
        _5547,
        _5549,
        _5604,
        _5594,
        _5523,
        _5500,
        _5589,
        _5588,
        _5499,
        _5501,
        _5509,
        _5522,
        _5521,
        _5528,
        _5539,
        _5554,
        _5555,
        _5559,
        _5560,
        _5507,
        _5565,
        _5583,
        _5587,
        _5590,
        _5592,
        _5593,
        _5599,
        _5600,
        _5601,
        _5608,
        _5615,
        _5641,
        _5642,
        _5612,
        _5533,
        _5534,
        _5557,
        _5558,
        _5504,
        _5505,
        _5514,
        _5515,
        _5516,
        _5517,
        _5519,
        _5520,
        _5536,
        _5537,
        _5551,
        _5552,
        _5553,
        _5563,
        _5564,
        _5567,
        _5568,
        _5575,
        _5576,
        _5578,
        _5579,
        _5581,
        _5582,
        _5598,
        _5617,
        _5618,
        _5624,
        _5625,
        _5627,
        _5628,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings import (
        _2399,
        _2403,
        _2405,
        _2401,
        _2395,
        _2397,
    )
    from mastapy._private.system_model.part_model.gears import (
        _2606,
        _2607,
        _2608,
        _2609,
        _2610,
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
    from mastapy._private import _7718

    Self = TypeVar("Self", bound="MultibodyDynamicsAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("MultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MultibodyDynamicsAnalysis:
    """Special nested class for casting MultibodyDynamicsAnalysis to subclasses."""

    __parent__: "MultibodyDynamicsAnalysis"

    @property
    def single_analysis(self: "CastSelf") -> "_2703.SingleAnalysis":
        return self.__parent__._cast(_2703.SingleAnalysis)

    @property
    def marshal_by_ref_object_permanent(
        self: "CastSelf",
    ) -> "_7718.MarshalByRefObjectPermanent":
        from mastapy._private import _7718

        return self.__parent__._cast(_7718.MarshalByRefObjectPermanent)

    @property
    def multibody_dynamics_analysis(self: "CastSelf") -> "MultibodyDynamicsAnalysis":
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
class MultibodyDynamicsAnalysis(_2703.SingleAnalysis):
    """MultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @enforce_parameter_types
    def results_for_concept_coupling_connection_load_case(
        self: "Self", design_entity_analysis: "_6985.ConceptCouplingConnectionLoadCase"
    ) -> "_5529.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptCouplingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CONCEPT_COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_connection(
        self: "Self", design_entity: "_2399.CouplingConnection"
    ) -> "_5540.CouplingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CouplingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_connection_load_case(
        self: "Self", design_entity_analysis: "_6998.CouplingConnectionLoadCase"
    ) -> "_5540.CouplingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CouplingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: "Self", design_entity: "_2403.SpringDamperConnection"
    ) -> "_5620.SpringDamperConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpringDamperConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_connection_load_case(
        self: "Self", design_entity_analysis: "_7105.SpringDamperConnectionLoadCase"
    ) -> "_5620.SpringDamperConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpringDamperConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPRING_DAMPER_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection(
        self: "Self", design_entity: "_2405.TorqueConverterConnection"
    ) -> "_5635.TorqueConverterConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection_load_case(
        self: "Self", design_entity_analysis: "_7121.TorqueConverterConnectionLoadCase"
    ) -> "_5635.TorqueConverterConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear_load_case(
        self: "Self", design_entity_analysis: "_7114.StraightBevelPlanetGearLoadCase"
    ) -> "_5629.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelPlanetGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear(
        self: "Self", design_entity: "_2606.StraightBevelSunGear"
    ) -> "_5630.StraightBevelSunGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelSunGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelSunGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear_load_case(
        self: "Self", design_entity_analysis: "_7115.StraightBevelSunGearLoadCase"
    ) -> "_5630.StraightBevelSunGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelSunGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear(
        self: "Self", design_entity: "_2607.WormGear"
    ) -> "_5645.WormGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.WormGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.WormGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_load_case(
        self: "Self", design_entity_analysis: "_7131.WormGearLoadCase"
    ) -> "_5645.WormGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.WormGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.WormGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_set(
        self: "Self", design_entity: "_2608.WormGearSet"
    ) -> "_5646.WormGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.WormGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.WormGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7133.WormGearSetLoadCase"
    ) -> "_5646.WormGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.WormGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear(
        self: "Self", design_entity: "_2609.ZerolBevelGear"
    ) -> "_5648.ZerolBevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ZerolBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_load_case(
        self: "Self", design_entity_analysis: "_7134.ZerolBevelGearLoadCase"
    ) -> "_5648.ZerolBevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set(
        self: "Self", design_entity: "_2610.ZerolBevelGearSet"
    ) -> "_5649.ZerolBevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ZerolBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7136.ZerolBevelGearSetLoadCase"
    ) -> "_5649.ZerolBevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ZEROL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly(
        self: "Self", design_entity: "_2624.CycloidalAssembly"
    ) -> "_5546.CycloidalAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CycloidalAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly_load_case(
        self: "Self", design_entity_analysis: "_7004.CycloidalAssemblyLoadCase"
    ) -> "_5546.CycloidalAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CycloidalAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc(
        self: "Self", design_entity: "_2625.CycloidalDisc"
    ) -> "_5548.CycloidalDiscMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CycloidalDiscMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.CycloidalDisc)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_load_case(
        self: "Self", design_entity_analysis: "_7006.CycloidalDiscLoadCase"
    ) -> "_5548.CycloidalDiscMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CycloidalDiscMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins(
        self: "Self", design_entity: "_2626.RingPins"
    ) -> "_5603.RingPinsMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RingPinsMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.cycloidal.RingPins)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_load_case(
        self: "Self", design_entity_analysis: "_7092.RingPinsLoadCase"
    ) -> "_5603.RingPinsMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RingPinsMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.RingPinsLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling(
        self: "Self", design_entity: "_2646.PartToPartShearCoupling"
    ) -> "_5596.PartToPartShearCouplingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PartToPartShearCouplingMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_load_case(
        self: "Self", design_entity_analysis: "_7080.PartToPartShearCouplingLoadCase"
    ) -> "_5596.PartToPartShearCouplingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PartToPartShearCouplingMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half(
        self: "Self", design_entity: "_2647.PartToPartShearCouplingHalf"
    ) -> "_5595.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_HALF
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half_load_case(
        self: "Self",
        design_entity_analysis: "_7079.PartToPartShearCouplingHalfLoadCase",
    ) -> "_5595.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_drive(
        self: "Self", design_entity: "_2633.BeltDrive"
    ) -> "_5512.BeltDriveMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BeltDriveMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.BeltDrive)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_drive_load_case(
        self: "Self", design_entity_analysis: "_6968.BeltDriveLoadCase"
    ) -> "_5512.BeltDriveMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BeltDriveMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch(
        self: "Self", design_entity: "_2635.Clutch"
    ) -> "_5525.ClutchMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ClutchMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Clutch)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_load_case(
        self: "Self", design_entity_analysis: "_6981.ClutchLoadCase"
    ) -> "_5525.ClutchMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ClutchMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ClutchLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_half(
        self: "Self", design_entity: "_2636.ClutchHalf"
    ) -> "_5524.ClutchHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ClutchHalfMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ClutchHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_half_load_case(
        self: "Self", design_entity_analysis: "_6980.ClutchHalfLoadCase"
    ) -> "_5524.ClutchHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ClutchHalfMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling(
        self: "Self", design_entity: "_2638.ConceptCoupling"
    ) -> "_5531.ConceptCouplingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptCouplingMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ConceptCoupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_load_case(
        self: "Self", design_entity_analysis: "_6987.ConceptCouplingLoadCase"
    ) -> "_5531.ConceptCouplingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptCouplingMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half(
        self: "Self", design_entity: "_2639.ConceptCouplingHalf"
    ) -> "_5530.ConceptCouplingHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptCouplingHalfMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half_load_case(
        self: "Self", design_entity_analysis: "_6986.ConceptCouplingHalfLoadCase"
    ) -> "_5530.ConceptCouplingHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptCouplingHalfMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CONCEPT_COUPLING_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling(
        self: "Self", design_entity: "_2641.Coupling"
    ) -> "_5542.CouplingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CouplingMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Coupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_load_case(
        self: "Self", design_entity_analysis: "_7000.CouplingLoadCase"
    ) -> "_5542.CouplingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CouplingMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_half(
        self: "Self", design_entity: "_2642.CouplingHalf"
    ) -> "_5541.CouplingHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CouplingHalfMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_half_load_case(
        self: "Self", design_entity_analysis: "_6999.CouplingHalfLoadCase"
    ) -> "_5541.CouplingHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CouplingHalfMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt(
        self: "Self", design_entity: "_2644.CVT"
    ) -> "_5544.CVTMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CVTMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CVT)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_load_case(
        self: "Self", design_entity_analysis: "_7002.CVTLoadCase"
    ) -> "_5544.CVTMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CVTMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CVTLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_pulley(
        self: "Self", design_entity: "_2645.CVTPulley"
    ) -> "_5545.CVTPulleyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CVTPulleyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.CVTPulley)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_pulley_load_case(
        self: "Self", design_entity_analysis: "_7003.CVTPulleyLoadCase"
    ) -> "_5545.CVTPulleyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CVTPulleyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_pulley(
        self: "Self", design_entity: "_2649.Pulley"
    ) -> "_5602.PulleyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PulleyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Pulley)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_pulley_load_case(
        self: "Self", design_entity_analysis: "_7089.PulleyLoadCase"
    ) -> "_5602.PulleyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PulleyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PulleyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection(
        self: "Self", design_entity: "_2657.ShaftHubConnection"
    ) -> "_5611.ShaftHubConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ShaftHubConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.ShaftHubConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection_load_case(
        self: "Self", design_entity_analysis: "_7098.ShaftHubConnectionLoadCase"
    ) -> "_5611.ShaftHubConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ShaftHubConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_HUB_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring(
        self: "Self", design_entity: "_2655.RollingRing"
    ) -> "_5607.RollingRingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RollingRingMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.RollingRing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_load_case(
        self: "Self", design_entity_analysis: "_7096.RollingRingLoadCase"
    ) -> "_5607.RollingRingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RollingRingMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.RollingRingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly(
        self: "Self", design_entity: "_2656.RollingRingAssembly"
    ) -> "_5605.RollingRingAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RollingRingAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.RollingRingAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly_load_case(
        self: "Self", design_entity_analysis: "_7094.RollingRingAssemblyLoadCase"
    ) -> "_5605.RollingRingAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RollingRingAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ROLLING_RING_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper(
        self: "Self", design_entity: "_2662.SpringDamper"
    ) -> "_5622.SpringDamperMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpringDamperMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SpringDamper)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_load_case(
        self: "Self", design_entity_analysis: "_7107.SpringDamperLoadCase"
    ) -> "_5622.SpringDamperMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpringDamperMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_half(
        self: "Self", design_entity: "_2663.SpringDamperHalf"
    ) -> "_5621.SpringDamperHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpringDamperHalfMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SpringDamperHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_half_load_case(
        self: "Self", design_entity_analysis: "_7106.SpringDamperHalfLoadCase"
    ) -> "_5621.SpringDamperHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpringDamperHalfMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPRING_DAMPER_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser(
        self: "Self", design_entity: "_2664.Synchroniser"
    ) -> "_5632.SynchroniserMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SynchroniserMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.Synchroniser)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_load_case(
        self: "Self", design_entity_analysis: "_7117.SynchroniserLoadCase"
    ) -> "_5632.SynchroniserMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SynchroniserMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_half(
        self: "Self", design_entity: "_2666.SynchroniserHalf"
    ) -> "_5631.SynchroniserHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SynchroniserHalfMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_half_load_case(
        self: "Self", design_entity_analysis: "_7116.SynchroniserHalfLoadCase"
    ) -> "_5631.SynchroniserHalfMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SynchroniserHalfMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_part(
        self: "Self", design_entity: "_2667.SynchroniserPart"
    ) -> "_5633.SynchroniserPartMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SynchroniserPartMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserPart)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_part_load_case(
        self: "Self", design_entity_analysis: "_7118.SynchroniserPartLoadCase"
    ) -> "_5633.SynchroniserPartMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SynchroniserPartMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve(
        self: "Self", design_entity: "_2668.SynchroniserSleeve"
    ) -> "_5634.SynchroniserSleeveMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SynchroniserSleeveMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.SynchroniserSleeve)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve_load_case(
        self: "Self", design_entity_analysis: "_7119.SynchroniserSleeveLoadCase"
    ) -> "_5634.SynchroniserSleeveMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SynchroniserSleeveMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SYNCHRONISER_SLEEVE_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter(
        self: "Self", design_entity: "_2669.TorqueConverter"
    ) -> "_5637.TorqueConverterMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverter)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_load_case(
        self: "Self", design_entity_analysis: "_7122.TorqueConverterLoadCase"
    ) -> "_5637.TorqueConverterMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump(
        self: "Self", design_entity: "_2670.TorqueConverterPump"
    ) -> "_5638.TorqueConverterPumpMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterPumpMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverterPump)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump_load_case(
        self: "Self", design_entity_analysis: "_7123.TorqueConverterPumpLoadCase"
    ) -> "_5638.TorqueConverterPumpMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterPumpMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_PUMP_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine(
        self: "Self", design_entity: "_2672.TorqueConverterTurbine"
    ) -> "_5640.TorqueConverterTurbineMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterTurbineMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine_load_case(
        self: "Self", design_entity_analysis: "_7124.TorqueConverterTurbineLoadCase"
    ) -> "_5640.TorqueConverterTurbineMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.TorqueConverterTurbineMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_TURBINE_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection(
        self: "Self", design_entity: "_2348.ShaftToMountableComponentConnection"
    ) -> "_5613.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7100.ShaftToMountableComponentConnectionLoadCase",
    ) -> "_5613.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection(
        self: "Self", design_entity: "_2326.CVTBeltConnection"
    ) -> "_5543.CVTBeltConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CVTBeltConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.CVTBeltConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection_load_case(
        self: "Self", design_entity_analysis: "_7001.CVTBeltConnectionLoadCase"
    ) -> "_5543.CVTBeltConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CVTBeltConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CVT_BELT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_connection(
        self: "Self", design_entity: "_2321.BeltConnection"
    ) -> "_5511.BeltConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BeltConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.BeltConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_connection_load_case(
        self: "Self", design_entity_analysis: "_6967.BeltConnectionLoadCase"
    ) -> "_5511.BeltConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BeltConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coaxial_connection(
        self: "Self", design_entity: "_2322.CoaxialConnection"
    ) -> "_5527.CoaxialConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CoaxialConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.CoaxialConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coaxial_connection_load_case(
        self: "Self", design_entity_analysis: "_6983.CoaxialConnectionLoadCase"
    ) -> "_5527.CoaxialConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CoaxialConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _COAXIAL_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connection(
        self: "Self", design_entity: "_2325.Connection"
    ) -> "_5538.ConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connection_load_case(
        self: "Self", design_entity_analysis: "_6996.ConnectionLoadCase"
    ) -> "_5538.ConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection(
        self: "Self", design_entity: "_2334.InterMountableComponentConnection"
    ) -> "_5573.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.InterMountableComponentConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _INTER_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7058.InterMountableComponentConnectionLoadCase",
    ) -> "_5573.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.InterMountableComponentConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_connection(
        self: "Self", design_entity: "_2340.PlanetaryConnection"
    ) -> "_5597.PlanetaryConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PlanetaryConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.PlanetaryConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_connection_load_case(
        self: "Self", design_entity_analysis: "_7081.PlanetaryConnectionLoadCase"
    ) -> "_5597.PlanetaryConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PlanetaryConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PLANETARY_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection(
        self: "Self", design_entity: "_2345.RollingRingConnection"
    ) -> "_5606.RollingRingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RollingRingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.RollingRingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection_load_case(
        self: "Self", design_entity_analysis: "_7095.RollingRingConnectionLoadCase"
    ) -> "_5606.RollingRingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RollingRingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ROLLING_RING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection(
        self: "Self", design_entity: "_2318.AbstractShaftToMountableComponentConnection"
    ) -> "_5502.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection_load_case(
        self: "Self",
        design_entity_analysis: "_6956.AbstractShaftToMountableComponentConnectionLoadCase",
    ) -> "_5502.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.AbstractShaftToMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh(
        self: "Self", design_entity: "_2354.BevelDifferentialGearMesh"
    ) -> "_5513.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_6970.BevelDifferentialGearMeshLoadCase"
    ) -> "_5513.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh(
        self: "Self", design_entity: "_2358.ConceptGearMesh"
    ) -> "_5532.ConceptGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_6989.ConceptGearMeshLoadCase"
    ) -> "_5532.ConceptGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh(
        self: "Self", design_entity: "_2364.FaceGearMesh"
    ) -> "_5556.FaceGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FaceGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7032.FaceGearMeshLoadCase"
    ) -> "_5556.FaceGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FaceGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh(
        self: "Self", design_entity: "_2378.StraightBevelDiffGearMesh"
    ) -> "_5623.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7109.StraightBevelDiffGearMeshLoadCase"
    ) -> "_5623.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh(
        self: "Self", design_entity: "_2356.BevelGearMesh"
    ) -> "_5518.BevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_6975.BevelGearMeshLoadCase"
    ) -> "_5518.BevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh(
        self: "Self", design_entity: "_2360.ConicalGearMesh"
    ) -> "_5535.ConicalGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_6993.ConicalGearMeshLoadCase"
    ) -> "_5535.ConicalGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh(
        self: "Self", design_entity: "_2352.AGMAGleasonConicalGearMesh"
    ) -> "_5503.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_6961.AGMAGleasonConicalGearMeshLoadCase"
    ) -> "_5503.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh(
        self: "Self", design_entity: "_2362.CylindricalGearMesh"
    ) -> "_5550.CylindricalGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CylindricalGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7010.CylindricalGearMeshLoadCase"
    ) -> "_5550.CylindricalGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CylindricalGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh(
        self: "Self", design_entity: "_2368.HypoidGearMesh"
    ) -> "_5566.HypoidGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.HypoidGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7053.HypoidGearMeshLoadCase"
    ) -> "_5566.HypoidGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.HypoidGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: "Self", design_entity: "_2371.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "_5574.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
        self: "Self",
        design_entity_analysis: "_7060.KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    ) -> "_5574.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: "Self", design_entity: "_2372.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "_5577.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
        self: "Self",
        design_entity_analysis: "_7063.KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    ) -> "_5577.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: "Self", design_entity: "_2373.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "_5580.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
        self: "Self",
        design_entity_analysis: "_7066.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    ) -> "_5580.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh(
        self: "Self", design_entity: "_2376.SpiralBevelGearMesh"
    ) -> "_5616.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7103.SpiralBevelGearMeshLoadCase"
    ) -> "_5616.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh(
        self: "Self", design_entity: "_2380.StraightBevelGearMesh"
    ) -> "_5626.StraightBevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7112.StraightBevelGearMeshLoadCase"
    ) -> "_5626.StraightBevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh(
        self: "Self", design_entity: "_2382.WormGearMesh"
    ) -> "_5644.WormGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.WormGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7132.WormGearMeshLoadCase"
    ) -> "_5644.WormGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.WormGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh(
        self: "Self", design_entity: "_2384.ZerolBevelGearMesh"
    ) -> "_5647.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7135.ZerolBevelGearMeshLoadCase"
    ) -> "_5647.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ZerolBevelGearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ZEROL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_mesh(
        self: "Self", design_entity: "_2366.GearMesh"
    ) -> "_5561.GearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.GearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.gears.GearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7039.GearMeshLoadCase"
    ) -> "_5561.GearMeshMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.GearMeshMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.GearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection(
        self: "Self", design_entity: "_2388.CycloidalDiscCentralBearingConnection"
    ) -> "_5547.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7005.CycloidalDiscCentralBearingConnectionLoadCase",
    ) -> "_5547.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CycloidalDiscCentralBearingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection(
        self: "Self", design_entity: "_2391.CycloidalDiscPlanetaryBearingConnection"
    ) -> "_5549.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7007.CycloidalDiscPlanetaryBearingConnectionLoadCase",
    ) -> "_5549.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection(
        self: "Self", design_entity: "_2394.RingPinsToDiscConnection"
    ) -> "_5604.RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RingPinsToDiscConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _RING_PINS_TO_DISC_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection_load_case(
        self: "Self", design_entity_analysis: "_7093.RingPinsToDiscConnectionLoadCase"
    ) -> "_5604.RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RingPinsToDiscConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _RING_PINS_TO_DISC_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection(
        self: "Self", design_entity: "_2401.PartToPartShearCouplingConnection"
    ) -> "_5594.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7078.PartToPartShearCouplingConnectionLoadCase",
    ) -> "_5594.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_connection(
        self: "Self", design_entity: "_2395.ClutchConnection"
    ) -> "_5523.ClutchConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ClutchConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_connection_load_case(
        self: "Self", design_entity_analysis: "_6979.ClutchConnectionLoadCase"
    ) -> "_5523.ClutchConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ClutchConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: "Self", design_entity: "_2397.ConceptCouplingConnection"
    ) -> "_5529.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptCouplingConnectionMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft(
        self: "Self", design_entity: "_2489.AbstractShaft"
    ) -> "_5500.AbstractShaftMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractShaftMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractShaft)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_load_case(
        self: "Self", design_entity_analysis: "_6954.AbstractShaftLoadCase"
    ) -> "_5500.AbstractShaftMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractShaftMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.AbstractShaftLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_microphone(
        self: "Self", design_entity: "_2518.Microphone"
    ) -> "_5589.MicrophoneMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MicrophoneMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.Microphone)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MICROPHONE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_microphone_load_case(
        self: "Self", design_entity_analysis: "_7072.MicrophoneLoadCase"
    ) -> "_5589.MicrophoneMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MicrophoneMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.MicrophoneLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MICROPHONE_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_microphone_array(
        self: "Self", design_entity: "_2519.MicrophoneArray"
    ) -> "_5588.MicrophoneArrayMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MicrophoneArrayMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.MicrophoneArray)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MICROPHONE_ARRAY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_microphone_array_load_case(
        self: "Self", design_entity_analysis: "_7071.MicrophoneArrayLoadCase"
    ) -> "_5588.MicrophoneArrayMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MicrophoneArrayMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.MicrophoneArrayLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MICROPHONE_ARRAY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_assembly(
        self: "Self", design_entity: "_2488.AbstractAssembly"
    ) -> "_5499.AbstractAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_assembly_load_case(
        self: "Self", design_entity_analysis: "_6953.AbstractAssemblyLoadCase"
    ) -> "_5499.AbstractAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing(
        self: "Self", design_entity: "_2490.AbstractShaftOrHousing"
    ) -> "_5501.AbstractShaftOrHousingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractShaftOrHousingMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.AbstractShaftOrHousing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing_load_case(
        self: "Self", design_entity_analysis: "_6955.AbstractShaftOrHousingLoadCase"
    ) -> "_5501.AbstractShaftOrHousingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AbstractShaftOrHousingMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bearing(
        self: "Self", design_entity: "_2493.Bearing"
    ) -> "_5509.BearingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BearingMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.Bearing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEARING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bearing_load_case(
        self: "Self", design_entity_analysis: "_6966.BearingLoadCase"
    ) -> "_5509.BearingMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BearingMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BearingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEARING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolt(
        self: "Self", design_entity: "_2496.Bolt"
    ) -> "_5522.BoltMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BoltMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.Bolt)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolt_load_case(
        self: "Self", design_entity_analysis: "_6978.BoltLoadCase"
    ) -> "_5522.BoltMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BoltMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BoltLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolted_joint(
        self: "Self", design_entity: "_2497.BoltedJoint"
    ) -> "_5521.BoltedJointMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BoltedJointMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.BoltedJoint)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolted_joint_load_case(
        self: "Self", design_entity_analysis: "_6977.BoltedJointLoadCase"
    ) -> "_5521.BoltedJointMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BoltedJointMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_component(
        self: "Self", design_entity: "_2498.Component"
    ) -> "_5528.ComponentMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ComponentMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_component_load_case(
        self: "Self", design_entity_analysis: "_6984.ComponentLoadCase"
    ) -> "_5528.ComponentMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ComponentMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connector(
        self: "Self", design_entity: "_2501.Connector"
    ) -> "_5539.ConnectorMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConnectorMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.Connector)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connector_load_case(
        self: "Self", design_entity_analysis: "_6997.ConnectorLoadCase"
    ) -> "_5539.ConnectorMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConnectorMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConnectorLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_datum(
        self: "Self", design_entity: "_2502.Datum"
    ) -> "_5554.DatumMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.DatumMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.Datum)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_DATUM](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_datum_load_case(
        self: "Self", design_entity_analysis: "_7016.DatumLoadCase"
    ) -> "_5554.DatumMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.DatumMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.DatumLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_DATUM_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_external_cad_model(
        self: "Self", design_entity: "_2506.ExternalCADModel"
    ) -> "_5555.ExternalCADModelMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ExternalCADModelMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.ExternalCADModel)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_external_cad_model_load_case(
        self: "Self", design_entity_analysis: "_7030.ExternalCADModelLoadCase"
    ) -> "_5555.ExternalCADModelMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ExternalCADModelMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _EXTERNAL_CAD_MODEL_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_fe_part(
        self: "Self", design_entity: "_2507.FEPart"
    ) -> "_5559.FEPartMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FEPartMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.FEPart)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FE_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_fe_part_load_case(
        self: "Self", design_entity_analysis: "_7034.FEPartLoadCase"
    ) -> "_5559.FEPartMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FEPartMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.FEPartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FE_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly(
        self: "Self", design_entity: "_2508.FlexiblePinAssembly"
    ) -> "_5560.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FlexiblePinAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.FlexiblePinAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly_load_case(
        self: "Self", design_entity_analysis: "_7035.FlexiblePinAssemblyLoadCase"
    ) -> "_5560.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FlexiblePinAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_assembly(
        self: "Self", design_entity: "_2487.Assembly"
    ) -> "_5507.AssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_assembly_load_case(
        self: "Self", design_entity_analysis: "_6965.AssemblyLoadCase"
    ) -> "_5507.AssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.AssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model(
        self: "Self", design_entity: "_2509.GuideDxfModel"
    ) -> "_5565.GuideDxfModelMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.GuideDxfModelMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.GuideDxfModel)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model_load_case(
        self: "Self", design_entity_analysis: "_7043.GuideDxfModelLoadCase"
    ) -> "_5565.GuideDxfModelMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.GuideDxfModelMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mass_disc(
        self: "Self", design_entity: "_2516.MassDisc"
    ) -> "_5583.MassDiscMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MassDiscMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.MassDisc)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mass_disc_load_case(
        self: "Self", design_entity_analysis: "_7068.MassDiscLoadCase"
    ) -> "_5583.MassDiscMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MassDiscMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.MassDiscLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_measurement_component(
        self: "Self", design_entity: "_2517.MeasurementComponent"
    ) -> "_5587.MeasurementComponentMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MeasurementComponentMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.MeasurementComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_measurement_component_load_case(
        self: "Self", design_entity_analysis: "_7069.MeasurementComponentLoadCase"
    ) -> "_5587.MeasurementComponentMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MeasurementComponentMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _MEASUREMENT_COMPONENT_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mountable_component(
        self: "Self", design_entity: "_2520.MountableComponent"
    ) -> "_5590.MountableComponentMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MountableComponentMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.MountableComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mountable_component_load_case(
        self: "Self", design_entity_analysis: "_7073.MountableComponentLoadCase"
    ) -> "_5590.MountableComponentMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.MountableComponentMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _MOUNTABLE_COMPONENT_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_oil_seal(
        self: "Self", design_entity: "_2522.OilSeal"
    ) -> "_5592.OilSealMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.OilSealMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.OilSeal)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_oil_seal_load_case(
        self: "Self", design_entity_analysis: "_7075.OilSealLoadCase"
    ) -> "_5592.OilSealMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.OilSealMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.OilSealLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part(
        self: "Self", design_entity: "_2524.Part"
    ) -> "_5593.PartMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PartMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.Part)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_load_case(
        self: "Self", design_entity_analysis: "_7077.PartLoadCase"
    ) -> "_5593.PartMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PartMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planet_carrier(
        self: "Self", design_entity: "_2525.PlanetCarrier"
    ) -> "_5599.PlanetCarrierMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PlanetCarrierMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.PlanetCarrier)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planet_carrier_load_case(
        self: "Self", design_entity_analysis: "_7084.PlanetCarrierLoadCase"
    ) -> "_5599.PlanetCarrierMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PlanetCarrierMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_point_load(
        self: "Self", design_entity: "_2527.PointLoad"
    ) -> "_5600.PointLoadMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PointLoadMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.PointLoad)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_point_load_load_case(
        self: "Self", design_entity_analysis: "_7087.PointLoadLoadCase"
    ) -> "_5600.PointLoadMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PointLoadMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PointLoadLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_power_load(
        self: "Self", design_entity: "_2528.PowerLoad"
    ) -> "_5601.PowerLoadMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PowerLoadMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.PowerLoad)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_power_load_load_case(
        self: "Self", design_entity_analysis: "_7088.PowerLoadLoadCase"
    ) -> "_5601.PowerLoadMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PowerLoadMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_root_assembly(
        self: "Self", design_entity: "_2530.RootAssembly"
    ) -> "_5608.RootAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RootAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.RootAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_root_assembly_load_case(
        self: "Self", design_entity_analysis: "_7097.RootAssemblyLoadCase"
    ) -> "_5608.RootAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.RootAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_specialised_assembly(
        self: "Self", design_entity: "_2532.SpecialisedAssembly"
    ) -> "_5615.SpecialisedAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpecialisedAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.SpecialisedAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_specialised_assembly_load_case(
        self: "Self", design_entity_analysis: "_7101.SpecialisedAssemblyLoadCase"
    ) -> "_5615.SpecialisedAssemblyMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpecialisedAssemblyMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPECIALISED_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass(
        self: "Self", design_entity: "_2533.UnbalancedMass"
    ) -> "_5641.UnbalancedMassMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.UnbalancedMassMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.UnbalancedMass)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass_load_case(
        self: "Self", design_entity_analysis: "_7129.UnbalancedMassLoadCase"
    ) -> "_5641.UnbalancedMassMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.UnbalancedMassMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_virtual_component(
        self: "Self", design_entity: "_2535.VirtualComponent"
    ) -> "_5642.VirtualComponentMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.VirtualComponentMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.VirtualComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_virtual_component_load_case(
        self: "Self", design_entity_analysis: "_7130.VirtualComponentLoadCase"
    ) -> "_5642.VirtualComponentMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.VirtualComponentMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft(
        self: "Self", design_entity: "_2538.Shaft"
    ) -> "_5612.ShaftMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ShaftMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.shaft_model.Shaft)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_load_case(
        self: "Self", design_entity_analysis: "_7099.ShaftLoadCase"
    ) -> "_5612.ShaftMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ShaftMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ShaftLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear(
        self: "Self", design_entity: "_2577.ConceptGear"
    ) -> "_5533.ConceptGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConceptGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_load_case(
        self: "Self", design_entity_analysis: "_6988.ConceptGearLoadCase"
    ) -> "_5533.ConceptGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_set(
        self: "Self", design_entity: "_2578.ConceptGearSet"
    ) -> "_5534.ConceptGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConceptGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_set_load_case(
        self: "Self", design_entity_analysis: "_6990.ConceptGearSetLoadCase"
    ) -> "_5534.ConceptGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConceptGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear(
        self: "Self", design_entity: "_2584.FaceGear"
    ) -> "_5557.FaceGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FaceGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.FaceGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_load_case(
        self: "Self", design_entity_analysis: "_7031.FaceGearLoadCase"
    ) -> "_5557.FaceGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FaceGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.FaceGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_set(
        self: "Self", design_entity: "_2585.FaceGearSet"
    ) -> "_5558.FaceGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FaceGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.FaceGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7033.FaceGearSetLoadCase"
    ) -> "_5558.FaceGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.FaceGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear(
        self: "Self", design_entity: "_2569.AGMAGleasonConicalGear"
    ) -> "_5504.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_load_case(
        self: "Self", design_entity_analysis: "_6960.AGMAGleasonConicalGearLoadCase"
    ) -> "_5504.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set(
        self: "Self", design_entity: "_2570.AGMAGleasonConicalGearSet"
    ) -> "_5505.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set_load_case(
        self: "Self", design_entity_analysis: "_6962.AGMAGleasonConicalGearSetLoadCase"
    ) -> "_5505.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear(
        self: "Self", design_entity: "_2571.BevelDifferentialGear"
    ) -> "_5514.BevelDifferentialGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_load_case(
        self: "Self", design_entity_analysis: "_6969.BevelDifferentialGearLoadCase"
    ) -> "_5514.BevelDifferentialGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set(
        self: "Self", design_entity: "_2572.BevelDifferentialGearSet"
    ) -> "_5515.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set_load_case(
        self: "Self", design_entity_analysis: "_6971.BevelDifferentialGearSetLoadCase"
    ) -> "_5515.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear(
        self: "Self", design_entity: "_2573.BevelDifferentialPlanetGear"
    ) -> "_5516.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_PLANET_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear_load_case(
        self: "Self",
        design_entity_analysis: "_6972.BevelDifferentialPlanetGearLoadCase",
    ) -> "_5516.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear(
        self: "Self", design_entity: "_2574.BevelDifferentialSunGear"
    ) -> "_5517.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialSunGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear_load_case(
        self: "Self", design_entity_analysis: "_6973.BevelDifferentialSunGearLoadCase"
    ) -> "_5517.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelDifferentialSunGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear(
        self: "Self", design_entity: "_2575.BevelGear"
    ) -> "_5519.BevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_load_case(
        self: "Self", design_entity_analysis: "_6974.BevelGearLoadCase"
    ) -> "_5519.BevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set(
        self: "Self", design_entity: "_2576.BevelGearSet"
    ) -> "_5520.BevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.BevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set_load_case(
        self: "Self", design_entity_analysis: "_6976.BevelGearSetLoadCase"
    ) -> "_5520.BevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.BevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear(
        self: "Self", design_entity: "_2579.ConicalGear"
    ) -> "_5536.ConicalGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConicalGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_load_case(
        self: "Self", design_entity_analysis: "_6991.ConicalGearLoadCase"
    ) -> "_5536.ConicalGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConicalGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_set(
        self: "Self", design_entity: "_2580.ConicalGearSet"
    ) -> "_5537.ConicalGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConicalGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.ConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_set_load_case(
        self: "Self", design_entity_analysis: "_6995.ConicalGearSetLoadCase"
    ) -> "_5537.ConicalGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.ConicalGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear(
        self: "Self", design_entity: "_2581.CylindricalGear"
    ) -> "_5551.CylindricalGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CylindricalGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_load_case(
        self: "Self", design_entity_analysis: "_7008.CylindricalGearLoadCase"
    ) -> "_5551.CylindricalGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CylindricalGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set(
        self: "Self", design_entity: "_2582.CylindricalGearSet"
    ) -> "_5552.CylindricalGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CylindricalGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7012.CylindricalGearSetLoadCase"
    ) -> "_5552.CylindricalGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CylindricalGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear(
        self: "Self", design_entity: "_2583.CylindricalPlanetGear"
    ) -> "_5553.CylindricalPlanetGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CylindricalPlanetGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.CylindricalPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear_load_case(
        self: "Self", design_entity_analysis: "_7013.CylindricalPlanetGearLoadCase"
    ) -> "_5553.CylindricalPlanetGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.CylindricalPlanetGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear(
        self: "Self", design_entity: "_2586.Gear"
    ) -> "_5563.GearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.GearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.Gear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_load_case(
        self: "Self", design_entity_analysis: "_7037.GearLoadCase"
    ) -> "_5563.GearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.GearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.GearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_set(
        self: "Self", design_entity: "_2588.GearSet"
    ) -> "_5564.GearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.GearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.GearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7042.GearSetLoadCase"
    ) -> "_5564.GearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.GearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.GearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear(
        self: "Self", design_entity: "_2590.HypoidGear"
    ) -> "_5567.HypoidGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.HypoidGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.HypoidGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_load_case(
        self: "Self", design_entity_analysis: "_7052.HypoidGearLoadCase"
    ) -> "_5567.HypoidGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.HypoidGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set(
        self: "Self", design_entity: "_2591.HypoidGearSet"
    ) -> "_5568.HypoidGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.HypoidGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.HypoidGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7054.HypoidGearSetLoadCase"
    ) -> "_5568.HypoidGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.HypoidGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear(
        self: "Self", design_entity: "_2592.KlingelnbergCycloPalloidConicalGear"
    ) -> "_5575.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(
        self: "Self",
        design_entity_analysis: "_7059.KlingelnbergCycloPalloidConicalGearLoadCase",
    ) -> "_5575.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: "Self", design_entity: "_2593.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "_5576.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(
        self: "Self",
        design_entity_analysis: "_7061.KlingelnbergCycloPalloidConicalGearSetLoadCase",
    ) -> "_5576.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: "Self", design_entity: "_2594.KlingelnbergCycloPalloidHypoidGear"
    ) -> "_5578.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(
        self: "Self",
        design_entity_analysis: "_7062.KlingelnbergCycloPalloidHypoidGearLoadCase",
    ) -> "_5578.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: "Self", design_entity: "_2595.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "_5579.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
        self: "Self",
        design_entity_analysis: "_7064.KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    ) -> "_5579.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "Self", design_entity: "_2596.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "_5581.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
        self: "Self",
        design_entity_analysis: "_7065.KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    ) -> "_5581.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: "Self", design_entity: "_2597.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "_5582.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
        self: "Self",
        design_entity_analysis: "_7067.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    ) -> "_5582.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set(
        self: "Self", design_entity: "_2598.PlanetaryGearSet"
    ) -> "_5598.PlanetaryGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PlanetaryGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.PlanetaryGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7082.PlanetaryGearSetLoadCase"
    ) -> "_5598.PlanetaryGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.PlanetaryGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PLANETARY_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear(
        self: "Self", design_entity: "_2599.SpiralBevelGear"
    ) -> "_5617.SpiralBevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.SpiralBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_load_case(
        self: "Self", design_entity_analysis: "_7102.SpiralBevelGearLoadCase"
    ) -> "_5617.SpiralBevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set(
        self: "Self", design_entity: "_2600.SpiralBevelGearSet"
    ) -> "_5618.SpiralBevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.SpiralBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7104.SpiralBevelGearSetLoadCase"
    ) -> "_5618.SpiralBevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear(
        self: "Self", design_entity: "_2601.StraightBevelDiffGear"
    ) -> "_5624.StraightBevelDiffGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelDiffGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_load_case(
        self: "Self", design_entity_analysis: "_7108.StraightBevelDiffGearLoadCase"
    ) -> "_5624.StraightBevelDiffGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set(
        self: "Self", design_entity: "_2602.StraightBevelDiffGearSet"
    ) -> "_5625.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7110.StraightBevelDiffGearSetLoadCase"
    ) -> "_5625.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear(
        self: "Self", design_entity: "_2603.StraightBevelGear"
    ) -> "_5627.StraightBevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_load_case(
        self: "Self", design_entity_analysis: "_7111.StraightBevelGearLoadCase"
    ) -> "_5627.StraightBevelGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelGearMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set(
        self: "Self", design_entity: "_2604.StraightBevelGearSet"
    ) -> "_5628.StraightBevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7113.StraightBevelGearSetLoadCase"
    ) -> "_5628.StraightBevelGearSetMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelGearSetMultibodyDynamicsAnalysis

        Args:
            design_entity_analysis (mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear(
        self: "Self", design_entity: "_2605.StraightBevelPlanetGear"
    ) -> "_5629.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelPlanetGearMultibodyDynamicsAnalysis

        Args:
            design_entity (mastapy._private.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_MultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_MultibodyDynamicsAnalysis
        """
        return _Cast_MultibodyDynamicsAnalysis(self)
