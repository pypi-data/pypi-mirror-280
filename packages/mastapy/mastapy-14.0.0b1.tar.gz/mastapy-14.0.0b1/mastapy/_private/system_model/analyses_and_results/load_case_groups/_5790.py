"""AbstractStaticLoadCaseGroup"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.part_model import _2493, _2507, _2527, _2528
from mastapy._private.system_model.analyses_and_results.static_loads import (
    _6966,
    _7008,
    _7010,
    _7012,
    _7034,
    _7037,
    _7039,
    _7042,
    _7087,
    _7088,
)
from mastapy._private.system_model.part_model.gears import _2582, _2581, _2588, _2586
from mastapy._private.system_model.connections_and_sockets.gears import _2362, _2366
from mastapy._private.system_model.analyses_and_results.load_case_groups import _5789
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "AbstractStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
        _5803,
        _5806,
        _5807,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups import (
        _5788,
        _5793,
        _5794,
        _5797,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _6951,
        _6964,
    )
    from mastapy._private.system_model.analyses_and_results import (
        _2764,
        _2759,
        _2741,
        _2751,
        _2761,
        _2754,
        _2744,
        _2760,
        _2743,
        _2748,
        _2702,
    )

    Self = TypeVar("Self", bound="AbstractStaticLoadCaseGroup")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractStaticLoadCaseGroup",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractStaticLoadCaseGroup:
    """Special nested class for casting AbstractStaticLoadCaseGroup to subclasses."""

    __parent__: "AbstractStaticLoadCaseGroup"

    @property
    def abstract_load_case_group(self: "CastSelf") -> "_5789.AbstractLoadCaseGroup":
        return self.__parent__._cast(_5789.AbstractLoadCaseGroup)

    @property
    def abstract_design_state_load_case_group(
        self: "CastSelf",
    ) -> "_5788.AbstractDesignStateLoadCaseGroup":
        return self.__parent__._cast(_5788.AbstractDesignStateLoadCaseGroup)

    @property
    def design_state(self: "CastSelf") -> "_5793.DesignState":
        from mastapy._private.system_model.analyses_and_results.load_case_groups import (
            _5793,
        )

        return self.__parent__._cast(_5793.DesignState)

    @property
    def duty_cycle(self: "CastSelf") -> "_5794.DutyCycle":
        from mastapy._private.system_model.analyses_and_results.load_case_groups import (
            _5794,
        )

        return self.__parent__._cast(_5794.DutyCycle)

    @property
    def sub_group_in_single_design_state(
        self: "CastSelf",
    ) -> "_5797.SubGroupInSingleDesignState":
        from mastapy._private.system_model.analyses_and_results.load_case_groups import (
            _5797,
        )

        return self.__parent__._cast(_5797.SubGroupInSingleDesignState)

    @property
    def abstract_static_load_case_group(
        self: "CastSelf",
    ) -> "AbstractStaticLoadCaseGroup":
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
class AbstractStaticLoadCaseGroup(_5789.AbstractLoadCaseGroup):
    """AbstractStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_STATIC_LOAD_CASE_GROUP

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def max_number_of_load_cases_to_display(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.MaxNumberOfLoadCasesToDisplay

        if temp is None:
            return 0

        return temp

    @max_number_of_load_cases_to_display.setter
    @enforce_parameter_types
    def max_number_of_load_cases_to_display(self: "Self", value: "int") -> None:
        self.wrapped.MaxNumberOfLoadCasesToDisplay = (
            int(value) if value is not None else 0
        )

    @property
    def bearings(
        self: "Self",
    ) -> (
        "List[_5803.ComponentStaticLoadCaseGroup[_2493.Bearing, _6966.BearingLoadCase]]"
    ):
        """List[mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy._private.system_model.part_model.Bearing, mastapy._private.system_model.analyses_and_results.static_loads.BearingLoadCase]]

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
    def cylindrical_gear_sets(
        self: "Self",
    ) -> "List[_5806.GearSetStaticLoadCaseGroup[_2582.CylindricalGearSet, _2581.CylindricalGear, _7008.CylindricalGearLoadCase, _2362.CylindricalGearMesh, _7010.CylindricalGearMeshLoadCase, _7012.CylindricalGearSetLoadCase]]":
        """List[mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.GearSetStaticLoadCaseGroup[mastapy._private.system_model.part_model.gears.CylindricalGearSet, mastapy._private.system_model.part_model.gears.CylindricalGear, mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase, mastapy._private.system_model.connections_and_sockets.gears.CylindricalGearMesh, mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase, mastapy._private.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase]]

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
    def design_states(self: "Self") -> "List[_5788.AbstractDesignStateLoadCaseGroup]":
        """List[mastapy._private.system_model.analyses_and_results.load_case_groups.AbstractDesignStateLoadCaseGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignStates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts(
        self: "Self",
    ) -> "List[_5803.ComponentStaticLoadCaseGroup[_2507.FEPart, _7034.FEPartLoadCase]]":
        """List[mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy._private.system_model.part_model.FEPart, mastapy._private.system_model.analyses_and_results.static_loads.FEPartLoadCase]]

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
    def gear_sets(
        self: "Self",
    ) -> "List[_5806.GearSetStaticLoadCaseGroup[_2588.GearSet, _2586.Gear, _7037.GearLoadCase, _2366.GearMesh, _7039.GearMeshLoadCase, _7042.GearSetLoadCase]]":
        """List[mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.GearSetStaticLoadCaseGroup[mastapy._private.system_model.part_model.gears.GearSet, mastapy._private.system_model.part_model.gears.Gear, mastapy._private.system_model.analyses_and_results.static_loads.GearLoadCase, mastapy._private.system_model.connections_and_sockets.gears.GearMesh, mastapy._private.system_model.analyses_and_results.static_loads.GearMeshLoadCase, mastapy._private.system_model.analyses_and_results.static_loads.GearSetLoadCase]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def parts_with_excitations(self: "Self") -> "List[_5807.PartStaticLoadCaseGroup]":
        """List[mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.PartStaticLoadCaseGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartsWithExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_loads(
        self: "Self",
    ) -> "List[_5803.ComponentStaticLoadCaseGroup[_2527.PointLoad, _7087.PointLoadLoadCase]]":
        """List[mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy._private.system_model.part_model.PointLoad, mastapy._private.system_model.analyses_and_results.static_loads.PointLoadLoadCase]]

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
    def power_loads(
        self: "Self",
    ) -> "List[_5803.ComponentStaticLoadCaseGroup[_2528.PowerLoad, _7088.PowerLoadLoadCase]]":
        """List[mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy._private.system_model.part_model.PowerLoad, mastapy._private.system_model.analyses_and_results.static_loads.PowerLoadLoadCase]]

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
    def static_loads(self: "Self") -> "List[_6951.StaticLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.StaticLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def static_loads_limited_by_max_number_of_load_cases_to_display(
        self: "Self",
    ) -> "List[_6951.StaticLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.StaticLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def compound_system_deflection(
        self: "Self",
    ) -> "_2764.CompoundSystemDeflectionAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundSystemDeflectionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_power_flow(self: "Self") -> "_2759.CompoundPowerFlowAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundPowerFlowAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundPowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_advanced_system_deflection(
        self: "Self",
    ) -> "_2741.CompoundAdvancedSystemDeflectionAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundAdvancedSystemDeflectionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundAdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_harmonic_analysis(self: "Self") -> "_2751.CompoundHarmonicAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundHarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundHarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_steady_state_synchronous_response(
        self: "Self",
    ) -> "_2761.CompoundSteadyStateSynchronousResponseAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundSteadyStateSynchronousResponseAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_modal_analysis(self: "Self") -> "_2754.CompoundModalAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_critical_speed_analysis(
        self: "Self",
    ) -> "_2744.CompoundCriticalSpeedAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundCriticalSpeedAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_stability_analysis(self: "Self") -> "_2760.CompoundStabilityAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundStabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundStabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "_2743.CompoundAdvancedTimeSteppingAnalysisForModulation":
        """mastapy._private.system_model.analyses_and_results.CompoundAdvancedTimeSteppingAnalysisForModulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_dynamic_model_for_modal_analysis(
        self: "Self",
    ) -> "_2748.CompoundDynamicModelForModalAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundDynamicModelForModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundDynamicModelForModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def clear_user_specified_excitation_data_for_all_load_cases(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()

    def run_power_flow(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(
        self: "Self",
    ) -> None:
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    @enforce_parameter_types
    def analysis_of(
        self: "Self", analysis_type: "_6964.AnalysisType"
    ) -> "_2702.CompoundAnalysis":
        """mastapy._private.system_model.analyses_and_results.CompoundAnalysis

        Args:
            analysis_type (mastapy._private.system_model.analyses_and_results.static_loads.AnalysisType)
        """
        analysis_type = conversion.mp_to_pn_enum(
            analysis_type,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType",
        )
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractStaticLoadCaseGroup":
        """Cast to another type.

        Returns:
            _Cast_AbstractStaticLoadCaseGroup
        """
        return _Cast_AbstractStaticLoadCaseGroup(self)
