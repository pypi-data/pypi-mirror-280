"""MutableFillet"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.gears.manufacturing.cylindrical.cutters import _742
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MUTABLE_FILLET = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "MutableFillet"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical.cutters import _726

    Self = TypeVar("Self", bound="MutableFillet")
    CastSelf = TypeVar("CastSelf", bound="MutableFillet._Cast_MutableFillet")


__docformat__ = "restructuredtext en"
__all__ = ("MutableFillet",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MutableFillet:
    """Special nested class for casting MutableFillet to subclasses."""

    __parent__: "MutableFillet"

    @property
    def mutable_common(self: "CastSelf") -> "_742.MutableCommon":
        return self.__parent__._cast(_742.MutableCommon)

    @property
    def curve_in_linked_list(self: "CastSelf") -> "_726.CurveInLinkedList":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _726

        return self.__parent__._cast(_726.CurveInLinkedList)

    @property
    def mutable_fillet(self: "CastSelf") -> "MutableFillet":
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
class MutableFillet(_742.MutableCommon):
    """MutableFillet

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MUTABLE_FILLET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def radius(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: "Self", value: "float") -> None:
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_MutableFillet":
        """Cast to another type.

        Returns:
            _Cast_MutableFillet
        """
        return _Cast_MutableFillet(self)
