"""Connection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import constructor, utility
from mastapy._private._internal.implicit import list_with_selected_item
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model import _2256
from mastapy._private._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model import _2498
    from mastapy._private.system_model.connections_and_sockets import (
        _2349,
        _2318,
        _2321,
        _2322,
        _2326,
        _2334,
        _2340,
        _2345,
        _2348,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2352,
        _2354,
        _2356,
        _2358,
        _2360,
        _2362,
        _2364,
        _2366,
        _2368,
        _2371,
        _2372,
        _2373,
        _2376,
        _2378,
        _2380,
        _2382,
        _2384,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import (
        _2388,
        _2391,
        _2394,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings import (
        _2395,
        _2397,
        _2399,
        _2401,
        _2403,
        _2405,
    )

    Self = TypeVar("Self", bound="Connection")
    CastSelf = TypeVar("CastSelf", bound="Connection._Cast_Connection")


__docformat__ = "restructuredtext en"
__all__ = ("Connection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Connection:
    """Special nested class for casting Connection to subclasses."""

    __parent__: "Connection"

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def abstract_shaft_to_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2318.AbstractShaftToMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2318

        return self.__parent__._cast(_2318.AbstractShaftToMountableComponentConnection)

    @property
    def belt_connection(self: "CastSelf") -> "_2321.BeltConnection":
        from mastapy._private.system_model.connections_and_sockets import _2321

        return self.__parent__._cast(_2321.BeltConnection)

    @property
    def coaxial_connection(self: "CastSelf") -> "_2322.CoaxialConnection":
        from mastapy._private.system_model.connections_and_sockets import _2322

        return self.__parent__._cast(_2322.CoaxialConnection)

    @property
    def cvt_belt_connection(self: "CastSelf") -> "_2326.CVTBeltConnection":
        from mastapy._private.system_model.connections_and_sockets import _2326

        return self.__parent__._cast(_2326.CVTBeltConnection)

    @property
    def inter_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2334.InterMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2334

        return self.__parent__._cast(_2334.InterMountableComponentConnection)

    @property
    def planetary_connection(self: "CastSelf") -> "_2340.PlanetaryConnection":
        from mastapy._private.system_model.connections_and_sockets import _2340

        return self.__parent__._cast(_2340.PlanetaryConnection)

    @property
    def rolling_ring_connection(self: "CastSelf") -> "_2345.RollingRingConnection":
        from mastapy._private.system_model.connections_and_sockets import _2345

        return self.__parent__._cast(_2345.RollingRingConnection)

    @property
    def shaft_to_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2348.ShaftToMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2348

        return self.__parent__._cast(_2348.ShaftToMountableComponentConnection)

    @property
    def agma_gleason_conical_gear_mesh(
        self: "CastSelf",
    ) -> "_2352.AGMAGleasonConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2352

        return self.__parent__._cast(_2352.AGMAGleasonConicalGearMesh)

    @property
    def bevel_differential_gear_mesh(
        self: "CastSelf",
    ) -> "_2354.BevelDifferentialGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2354

        return self.__parent__._cast(_2354.BevelDifferentialGearMesh)

    @property
    def bevel_gear_mesh(self: "CastSelf") -> "_2356.BevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2356

        return self.__parent__._cast(_2356.BevelGearMesh)

    @property
    def concept_gear_mesh(self: "CastSelf") -> "_2358.ConceptGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2358

        return self.__parent__._cast(_2358.ConceptGearMesh)

    @property
    def conical_gear_mesh(self: "CastSelf") -> "_2360.ConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2360

        return self.__parent__._cast(_2360.ConicalGearMesh)

    @property
    def cylindrical_gear_mesh(self: "CastSelf") -> "_2362.CylindricalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2362

        return self.__parent__._cast(_2362.CylindricalGearMesh)

    @property
    def face_gear_mesh(self: "CastSelf") -> "_2364.FaceGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2364

        return self.__parent__._cast(_2364.FaceGearMesh)

    @property
    def gear_mesh(self: "CastSelf") -> "_2366.GearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2366

        return self.__parent__._cast(_2366.GearMesh)

    @property
    def hypoid_gear_mesh(self: "CastSelf") -> "_2368.HypoidGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2368

        return self.__parent__._cast(_2368.HypoidGearMesh)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: "CastSelf",
    ) -> "_2371.KlingelnbergCycloPalloidConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2371

        return self.__parent__._cast(_2371.KlingelnbergCycloPalloidConicalGearMesh)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: "CastSelf",
    ) -> "_2372.KlingelnbergCycloPalloidHypoidGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2372

        return self.__parent__._cast(_2372.KlingelnbergCycloPalloidHypoidGearMesh)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: "CastSelf",
    ) -> "_2373.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2373

        return self.__parent__._cast(_2373.KlingelnbergCycloPalloidSpiralBevelGearMesh)

    @property
    def spiral_bevel_gear_mesh(self: "CastSelf") -> "_2376.SpiralBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2376

        return self.__parent__._cast(_2376.SpiralBevelGearMesh)

    @property
    def straight_bevel_diff_gear_mesh(
        self: "CastSelf",
    ) -> "_2378.StraightBevelDiffGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2378

        return self.__parent__._cast(_2378.StraightBevelDiffGearMesh)

    @property
    def straight_bevel_gear_mesh(self: "CastSelf") -> "_2380.StraightBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2380

        return self.__parent__._cast(_2380.StraightBevelGearMesh)

    @property
    def worm_gear_mesh(self: "CastSelf") -> "_2382.WormGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2382

        return self.__parent__._cast(_2382.WormGearMesh)

    @property
    def zerol_bevel_gear_mesh(self: "CastSelf") -> "_2384.ZerolBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2384

        return self.__parent__._cast(_2384.ZerolBevelGearMesh)

    @property
    def cycloidal_disc_central_bearing_connection(
        self: "CastSelf",
    ) -> "_2388.CycloidalDiscCentralBearingConnection":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2388,
        )

        return self.__parent__._cast(_2388.CycloidalDiscCentralBearingConnection)

    @property
    def cycloidal_disc_planetary_bearing_connection(
        self: "CastSelf",
    ) -> "_2391.CycloidalDiscPlanetaryBearingConnection":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2391,
        )

        return self.__parent__._cast(_2391.CycloidalDiscPlanetaryBearingConnection)

    @property
    def ring_pins_to_disc_connection(
        self: "CastSelf",
    ) -> "_2394.RingPinsToDiscConnection":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2394,
        )

        return self.__parent__._cast(_2394.RingPinsToDiscConnection)

    @property
    def clutch_connection(self: "CastSelf") -> "_2395.ClutchConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2395,
        )

        return self.__parent__._cast(_2395.ClutchConnection)

    @property
    def concept_coupling_connection(
        self: "CastSelf",
    ) -> "_2397.ConceptCouplingConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2397,
        )

        return self.__parent__._cast(_2397.ConceptCouplingConnection)

    @property
    def coupling_connection(self: "CastSelf") -> "_2399.CouplingConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2399,
        )

        return self.__parent__._cast(_2399.CouplingConnection)

    @property
    def part_to_part_shear_coupling_connection(
        self: "CastSelf",
    ) -> "_2401.PartToPartShearCouplingConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2401,
        )

        return self.__parent__._cast(_2401.PartToPartShearCouplingConnection)

    @property
    def spring_damper_connection(self: "CastSelf") -> "_2403.SpringDamperConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2403,
        )

        return self.__parent__._cast(_2403.SpringDamperConnection)

    @property
    def torque_converter_connection(
        self: "CastSelf",
    ) -> "_2405.TorqueConverterConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2405,
        )

        return self.__parent__._cast(_2405.TorqueConverterConnection)

    @property
    def connection(self: "CastSelf") -> "Connection":
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
class Connection(_2256.DesignEntity):
    """Connection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_id(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionID

        if temp is None:
            return ""

        return temp

    @property
    def drawing_position(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.DrawingPosition

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @drawing_position.setter
    @enforce_parameter_types
    def drawing_position(self: "Self", value: "str") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.DrawingPosition = value

    @property
    def full_name_without_root_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullNameWithoutRootName

        if temp is None:
            return ""

        return temp

    @property
    def speed_ratio_from_a_to_b(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_from_a_to_b(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def unique_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def owner_a(self: "Self") -> "_2498.Component":
        """mastapy._private.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OwnerA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def owner_b(self: "Self") -> "_2498.Component":
        """mastapy._private.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OwnerB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_a(self: "Self") -> "_2349.Socket":
        """mastapy._private.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_b(self: "Self") -> "_2349.Socket":
        """mastapy._private.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def other_owner(self: "Self", component: "_2498.Component") -> "_2498.Component":
        """mastapy._private.system_model.part_model.Component

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherOwner(
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_socket_for_component(
        self: "Self", component: "_2498.Component"
    ) -> "_2349.Socket":
        """mastapy._private.system_model.connections_and_sockets.Socket

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherSocket.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_socket(self: "Self", socket: "_2349.Socket") -> "_2349.Socket":
        """mastapy._private.system_model.connections_and_sockets.Socket

        Args:
            socket (mastapy._private.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.OtherSocket.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def socket_for(self: "Self", component: "_2498.Component") -> "_2349.Socket":
        """mastapy._private.system_model.connections_and_sockets.Socket

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.SocketFor(component.wrapped if component else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_Connection":
        """Cast to another type.

        Returns:
            _Cast_Connection
        """
        return _Cast_Connection(self)
