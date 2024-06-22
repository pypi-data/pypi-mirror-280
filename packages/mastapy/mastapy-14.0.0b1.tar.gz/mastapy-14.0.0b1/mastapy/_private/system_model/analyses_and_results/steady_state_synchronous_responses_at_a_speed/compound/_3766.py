"""ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3634,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3734,
        _3736,
        _3740,
        _3743,
        _3748,
        _3753,
        _3755,
        _3758,
        _3761,
        _3764,
        _3769,
        _3771,
        _3775,
        _3777,
        _3779,
        _3785,
        _3790,
        _3794,
        _3796,
        _3798,
        _3801,
        _3804,
        _3814,
        _3816,
        _3823,
        _3826,
        _3830,
        _3833,
        _3836,
        _3839,
        _3842,
        _3851,
        _3857,
        _3860,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7708
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting ConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.ConnectionCompoundAnalysis":
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
    def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3734.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3734,
        )

        return self.__parent__._cast(
            _3734.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
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
    def belt_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3740.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3740,
        )

        return self.__parent__._cast(
            _3740.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3743.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3743,
        )

        return self.__parent__._cast(
            _3743.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3748.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3748,
        )

        return self.__parent__._cast(
            _3748.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3753.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3753,
        )

        return self.__parent__._cast(
            _3753.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coaxial_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3755.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3755,
        )

        return self.__parent__._cast(
            _3755.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3758.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3758,
        )

        return self.__parent__._cast(
            _3758.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3761.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3761,
        )

        return self.__parent__._cast(
            _3761.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
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
    def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3769.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3769,
        )

        return self.__parent__._cast(
            _3769.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_belt_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3771.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3771,
        )

        return self.__parent__._cast(
            _3771.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3775.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3775,
        )

        return self.__parent__._cast(
            _3775.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3777.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3777,
        )

        return self.__parent__._cast(
            _3777.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3779.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3779,
        )

        return self.__parent__._cast(
            _3779.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def face_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3785.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3785,
        )

        return self.__parent__._cast(
            _3785.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
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
    def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3794.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3794,
        )

        return self.__parent__._cast(
            _3794.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
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
    def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3798.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3798,
        )

        return self.__parent__._cast(
            _3798.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3801.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3801,
        )

        return self.__parent__._cast(
            _3801.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3804.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3804,
        )

        return self.__parent__._cast(
            _3804.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3814.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3814,
        )

        return self.__parent__._cast(
            _3814.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planetary_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3816.PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3816,
        )

        return self.__parent__._cast(
            _3816.PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3823.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3823,
        )

        return self.__parent__._cast(
            _3823.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3826.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3826,
        )

        return self.__parent__._cast(
            _3826.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3830.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3830,
        )

        return self.__parent__._cast(
            _3830.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3833.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3833,
        )

        return self.__parent__._cast(
            _3833.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3836.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3836,
        )

        return self.__parent__._cast(
            _3836.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3839.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3839,
        )

        return self.__parent__._cast(
            _3839.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3842.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3842,
        )

        return self.__parent__._cast(
            _3842.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3851.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3851,
        )

        return self.__parent__._cast(
            _3851.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def worm_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3857.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3857,
        )

        return self.__parent__._cast(
            _3857.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3860.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3860,
        )

        return self.__parent__._cast(
            _3860.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
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
class ConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
    _7704.ConnectionCompoundAnalysis
):
    """ConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_3634.ConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConnectionSteadyStateSynchronousResponseAtASpeed]

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
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3634.ConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConnectionSteadyStateSynchronousResponseAtASpeed]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_ConnectionCompoundSteadyStateSynchronousResponseAtASpeed(self)
