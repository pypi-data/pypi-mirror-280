"""CouplingHalfCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3284,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CouplingHalfCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3108,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3228,
        _3233,
        _3247,
        _3289,
        _3295,
        _3299,
        _3311,
        _3321,
        _3322,
        _3323,
        _3326,
        _3327,
        _3230,
        _3286,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CouplingHalfCompoundSteadyStateSynchronousResponse")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingHalfCompoundSteadyStateSynchronousResponse._Cast_CouplingHalfCompoundSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfCompoundSteadyStateSynchronousResponse:
    """Special nested class for casting CouplingHalfCompoundSteadyStateSynchronousResponse to subclasses."""

    __parent__: "CouplingHalfCompoundSteadyStateSynchronousResponse"

    @property
    def mountable_component_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3284.MountableComponentCompoundSteadyStateSynchronousResponse":
        return self.__parent__._cast(
            _3284.MountableComponentCompoundSteadyStateSynchronousResponse
        )

    @property
    def component_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3230.ComponentCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3230,
        )

        return self.__parent__._cast(
            _3230.ComponentCompoundSteadyStateSynchronousResponse
        )

    @property
    def part_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3286.PartCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3286,
        )

        return self.__parent__._cast(_3286.PartCompoundSteadyStateSynchronousResponse)

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
    def clutch_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3228.ClutchHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3228,
        )

        return self.__parent__._cast(
            _3228.ClutchHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def concept_coupling_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3233.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3233,
        )

        return self.__parent__._cast(
            _3233.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def cvt_pulley_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3247.CVTPulleyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3247,
        )

        return self.__parent__._cast(
            _3247.CVTPulleyCompoundSteadyStateSynchronousResponse
        )

    @property
    def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3289.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3289,
        )

        return self.__parent__._cast(
            _3289.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def pulley_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3295.PulleyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3295,
        )

        return self.__parent__._cast(_3295.PulleyCompoundSteadyStateSynchronousResponse)

    @property
    def rolling_ring_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3299.RollingRingCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3299,
        )

        return self.__parent__._cast(
            _3299.RollingRingCompoundSteadyStateSynchronousResponse
        )

    @property
    def spring_damper_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3311.SpringDamperHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3311,
        )

        return self.__parent__._cast(
            _3311.SpringDamperHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3321.SynchroniserHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3321,
        )

        return self.__parent__._cast(
            _3321.SynchroniserHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_part_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3322.SynchroniserPartCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3322,
        )

        return self.__parent__._cast(
            _3322.SynchroniserPartCompoundSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_sleeve_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3323.SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3323,
        )

        return self.__parent__._cast(
            _3323.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
        )

    @property
    def torque_converter_pump_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3326.TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3326,
        )

        return self.__parent__._cast(
            _3326.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
        )

    @property
    def torque_converter_turbine_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3327.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3327,
        )

        return self.__parent__._cast(
            _3327.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
        )

    @property
    def coupling_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "CouplingHalfCompoundSteadyStateSynchronousResponse":
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
class CouplingHalfCompoundSteadyStateSynchronousResponse(
    _3284.MountableComponentCompoundSteadyStateSynchronousResponse
):
    """CouplingHalfCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3108.CouplingHalfSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.CouplingHalfSteadyStateSynchronousResponse]

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
    ) -> "List[_3108.CouplingHalfSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.CouplingHalfSteadyStateSynchronousResponse]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_CouplingHalfCompoundSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfCompoundSteadyStateSynchronousResponse
        """
        return _Cast_CouplingHalfCompoundSteadyStateSynchronousResponse(self)
