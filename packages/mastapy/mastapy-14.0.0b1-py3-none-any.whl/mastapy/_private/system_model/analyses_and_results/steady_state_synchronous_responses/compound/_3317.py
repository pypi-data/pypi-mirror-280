"""StraightBevelGearSetCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3223,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2604
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3185,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3315,
        _3316,
        _3211,
        _3239,
        _3265,
        _3305,
        _3205,
        _3286,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="StraightBevelGearSetCompoundSteadyStateSynchronousResponse"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetCompoundSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse:
    """Special nested class for casting StraightBevelGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

    __parent__: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse"

    @property
    def bevel_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3223.BevelGearSetCompoundSteadyStateSynchronousResponse":
        return self.__parent__._cast(
            _3223.BevelGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3211.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3211,
        )

        return self.__parent__._cast(
            _3211.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def conical_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3239.ConicalGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3239,
        )

        return self.__parent__._cast(
            _3239.ConicalGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3265.GearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3265,
        )

        return self.__parent__._cast(
            _3265.GearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def specialised_assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3305.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3305,
        )

        return self.__parent__._cast(
            _3305.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
        )

    @property
    def abstract_assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3205.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3205,
        )

        return self.__parent__._cast(
            _3205.AbstractAssemblyCompoundSteadyStateSynchronousResponse
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
    def straight_bevel_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
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
class StraightBevelGearSetCompoundSteadyStateSynchronousResponse(
    _3223.BevelGearSetCompoundSteadyStateSynchronousResponse
):
    """StraightBevelGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2604.StraightBevelGearSet":
        """mastapy._private.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2604.StraightBevelGearSet":
        """mastapy._private.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3185.StraightBevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gears_compound_steady_state_synchronous_response(
        self: "Self",
    ) -> "List[_3315.StraightBevelGearCompoundSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound.StraightBevelGearCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_compound_steady_state_synchronous_response(
        self: "Self",
    ) -> "List[_3316.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_3185.StraightBevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse
        """
        return _Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse(self)
