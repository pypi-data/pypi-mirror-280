"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.materials.efficiency import _303
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar("Self", bound="EnumWithSelectedValue_BearingEfficiencyRatingMethod")


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BearingEfficiencyRatingMethod",)


class EnumWithSelectedValue_BearingEfficiencyRatingMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_BearingEfficiencyRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BearingEfficiencyRatingMethod' types.
    """

    __qualname__ = "BearingEfficiencyRatingMethod"

    @classmethod
    def wrapper_type(
        cls: "Type[EnumWithSelectedValue_BearingEfficiencyRatingMethod]",
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
        cls: "Type[EnumWithSelectedValue_BearingEfficiencyRatingMethod]",
    ) -> "_303.BearingEfficiencyRatingMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _303.BearingEfficiencyRatingMethod
        """
        return _303.BearingEfficiencyRatingMethod

    @classmethod
    def implicit_type(
        cls: "Type[EnumWithSelectedValue_BearingEfficiencyRatingMethod]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _303.BearingEfficiencyRatingMethod.type_()

    @property
    def selected_value(self: "Self") -> "_303.BearingEfficiencyRatingMethod":
        """mastapy._private.materials.efficiency.BearingEfficiencyRatingMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_303.BearingEfficiencyRatingMethod]":
        """List[mastapy._private.materials.efficiency.BearingEfficiencyRatingMethod]

        Note:
            This property is readonly.
        """
        return None
