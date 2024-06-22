"""FlexiblePinAssemblySystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections import _2891
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "FlexiblePinAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2508
    from mastapy._private.system_model.analyses_and_results.static_loads import _7035
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2889,
        _2825,
        _2781,
        _2886,
        _2861,
        _2868,
        _2828,
        _2768,
        _2870,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4195
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7712,
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="FlexiblePinAssemblySystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="FlexiblePinAssemblySystemDeflection._Cast_FlexiblePinAssemblySystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblySystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FlexiblePinAssemblySystemDeflection:
    """Special nested class for casting FlexiblePinAssemblySystemDeflection to subclasses."""

    __parent__: "FlexiblePinAssemblySystemDeflection"

    @property
    def specialised_assembly_system_deflection(
        self: "CastSelf",
    ) -> "_2891.SpecialisedAssemblySystemDeflection":
        return self.__parent__._cast(_2891.SpecialisedAssemblySystemDeflection)

    @property
    def abstract_assembly_system_deflection(
        self: "CastSelf",
    ) -> "_2768.AbstractAssemblySystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2768,
        )

        return self.__parent__._cast(_2768.AbstractAssemblySystemDeflection)

    @property
    def part_system_deflection(self: "CastSelf") -> "_2870.PartSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2870,
        )

        return self.__parent__._cast(_2870.PartSystemDeflection)

    @property
    def part_fe_analysis(self: "CastSelf") -> "_7712.PartFEAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7712,
        )

        return self.__parent__._cast(_7712.PartFEAnalysis)

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
    def flexible_pin_assembly_system_deflection(
        self: "CastSelf",
    ) -> "FlexiblePinAssemblySystemDeflection":
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
class FlexiblePinAssemblySystemDeflection(_2891.SpecialisedAssemblySystemDeflection):
    """FlexiblePinAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def pin_tangential_oscillation_amplitude(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinTangentialOscillationAmplitude

        if temp is None:
            return 0.0

        return temp

    @property
    def pin_tangential_oscillation_frequency(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinTangentialOscillationFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def assembly_design(self: "Self") -> "_2508.FlexiblePinAssembly":
        """mastapy._private.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_7035.FlexiblePinAssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def flexible_pin_shaft_details(self: "Self") -> "_2889.ShaftSystemDeflection":
        """mastapy._private.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinShaftDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pin_analysis(self: "Self") -> "_2889.ShaftSystemDeflection":
        """mastapy._private.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: "Self") -> "_4195.FlexiblePinAssemblyPowerFlow":
        """mastapy._private.system_model.analyses_and_results.power_flows.FlexiblePinAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def separate_gear_set_details(
        self: "Self",
    ) -> "_2825.CylindricalGearSetSystemDeflection":
        """mastapy._private.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparateGearSetDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spindle_analyses(self: "Self") -> "_2889.ShaftSystemDeflection":
        """mastapy._private.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpindleAnalyses

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_static_analyses(self: "Self") -> "List[_2781.BearingSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.BearingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingStaticAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flexible_pin_fit_details(
        self: "Self",
    ) -> "List[_2886.ShaftHubConnectionSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinFitDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def load_sharing_factor_reporters(
        self: "Self",
    ) -> "List[_2861.LoadSharingFactorReporter]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.LoadSharingFactorReporter]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactorReporters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def observed_pin_stiffness_reporters(
        self: "Self",
    ) -> "List[_2868.ObservedPinStiffnessReporter]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.ObservedPinStiffnessReporter]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ObservedPinStiffnessReporters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def pin_spindle_fit_analyses(
        self: "Self",
    ) -> "List[_2886.ShaftHubConnectionSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinSpindleFitAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planet_gear_system_deflections(
        self: "Self",
    ) -> "List[_2828.CylindricalGearSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetGearSystemDeflections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_FlexiblePinAssemblySystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_FlexiblePinAssemblySystemDeflection
        """
        return _Cast_FlexiblePinAssemblySystemDeflection(self)
