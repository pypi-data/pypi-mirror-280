"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from mastapy._private.system_model.analyses_and_results.harmonic_analyses import _5899
from mastapy._private._internal import mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar(
        "Self", bound="EnumWithSelectedValue_HarmonicAnalysisTorqueInputType"
    )


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_HarmonicAnalysisTorqueInputType",)


class EnumWithSelectedValue_HarmonicAnalysisTorqueInputType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_HarmonicAnalysisTorqueInputType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicAnalysisTorqueInputType' types.
    """

    __qualname__ = "HarmonicAnalysisTorqueInputType"

    @classmethod
    def wrapper_type(
        cls: "Type[EnumWithSelectedValue_HarmonicAnalysisTorqueInputType]",
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
        cls: "Type[EnumWithSelectedValue_HarmonicAnalysisTorqueInputType]",
    ) -> "_5899.HarmonicAnalysisTorqueInputType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly

        Returns:
            _5899.HarmonicAnalysisTorqueInputType
        """
        return _5899.HarmonicAnalysisTorqueInputType

    @classmethod
    def implicit_type(
        cls: "Type[EnumWithSelectedValue_HarmonicAnalysisTorqueInputType]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _5899.HarmonicAnalysisTorqueInputType.type_()

    @property
    def selected_value(self: "Self") -> "_5899.HarmonicAnalysisTorqueInputType":
        """mastapy._private.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisTorqueInputType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: "Self") -> "List[_5899.HarmonicAnalysisTorqueInputType]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisTorqueInputType]

        Note:
            This property is readonly.
        """
        return None
