"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.electric_machines import _1294
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar("Self", bound="EnumWithSelectedValue_CoilPositionInSlot")


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CoilPositionInSlot",)


class EnumWithSelectedValue_CoilPositionInSlot(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CoilPositionInSlot

    A specific implementation of 'EnumWithSelectedValue' for 'CoilPositionInSlot' types.
    """

    __qualname__ = "CoilPositionInSlot"

    @classmethod
    def wrapper_type(cls: "Type[EnumWithSelectedValue_CoilPositionInSlot]") -> "Any":
        """Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(
        cls: "Type[EnumWithSelectedValue_CoilPositionInSlot]",
    ) -> "_1294.CoilPositionInSlot":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _1294.CoilPositionInSlot
        """
        return _1294.CoilPositionInSlot

    @classmethod
    def implicit_type(cls: "Type[EnumWithSelectedValue_CoilPositionInSlot]") -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _1294.CoilPositionInSlot.type_()

    @property
    def selected_value(self: "Self") -> "_1294.CoilPositionInSlot":
        """mastapy._private.electric_machines.CoilPositionInSlot

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_1294.CoilPositionInSlot]":
        """List[mastapy._private.electric_machines.CoilPositionInSlot]

        Note:
            This property is readonly.
        """
        return None
