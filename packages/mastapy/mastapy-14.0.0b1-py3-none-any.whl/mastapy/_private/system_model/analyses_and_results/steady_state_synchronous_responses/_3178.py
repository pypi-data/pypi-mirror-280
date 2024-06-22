"""SteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7702
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3180,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7715,
        _7700,
    )
    from mastapy._private.system_model.analyses_and_results import _2733

    Self = TypeVar("Self", bound="SteadyStateSynchronousResponse")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SteadyStateSynchronousResponse:
    """Special nested class for casting SteadyStateSynchronousResponse to subclasses."""

    __parent__: "SteadyStateSynchronousResponse"

    @property
    def compound_analysis_case(self: "CastSelf") -> "_7702.CompoundAnalysisCase":
        return self.__parent__._cast(_7702.CompoundAnalysisCase)

    @property
    def static_load_analysis_case(self: "CastSelf") -> "_7715.StaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7715,
        )

        return self.__parent__._cast(_7715.StaticLoadAnalysisCase)

    @property
    def analysis_case(self: "CastSelf") -> "_7700.AnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7700,
        )

        return self.__parent__._cast(_7700.AnalysisCase)

    @property
    def context(self: "CastSelf") -> "_2733.Context":
        from mastapy._private.system_model.analyses_and_results import _2733

        return self.__parent__._cast(_2733.Context)

    @property
    def steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "SteadyStateSynchronousResponse":
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
class SteadyStateSynchronousResponse(_7702.CompoundAnalysisCase):
    """SteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def steady_state_analysis_options(
        self: "Self",
    ) -> "_3180.SteadyStateSynchronousResponseOptions":
        """mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.SteadyStateSynchronousResponseOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_SteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_SteadyStateSynchronousResponse
        """
        return _Cast_SteadyStateSynchronousResponse(self)
