"""InnerShaftSocketBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.connections_and_sockets import _2347
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_INNER_SHAFT_SOCKET_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "InnerShaftSocketBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import (
        _2332,
        _2329,
        _2349,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import (
        _2386,
        _2389,
    )

    Self = TypeVar("Self", bound="InnerShaftSocketBase")
    CastSelf = TypeVar(
        "CastSelf", bound="InnerShaftSocketBase._Cast_InnerShaftSocketBase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("InnerShaftSocketBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InnerShaftSocketBase:
    """Special nested class for casting InnerShaftSocketBase to subclasses."""

    __parent__: "InnerShaftSocketBase"

    @property
    def shaft_socket(self: "CastSelf") -> "_2347.ShaftSocket":
        return self.__parent__._cast(_2347.ShaftSocket)

    @property
    def cylindrical_socket(self: "CastSelf") -> "_2329.CylindricalSocket":
        from mastapy._private.system_model.connections_and_sockets import _2329

        return self.__parent__._cast(_2329.CylindricalSocket)

    @property
    def socket(self: "CastSelf") -> "_2349.Socket":
        from mastapy._private.system_model.connections_and_sockets import _2349

        return self.__parent__._cast(_2349.Socket)

    @property
    def inner_shaft_socket(self: "CastSelf") -> "_2332.InnerShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2332

        return self.__parent__._cast(_2332.InnerShaftSocket)

    @property
    def cycloidal_disc_axial_left_socket(
        self: "CastSelf",
    ) -> "_2386.CycloidalDiscAxialLeftSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2386,
        )

        return self.__parent__._cast(_2386.CycloidalDiscAxialLeftSocket)

    @property
    def cycloidal_disc_inner_socket(
        self: "CastSelf",
    ) -> "_2389.CycloidalDiscInnerSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2389,
        )

        return self.__parent__._cast(_2389.CycloidalDiscInnerSocket)

    @property
    def inner_shaft_socket_base(self: "CastSelf") -> "InnerShaftSocketBase":
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
class InnerShaftSocketBase(_2347.ShaftSocket):
    """InnerShaftSocketBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _INNER_SHAFT_SOCKET_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_InnerShaftSocketBase":
        """Cast to another type.

        Returns:
            _Cast_InnerShaftSocketBase
        """
        return _Cast_InnerShaftSocketBase(self)
