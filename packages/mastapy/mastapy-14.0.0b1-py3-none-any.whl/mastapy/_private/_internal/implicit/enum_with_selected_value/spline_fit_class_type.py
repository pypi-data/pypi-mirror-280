"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.detailed_rigid_connectors.splines import _1458
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar("Self", bound="EnumWithSelectedValue_SplineFitClassType")


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_SplineFitClassType",)


class EnumWithSelectedValue_SplineFitClassType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineFitClassType

    A specific implementation of 'EnumWithSelectedValue' for 'SplineFitClassType' types.
    """

    __qualname__ = "SplineFitClassType"

    @classmethod
    def wrapper_type(cls: "Type[EnumWithSelectedValue_SplineFitClassType]") -> "Any":
        """Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(
        cls: "Type[EnumWithSelectedValue_SplineFitClassType]",
    ) -> "_1458.SplineFitClassType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _1458.SplineFitClassType
        """
        return _1458.SplineFitClassType

    @classmethod
    def implicit_type(cls: "Type[EnumWithSelectedValue_SplineFitClassType]") -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _1458.SplineFitClassType.type_()

    @property
    def selected_value(self: "Self") -> "_1458.SplineFitClassType":
        """mastapy._private.detailed_rigid_connectors.splines.SplineFitClassType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_1458.SplineFitClassType]":
        """List[mastapy._private.detailed_rigid_connectors.splines.SplineFitClassType]

        Note:
            This property is readonly.
        """
        return None
