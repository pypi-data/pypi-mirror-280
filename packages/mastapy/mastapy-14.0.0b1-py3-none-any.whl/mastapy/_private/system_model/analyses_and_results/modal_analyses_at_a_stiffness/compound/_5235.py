"""ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5123,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2610
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _5104,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5233,
        _5234,
        _5111,
        _5139,
        _5165,
        _5205,
        _5105,
        _5186,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundModalAnalysisAtAStiffness")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness:
    """Special nested class for casting ZerolBevelGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

    __parent__: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"

    @property
    def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5123.BevelGearSetCompoundModalAnalysisAtAStiffness":
        return self.__parent__._cast(
            _5123.BevelGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5111.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5111,
        )

        return self.__parent__._cast(
            _5111.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def conical_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5139.ConicalGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5139,
        )

        return self.__parent__._cast(
            _5139.ConicalGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5165.GearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5165,
        )

        return self.__parent__._cast(_5165.GearSetCompoundModalAnalysisAtAStiffness)

    @property
    def specialised_assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5205.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5205,
        )

        return self.__parent__._cast(
            _5205.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
        )

    @property
    def abstract_assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5105.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5105,
        )

        return self.__parent__._cast(
            _5105.AbstractAssemblyCompoundModalAnalysisAtAStiffness
        )

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
    def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
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
class ZerolBevelGearSetCompoundModalAnalysisAtAStiffness(
    _5123.BevelGearSetCompoundModalAnalysisAtAStiffness
):
    """ZerolBevelGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _ZEROL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2610.ZerolBevelGearSet":
        """mastapy._private.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2610.ZerolBevelGearSet":
        """mastapy._private.system_model.part_model.gears.ZerolBevelGearSet

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
    ) -> "List[_5104.ZerolBevelGearSetModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearSetModalAnalysisAtAStiffness]

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
    def zerol_bevel_gears_compound_modal_analysis_at_a_stiffness(
        self: "Self",
    ) -> "List[_5233.ZerolBevelGearCompoundModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.ZerolBevelGearCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_modal_analysis_at_a_stiffness(
        self: "Self",
    ) -> "List[_5234.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_5104.ZerolBevelGearSetModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearSetModalAnalysisAtAStiffness]

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
    ) -> "_Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
        """Cast to another type.

        Returns:
            _Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
        """
        return _Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness(self)
