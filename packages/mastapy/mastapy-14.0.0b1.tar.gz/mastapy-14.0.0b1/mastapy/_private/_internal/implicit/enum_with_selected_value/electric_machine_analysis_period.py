"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.nodal_analysis.elmer import _176
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar("Self", bound="EnumWithSelectedValue_ElectricMachineAnalysisPeriod")


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ElectricMachineAnalysisPeriod",)


class EnumWithSelectedValue_ElectricMachineAnalysisPeriod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ElectricMachineAnalysisPeriod

    A specific implementation of 'EnumWithSelectedValue' for 'ElectricMachineAnalysisPeriod' types.
    """

    __qualname__ = "ElectricMachineAnalysisPeriod"

    @classmethod
    def wrapper_type(
        cls: "Type[EnumWithSelectedValue_ElectricMachineAnalysisPeriod]",
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
        cls: "Type[EnumWithSelectedValue_ElectricMachineAnalysisPeriod]",
    ) -> "_176.ElectricMachineAnalysisPeriod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _176.ElectricMachineAnalysisPeriod
        """
        return _176.ElectricMachineAnalysisPeriod

    @classmethod
    def implicit_type(
        cls: "Type[EnumWithSelectedValue_ElectricMachineAnalysisPeriod]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _176.ElectricMachineAnalysisPeriod.type_()

    @property
    def selected_value(self: "Self") -> "_176.ElectricMachineAnalysisPeriod":
        """mastapy._private.nodal_analysis.elmer.ElectricMachineAnalysisPeriod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_176.ElectricMachineAnalysisPeriod]":
        """List[mastapy._private.nodal_analysis.elmer.ElectricMachineAnalysisPeriod]

        Note:
            This property is readonly.
        """
        return None
