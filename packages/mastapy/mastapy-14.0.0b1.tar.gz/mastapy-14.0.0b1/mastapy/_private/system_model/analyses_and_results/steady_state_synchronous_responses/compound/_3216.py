"""BevelDifferentialGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3221,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2571
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3083,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3219,
        _3220,
        _3209,
        _3237,
        _3263,
        _3284,
        _3230,
        _3286,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="BevelDifferentialGearCompoundSteadyStateSynchronousResponse"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse:
    """Special nested class for casting BevelDifferentialGearCompoundSteadyStateSynchronousResponse to subclasses."""

    __parent__: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse"

    @property
    def bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3221.BevelGearCompoundSteadyStateSynchronousResponse":
        return self.__parent__._cast(
            _3221.BevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3209.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3209,
        )

        return self.__parent__._cast(
            _3209.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def conical_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3237.ConicalGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3237,
        )

        return self.__parent__._cast(
            _3237.ConicalGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3263.GearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3263,
        )

        return self.__parent__._cast(_3263.GearCompoundSteadyStateSynchronousResponse)

    @property
    def mountable_component_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3284.MountableComponentCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3284,
        )

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
    def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3219.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3219,
        )

        return self.__parent__._cast(
            _3219.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3220.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3220,
        )

        return self.__parent__._cast(
            _3220.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def bevel_differential_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
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
class BevelDifferentialGearCompoundSteadyStateSynchronousResponse(
    _3221.BevelGearCompoundSteadyStateSynchronousResponse
):
    """BevelDifferentialGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2571.BevelDifferentialGear":
        """mastapy._private.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3083.BevelDifferentialGearSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearSteadyStateSynchronousResponse]

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
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3083.BevelDifferentialGearSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearSteadyStateSynchronousResponse]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse
        """
        return _Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse(self)
