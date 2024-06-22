"""InterMountableComponentConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
    _5271,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import _2334
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5240,
        _5245,
        _5247,
        _5252,
        _5257,
        _5262,
        _5265,
        _5268,
        _5273,
        _5276,
        _5283,
        _5289,
        _5294,
        _5298,
        _5302,
        _5305,
        _5308,
        _5319,
        _5329,
        _5331,
        _5338,
        _5341,
        _5344,
        _5347,
        _5356,
        _5362,
        _5365,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7703,
    )
    from mastapy._private.system_model.analyses_and_results import _2732, _2736, _2734

    Self = TypeVar(
        "Self", bound="InterMountableComponentConnectionModalAnalysisAtASpeed"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionModalAnalysisAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InterMountableComponentConnectionModalAnalysisAtASpeed:
    """Special nested class for casting InterMountableComponentConnectionModalAnalysisAtASpeed to subclasses."""

    __parent__: "InterMountableComponentConnectionModalAnalysisAtASpeed"

    @property
    def connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5271.ConnectionModalAnalysisAtASpeed":
        return self.__parent__._cast(_5271.ConnectionModalAnalysisAtASpeed)

    @property
    def connection_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7706.ConnectionStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7706,
        )

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
    def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5240.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5240,
        )

        return self.__parent__._cast(
            _5240.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
        )

    @property
    def belt_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5245.BeltConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5245,
        )

        return self.__parent__._cast(_5245.BeltConnectionModalAnalysisAtASpeed)

    @property
    def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5247.BevelDifferentialGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5247,
        )

        return self.__parent__._cast(
            _5247.BevelDifferentialGearMeshModalAnalysisAtASpeed
        )

    @property
    def bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5252.BevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5252,
        )

        return self.__parent__._cast(_5252.BevelGearMeshModalAnalysisAtASpeed)

    @property
    def clutch_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5257.ClutchConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5257,
        )

        return self.__parent__._cast(_5257.ClutchConnectionModalAnalysisAtASpeed)

    @property
    def concept_coupling_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5262.ConceptCouplingConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5262,
        )

        return self.__parent__._cast(
            _5262.ConceptCouplingConnectionModalAnalysisAtASpeed
        )

    @property
    def concept_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5265.ConceptGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5265,
        )

        return self.__parent__._cast(_5265.ConceptGearMeshModalAnalysisAtASpeed)

    @property
    def conical_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5268.ConicalGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5268,
        )

        return self.__parent__._cast(_5268.ConicalGearMeshModalAnalysisAtASpeed)

    @property
    def coupling_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5273.CouplingConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5273,
        )

        return self.__parent__._cast(_5273.CouplingConnectionModalAnalysisAtASpeed)

    @property
    def cvt_belt_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5276.CVTBeltConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5276,
        )

        return self.__parent__._cast(_5276.CVTBeltConnectionModalAnalysisAtASpeed)

    @property
    def cylindrical_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5283.CylindricalGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5283,
        )

        return self.__parent__._cast(_5283.CylindricalGearMeshModalAnalysisAtASpeed)

    @property
    def face_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5289.FaceGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5289,
        )

        return self.__parent__._cast(_5289.FaceGearMeshModalAnalysisAtASpeed)

    @property
    def gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5294.GearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5294,
        )

        return self.__parent__._cast(_5294.GearMeshModalAnalysisAtASpeed)

    @property
    def hypoid_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5298.HypoidGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5298,
        )

        return self.__parent__._cast(_5298.HypoidGearMeshModalAnalysisAtASpeed)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5302.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5302,
        )

        return self.__parent__._cast(
            _5302.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5305.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5305,
        )

        return self.__parent__._cast(
            _5305.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5308.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5308,
        )

        return self.__parent__._cast(
            _5308.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
        )

    @property
    def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5319.PartToPartShearCouplingConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5319,
        )

        return self.__parent__._cast(
            _5319.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
        )

    @property
    def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5329.RingPinsToDiscConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5329,
        )

        return self.__parent__._cast(
            _5329.RingPinsToDiscConnectionModalAnalysisAtASpeed
        )

    @property
    def rolling_ring_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5331.RollingRingConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5331,
        )

        return self.__parent__._cast(_5331.RollingRingConnectionModalAnalysisAtASpeed)

    @property
    def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5338.SpiralBevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5338,
        )

        return self.__parent__._cast(_5338.SpiralBevelGearMeshModalAnalysisAtASpeed)

    @property
    def spring_damper_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5341.SpringDamperConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5341,
        )

        return self.__parent__._cast(_5341.SpringDamperConnectionModalAnalysisAtASpeed)

    @property
    def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5344.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5344,
        )

        return self.__parent__._cast(
            _5344.StraightBevelDiffGearMeshModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5347.StraightBevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5347,
        )

        return self.__parent__._cast(_5347.StraightBevelGearMeshModalAnalysisAtASpeed)

    @property
    def torque_converter_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5356.TorqueConverterConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5356,
        )

        return self.__parent__._cast(
            _5356.TorqueConverterConnectionModalAnalysisAtASpeed
        )

    @property
    def worm_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5362.WormGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5362,
        )

        return self.__parent__._cast(_5362.WormGearMeshModalAnalysisAtASpeed)

    @property
    def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5365.ZerolBevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5365,
        )

        return self.__parent__._cast(_5365.ZerolBevelGearMeshModalAnalysisAtASpeed)

    @property
    def inter_mountable_component_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "InterMountableComponentConnectionModalAnalysisAtASpeed":
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
class InterMountableComponentConnectionModalAnalysisAtASpeed(
    _5271.ConnectionModalAnalysisAtASpeed
):
    """InterMountableComponentConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2334.InterMountableComponentConnection":
        """mastapy._private.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_InterMountableComponentConnectionModalAnalysisAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_InterMountableComponentConnectionModalAnalysisAtASpeed
        """
        return _Cast_InterMountableComponentConnectionModalAnalysisAtASpeed(self)
