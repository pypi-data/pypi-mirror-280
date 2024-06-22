"""MutableCurve"""
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
from mastapy._private.geometry.two_d.curves import _323
from mastapy._private.gears.manufacturing.cylindrical.cutters import _742
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MUTABLE_CURVE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "MutableCurve"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical.cutters import _726

    Self = TypeVar("Self", bound="MutableCurve")
    CastSelf = TypeVar("CastSelf", bound="MutableCurve._Cast_MutableCurve")


__docformat__ = "restructuredtext en"
__all__ = ("MutableCurve",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MutableCurve:
    """Special nested class for casting MutableCurve to subclasses."""

    __parent__: "MutableCurve"

    @property
    def mutable_common(self: "CastSelf") -> "_742.MutableCommon":
        return self.__parent__._cast(_742.MutableCommon)

    @property
    def curve_in_linked_list(self: "CastSelf") -> "_726.CurveInLinkedList":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _726

        return self.__parent__._cast(_726.CurveInLinkedList)

    @property
    def mutable_curve(self: "CastSelf") -> "MutableCurve":
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
class MutableCurve(_742.MutableCommon):
    """MutableCurve

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MUTABLE_CURVE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def crowning(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return temp

    @crowning.setter
    @enforce_parameter_types
    def crowning(self: "Self", value: "float") -> None:
        self.wrapped.Crowning = float(value) if value is not None else 0.0

    @property
    def curve_type(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes":
        """EnumWithSelectedValue[mastapy._private.geometry.two_d.curves.BasicCurveTypes]"""
        temp = self.wrapped.CurveType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @curve_type.setter
    @enforce_parameter_types
    def curve_type(self: "Self", value: "_323.BasicCurveTypes") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.CurveType = value

    @property
    def height(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Height

        if temp is None:
            return 0.0

        return temp

    @height.setter
    @enforce_parameter_types
    def height(self: "Self", value: "float") -> None:
        self.wrapped.Height = float(value) if value is not None else 0.0

    @property
    def height_end(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def length(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: "Self", value: "float") -> None:
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def linear_modification(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearModification

        if temp is None:
            return 0.0

        return temp

    @linear_modification.setter
    @enforce_parameter_types
    def linear_modification(self: "Self", value: "float") -> None:
        self.wrapped.LinearModification = float(value) if value is not None else 0.0

    @property
    def nominal_section_pressure_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NominalSectionPressureAngle

        if temp is None:
            return 0.0

        return temp

    @nominal_section_pressure_angle.setter
    @enforce_parameter_types
    def nominal_section_pressure_angle(self: "Self", value: "float") -> None:
        self.wrapped.NominalSectionPressureAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def pressure_angle_modification(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PressureAngleModification

        if temp is None:
            return 0.0

        return temp

    @pressure_angle_modification.setter
    @enforce_parameter_types
    def pressure_angle_modification(self: "Self", value: "float") -> None:
        self.wrapped.PressureAngleModification = (
            float(value) if value is not None else 0.0
        )

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
    def cast_to(self: "Self") -> "_Cast_MutableCurve":
        """Cast to another type.

        Returns:
            _Cast_MutableCurve
        """
        return _Cast_MutableCurve(self)
