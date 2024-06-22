"""HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7164,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_HYPOID_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2591
    from mastapy._private.system_model.analyses_and_results.static_loads import _7054
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2847,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7222,
        _7223,
        _7193,
        _7219,
        _7260,
        _7154,
        _7241,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar(
        "Self", bound="HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="HypoidGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HypoidGearSetAdvancedTimeSteppingAnalysisForModulation:
    """Special nested class for casting HypoidGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

    __parent__: "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"

    @property
    def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7164.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self.__parent__._cast(
            _7164.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7193.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7193,
        )

        return self.__parent__._cast(
            _7193.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7219.GearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7219,
        )

        return self.__parent__._cast(
            _7219.GearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7260.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7260,
        )

        return self.__parent__._cast(
            _7260.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7154.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7154,
        )

        return self.__parent__._cast(
            _7154.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7241.PartAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7241,
        )

        return self.__parent__._cast(
            _7241.PartAdvancedTimeSteppingAnalysisForModulation
        )

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
    def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
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
class HypoidGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7164.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
):
    """HypoidGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _HYPOID_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2591.HypoidGearSet":
        """mastapy._private.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_7054.HypoidGearSetLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: "Self",
    ) -> "_2847.HypoidGearSetSystemDeflection":
        """mastapy._private.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma_gleason_conical_gears_advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "List[_7222.HypoidGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.HypoidGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AGMAGleasonConicalGearsAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "List[_7222.HypoidGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.HypoidGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "List[_7223.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AGMAGleasonConicalMeshesAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "List[_7223.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
        """Cast to another type.

        Returns:
            _Cast_HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
        """
        return _Cast_HypoidGearSetAdvancedTimeSteppingAnalysisForModulation(self)
