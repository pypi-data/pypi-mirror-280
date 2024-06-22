"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.gears.manufacturing.cylindrical import _647
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar("Self", bound="EnumWithSelectedValue_CylindricalMftRoughingMethods")


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CylindricalMftRoughingMethods",)


class EnumWithSelectedValue_CylindricalMftRoughingMethods(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_CylindricalMftRoughingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftRoughingMethods' types.
    """

    __qualname__ = "CylindricalMftRoughingMethods"

    @classmethod
    def wrapper_type(
        cls: "Type[EnumWithSelectedValue_CylindricalMftRoughingMethods]",
    ) -> "Any":
        """Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(
        cls: "Type[EnumWithSelectedValue_CylindricalMftRoughingMethods]",
    ) -> "_647.CylindricalMftRoughingMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _647.CylindricalMftRoughingMethods
        """
        return _647.CylindricalMftRoughingMethods

    @classmethod
    def implicit_type(
        cls: "Type[EnumWithSelectedValue_CylindricalMftRoughingMethods]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _647.CylindricalMftRoughingMethods.type_()

    @property
    def selected_value(self: "Self") -> "_647.CylindricalMftRoughingMethods":
        """mastapy._private.gears.manufacturing.cylindrical.CylindricalMftRoughingMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_647.CylindricalMftRoughingMethods]":
        """List[mastapy._private.gears.manufacturing.cylindrical.CylindricalMftRoughingMethods]

        Note:
            This property is readonly.
        """
        return None
