"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.gears.micro_geometry import _584
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar("Self", bound="EnumWithSelectedValue_LocationOfEvaluationLowerLimit")


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LocationOfEvaluationLowerLimit",)


class EnumWithSelectedValue_LocationOfEvaluationLowerLimit(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LocationOfEvaluationLowerLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationLowerLimit' types.
    """

    __qualname__ = "LocationOfEvaluationLowerLimit"

    @classmethod
    def wrapper_type(
        cls: "Type[EnumWithSelectedValue_LocationOfEvaluationLowerLimit]",
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
        cls: "Type[EnumWithSelectedValue_LocationOfEvaluationLowerLimit]",
    ) -> "_584.LocationOfEvaluationLowerLimit":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _584.LocationOfEvaluationLowerLimit
        """
        return _584.LocationOfEvaluationLowerLimit

    @classmethod
    def implicit_type(
        cls: "Type[EnumWithSelectedValue_LocationOfEvaluationLowerLimit]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _584.LocationOfEvaluationLowerLimit.type_()

    @property
    def selected_value(self: "Self") -> "_584.LocationOfEvaluationLowerLimit":
        """mastapy._private.gears.micro_geometry.LocationOfEvaluationLowerLimit

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_584.LocationOfEvaluationLowerLimit]":
        """List[mastapy._private.gears.micro_geometry.LocationOfEvaluationLowerLimit]

        Note:
            This property is readonly.
        """
        return None
