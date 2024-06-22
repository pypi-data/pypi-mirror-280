"""Socket"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2498, _2499
    from mastapy._private.system_model.connections_and_sockets import (
        _2325,
        _2319,
        _2320,
        _2327,
        _2329,
        _2331,
        _2332,
        _2333,
        _2335,
        _2336,
        _2337,
        _2338,
        _2339,
        _2341,
        _2342,
        _2343,
        _2346,
        _2347,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2353,
        _2355,
        _2357,
        _2359,
        _2361,
        _2363,
        _2365,
        _2367,
        _2369,
        _2370,
        _2374,
        _2375,
        _2377,
        _2379,
        _2381,
        _2383,
        _2385,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import (
        _2386,
        _2387,
        _2389,
        _2390,
        _2392,
        _2393,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings import (
        _2396,
        _2398,
        _2400,
        _2402,
        _2404,
        _2406,
        _2407,
    )

    Self = TypeVar("Self", bound="Socket")
    CastSelf = TypeVar("CastSelf", bound="Socket._Cast_Socket")


__docformat__ = "restructuredtext en"
__all__ = ("Socket",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Socket:
    """Special nested class for casting Socket to subclasses."""

    __parent__: "Socket"

    @property
    def bearing_inner_socket(self: "CastSelf") -> "_2319.BearingInnerSocket":
        from mastapy._private.system_model.connections_and_sockets import _2319

        return self.__parent__._cast(_2319.BearingInnerSocket)

    @property
    def bearing_outer_socket(self: "CastSelf") -> "_2320.BearingOuterSocket":
        from mastapy._private.system_model.connections_and_sockets import _2320

        return self.__parent__._cast(_2320.BearingOuterSocket)

    @property
    def cvt_pulley_socket(self: "CastSelf") -> "_2327.CVTPulleySocket":
        from mastapy._private.system_model.connections_and_sockets import _2327

        return self.__parent__._cast(_2327.CVTPulleySocket)

    @property
    def cylindrical_socket(self: "CastSelf") -> "_2329.CylindricalSocket":
        from mastapy._private.system_model.connections_and_sockets import _2329

        return self.__parent__._cast(_2329.CylindricalSocket)

    @property
    def electric_machine_stator_socket(
        self: "CastSelf",
    ) -> "_2331.ElectricMachineStatorSocket":
        from mastapy._private.system_model.connections_and_sockets import _2331

        return self.__parent__._cast(_2331.ElectricMachineStatorSocket)

    @property
    def inner_shaft_socket(self: "CastSelf") -> "_2332.InnerShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2332

        return self.__parent__._cast(_2332.InnerShaftSocket)

    @property
    def inner_shaft_socket_base(self: "CastSelf") -> "_2333.InnerShaftSocketBase":
        from mastapy._private.system_model.connections_and_sockets import _2333

        return self.__parent__._cast(_2333.InnerShaftSocketBase)

    @property
    def mountable_component_inner_socket(
        self: "CastSelf",
    ) -> "_2335.MountableComponentInnerSocket":
        from mastapy._private.system_model.connections_and_sockets import _2335

        return self.__parent__._cast(_2335.MountableComponentInnerSocket)

    @property
    def mountable_component_outer_socket(
        self: "CastSelf",
    ) -> "_2336.MountableComponentOuterSocket":
        from mastapy._private.system_model.connections_and_sockets import _2336

        return self.__parent__._cast(_2336.MountableComponentOuterSocket)

    @property
    def mountable_component_socket(
        self: "CastSelf",
    ) -> "_2337.MountableComponentSocket":
        from mastapy._private.system_model.connections_and_sockets import _2337

        return self.__parent__._cast(_2337.MountableComponentSocket)

    @property
    def outer_shaft_socket(self: "CastSelf") -> "_2338.OuterShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2338

        return self.__parent__._cast(_2338.OuterShaftSocket)

    @property
    def outer_shaft_socket_base(self: "CastSelf") -> "_2339.OuterShaftSocketBase":
        from mastapy._private.system_model.connections_and_sockets import _2339

        return self.__parent__._cast(_2339.OuterShaftSocketBase)

    @property
    def planetary_socket(self: "CastSelf") -> "_2341.PlanetarySocket":
        from mastapy._private.system_model.connections_and_sockets import _2341

        return self.__parent__._cast(_2341.PlanetarySocket)

    @property
    def planetary_socket_base(self: "CastSelf") -> "_2342.PlanetarySocketBase":
        from mastapy._private.system_model.connections_and_sockets import _2342

        return self.__parent__._cast(_2342.PlanetarySocketBase)

    @property
    def pulley_socket(self: "CastSelf") -> "_2343.PulleySocket":
        from mastapy._private.system_model.connections_and_sockets import _2343

        return self.__parent__._cast(_2343.PulleySocket)

    @property
    def rolling_ring_socket(self: "CastSelf") -> "_2346.RollingRingSocket":
        from mastapy._private.system_model.connections_and_sockets import _2346

        return self.__parent__._cast(_2346.RollingRingSocket)

    @property
    def shaft_socket(self: "CastSelf") -> "_2347.ShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2347

        return self.__parent__._cast(_2347.ShaftSocket)

    @property
    def agma_gleason_conical_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2353.AGMAGleasonConicalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2353

        return self.__parent__._cast(_2353.AGMAGleasonConicalGearTeethSocket)

    @property
    def bevel_differential_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2355.BevelDifferentialGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2355

        return self.__parent__._cast(_2355.BevelDifferentialGearTeethSocket)

    @property
    def bevel_gear_teeth_socket(self: "CastSelf") -> "_2357.BevelGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2357

        return self.__parent__._cast(_2357.BevelGearTeethSocket)

    @property
    def concept_gear_teeth_socket(self: "CastSelf") -> "_2359.ConceptGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2359

        return self.__parent__._cast(_2359.ConceptGearTeethSocket)

    @property
    def conical_gear_teeth_socket(self: "CastSelf") -> "_2361.ConicalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2361

        return self.__parent__._cast(_2361.ConicalGearTeethSocket)

    @property
    def cylindrical_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2363.CylindricalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2363

        return self.__parent__._cast(_2363.CylindricalGearTeethSocket)

    @property
    def face_gear_teeth_socket(self: "CastSelf") -> "_2365.FaceGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2365

        return self.__parent__._cast(_2365.FaceGearTeethSocket)

    @property
    def gear_teeth_socket(self: "CastSelf") -> "_2367.GearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2367

        return self.__parent__._cast(_2367.GearTeethSocket)

    @property
    def hypoid_gear_teeth_socket(self: "CastSelf") -> "_2369.HypoidGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2369

        return self.__parent__._cast(_2369.HypoidGearTeethSocket)

    @property
    def klingelnberg_conical_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2370.KlingelnbergConicalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2370

        return self.__parent__._cast(_2370.KlingelnbergConicalGearTeethSocket)

    @property
    def klingelnberg_hypoid_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2374.KlingelnbergHypoidGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2374

        return self.__parent__._cast(_2374.KlingelnbergHypoidGearTeethSocket)

    @property
    def klingelnberg_spiral_bevel_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2375.KlingelnbergSpiralBevelGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2375

        return self.__parent__._cast(_2375.KlingelnbergSpiralBevelGearTeethSocket)

    @property
    def spiral_bevel_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2377.SpiralBevelGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2377

        return self.__parent__._cast(_2377.SpiralBevelGearTeethSocket)

    @property
    def straight_bevel_diff_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2379.StraightBevelDiffGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2379

        return self.__parent__._cast(_2379.StraightBevelDiffGearTeethSocket)

    @property
    def straight_bevel_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2381.StraightBevelGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2381

        return self.__parent__._cast(_2381.StraightBevelGearTeethSocket)

    @property
    def worm_gear_teeth_socket(self: "CastSelf") -> "_2383.WormGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2383

        return self.__parent__._cast(_2383.WormGearTeethSocket)

    @property
    def zerol_bevel_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2385.ZerolBevelGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2385

        return self.__parent__._cast(_2385.ZerolBevelGearTeethSocket)

    @property
    def cycloidal_disc_axial_left_socket(
        self: "CastSelf",
    ) -> "_2386.CycloidalDiscAxialLeftSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2386,
        )

        return self.__parent__._cast(_2386.CycloidalDiscAxialLeftSocket)

    @property
    def cycloidal_disc_axial_right_socket(
        self: "CastSelf",
    ) -> "_2387.CycloidalDiscAxialRightSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2387,
        )

        return self.__parent__._cast(_2387.CycloidalDiscAxialRightSocket)

    @property
    def cycloidal_disc_inner_socket(
        self: "CastSelf",
    ) -> "_2389.CycloidalDiscInnerSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2389,
        )

        return self.__parent__._cast(_2389.CycloidalDiscInnerSocket)

    @property
    def cycloidal_disc_outer_socket(
        self: "CastSelf",
    ) -> "_2390.CycloidalDiscOuterSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2390,
        )

        return self.__parent__._cast(_2390.CycloidalDiscOuterSocket)

    @property
    def cycloidal_disc_planetary_bearing_socket(
        self: "CastSelf",
    ) -> "_2392.CycloidalDiscPlanetaryBearingSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2392,
        )

        return self.__parent__._cast(_2392.CycloidalDiscPlanetaryBearingSocket)

    @property
    def ring_pins_socket(self: "CastSelf") -> "_2393.RingPinsSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2393,
        )

        return self.__parent__._cast(_2393.RingPinsSocket)

    @property
    def clutch_socket(self: "CastSelf") -> "_2396.ClutchSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2396,
        )

        return self.__parent__._cast(_2396.ClutchSocket)

    @property
    def concept_coupling_socket(self: "CastSelf") -> "_2398.ConceptCouplingSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2398,
        )

        return self.__parent__._cast(_2398.ConceptCouplingSocket)

    @property
    def coupling_socket(self: "CastSelf") -> "_2400.CouplingSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2400,
        )

        return self.__parent__._cast(_2400.CouplingSocket)

    @property
    def part_to_part_shear_coupling_socket(
        self: "CastSelf",
    ) -> "_2402.PartToPartShearCouplingSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2402,
        )

        return self.__parent__._cast(_2402.PartToPartShearCouplingSocket)

    @property
    def spring_damper_socket(self: "CastSelf") -> "_2404.SpringDamperSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2404,
        )

        return self.__parent__._cast(_2404.SpringDamperSocket)

    @property
    def torque_converter_pump_socket(
        self: "CastSelf",
    ) -> "_2406.TorqueConverterPumpSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2406,
        )

        return self.__parent__._cast(_2406.TorqueConverterPumpSocket)

    @property
    def torque_converter_turbine_socket(
        self: "CastSelf",
    ) -> "_2407.TorqueConverterTurbineSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2407,
        )

        return self.__parent__._cast(_2407.TorqueConverterTurbineSocket)

    @property
    def socket(self: "CastSelf") -> "Socket":
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
class Socket(_0.APIBase):
    """Socket

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SOCKET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def connected_components(self: "Self") -> "List[_2498.Component]":
        """List[mastapy._private.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connections(self: "Self") -> "List[_2325.Connection]":
        """List[mastapy._private.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def owner(self: "Self") -> "_2498.Component":
        """mastapy._private.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Owner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def connect_to(
        self: "Self", component: "_2498.Component"
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connect_to_socket(
        self: "Self", socket: "Socket"
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            socket (mastapy._private.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connection_to(self: "Self", socket: "Socket") -> "_2325.Connection":
        """mastapy._private.system_model.connections_and_sockets.Connection

        Args:
            socket (mastapy._private.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectionTo(socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def get_possible_sockets_to_connect_to(
        self: "Self", component_to_connect_to: "_2498.Component"
    ) -> "List[Socket]":
        """List[mastapy._private.system_model.connections_and_sockets.Socket]

        Args:
            component_to_connect_to (mastapy._private.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetPossibleSocketsToConnectTo(
                component_to_connect_to.wrapped if component_to_connect_to else None
            )
        )

    @property
    def cast_to(self: "Self") -> "_Cast_Socket":
        """Cast to another type.

        Returns:
            _Cast_Socket
        """
        return _Cast_Socket(self)
