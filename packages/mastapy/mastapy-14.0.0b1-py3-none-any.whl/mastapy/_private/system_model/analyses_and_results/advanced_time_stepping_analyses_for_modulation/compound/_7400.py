"""StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7309,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2602
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7269,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7398,
        _7399,
        _7297,
        _7325,
        _7351,
        _7391,
        _7291,
        _7372,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self",
        bound="StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
    """Special nested class for casting StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

    __parent__: "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"

    @property
    def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7309.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self.__parent__._cast(
            _7309.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7297.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7297,
        )

        return self.__parent__._cast(
            _7297.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7325.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7325,
        )

        return self.__parent__._cast(
            _7325.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7351.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7351,
        )

        return self.__parent__._cast(
            _7351.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7391.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7391,
        )

        return self.__parent__._cast(
            _7391.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7291.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7291,
        )

        return self.__parent__._cast(
            _7291.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7372.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7372,
        )

        return self.__parent__._cast(
            _7372.PartCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7711.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7711,
        )

        return self.__parent__._cast(_7711.PartCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7708.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7708,
        )

        return self.__parent__._cast(_7708.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
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
class StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7309.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2602.StraightBevelDiffGearSet":
        """mastapy._private.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2602.StraightBevelDiffGearSet":
        """mastapy._private.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> (
        "List[_7269.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gears_compound_advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "List[_7398.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.StraightBevelDiffGearsCompoundAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "List[_7399.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.StraightBevelDiffMeshesCompoundAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> (
        "List[_7269.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        """
        return _Cast_StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
