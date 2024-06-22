"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.gears.rating.cylindrical import _493
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar(
        "Self", bound="EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod"
    )


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod",)


class EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingIntegralTemperatureRatingMethod' types.
    """

    __qualname__ = "ScuffingIntegralTemperatureRatingMethod"

    @classmethod
    def wrapper_type(
        cls: "Type[EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod]",
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
        cls: "Type[EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod]",
    ) -> "_493.ScuffingIntegralTemperatureRatingMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _493.ScuffingIntegralTemperatureRatingMethod
        """
        return _493.ScuffingIntegralTemperatureRatingMethod

    @classmethod
    def implicit_type(
        cls: "Type[EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _493.ScuffingIntegralTemperatureRatingMethod.type_()

    @property
    def selected_value(self: "Self") -> "_493.ScuffingIntegralTemperatureRatingMethod":
        """mastapy._private.gears.rating.cylindrical.ScuffingIntegralTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: "Self",
    ) -> "List[_493.ScuffingIntegralTemperatureRatingMethod]":
        """List[mastapy._private.gears.rating.cylindrical.ScuffingIntegralTemperatureRatingMethod]

        Note:
            This property is readonly.
        """
        return None
