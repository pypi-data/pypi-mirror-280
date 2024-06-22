"""HarmonicAnalysis"""
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
_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "HarmonicAnalysis"
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
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5836,
        _5847,
        _5947,
        _5963,
        _5957,
        _5958,
        _5970,
        _5972,
        _5973,
        _5975,
        _5853,
        _5855,
        _5932,
        _5923,
        _5922,
        _5819,
        _5832,
        _5831,
        _5838,
        _5837,
        _5849,
        _5848,
        _5851,
        _5852,
        _5930,
        _5939,
        _5936,
        _5934,
        _5949,
        _5948,
        _5960,
        _5959,
        _5961,
        _5962,
        _5964,
        _5965,
        _5966,
        _5940,
        _5850,
        _5818,
        _5833,
        _5845,
        _5904,
        _5925,
        _5935,
        _5812,
        _5821,
        _5840,
        _5878,
        _5952,
        _5826,
        _5843,
        _5814,
        _5858,
        _5902,
        _5906,
        _5909,
        _5912,
        _5945,
        _5955,
        _5971,
        _5974,
        _5885,
        _5854,
        _5856,
        _5933,
        _5921,
        _5830,
        _5810,
        _5917,
        _5916,
        _5808,
        _5811,
        _5817,
        _5829,
        _5828,
        _5835,
        _5846,
        _5861,
        _5876,
        _5880,
        _5881,
        _5816,
        _5890,
        _5914,
        _5915,
        _5918,
        _5919,
        _5920,
        _5927,
        _5928,
        _5929,
        _5937,
        _5942,
        _5968,
        _5969,
        _5938,
        _5839,
        _5841,
        _5877,
        _5879,
        _5813,
        _5815,
        _5820,
        _5822,
        _5823,
        _5824,
        _5825,
        _5827,
        _5842,
        _5844,
        _5857,
        _5859,
        _5860,
        _5883,
        _5888,
        _5901,
        _5903,
        _5905,
        _5907,
        _5908,
        _5910,
        _5911,
        _5913,
        _5926,
        _5944,
        _5946,
        _5951,
        _5953,
        _5954,
        _5956,
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

    Self = TypeVar("Self", bound="HarmonicAnalysis")
    CastSelf = TypeVar("CastSelf", bound="HarmonicAnalysis._Cast_HarmonicAnalysis")


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HarmonicAnalysis:
    """Special nested class for casting HarmonicAnalysis to subclasses."""

    __parent__: "HarmonicAnalysis"

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
    def harmonic_analysis(self: "CastSelf") -> "HarmonicAnalysis":
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
class HarmonicAnalysis(_2703.SingleAnalysis):
    """HarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HARMONIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @enforce_parameter_types
    def results_for_concept_coupling_connection_load_case(
        self: "Self", design_entity_analysis: "_6985.ConceptCouplingConnectionLoadCase"
    ) -> "_5836.ConceptCouplingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingConnectionHarmonicAnalysis

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
    ) -> "_5847.CouplingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CouplingConnectionHarmonicAnalysis

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
    ) -> "_5847.CouplingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CouplingConnectionHarmonicAnalysis

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
    ) -> "_5947.SpringDamperConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpringDamperConnectionHarmonicAnalysis

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
    ) -> "_5947.SpringDamperConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpringDamperConnectionHarmonicAnalysis

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
    ) -> "_5963.TorqueConverterConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.TorqueConverterConnectionHarmonicAnalysis

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
    ) -> "_5963.TorqueConverterConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.TorqueConverterConnectionHarmonicAnalysis

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
    ) -> "_5957.StraightBevelPlanetGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelPlanetGearHarmonicAnalysis

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
    ) -> "_5958.StraightBevelSunGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelSunGearHarmonicAnalysis

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
    ) -> "_5958.StraightBevelSunGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelSunGearHarmonicAnalysis

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
    ) -> "_5970.WormGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.WormGearHarmonicAnalysis

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
    ) -> "_5970.WormGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.WormGearHarmonicAnalysis

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
    ) -> "_5972.WormGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.WormGearSetHarmonicAnalysis

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
    ) -> "_5972.WormGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.WormGearSetHarmonicAnalysis

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
    ) -> "_5973.ZerolBevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearHarmonicAnalysis

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
    ) -> "_5973.ZerolBevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearHarmonicAnalysis

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
    ) -> "_5975.ZerolBevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearSetHarmonicAnalysis

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
    ) -> "_5975.ZerolBevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearSetHarmonicAnalysis

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
    ) -> "_5853.CycloidalAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CycloidalAssemblyHarmonicAnalysis

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
    ) -> "_5853.CycloidalAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CycloidalAssemblyHarmonicAnalysis

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
    ) -> "_5855.CycloidalDiscHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscHarmonicAnalysis

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
    ) -> "_5855.CycloidalDiscHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscHarmonicAnalysis

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
    ) -> "_5932.RingPinsHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RingPinsHarmonicAnalysis

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
    ) -> "_5932.RingPinsHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RingPinsHarmonicAnalysis

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
    ) -> "_5923.PartToPartShearCouplingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingHarmonicAnalysis

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
    ) -> "_5923.PartToPartShearCouplingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingHarmonicAnalysis

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
    ) -> "_5922.PartToPartShearCouplingHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingHalfHarmonicAnalysis

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
    ) -> "_5922.PartToPartShearCouplingHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingHalfHarmonicAnalysis

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
    ) -> "_5819.BeltDriveHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BeltDriveHarmonicAnalysis

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
    ) -> "_5819.BeltDriveHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BeltDriveHarmonicAnalysis

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
    ) -> "_5832.ClutchHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ClutchHarmonicAnalysis

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
    ) -> "_5832.ClutchHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ClutchHarmonicAnalysis

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
    ) -> "_5831.ClutchHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ClutchHalfHarmonicAnalysis

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
    ) -> "_5831.ClutchHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ClutchHalfHarmonicAnalysis

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
    ) -> "_5838.ConceptCouplingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHarmonicAnalysis

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
    ) -> "_5838.ConceptCouplingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHarmonicAnalysis

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
    ) -> "_5837.ConceptCouplingHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHalfHarmonicAnalysis

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
    ) -> "_5837.ConceptCouplingHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHalfHarmonicAnalysis

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
    ) -> "_5849.CouplingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CouplingHarmonicAnalysis

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
    ) -> "_5849.CouplingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CouplingHarmonicAnalysis

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
    ) -> "_5848.CouplingHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis

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
    ) -> "_5848.CouplingHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis

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
    ) -> "_5851.CVTHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CVTHarmonicAnalysis

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
    ) -> "_5851.CVTHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CVTHarmonicAnalysis

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
    ) -> "_5852.CVTPulleyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CVTPulleyHarmonicAnalysis

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
    ) -> "_5852.CVTPulleyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CVTPulleyHarmonicAnalysis

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
    ) -> "_5930.PulleyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PulleyHarmonicAnalysis

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
    ) -> "_5930.PulleyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PulleyHarmonicAnalysis

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
    ) -> "_5939.ShaftHubConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ShaftHubConnectionHarmonicAnalysis

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
    ) -> "_5939.ShaftHubConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ShaftHubConnectionHarmonicAnalysis

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
    ) -> "_5936.RollingRingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RollingRingHarmonicAnalysis

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
    ) -> "_5936.RollingRingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RollingRingHarmonicAnalysis

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
    ) -> "_5934.RollingRingAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RollingRingAssemblyHarmonicAnalysis

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
    ) -> "_5934.RollingRingAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RollingRingAssemblyHarmonicAnalysis

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
    ) -> "_5949.SpringDamperHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpringDamperHarmonicAnalysis

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
    ) -> "_5949.SpringDamperHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpringDamperHarmonicAnalysis

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
    ) -> "_5948.SpringDamperHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpringDamperHalfHarmonicAnalysis

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
    ) -> "_5948.SpringDamperHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpringDamperHalfHarmonicAnalysis

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
    ) -> "_5960.SynchroniserHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SynchroniserHarmonicAnalysis

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
    ) -> "_5960.SynchroniserHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SynchroniserHarmonicAnalysis

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
    ) -> "_5959.SynchroniserHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SynchroniserHalfHarmonicAnalysis

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
    ) -> "_5959.SynchroniserHalfHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SynchroniserHalfHarmonicAnalysis

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
    ) -> "_5961.SynchroniserPartHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SynchroniserPartHarmonicAnalysis

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
    ) -> "_5961.SynchroniserPartHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SynchroniserPartHarmonicAnalysis

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
    ) -> "_5962.SynchroniserSleeveHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SynchroniserSleeveHarmonicAnalysis

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
    ) -> "_5962.SynchroniserSleeveHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SynchroniserSleeveHarmonicAnalysis

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
    ) -> "_5964.TorqueConverterHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.TorqueConverterHarmonicAnalysis

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
    ) -> "_5964.TorqueConverterHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.TorqueConverterHarmonicAnalysis

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
    ) -> "_5965.TorqueConverterPumpHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.TorqueConverterPumpHarmonicAnalysis

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
    ) -> "_5965.TorqueConverterPumpHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.TorqueConverterPumpHarmonicAnalysis

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
    ) -> "_5966.TorqueConverterTurbineHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.TorqueConverterTurbineHarmonicAnalysis

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
    ) -> "_5966.TorqueConverterTurbineHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.TorqueConverterTurbineHarmonicAnalysis

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
    ) -> "_5940.ShaftToMountableComponentConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ShaftToMountableComponentConnectionHarmonicAnalysis

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
    ) -> "_5940.ShaftToMountableComponentConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ShaftToMountableComponentConnectionHarmonicAnalysis

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
    ) -> "_5850.CVTBeltConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CVTBeltConnectionHarmonicAnalysis

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
    ) -> "_5850.CVTBeltConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CVTBeltConnectionHarmonicAnalysis

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
    ) -> "_5818.BeltConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BeltConnectionHarmonicAnalysis

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
    ) -> "_5818.BeltConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BeltConnectionHarmonicAnalysis

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
    ) -> "_5833.CoaxialConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CoaxialConnectionHarmonicAnalysis

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
    ) -> "_5833.CoaxialConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CoaxialConnectionHarmonicAnalysis

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
    ) -> "_5845.ConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConnectionHarmonicAnalysis

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
    ) -> "_5845.ConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConnectionHarmonicAnalysis

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
    ) -> "_5904.InterMountableComponentConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.InterMountableComponentConnectionHarmonicAnalysis

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
    ) -> "_5904.InterMountableComponentConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.InterMountableComponentConnectionHarmonicAnalysis

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
    ) -> "_5925.PlanetaryConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PlanetaryConnectionHarmonicAnalysis

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
    ) -> "_5925.PlanetaryConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PlanetaryConnectionHarmonicAnalysis

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
    ) -> "_5935.RollingRingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RollingRingConnectionHarmonicAnalysis

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
    ) -> "_5935.RollingRingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RollingRingConnectionHarmonicAnalysis

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
    ) -> "_5812.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractShaftToMountableComponentConnectionHarmonicAnalysis

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
    ) -> "_5812.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractShaftToMountableComponentConnectionHarmonicAnalysis

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
    ) -> "_5821.BevelDifferentialGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearMeshHarmonicAnalysis

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
    ) -> "_5821.BevelDifferentialGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearMeshHarmonicAnalysis

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
    ) -> "_5840.ConceptGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptGearMeshHarmonicAnalysis

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
    ) -> "_5840.ConceptGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptGearMeshHarmonicAnalysis

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
    ) -> "_5878.FaceGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FaceGearMeshHarmonicAnalysis

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
    ) -> "_5878.FaceGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FaceGearMeshHarmonicAnalysis

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
    ) -> "_5952.StraightBevelDiffGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearMeshHarmonicAnalysis

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
    ) -> "_5952.StraightBevelDiffGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearMeshHarmonicAnalysis

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
    ) -> "_5826.BevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelGearMeshHarmonicAnalysis

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
    ) -> "_5826.BevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelGearMeshHarmonicAnalysis

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
    ) -> "_5843.ConicalGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis

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
    ) -> "_5843.ConicalGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis

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
    ) -> "_5814.AGMAGleasonConicalGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearMeshHarmonicAnalysis

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
    ) -> "_5814.AGMAGleasonConicalGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearMeshHarmonicAnalysis

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
    ) -> "_5858.CylindricalGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CylindricalGearMeshHarmonicAnalysis

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
    ) -> "_5858.CylindricalGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CylindricalGearMeshHarmonicAnalysis

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
    ) -> "_5902.HypoidGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.HypoidGearMeshHarmonicAnalysis

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
    ) -> "_5902.HypoidGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.HypoidGearMeshHarmonicAnalysis

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
    ) -> "_5906.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis

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
    ) -> "_5906.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis

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
    ) -> "_5909.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis

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
    ) -> "_5909.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis

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
    ) -> "_5912.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis

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
    ) -> "_5912.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis

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
    ) -> "_5945.SpiralBevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearMeshHarmonicAnalysis

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
    ) -> "_5945.SpiralBevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearMeshHarmonicAnalysis

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
    ) -> "_5955.StraightBevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearMeshHarmonicAnalysis

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
    ) -> "_5955.StraightBevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearMeshHarmonicAnalysis

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
    ) -> "_5971.WormGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis

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
    ) -> "_5971.WormGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis

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
    ) -> "_5974.ZerolBevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearMeshHarmonicAnalysis

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
    ) -> "_5974.ZerolBevelGearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearMeshHarmonicAnalysis

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
    ) -> "_5885.GearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis

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
    ) -> "_5885.GearMeshHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis

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
    ) -> "_5854.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis

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
    ) -> "_5854.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis

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
    ) -> "_5856.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis

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
    ) -> "_5856.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis

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
    ) -> "_5933.RingPinsToDiscConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RingPinsToDiscConnectionHarmonicAnalysis

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
    ) -> "_5933.RingPinsToDiscConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RingPinsToDiscConnectionHarmonicAnalysis

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
    ) -> "_5921.PartToPartShearCouplingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingConnectionHarmonicAnalysis

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
    ) -> "_5921.PartToPartShearCouplingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingConnectionHarmonicAnalysis

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
    ) -> "_5830.ClutchConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ClutchConnectionHarmonicAnalysis

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
    ) -> "_5830.ClutchConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ClutchConnectionHarmonicAnalysis

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
    ) -> "_5836.ConceptCouplingConnectionHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingConnectionHarmonicAnalysis

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
    ) -> "_5810.AbstractShaftHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractShaftHarmonicAnalysis

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
    ) -> "_5810.AbstractShaftHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractShaftHarmonicAnalysis

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
    ) -> "_5917.MicrophoneHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MicrophoneHarmonicAnalysis

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
    ) -> "_5917.MicrophoneHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MicrophoneHarmonicAnalysis

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
    ) -> "_5916.MicrophoneArrayHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MicrophoneArrayHarmonicAnalysis

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
    ) -> "_5916.MicrophoneArrayHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MicrophoneArrayHarmonicAnalysis

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
    ) -> "_5808.AbstractAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractAssemblyHarmonicAnalysis

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
    ) -> "_5808.AbstractAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractAssemblyHarmonicAnalysis

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
    ) -> "_5811.AbstractShaftOrHousingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractShaftOrHousingHarmonicAnalysis

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
    ) -> "_5811.AbstractShaftOrHousingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractShaftOrHousingHarmonicAnalysis

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
    ) -> "_5817.BearingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BearingHarmonicAnalysis

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
    ) -> "_5817.BearingHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BearingHarmonicAnalysis

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
    ) -> "_5829.BoltHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BoltHarmonicAnalysis

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
    ) -> "_5829.BoltHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BoltHarmonicAnalysis

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
    ) -> "_5828.BoltedJointHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BoltedJointHarmonicAnalysis

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
    ) -> "_5828.BoltedJointHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BoltedJointHarmonicAnalysis

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
    ) -> "_5835.ComponentHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ComponentHarmonicAnalysis

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
    ) -> "_5835.ComponentHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ComponentHarmonicAnalysis

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
    ) -> "_5846.ConnectorHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConnectorHarmonicAnalysis

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
    ) -> "_5846.ConnectorHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConnectorHarmonicAnalysis

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
    ) -> "_5861.DatumHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.DatumHarmonicAnalysis

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
    ) -> "_5861.DatumHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.DatumHarmonicAnalysis

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
    ) -> "_5876.ExternalCADModelHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ExternalCADModelHarmonicAnalysis

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
    ) -> "_5876.ExternalCADModelHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ExternalCADModelHarmonicAnalysis

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
    ) -> "_5880.FEPartHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FEPartHarmonicAnalysis

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
    ) -> "_5880.FEPartHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FEPartHarmonicAnalysis

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
    ) -> "_5881.FlexiblePinAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FlexiblePinAssemblyHarmonicAnalysis

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
    ) -> "_5881.FlexiblePinAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FlexiblePinAssemblyHarmonicAnalysis

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
    ) -> "_5816.AssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AssemblyHarmonicAnalysis

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
    ) -> "_5816.AssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AssemblyHarmonicAnalysis

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
    ) -> "_5890.GuideDxfModelHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.GuideDxfModelHarmonicAnalysis

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
    ) -> "_5890.GuideDxfModelHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.GuideDxfModelHarmonicAnalysis

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
    ) -> "_5914.MassDiscHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MassDiscHarmonicAnalysis

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
    ) -> "_5914.MassDiscHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MassDiscHarmonicAnalysis

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
    ) -> "_5915.MeasurementComponentHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MeasurementComponentHarmonicAnalysis

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
    ) -> "_5915.MeasurementComponentHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MeasurementComponentHarmonicAnalysis

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
    ) -> "_5918.MountableComponentHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MountableComponentHarmonicAnalysis

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
    ) -> "_5918.MountableComponentHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.MountableComponentHarmonicAnalysis

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
    ) -> "_5919.OilSealHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.OilSealHarmonicAnalysis

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
    ) -> "_5919.OilSealHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.OilSealHarmonicAnalysis

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
    ) -> "_5920.PartHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PartHarmonicAnalysis

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
    ) -> "_5920.PartHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PartHarmonicAnalysis

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
    ) -> "_5927.PlanetCarrierHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PlanetCarrierHarmonicAnalysis

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
    ) -> "_5927.PlanetCarrierHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PlanetCarrierHarmonicAnalysis

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
    ) -> "_5928.PointLoadHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PointLoadHarmonicAnalysis

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
    ) -> "_5928.PointLoadHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PointLoadHarmonicAnalysis

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
    ) -> "_5929.PowerLoadHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PowerLoadHarmonicAnalysis

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
    ) -> "_5929.PowerLoadHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PowerLoadHarmonicAnalysis

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
    ) -> "_5937.RootAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RootAssemblyHarmonicAnalysis

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
    ) -> "_5937.RootAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.RootAssemblyHarmonicAnalysis

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
    ) -> "_5942.SpecialisedAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpecialisedAssemblyHarmonicAnalysis

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
    ) -> "_5942.SpecialisedAssemblyHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpecialisedAssemblyHarmonicAnalysis

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
    ) -> "_5968.UnbalancedMassHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.UnbalancedMassHarmonicAnalysis

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
    ) -> "_5968.UnbalancedMassHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.UnbalancedMassHarmonicAnalysis

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
    ) -> "_5969.VirtualComponentHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.VirtualComponentHarmonicAnalysis

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
    ) -> "_5969.VirtualComponentHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.VirtualComponentHarmonicAnalysis

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
    ) -> "_5938.ShaftHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ShaftHarmonicAnalysis

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
    ) -> "_5938.ShaftHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ShaftHarmonicAnalysis

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
    ) -> "_5839.ConceptGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptGearHarmonicAnalysis

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
    ) -> "_5839.ConceptGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptGearHarmonicAnalysis

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
    ) -> "_5841.ConceptGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptGearSetHarmonicAnalysis

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
    ) -> "_5841.ConceptGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConceptGearSetHarmonicAnalysis

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
    ) -> "_5877.FaceGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FaceGearHarmonicAnalysis

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
    ) -> "_5877.FaceGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FaceGearHarmonicAnalysis

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
    ) -> "_5879.FaceGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FaceGearSetHarmonicAnalysis

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
    ) -> "_5879.FaceGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.FaceGearSetHarmonicAnalysis

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
    ) -> "_5813.AGMAGleasonConicalGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearHarmonicAnalysis

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
    ) -> "_5813.AGMAGleasonConicalGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearHarmonicAnalysis

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
    ) -> "_5815.AGMAGleasonConicalGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearSetHarmonicAnalysis

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
    ) -> "_5815.AGMAGleasonConicalGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearSetHarmonicAnalysis

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
    ) -> "_5820.BevelDifferentialGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearHarmonicAnalysis

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
    ) -> "_5820.BevelDifferentialGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearHarmonicAnalysis

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
    ) -> "_5822.BevelDifferentialGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearSetHarmonicAnalysis

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
    ) -> "_5822.BevelDifferentialGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearSetHarmonicAnalysis

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
    ) -> "_5823.BevelDifferentialPlanetGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialPlanetGearHarmonicAnalysis

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
    ) -> "_5823.BevelDifferentialPlanetGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialPlanetGearHarmonicAnalysis

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
    ) -> "_5824.BevelDifferentialSunGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialSunGearHarmonicAnalysis

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
    ) -> "_5824.BevelDifferentialSunGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialSunGearHarmonicAnalysis

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
    ) -> "_5825.BevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelGearHarmonicAnalysis

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
    ) -> "_5825.BevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelGearHarmonicAnalysis

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
    ) -> "_5827.BevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelGearSetHarmonicAnalysis

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
    ) -> "_5827.BevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.BevelGearSetHarmonicAnalysis

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
    ) -> "_5842.ConicalGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis

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
    ) -> "_5842.ConicalGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis

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
    ) -> "_5844.ConicalGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConicalGearSetHarmonicAnalysis

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
    ) -> "_5844.ConicalGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.ConicalGearSetHarmonicAnalysis

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
    ) -> "_5857.CylindricalGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CylindricalGearHarmonicAnalysis

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
    ) -> "_5857.CylindricalGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CylindricalGearHarmonicAnalysis

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
    ) -> "_5859.CylindricalGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CylindricalGearSetHarmonicAnalysis

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
    ) -> "_5859.CylindricalGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CylindricalGearSetHarmonicAnalysis

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
    ) -> "_5860.CylindricalPlanetGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CylindricalPlanetGearHarmonicAnalysis

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
    ) -> "_5860.CylindricalPlanetGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.CylindricalPlanetGearHarmonicAnalysis

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
    ) -> "_5883.GearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis

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
    ) -> "_5883.GearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis

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
    ) -> "_5888.GearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.GearSetHarmonicAnalysis

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
    ) -> "_5888.GearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.GearSetHarmonicAnalysis

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
    ) -> "_5901.HypoidGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.HypoidGearHarmonicAnalysis

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
    ) -> "_5901.HypoidGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.HypoidGearHarmonicAnalysis

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
    ) -> "_5903.HypoidGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.HypoidGearSetHarmonicAnalysis

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
    ) -> "_5903.HypoidGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.HypoidGearSetHarmonicAnalysis

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
    ) -> "_5905.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis

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
    ) -> "_5905.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis

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
    ) -> "_5907.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis

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
    ) -> "_5907.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis

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
    ) -> "_5908.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis

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
    ) -> "_5908.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis

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
    ) -> "_5910.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis

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
    ) -> "_5910.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis

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
    ) -> "_5911.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis

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
    ) -> "_5911.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis

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
    ) -> "_5913.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis

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
    ) -> "_5913.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis

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
    ) -> "_5926.PlanetaryGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PlanetaryGearSetHarmonicAnalysis

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
    ) -> "_5926.PlanetaryGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.PlanetaryGearSetHarmonicAnalysis

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
    ) -> "_5944.SpiralBevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearHarmonicAnalysis

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
    ) -> "_5944.SpiralBevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearHarmonicAnalysis

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
    ) -> "_5946.SpiralBevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearSetHarmonicAnalysis

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
    ) -> "_5946.SpiralBevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearSetHarmonicAnalysis

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
    ) -> "_5951.StraightBevelDiffGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearHarmonicAnalysis

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
    ) -> "_5951.StraightBevelDiffGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearHarmonicAnalysis

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
    ) -> "_5953.StraightBevelDiffGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearSetHarmonicAnalysis

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
    ) -> "_5953.StraightBevelDiffGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearSetHarmonicAnalysis

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
    ) -> "_5954.StraightBevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearHarmonicAnalysis

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
    ) -> "_5954.StraightBevelGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearHarmonicAnalysis

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
    ) -> "_5956.StraightBevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearSetHarmonicAnalysis

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
    ) -> "_5956.StraightBevelGearSetHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearSetHarmonicAnalysis

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
    ) -> "_5957.StraightBevelPlanetGearHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.StraightBevelPlanetGearHarmonicAnalysis

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
    def cast_to(self: "Self") -> "_Cast_HarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_HarmonicAnalysis
        """
        return _Cast_HarmonicAnalysis(self)
