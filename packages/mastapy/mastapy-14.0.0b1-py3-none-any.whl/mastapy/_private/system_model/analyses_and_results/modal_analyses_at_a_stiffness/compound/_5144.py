"""CouplingHalfCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5184,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _5010,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5128,
        _5133,
        _5147,
        _5189,
        _5195,
        _5199,
        _5211,
        _5221,
        _5222,
        _5223,
        _5226,
        _5227,
        _5130,
        _5186,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysisAtAStiffness")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysisAtAStiffness",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfCompoundModalAnalysisAtAStiffness:
    """Special nested class for casting CouplingHalfCompoundModalAnalysisAtAStiffness to subclasses."""

    __parent__: "CouplingHalfCompoundModalAnalysisAtAStiffness"

    @property
    def mountable_component_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5184.MountableComponentCompoundModalAnalysisAtAStiffness":
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
    def clutch_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5128.ClutchHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5128,
        )

        return self.__parent__._cast(_5128.ClutchHalfCompoundModalAnalysisAtAStiffness)

    @property
    def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5133.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5133,
        )

        return self.__parent__._cast(
            _5133.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def cvt_pulley_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5147.CVTPulleyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5147,
        )

        return self.__parent__._cast(_5147.CVTPulleyCompoundModalAnalysisAtAStiffness)

    @property
    def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5189.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5189,
        )

        return self.__parent__._cast(
            _5189.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def pulley_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5195.PulleyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5195,
        )

        return self.__parent__._cast(_5195.PulleyCompoundModalAnalysisAtAStiffness)

    @property
    def rolling_ring_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5199.RollingRingCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5199,
        )

        return self.__parent__._cast(_5199.RollingRingCompoundModalAnalysisAtAStiffness)

    @property
    def spring_damper_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5211.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5211,
        )

        return self.__parent__._cast(
            _5211.SpringDamperHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def synchroniser_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5221.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5221,
        )

        return self.__parent__._cast(
            _5221.SynchroniserHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def synchroniser_part_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5222.SynchroniserPartCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5222,
        )

        return self.__parent__._cast(
            _5222.SynchroniserPartCompoundModalAnalysisAtAStiffness
        )

    @property
    def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5223.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5223,
        )

        return self.__parent__._cast(
            _5223.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
        )

    @property
    def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5226.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5226,
        )

        return self.__parent__._cast(
            _5226.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
        )

    @property
    def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5227.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5227,
        )

        return self.__parent__._cast(
            _5227.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
        )

    @property
    def coupling_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "CouplingHalfCompoundModalAnalysisAtAStiffness":
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
class CouplingHalfCompoundModalAnalysisAtAStiffness(
    _5184.MountableComponentCompoundModalAnalysisAtAStiffness
):
    """CouplingHalfCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_5010.CouplingHalfModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingHalfModalAnalysisAtAStiffness]

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
    ) -> "List[_5010.CouplingHalfModalAnalysisAtAStiffness]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingHalfModalAnalysisAtAStiffness]

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
    def cast_to(self: "Self") -> "_Cast_CouplingHalfCompoundModalAnalysisAtAStiffness":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfCompoundModalAnalysisAtAStiffness
        """
        return _Cast_CouplingHalfCompoundModalAnalysisAtAStiffness(self)
