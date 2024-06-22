"""SpringDamperHalfSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3108,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SpringDamperHalfSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model.couplings import _2663
    from mastapy._private.system_model.analyses_and_results.static_loads import _7106
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3150,
        _3095,
        _3152,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="SpringDamperHalfSteadyStateSynchronousResponse")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpringDamperHalfSteadyStateSynchronousResponse._Cast_SpringDamperHalfSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpringDamperHalfSteadyStateSynchronousResponse:
    """Special nested class for casting SpringDamperHalfSteadyStateSynchronousResponse to subclasses."""

    __parent__: "SpringDamperHalfSteadyStateSynchronousResponse"

    @property
    def coupling_half_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3108.CouplingHalfSteadyStateSynchronousResponse":
        return self.__parent__._cast(_3108.CouplingHalfSteadyStateSynchronousResponse)

    @property
    def mountable_component_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3150.MountableComponentSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3150,
        )

        return self.__parent__._cast(
            _3150.MountableComponentSteadyStateSynchronousResponse
        )

    @property
    def component_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3095.ComponentSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3095,
        )

        return self.__parent__._cast(_3095.ComponentSteadyStateSynchronousResponse)

    @property
    def part_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3152.PartSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3152,
        )

        return self.__parent__._cast(_3152.PartSteadyStateSynchronousResponse)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7713.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7713,
        )

        return self.__parent__._cast(_7713.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7710.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def spring_damper_half_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "SpringDamperHalfSteadyStateSynchronousResponse":
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
class SpringDamperHalfSteadyStateSynchronousResponse(
    _3108.CouplingHalfSteadyStateSynchronousResponse
):
    """SpringDamperHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPRING_DAMPER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2663.SpringDamperHalf":
        """mastapy._private.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: "Self") -> "_7106.SpringDamperHalfLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_SpringDamperHalfSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_SpringDamperHalfSteadyStateSynchronousResponse
        """
        return _Cast_SpringDamperHalfSteadyStateSynchronousResponse(self)
