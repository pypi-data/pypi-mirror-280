"""StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3748,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.connections_and_sockets.gears import _2378
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3707,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3736,
        _3764,
        _3790,
        _3796,
        _3766,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self",
        bound="StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"

    @property
    def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3748.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        return self.__parent__._cast(
            _3748.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3736.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3736,
        )

        return self.__parent__._cast(
            _3736.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3764.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3764,
        )

        return self.__parent__._cast(
            _3764.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3790.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3790,
        )

        return self.__parent__._cast(
            _3790.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3796.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3796,
        )

        return self.__parent__._cast(
            _3796.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3766.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3766,
        )

        return self.__parent__._cast(
            _3766.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
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
    def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
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
class StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
    _3748.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2378.StraightBevelDiffGearMesh":
        """mastapy._private.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: "Self") -> "_2378.StraightBevelDiffGearMesh":
        """mastapy._private.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

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
    ) -> "List[_3707.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3707.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed]

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
    ) -> (
        "_Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        """Cast to another type.

        Returns:
            _Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
