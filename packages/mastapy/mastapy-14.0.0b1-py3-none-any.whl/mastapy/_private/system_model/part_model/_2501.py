"""Connector"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.part_model import _2520
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONNECTOR = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model import (
        _2489,
        _2498,
        _2499,
        _2493,
        _2522,
        _2524,
    )
    from mastapy._private.system_model.connections_and_sockets import _2325, _2329
    from mastapy._private.system_model.part_model.couplings import _2657
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="Connector")
    CastSelf = TypeVar("CastSelf", bound="Connector._Cast_Connector")


__docformat__ = "restructuredtext en"
__all__ = ("Connector",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Connector:
    """Special nested class for casting Connector to subclasses."""

    __parent__: "Connector"

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
        return self.__parent__._cast(_2520.MountableComponent)

    @property
    def component(self: "CastSelf") -> "_2498.Component":
        return self.__parent__._cast(_2498.Component)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def bearing(self: "CastSelf") -> "_2493.Bearing":
        from mastapy._private.system_model.part_model import _2493

        return self.__parent__._cast(_2493.Bearing)

    @property
    def oil_seal(self: "CastSelf") -> "_2522.OilSeal":
        from mastapy._private.system_model.part_model import _2522

        return self.__parent__._cast(_2522.OilSeal)

    @property
    def shaft_hub_connection(self: "CastSelf") -> "_2657.ShaftHubConnection":
        from mastapy._private.system_model.part_model.couplings import _2657

        return self.__parent__._cast(_2657.ShaftHubConnection)

    @property
    def connector(self: "CastSelf") -> "Connector":
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
class Connector(_2520.MountableComponent):
    """Connector

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTOR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def outer_component(self: "Self") -> "_2489.AbstractShaft":
        """mastapy._private.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_connection(self: "Self") -> "_2325.Connection":
        """mastapy._private.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_socket(self: "Self") -> "_2329.CylindricalSocket":
        """mastapy._private.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def house_in(
        self: "Self", shaft: "_2489.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2325.Connection":
        """mastapy._private.system_model.connections_and_sockets.Connection

        Args:
            shaft (mastapy._private.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.HouseIn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_component(
        self: "Self", component: "_2498.Component"
    ) -> "_2489.AbstractShaft":
        """mastapy._private.system_model.part_model.AbstractShaft

        Args:
            component (mastapy._private.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherComponent(
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_house_in(
        self: "Self", shaft: "_2489.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2499.ComponentsConnectedResult":
        """mastapy._private.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy._private.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryHouseIn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_Connector":
        """Cast to another type.

        Returns:
            _Cast_Connector
        """
        return _Cast_Connector(self)
