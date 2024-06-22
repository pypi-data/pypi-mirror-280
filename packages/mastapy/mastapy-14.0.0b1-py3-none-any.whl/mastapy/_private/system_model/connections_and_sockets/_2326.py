"""CVTBeltConnection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.connections_and_sockets import _2321
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CVT_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTBeltConnection"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.system_model.connections_and_sockets import _2334, _2325
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="CVTBeltConnection")
    CastSelf = TypeVar("CastSelf", bound="CVTBeltConnection._Cast_CVTBeltConnection")


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CVTBeltConnection:
    """Special nested class for casting CVTBeltConnection to subclasses."""

    __parent__: "CVTBeltConnection"

    @property
    def belt_connection(self: "CastSelf") -> "_2321.BeltConnection":
        return self.__parent__._cast(_2321.BeltConnection)

    @property
    def inter_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2334.InterMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2334

        return self.__parent__._cast(_2334.InterMountableComponentConnection)

    @property
    def connection(self: "CastSelf") -> "_2325.Connection":
        from mastapy._private.system_model.connections_and_sockets import _2325

        return self.__parent__._cast(_2325.Connection)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def cvt_belt_connection(self: "CastSelf") -> "CVTBeltConnection":
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
class CVTBeltConnection(_2321.BeltConnection):
    """CVTBeltConnection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CVT_BELT_CONNECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def belt_efficiency(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BeltEfficiency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @belt_efficiency.setter
    @enforce_parameter_types
    def belt_efficiency(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BeltEfficiency = value

    @property
    def cast_to(self: "Self") -> "_Cast_CVTBeltConnection":
        """Cast to another type.

        Returns:
            _Cast_CVTBeltConnection
        """
        return _Cast_CVTBeltConnection(self)
