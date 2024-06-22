"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.gears.gear_set_pareto_optimiser import _926
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar("Self", bound="EnumWithSelectedValue_CandidateDisplayChoice")


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CandidateDisplayChoice",)


class EnumWithSelectedValue_CandidateDisplayChoice(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_CandidateDisplayChoice

    A specific implementation of 'EnumWithSelectedValue' for 'CandidateDisplayChoice' types.
    """

    __qualname__ = "CandidateDisplayChoice"

    @classmethod
    def wrapper_type(
        cls: "Type[EnumWithSelectedValue_CandidateDisplayChoice]",
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
        cls: "Type[EnumWithSelectedValue_CandidateDisplayChoice]",
    ) -> "_926.CandidateDisplayChoice":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _926.CandidateDisplayChoice
        """
        return _926.CandidateDisplayChoice

    @classmethod
    def implicit_type(
        cls: "Type[EnumWithSelectedValue_CandidateDisplayChoice]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _926.CandidateDisplayChoice.type_()

    @property
    def selected_value(self: "Self") -> "_926.CandidateDisplayChoice":
        """mastapy._private.gears.gear_set_pareto_optimiser.CandidateDisplayChoice

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_926.CandidateDisplayChoice]":
        """List[mastapy._private.gears.gear_set_pareto_optimiser.CandidateDisplayChoice]

        Note:
            This property is readonly.
        """
        return None
