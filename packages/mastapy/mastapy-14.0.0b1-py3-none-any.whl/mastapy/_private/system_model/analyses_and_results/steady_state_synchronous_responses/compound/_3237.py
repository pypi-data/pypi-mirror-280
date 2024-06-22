"""ConicalGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3263,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ConicalGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3104,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3209,
        _3216,
        _3219,
        _3220,
        _3221,
        _3267,
        _3271,
        _3274,
        _3277,
        _3306,
        _3312,
        _3315,
        _3318,
        _3319,
        _3333,
        _3284,
        _3230,
        _3286,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="ConicalGearCompoundSteadyStateSynchronousResponse")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearCompoundSteadyStateSynchronousResponse._Cast_ConicalGearCompoundSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearCompoundSteadyStateSynchronousResponse:
    """Special nested class for casting ConicalGearCompoundSteadyStateSynchronousResponse to subclasses."""

    __parent__: "ConicalGearCompoundSteadyStateSynchronousResponse"

    @property
    def gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3263.GearCompoundSteadyStateSynchronousResponse":
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
    def bevel_differential_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3216.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3216,
        )

        return self.__parent__._cast(
            _3216.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
        )

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
    def bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3221.BevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3221,
        )

        return self.__parent__._cast(
            _3221.BevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def hypoid_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3267.HypoidGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3267,
        )

        return self.__parent__._cast(
            _3267.HypoidGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3271.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3271,
        )

        return self.__parent__._cast(
            _3271.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> (
        "_3274.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3274,
        )

        return self.__parent__._cast(
            _3274.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3277.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3277,
        )

        return self.__parent__._cast(
            _3277.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def spiral_bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3306.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3306,
        )

        return self.__parent__._cast(
            _3306.SpiralBevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3312.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3312,
        )

        return self.__parent__._cast(
            _3312.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3315.StraightBevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3315,
        )

        return self.__parent__._cast(
            _3315.StraightBevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3318.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3318,
        )

        return self.__parent__._cast(
            _3318.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3319.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3319,
        )

        return self.__parent__._cast(
            _3319.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def zerol_bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3333.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3333,
        )

        return self.__parent__._cast(
            _3333.ZerolBevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def conical_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "ConicalGearCompoundSteadyStateSynchronousResponse":
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
class ConicalGearCompoundSteadyStateSynchronousResponse(
    _3263.GearCompoundSteadyStateSynchronousResponse
):
    """ConicalGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def planetaries(
        self: "Self",
    ) -> "List[ConicalGearCompoundSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound.ConicalGearCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3104.ConicalGearSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3104.ConicalGearSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearSteadyStateSynchronousResponse]

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
    ) -> "_Cast_ConicalGearCompoundSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearCompoundSteadyStateSynchronousResponse
        """
        return _Cast_ConicalGearCompoundSteadyStateSynchronousResponse(self)
