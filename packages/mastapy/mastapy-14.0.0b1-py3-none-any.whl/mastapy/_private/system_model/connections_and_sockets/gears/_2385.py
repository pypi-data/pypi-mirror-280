"""ZerolBevelGearTeethSocket"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.connections_and_sockets.gears import _2357
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_ZEROL_BEVEL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearTeethSocket"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2353,
        _2361,
        _2367,
    )
    from mastapy._private.system_model.connections_and_sockets import _2349

    Self = TypeVar("Self", bound="ZerolBevelGearTeethSocket")
    CastSelf = TypeVar(
        "CastSelf", bound="ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearTeethSocket",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ZerolBevelGearTeethSocket:
    """Special nested class for casting ZerolBevelGearTeethSocket to subclasses."""

    __parent__: "ZerolBevelGearTeethSocket"

    @property
    def bevel_gear_teeth_socket(self: "CastSelf") -> "_2357.BevelGearTeethSocket":
        return self.__parent__._cast(_2357.BevelGearTeethSocket)

    @property
    def agma_gleason_conical_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2353.AGMAGleasonConicalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2353

        return self.__parent__._cast(_2353.AGMAGleasonConicalGearTeethSocket)

    @property
    def conical_gear_teeth_socket(self: "CastSelf") -> "_2361.ConicalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2361

        return self.__parent__._cast(_2361.ConicalGearTeethSocket)

    @property
    def gear_teeth_socket(self: "CastSelf") -> "_2367.GearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2367

        return self.__parent__._cast(_2367.GearTeethSocket)

    @property
    def socket(self: "CastSelf") -> "_2349.Socket":
        from mastapy._private.system_model.connections_and_sockets import _2349

        return self.__parent__._cast(_2349.Socket)

    @property
    def zerol_bevel_gear_teeth_socket(self: "CastSelf") -> "ZerolBevelGearTeethSocket":
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
class ZerolBevelGearTeethSocket(_2357.BevelGearTeethSocket):
    """ZerolBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ZEROL_BEVEL_GEAR_TEETH_SOCKET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_ZerolBevelGearTeethSocket":
        """Cast to another type.

        Returns:
            _Cast_ZerolBevelGearTeethSocket
        """
        return _Cast_ZerolBevelGearTeethSocket(self)
