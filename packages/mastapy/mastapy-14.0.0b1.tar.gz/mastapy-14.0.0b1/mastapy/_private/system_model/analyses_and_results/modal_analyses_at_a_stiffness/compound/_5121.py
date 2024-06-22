"""BevelGearCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5109,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "BevelGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4989,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5116,
        _5119,
        _5120,
        _5206,
        _5212,
        _5215,
        _5218,
        _5219,
        _5233,
        _5137,
        _5163,
        _5184,
        _5130,
        _5186,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="BevelGearCompoundModalAnalysisAtAStiffness")
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelGearCompoundModalAnalysisAtAStiffness._Cast_BevelGearCompoundModalAnalysisAtAStiffness",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundModalAnalysisAtAStiffness",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelGearCompoundModalAnalysisAtAStiffness:
    """Special nested class for casting BevelGearCompoundModalAnalysisAtAStiffness to subclasses."""

    __parent__: "BevelGearCompoundModalAnalysisAtAStiffness"

    @property
    def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5109.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
        return self.__parent__._cast(
            _5109.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def conical_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5137.ConicalGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5137,
        )

        return self.__parent__._cast(_5137.ConicalGearCompoundModalAnalysisAtAStiffness)

    @property
    def gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5163.GearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5163,
        )

        return self.__parent__._cast(_5163.GearCompoundModalAnalysisAtAStiffness)

    @property
    def mountable_component_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5184.MountableComponentCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5184,
        )

        return self.__parent__._cast(
            _5184.MountableComponentCompoundModalAnalysisAtAStiffness
        )

    @property
    def component_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5130.ComponentCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5130,
        )

        return self.__parent__._cast(_5130.ComponentCompoundModalAnalysisAtAStiffness)

    @property
    def part_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5186.PartCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5186,
        )

        return self.__parent__._cast(_5186.PartCompoundModalAnalysisAtAStiffness)

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
    def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5116.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5116,
        )

        return self.__parent__._cast(
            _5116.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5119.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5119,
        )

        return self.__parent__._cast(
            _5119.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5120.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5120,
        )

        return self.__parent__._cast(
            _5120.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5206.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5206,
        )

        return self.__parent__._cast(
            _5206.SpiralBevelGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5212.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5212,
        )

        return self.__parent__._cast(
            _5212.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5215.StraightBevelGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5215,
        )

        return self.__parent__._cast(
            _5215.StraightBevelGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5218.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5218,
        )

        return self.__parent__._cast(
            _5218.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5219.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5219,
        )

        return self.__parent__._cast(
            _5219.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5233.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5233,
        )

        return self.__parent__._cast(
            _5233.ZerolBevelGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "BevelGearCompoundModalAnalysisAtAStiffness":
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
class BevelGearCompoundModalAnalysisAtAStiffness(
    _5109.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
):
    """BevelGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_4989.BevelGearModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4989.BevelGearModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_BevelGearCompoundModalAnalysisAtAStiffness":
        """Cast to another type.

        Returns:
            _Cast_BevelGearCompoundModalAnalysisAtAStiffness
        """
        return _Cast_BevelGearCompoundModalAnalysisAtAStiffness(self)
