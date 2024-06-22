"""ConnectionSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7706
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import _2325
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3706,
        _3602,
        _3603,
        _3608,
        _3610,
        _3615,
        _3620,
        _3623,
        _3625,
        _3628,
        _3631,
        _3636,
        _3639,
        _3643,
        _3644,
        _3646,
        _3652,
        _3657,
        _3661,
        _3664,
        _3665,
        _3668,
        _3671,
        _3681,
        _3684,
        _3691,
        _3693,
        _3698,
        _3700,
        _3703,
        _3707,
        _3710,
        _3719,
        _3725,
        _3728,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7703
    from mastapy._private.system_model.analyses_and_results import _2732, _2736, _2734

    Self = TypeVar("Self", bound="ConnectionSteadyStateSynchronousResponseAtASpeed")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting ConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "ConnectionSteadyStateSynchronousResponseAtASpeed"

    @property
    def connection_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7706.ConnectionStaticLoadAnalysisCase":
        return self.__parent__._cast(_7706.ConnectionStaticLoadAnalysisCase)

    @property
    def connection_analysis_case(self: "CastSelf") -> "_7703.ConnectionAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7703,
        )

        return self.__parent__._cast(_7703.ConnectionAnalysisCase)

    @property
    def connection_analysis(self: "CastSelf") -> "_2732.ConnectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2732

        return self.__parent__._cast(_2732.ConnectionAnalysis)

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
    def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3602.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3602,
        )

        return self.__parent__._cast(
            _3602.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3603.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3603,
        )

        return self.__parent__._cast(
            _3603.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def belt_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3608.BeltConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3608,
        )

        return self.__parent__._cast(
            _3608.BeltConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3610.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3610,
        )

        return self.__parent__._cast(
            _3610.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3615.BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3615,
        )

        return self.__parent__._cast(
            _3615.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3620.ClutchConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3620,
        )

        return self.__parent__._cast(
            _3620.ClutchConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coaxial_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3623.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3623,
        )

        return self.__parent__._cast(
            _3623.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3625.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3625,
        )

        return self.__parent__._cast(
            _3625.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3628.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3628,
        )

        return self.__parent__._cast(
            _3628.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3631.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3631,
        )

        return self.__parent__._cast(
            _3631.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coupling_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3636.CouplingConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3636,
        )

        return self.__parent__._cast(
            _3636.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3639.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3639,
        )

        return self.__parent__._cast(
            _3639.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3643.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3643,
        )

        return self.__parent__._cast(
            _3643.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3644.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3644,
        )

        return self.__parent__._cast(
            _3644.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3646.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3646,
        )

        return self.__parent__._cast(
            _3646.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3652.FaceGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3652,
        )

        return self.__parent__._cast(
            _3652.FaceGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3657.GearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3657,
        )

        return self.__parent__._cast(
            _3657.GearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3661.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3661,
        )

        return self.__parent__._cast(
            _3661.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3664.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3664,
        )

        return self.__parent__._cast(
            _3664.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3665.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3665,
        )

        return self.__parent__._cast(
            _3665.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3668.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3668,
        )

        return self.__parent__._cast(
            _3668.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3671.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3671,
        )

        return self.__parent__._cast(
            _3671.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3681.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3681,
        )

        return self.__parent__._cast(
            _3681.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planetary_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3684.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3684,
        )

        return self.__parent__._cast(
            _3684.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def ring_pins_to_disc_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3691.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3691,
        )

        return self.__parent__._cast(
            _3691.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3693.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3693,
        )

        return self.__parent__._cast(
            _3693.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3698.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3698,
        )

        return self.__parent__._cast(
            _3698.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3700.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3700,
        )

        return self.__parent__._cast(
            _3700.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3703.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3703,
        )

        return self.__parent__._cast(
            _3703.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3707.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3707,
        )

        return self.__parent__._cast(
            _3707.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3710.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3710,
        )

        return self.__parent__._cast(
            _3710.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3719.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3719,
        )

        return self.__parent__._cast(
            _3719.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3725.WormGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3725,
        )

        return self.__parent__._cast(
            _3725.WormGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3728.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3728,
        )

        return self.__parent__._cast(
            _3728.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "ConnectionSteadyStateSynchronousResponseAtASpeed":
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
class ConnectionSteadyStateSynchronousResponseAtASpeed(
    _7706.ConnectionStaticLoadAnalysisCase
):
    """ConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2325.Connection":
        """mastapy._private.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: "Self") -> "_2325.Connection":
        """mastapy._private.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_at_a_speed(
        self: "Self",
    ) -> "_3706.SteadyStateSynchronousResponseAtASpeed":
        """mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SteadyStateSynchronousResponseAtASpeed

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_ConnectionSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_ConnectionSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_ConnectionSteadyStateSynchronousResponseAtASpeed(self)
