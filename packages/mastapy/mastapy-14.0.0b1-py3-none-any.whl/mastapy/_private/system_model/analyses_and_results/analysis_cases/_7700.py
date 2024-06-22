"""AnalysisCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results import _2733
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "AnalysisCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility import _1625
    from mastapy._private.system_model import _2256
    from mastapy._private.system_model.analyses_and_results import _2734
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2910,
        _2917,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3122,
        _3178,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3443,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3706,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3915,
        _3971,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4227
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4497,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses import (
        _4736,
        _4767,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _5024,
        _5052,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5315,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5591
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5862,
        _5891,
        _5895,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6204,
        _6222,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6467,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6725,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7158,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7426,
        _7428,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7702,
        _7709,
        _7715,
        _7716,
    )

    Self = TypeVar("Self", bound="AnalysisCase")
    CastSelf = TypeVar("CastSelf", bound="AnalysisCase._Cast_AnalysisCase")


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AnalysisCase:
    """Special nested class for casting AnalysisCase to subclasses."""

    __parent__: "AnalysisCase"

    @property
    def context(self: "CastSelf") -> "_2733.Context":
        return self.__parent__._cast(_2733.Context)

    @property
    def system_deflection(self: "CastSelf") -> "_2910.SystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2910,
        )

        return self.__parent__._cast(_2910.SystemDeflection)

    @property
    def torsional_system_deflection(
        self: "CastSelf",
    ) -> "_2917.TorsionalSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2917,
        )

        return self.__parent__._cast(_2917.TorsionalSystemDeflection)

    @property
    def dynamic_model_for_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3122.DynamicModelForSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3122,
        )

        return self.__parent__._cast(
            _3122.DynamicModelForSteadyStateSynchronousResponse
        )

    @property
    def steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3178.SteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3178,
        )

        return self.__parent__._cast(_3178.SteadyStateSynchronousResponse)

    @property
    def steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3443.SteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3443,
        )

        return self.__parent__._cast(_3443.SteadyStateSynchronousResponseOnAShaft)

    @property
    def steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3706.SteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3706,
        )

        return self.__parent__._cast(_3706.SteadyStateSynchronousResponseAtASpeed)

    @property
    def dynamic_model_for_stability_analysis(
        self: "CastSelf",
    ) -> "_3915.DynamicModelForStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3915,
        )

        return self.__parent__._cast(_3915.DynamicModelForStabilityAnalysis)

    @property
    def stability_analysis(self: "CastSelf") -> "_3971.StabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3971,
        )

        return self.__parent__._cast(_3971.StabilityAnalysis)

    @property
    def power_flow(self: "CastSelf") -> "_4227.PowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4227

        return self.__parent__._cast(_4227.PowerFlow)

    @property
    def parametric_study_tool(self: "CastSelf") -> "_4497.ParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4497,
        )

        return self.__parent__._cast(_4497.ParametricStudyTool)

    @property
    def dynamic_model_for_modal_analysis(
        self: "CastSelf",
    ) -> "_4736.DynamicModelForModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4736,
        )

        return self.__parent__._cast(_4736.DynamicModelForModalAnalysis)

    @property
    def modal_analysis(self: "CastSelf") -> "_4767.ModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4767,
        )

        return self.__parent__._cast(_4767.ModalAnalysis)

    @property
    def dynamic_model_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5024.DynamicModelAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5024,
        )

        return self.__parent__._cast(_5024.DynamicModelAtAStiffness)

    @property
    def modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5052.ModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5052,
        )

        return self.__parent__._cast(_5052.ModalAnalysisAtAStiffness)

    @property
    def modal_analysis_at_a_speed(self: "CastSelf") -> "_5315.ModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5315,
        )

        return self.__parent__._cast(_5315.ModalAnalysisAtASpeed)

    @property
    def multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5591.MultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5591,
        )

        return self.__parent__._cast(_5591.MultibodyDynamicsAnalysis)

    @property
    def dynamic_model_for_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5862.DynamicModelForHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5862,
        )

        return self.__parent__._cast(_5862.DynamicModelForHarmonicAnalysis)

    @property
    def harmonic_analysis(self: "CastSelf") -> "_5891.HarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5891,
        )

        return self.__parent__._cast(_5891.HarmonicAnalysis)

    @property
    def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_5895.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5895,
        )

        return self.__parent__._cast(
            _5895.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6204.HarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6204,
        )

        return self.__parent__._cast(_6204.HarmonicAnalysisOfSingleExcitation)

    @property
    def modal_analysis_for_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6222.ModalAnalysisForHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6222,
        )

        return self.__parent__._cast(_6222.ModalAnalysisForHarmonicAnalysis)

    @property
    def dynamic_analysis(self: "CastSelf") -> "_6467.DynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
            _6467,
        )

        return self.__parent__._cast(_6467.DynamicAnalysis)

    @property
    def critical_speed_analysis(self: "CastSelf") -> "_6725.CriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6725,
        )

        return self.__parent__._cast(_6725.CriticalSpeedAnalysis)

    @property
    def advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7158.AdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7158,
        )

        return self.__parent__._cast(_7158.AdvancedTimeSteppingAnalysisForModulation)

    @property
    def advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7426.AdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7426,
        )

        return self.__parent__._cast(_7426.AdvancedSystemDeflection)

    @property
    def advanced_system_deflection_sub_analysis(
        self: "CastSelf",
    ) -> "_7428.AdvancedSystemDeflectionSubAnalysis":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7428,
        )

        return self.__parent__._cast(_7428.AdvancedSystemDeflectionSubAnalysis)

    @property
    def compound_analysis_case(self: "CastSelf") -> "_7702.CompoundAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7702,
        )

        return self.__parent__._cast(_7702.CompoundAnalysisCase)

    @property
    def fe_analysis(self: "CastSelf") -> "_7709.FEAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7709,
        )

        return self.__parent__._cast(_7709.FEAnalysis)

    @property
    def static_load_analysis_case(self: "CastSelf") -> "_7715.StaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7715,
        )

        return self.__parent__._cast(_7715.StaticLoadAnalysisCase)

    @property
    def time_series_load_analysis_case(
        self: "CastSelf",
    ) -> "_7716.TimeSeriesLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7716,
        )

        return self.__parent__._cast(_7716.TimeSeriesLoadAnalysisCase)

    @property
    def analysis_case(self: "CastSelf") -> "AnalysisCase":
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
class AnalysisCase(_2733.Context):
    """AnalysisCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ANALYSIS_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def analysis_setup_time(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSetupTime

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ""

        return temp

    @property
    def analysis_run_information(self: "Self") -> "_1625.AnalysisRunInformation":
        """mastapy._private.utility.AnalysisRunInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisRunInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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

    @enforce_parameter_types
    def results_for(
        self: "Self", design_entity: "_2256.DesignEntity"
    ) -> "_2734.DesignEntityAnalysis":
        """mastapy._private.system_model.analyses_and_results.DesignEntityAnalysis

        Args:
            design_entity (mastapy._private.system_model.DesignEntity)
        """
        method_result = self.wrapped.ResultsFor(
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def perform_analysis(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @property
    def cast_to(self: "Self") -> "_Cast_AnalysisCase":
        """Cast to another type.

        Returns:
            _Cast_AnalysisCase
        """
        return _Cast_AnalysisCase(self)
