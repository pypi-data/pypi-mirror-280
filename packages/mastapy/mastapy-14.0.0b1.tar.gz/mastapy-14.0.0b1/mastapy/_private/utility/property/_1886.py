"""EnumWithSelectedValue"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private import _7718
from mastapy._private.utility.property import _7744
from mastapy._private._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import Any, Type, List

    Self = TypeVar("Self", bound="EnumWithSelectedValue")
    CastSelf = TypeVar(
        "CastSelf", bound="EnumWithSelectedValue._Cast_EnumWithSelectedValue"
    )

TAPIEnum = TypeVar("TAPIEnum")

__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_EnumWithSelectedValue:
    """Special nested class for casting EnumWithSelectedValue to subclasses."""

    __parent__: "EnumWithSelectedValue"

    @property
    def marshal_by_ref_object_permanent(
        self: "CastSelf",
    ) -> "_7718.MarshalByRefObjectPermanent":
        return self.__parent__._cast(_7718.MarshalByRefObjectPermanent)

    @property
    def enum_with_selected_value(self: "CastSelf") -> "EnumWithSelectedValue":
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
class EnumWithSelectedValue(
    _7718.MarshalByRefObjectPermanent, _7744.IEnumWithSelectedValue, Generic[TAPIEnum]
):
    """EnumWithSelectedValue

    This is a mastapy class.

    Generic Types:
        TAPIEnum
    """

    TYPE: ClassVar["Type"] = _ENUM_WITH_SELECTED_VALUE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def selected_value(self: "Self") -> "TAPIEnum":
        """TAPIEnum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_values(self: "Self") -> "List[TAPIEnum]":
        """List[TAPIEnum]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_EnumWithSelectedValue":
        """Cast to another type.

        Returns:
            _Cast_EnumWithSelectedValue
        """
        return _Cast_EnumWithSelectedValue(self)
