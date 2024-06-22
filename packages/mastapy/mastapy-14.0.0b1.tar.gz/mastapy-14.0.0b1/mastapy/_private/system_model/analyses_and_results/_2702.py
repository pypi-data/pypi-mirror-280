"""CompoundAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private import _7718
from mastapy._private._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, Iterable, TypeVar

    from mastapy._private import _7724
    from mastapy._private.system_model import _2256
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7708
    from mastapy._private.system_model.analyses_and_results import (
        _2741,
        _2742,
        _2743,
        _2744,
        _2745,
        _2746,
        _2747,
        _2748,
        _2749,
        _2750,
        _2751,
        _2752,
        _2753,
        _2754,
        _2755,
        _2756,
        _2757,
        _2758,
        _2759,
        _2760,
        _2761,
        _2762,
        _2763,
        _2764,
        _2765,
    )

    Self = TypeVar("Self", bound="CompoundAnalysis")
    CastSelf = TypeVar("CastSelf", bound="CompoundAnalysis._Cast_CompoundAnalysis")


__docformat__ = "restructuredtext en"
__all__ = ("CompoundAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CompoundAnalysis:
    """Special nested class for casting CompoundAnalysis to subclasses."""

    __parent__: "CompoundAnalysis"

    @property
    def marshal_by_ref_object_permanent(
        self: "CastSelf",
    ) -> "_7718.MarshalByRefObjectPermanent":
        return self.__parent__._cast(_7718.MarshalByRefObjectPermanent)

    @property
    def compound_advanced_system_deflection_analysis(
        self: "CastSelf",
    ) -> "_2741.CompoundAdvancedSystemDeflectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2741

        return self.__parent__._cast(_2741.CompoundAdvancedSystemDeflectionAnalysis)

    @property
    def compound_advanced_system_deflection_sub_analysis(
        self: "CastSelf",
    ) -> "_2742.CompoundAdvancedSystemDeflectionSubAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2742

        return self.__parent__._cast(_2742.CompoundAdvancedSystemDeflectionSubAnalysis)

    @property
    def compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_2743.CompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results import _2743

        return self.__parent__._cast(
            _2743.CompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_2744.CompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2744

        return self.__parent__._cast(_2744.CompoundCriticalSpeedAnalysis)

    @property
    def compound_dynamic_analysis(self: "CastSelf") -> "_2745.CompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2745

        return self.__parent__._cast(_2745.CompoundDynamicAnalysis)

    @property
    def compound_dynamic_model_at_a_stiffness_analysis(
        self: "CastSelf",
    ) -> "_2746.CompoundDynamicModelAtAStiffnessAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2746

        return self.__parent__._cast(_2746.CompoundDynamicModelAtAStiffnessAnalysis)

    @property
    def compound_dynamic_model_for_harmonic_analysis(
        self: "CastSelf",
    ) -> "_2747.CompoundDynamicModelForHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2747

        return self.__parent__._cast(_2747.CompoundDynamicModelForHarmonicAnalysis)

    @property
    def compound_dynamic_model_for_modal_analysis(
        self: "CastSelf",
    ) -> "_2748.CompoundDynamicModelForModalAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2748

        return self.__parent__._cast(_2748.CompoundDynamicModelForModalAnalysis)

    @property
    def compound_dynamic_model_for_stability_analysis(
        self: "CastSelf",
    ) -> "_2749.CompoundDynamicModelForStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2749

        return self.__parent__._cast(_2749.CompoundDynamicModelForStabilityAnalysis)

    @property
    def compound_dynamic_model_for_steady_state_synchronous_response_analysis(
        self: "CastSelf",
    ) -> "_2750.CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2750

        return self.__parent__._cast(
            _2750.CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
        )

    @property
    def compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_2751.CompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2751

        return self.__parent__._cast(_2751.CompoundHarmonicAnalysis)

    @property
    def compound_harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_2752.CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results import _2752

        return self.__parent__._cast(
            _2752.CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def compound_harmonic_analysis_of_single_excitation_analysis(
        self: "CastSelf",
    ) -> "_2753.CompoundHarmonicAnalysisOfSingleExcitationAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2753

        return self.__parent__._cast(
            _2753.CompoundHarmonicAnalysisOfSingleExcitationAnalysis
        )

    @property
    def compound_modal_analysis(self: "CastSelf") -> "_2754.CompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2754

        return self.__parent__._cast(_2754.CompoundModalAnalysis)

    @property
    def compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_2755.CompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results import _2755

        return self.__parent__._cast(_2755.CompoundModalAnalysisAtASpeed)

    @property
    def compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_2756.CompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results import _2756

        return self.__parent__._cast(_2756.CompoundModalAnalysisAtAStiffness)

    @property
    def compound_modal_analysis_for_harmonic_analysis(
        self: "CastSelf",
    ) -> "_2757.CompoundModalAnalysisForHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2757

        return self.__parent__._cast(_2757.CompoundModalAnalysisForHarmonicAnalysis)

    @property
    def compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_2758.CompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2758

        return self.__parent__._cast(_2758.CompoundMultibodyDynamicsAnalysis)

    @property
    def compound_power_flow_analysis(
        self: "CastSelf",
    ) -> "_2759.CompoundPowerFlowAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2759

        return self.__parent__._cast(_2759.CompoundPowerFlowAnalysis)

    @property
    def compound_stability_analysis(
        self: "CastSelf",
    ) -> "_2760.CompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2760

        return self.__parent__._cast(_2760.CompoundStabilityAnalysis)

    @property
    def compound_steady_state_synchronous_response_analysis(
        self: "CastSelf",
    ) -> "_2761.CompoundSteadyStateSynchronousResponseAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2761

        return self.__parent__._cast(
            _2761.CompoundSteadyStateSynchronousResponseAnalysis
        )

    @property
    def compound_steady_state_synchronous_response_at_a_speed_analysis(
        self: "CastSelf",
    ) -> "_2762.CompoundSteadyStateSynchronousResponseAtASpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2762

        return self.__parent__._cast(
            _2762.CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
        )

    @property
    def compound_steady_state_synchronous_response_on_a_shaft_analysis(
        self: "CastSelf",
    ) -> "_2763.CompoundSteadyStateSynchronousResponseOnAShaftAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2763

        return self.__parent__._cast(
            _2763.CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
        )

    @property
    def compound_system_deflection_analysis(
        self: "CastSelf",
    ) -> "_2764.CompoundSystemDeflectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2764

        return self.__parent__._cast(_2764.CompoundSystemDeflectionAnalysis)

    @property
    def compound_torsional_system_deflection_analysis(
        self: "CastSelf",
    ) -> "_2765.CompoundTorsionalSystemDeflectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2765

        return self.__parent__._cast(_2765.CompoundTorsionalSystemDeflectionAnalysis)

    @property
    def compound_analysis(self: "CastSelf") -> "CompoundAnalysis":
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
class CompoundAnalysis(_7718.MarshalByRefObjectPermanent):
    """CompoundAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPOUND_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def results_ready(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

    def perform_analysis(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @enforce_parameter_types
    def perform_analysis_with_progress(
        self: "Self", progress: "_7724.TaskProgress"
    ) -> None:
        """Method does not return.

        Args:
            progress (mastapy._private.TaskProgress)
        """
        self.wrapped.PerformAnalysis.Overloads[_TASK_PROGRESS](
            progress.wrapped if progress else None
        )

    @enforce_parameter_types
    def results_for(
        self: "Self", design_entity: "_2256.DesignEntity"
    ) -> "Iterable[_7708.DesignEntityCompoundAnalysis]":
        """Iterable[mastapy._private.system_model.analyses_and_results.analysis_cases.DesignEntityCompoundAnalysis]

        Args:
            design_entity (mastapy._private.system_model.DesignEntity)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        )

    @property
    def cast_to(self: "Self") -> "_Cast_CompoundAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CompoundAnalysis
        """
        return _Cast_CompoundAnalysis(self)
