"""MutableCommon"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.gears.manufacturing.cylindrical import _632
from mastapy._private.gears.manufacturing.cylindrical.cutters import _726
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MUTABLE_COMMON = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "MutableCommon"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical.cutters import _743, _744

    Self = TypeVar("Self", bound="MutableCommon")
    CastSelf = TypeVar("CastSelf", bound="MutableCommon._Cast_MutableCommon")


__docformat__ = "restructuredtext en"
__all__ = ("MutableCommon",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MutableCommon:
    """Special nested class for casting MutableCommon to subclasses."""

    __parent__: "MutableCommon"

    @property
    def curve_in_linked_list(self: "CastSelf") -> "_726.CurveInLinkedList":
        return self.__parent__._cast(_726.CurveInLinkedList)

    @property
    def mutable_curve(self: "CastSelf") -> "_743.MutableCurve":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _743

        return self.__parent__._cast(_743.MutableCurve)

    @property
    def mutable_fillet(self: "CastSelf") -> "_744.MutableFillet":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _744

        return self.__parent__._cast(_744.MutableFillet)

    @property
    def mutable_common(self: "CastSelf") -> "MutableCommon":
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
class MutableCommon(_726.CurveInLinkedList):
    """MutableCommon

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MUTABLE_COMMON

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def protuberance(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Protuberance

        if temp is None:
            return 0.0

        return temp

    @protuberance.setter
    @enforce_parameter_types
    def protuberance(self: "Self", value: "float") -> None:
        self.wrapped.Protuberance = float(value) if value is not None else 0.0

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
    def section(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections":
        """EnumWithSelectedValue[mastapy._private.gears.manufacturing.cylindrical.CutterFlankSections]"""
        temp = self.wrapped.Section

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @section.setter
    @enforce_parameter_types
    def section(self: "Self", value: "_632.CutterFlankSections") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Section = value

    def remove(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.Remove()

    def split(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.Split()

    @property
    def cast_to(self: "Self") -> "_Cast_MutableCommon":
        """Cast to another type.

        Returns:
            _Cast_MutableCommon
        """
        return _Cast_MutableCommon(self)
