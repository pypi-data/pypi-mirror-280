"""CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3229,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3114,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3304,
        _3208,
        _3240,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self",
        bound="CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse:
    """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

    __parent__: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse"

    @property
    def coaxial_connection_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3229.CoaxialConnectionCompoundSteadyStateSynchronousResponse":
        return self.__parent__._cast(
            _3229.CoaxialConnectionCompoundSteadyStateSynchronousResponse
        )

    @property
    def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3304.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3304,
        )

        return self.__parent__._cast(
            _3304.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
        )

    @property
    def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3208.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3208,
        )

        return self.__parent__._cast(
            _3208.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
        )

    @property
    def connection_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3240.ConnectionCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3240,
        )

        return self.__parent__._cast(
            _3240.ConnectionCompoundSteadyStateSynchronousResponse
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
    def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
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
class CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse(
    _3229.CoaxialConnectionCompoundSteadyStateSynchronousResponse
):
    """CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3114.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]

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
    ) -> "List[_3114.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]

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
    ) -> "_Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
        """
        return _Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
