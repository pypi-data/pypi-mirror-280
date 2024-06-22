"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.gears.manufacturing.cylindrical.plunge_shaving import _666
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar("Self", bound="EnumWithSelectedValue_ChartType")


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ChartType",)


class EnumWithSelectedValue_ChartType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ChartType

    A specific implementation of 'EnumWithSelectedValue' for 'ChartType' types.
    """

    __qualname__ = "ChartType"

    @classmethod
    def wrapper_type(cls: "Type[EnumWithSelectedValue_ChartType]") -> "Any":
        """Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls: "Type[EnumWithSelectedValue_ChartType]") -> "_666.ChartType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _666.ChartType
        """
        return _666.ChartType

    @classmethod
    def implicit_type(cls: "Type[EnumWithSelectedValue_ChartType]") -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _666.ChartType.type_()

    @property
    def selected_value(self: "Self") -> "_666.ChartType":
        """mastapy._private.gears.manufacturing.cylindrical.plunge_shaving.ChartType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_666.ChartType]":
        """List[mastapy._private.gears.manufacturing.cylindrical.plunge_shaving.ChartType]

        Note:
            This property is readonly.
        """
        return None
