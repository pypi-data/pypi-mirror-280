"""CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3547,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3374,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3491,
        _3496,
        _3510,
        _3552,
        _3558,
        _3562,
        _3574,
        _3584,
        _3585,
        _3586,
        _3589,
        _3590,
        _3493,
        _3549,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft:
    """Special nested class for casting CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

    __parent__: "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"

    @property
    def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3547.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        return self.__parent__._cast(
            _3547.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3493.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3493,
        )

        return self.__parent__._cast(
            _3493.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3549.PartCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3549,
        )

        return self.__parent__._cast(
            _3549.PartCompoundSteadyStateSynchronousResponseOnAShaft
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
    def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3491.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3491,
        )

        return self.__parent__._cast(
            _3491.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3496.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3496,
        )

        return self.__parent__._cast(
            _3496.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3510.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3510,
        )

        return self.__parent__._cast(
            _3510.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3552.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3552,
        )

        return self.__parent__._cast(
            _3552.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def pulley_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3558.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3558,
        )

        return self.__parent__._cast(
            _3558.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3562.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3562,
        )

        return self.__parent__._cast(
            _3562.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3574.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3574,
        )

        return self.__parent__._cast(
            _3574.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3584.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3584,
        )

        return self.__parent__._cast(
            _3584.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3585.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3585,
        )

        return self.__parent__._cast(
            _3585.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3586.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3586,
        )

        return self.__parent__._cast(
            _3586.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3589.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3589,
        )

        return self.__parent__._cast(
            _3589.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3590.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3590,
        )

        return self.__parent__._cast(
            _3590.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
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
class CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(
    _3547.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3374.CouplingHalfSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CouplingHalfSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3374.CouplingHalfSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CouplingHalfSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "_Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        """
        return _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(self)
