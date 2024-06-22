"""Implementations of 'ListWithSelectedItem' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._private.gears.manufacturing.cylindrical import _648
from mastapy._private._internal import constructor, conversion, mixins
from mastapy._private._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_LIST_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Property", "ListWithSelectedItem"
)

if TYPE_CHECKING:
    from typing import List, Type, Any, TypeVar

    Self = TypeVar(
        "Self", bound="ListWithSelectedItem_CylindricalSetManufacturingConfig"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ListWithSelectedItem_CylindricalSetManufacturingConfig",)


class ListWithSelectedItem_CylindricalSetManufacturingConfig(
    _648.CylindricalSetManufacturingConfig, mixins.ListWithSelectedItemMixin
):
    """ListWithSelectedItem_CylindricalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalSetManufacturingConfig' types.
    """

    __qualname__ = "CylindricalSetManufacturingConfig"

    def __init__(self: "Self", instance_to_wrap: "Any") -> None:
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(
        cls: "Type[ListWithSelectedItem_CylindricalSetManufacturingConfig]",
    ) -> "Any":
        """Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(
        cls: "Type[ListWithSelectedItem_CylindricalSetManufacturingConfig]",
    ) -> "Any":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.

        Returns:
            Any
        """
        return _648.CylindricalSetManufacturingConfig.TYPE

    @property
    def selected_value(self: "Self") -> "_648.CylindricalSetManufacturingConfig":
        """mastapy._private.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_values(
        self: "Self",
    ) -> "List[_648.CylindricalSetManufacturingConfig]":
        """List[mastapy._private.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig]

        Note:
            This property is readonly.
        """
        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value
