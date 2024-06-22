"""SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3506,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.connections_and_sockets.couplings import _2403
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3440,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3533,
        _3503,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self",
        bound="SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
    """Special nested class for casting SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

    __parent__: "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"

    @property
    def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3506.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self.__parent__._cast(
            _3506.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3533.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3533,
        )

        return self.__parent__._cast(
            _3533.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def connection_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3503.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3503,
        )

        return self.__parent__._cast(
            _3503.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.ConnectionCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7704,
        )

        return self.__parent__._cast(_7704.ConnectionCompoundAnalysis)

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
    def spring_damper_connection_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
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
class SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3506.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _SPRING_DAMPER_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2403.SpringDamperConnection":
        """mastapy._private.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: "Self") -> "_2403.SpringDamperConnection":
        """mastapy._private.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3440.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_3440.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        """Cast to another type.

        Returns:
            _Cast_SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft
        """
        return (
            _Cast_SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
