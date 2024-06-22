"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.bearings.bearing_results.rolling import _2025
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar(
        "Self", bound="EnumWithSelectedValue_FrictionModelForGyroscopicMoment"
    )


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_FrictionModelForGyroscopicMoment",)


class EnumWithSelectedValue_FrictionModelForGyroscopicMoment(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_FrictionModelForGyroscopicMoment

    A specific implementation of 'EnumWithSelectedValue' for 'FrictionModelForGyroscopicMoment' types.
    """

    __qualname__ = "FrictionModelForGyroscopicMoment"

    @classmethod
    def wrapper_type(
        cls: "Type[EnumWithSelectedValue_FrictionModelForGyroscopicMoment]",
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
        cls: "Type[EnumWithSelectedValue_FrictionModelForGyroscopicMoment]",
    ) -> "_2025.FrictionModelForGyroscopicMoment":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _2025.FrictionModelForGyroscopicMoment
        """
        return _2025.FrictionModelForGyroscopicMoment

    @classmethod
    def implicit_type(
        cls: "Type[EnumWithSelectedValue_FrictionModelForGyroscopicMoment]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _2025.FrictionModelForGyroscopicMoment.type_()

    @property
    def selected_value(self: "Self") -> "_2025.FrictionModelForGyroscopicMoment":
        """mastapy._private.bearings.bearing_results.rolling.FrictionModelForGyroscopicMoment

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: "Self",
    ) -> "List[_2025.FrictionModelForGyroscopicMoment]":
        """List[mastapy._private.bearings.bearing_results.rolling.FrictionModelForGyroscopicMoment]

        Note:
            This property is readonly.
        """
        return None
