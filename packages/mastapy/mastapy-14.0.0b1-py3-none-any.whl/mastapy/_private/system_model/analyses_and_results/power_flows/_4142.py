"""AssemblyPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.power_flows import _4135
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "AssemblyPowerFlow"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2487
    from mastapy._private.system_model.analyses_and_results.static_loads import _6965
    from mastapy._private.gears.analysis import _1265
    from mastapy._private.system_model.analyses_and_results.power_flows import (
        _4143,
        _4145,
        _4148,
        _4154,
        _4155,
        _4176,
        _4158,
        _4163,
        _4166,
        _4178,
        _4181,
        _4185,
        _4194,
        _4191,
        _4195,
        _4202,
        _4209,
        _4212,
        _4198,
        _4213,
        _4214,
        _4216,
        _4218,
        _4222,
        _4225,
        _4226,
        _4229,
        _4231,
        _4233,
        _4237,
        _4238,
        _4243,
        _4246,
        _4249,
        _4252,
        _4257,
        _4261,
        _4264,
        _4268,
        _4271,
        _4236,
        _4219,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="AssemblyPowerFlow")
    CastSelf = TypeVar("CastSelf", bound="AssemblyPowerFlow._Cast_AssemblyPowerFlow")


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AssemblyPowerFlow:
    """Special nested class for casting AssemblyPowerFlow to subclasses."""

    __parent__: "AssemblyPowerFlow"

    @property
    def abstract_assembly_power_flow(
        self: "CastSelf",
    ) -> "_4135.AbstractAssemblyPowerFlow":
        return self.__parent__._cast(_4135.AbstractAssemblyPowerFlow)

    @property
    def part_power_flow(self: "CastSelf") -> "_4219.PartPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4219

        return self.__parent__._cast(_4219.PartPowerFlow)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7713.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7713,
        )

        return self.__parent__._cast(_7713.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7710.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def root_assembly_power_flow(self: "CastSelf") -> "_4236.RootAssemblyPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4236

        return self.__parent__._cast(_4236.RootAssemblyPowerFlow)

    @property
    def assembly_power_flow(self: "CastSelf") -> "AssemblyPowerFlow":
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
class AssemblyPowerFlow(_4135.AbstractAssemblyPowerFlow):
    """AssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ASSEMBLY_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2487.Assembly":
        """mastapy._private.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_6965.AssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.AssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating_for_all_gear_sets(self: "Self") -> "_1265.GearSetGroupDutyCycle":
        """mastapy._private.gears.analysis.GearSetGroupDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingForAllGearSets

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearings(self: "Self") -> "List[_4143.BearingPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.BearingPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def belt_drives(self: "Self") -> "List[_4145.BeltDrivePowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.BeltDrivePowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gear_sets(
        self: "Self",
    ) -> "List[_4148.BevelDifferentialGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.BevelDifferentialGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolted_joints(self: "Self") -> "List[_4154.BoltedJointPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.BoltedJointPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolts(self: "Self") -> "List[_4155.BoltPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.BoltPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cv_ts(self: "Self") -> "List[_4176.CVTPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.CVTPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def clutches(self: "Self") -> "List[_4158.ClutchPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.ClutchPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_couplings(self: "Self") -> "List[_4163.ConceptCouplingPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.ConceptCouplingPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gear_sets(self: "Self") -> "List[_4166.ConceptGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.ConceptGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_assemblies(self: "Self") -> "List[_4178.CycloidalAssemblyPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.CycloidalAssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_discs(self: "Self") -> "List[_4181.CycloidalDiscPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.CycloidalDiscPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_sets(
        self: "Self",
    ) -> "List[_4185.CylindricalGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.CylindricalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts(self: "Self") -> "List[_4194.FEPartPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.FEPartPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gear_sets(self: "Self") -> "List[_4191.FaceGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.FaceGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flexible_pin_assemblies(
        self: "Self",
    ) -> "List[_4195.FlexiblePinAssemblyPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.FlexiblePinAssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gear_sets(self: "Self") -> "List[_4202.HypoidGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.HypoidGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(
        self: "Self",
    ) -> "List[_4209.KlingelnbergCycloPalloidHypoidGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(
        self: "Self",
    ) -> "List[_4212.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def loaded_gear_sets(self: "Self") -> "List[_4198.GearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.GearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mass_discs(self: "Self") -> "List[_4213.MassDiscPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.MassDiscPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def measurement_components(
        self: "Self",
    ) -> "List[_4214.MeasurementComponentPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.MeasurementComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def microphones(self: "Self") -> "List[_4216.MicrophonePowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.MicrophonePowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Microphones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def oil_seals(self: "Self") -> "List[_4218.OilSealPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.OilSealPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def part_to_part_shear_couplings(
        self: "Self",
    ) -> "List[_4222.PartToPartShearCouplingPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.PartToPartShearCouplingPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planet_carriers(self: "Self") -> "List[_4225.PlanetCarrierPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.PlanetCarrierPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_loads(self: "Self") -> "List[_4226.PointLoadPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.PointLoadPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_loads(self: "Self") -> "List[_4229.PowerLoadPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.PowerLoadPowerFlow]

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

    @property
    def ring_pins(self: "Self") -> "List[_4231.RingPinsPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.RingPinsPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rolling_ring_assemblies(
        self: "Self",
    ) -> "List[_4233.RollingRingAssemblyPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.RollingRingAssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_hub_connections(
        self: "Self",
    ) -> "List[_4237.ShaftHubConnectionPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.ShaftHubConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shafts(self: "Self") -> "List[_4238.ShaftPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.ShaftPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gear_sets(
        self: "Self",
    ) -> "List[_4243.SpiralBevelGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.SpiralBevelGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spring_dampers(self: "Self") -> "List[_4246.SpringDamperPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gear_sets(
        self: "Self",
    ) -> "List[_4249.StraightBevelDiffGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.StraightBevelDiffGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gear_sets(
        self: "Self",
    ) -> "List[_4252.StraightBevelGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.StraightBevelGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def synchronisers(self: "Self") -> "List[_4257.SynchroniserPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.SynchroniserPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def torque_converters(self: "Self") -> "List[_4261.TorqueConverterPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.TorqueConverterPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def unbalanced_masses(self: "Self") -> "List[_4264.UnbalancedMassPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.UnbalancedMassPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gear_sets(self: "Self") -> "List[_4268.WormGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.WormGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gear_sets(self: "Self") -> "List[_4271.ZerolBevelGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.ZerolBevelGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_AssemblyPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_AssemblyPowerFlow
        """
        return _Cast_AssemblyPowerFlow(self)
