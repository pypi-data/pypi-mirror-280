"""CustomTable"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.utility.report import _1817, _1826
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CUSTOM_TABLE = python_net_import("SMT.MastaAPI.Utility.Report", "CustomTable")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.cylindrical import _1065
    from mastapy._private.utility_gui.charts import _1907
    from mastapy._private.utility.report import _1818, _1819, _1811

    Self = TypeVar("Self", bound="CustomTable")
    CastSelf = TypeVar("CastSelf", bound="CustomTable._Cast_CustomTable")


__docformat__ = "restructuredtext en"
__all__ = ("CustomTable",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CustomTable:
    """Special nested class for casting CustomTable to subclasses."""

    __parent__: "CustomTable"

    @property
    def custom_report_multi_property_item(
        self: "CastSelf",
    ) -> "_1817.CustomReportMultiPropertyItem":
        return self.__parent__._cast(_1817.CustomReportMultiPropertyItem)

    @property
    def custom_report_multi_property_item_base(
        self: "CastSelf",
    ) -> "_1818.CustomReportMultiPropertyItemBase":
        from mastapy._private.utility.report import _1818

        return self.__parent__._cast(_1818.CustomReportMultiPropertyItemBase)

    @property
    def custom_report_nameable_item(
        self: "CastSelf",
    ) -> "_1819.CustomReportNameableItem":
        from mastapy._private.utility.report import _1819

        return self.__parent__._cast(_1819.CustomReportNameableItem)

    @property
    def custom_report_item(self: "CastSelf") -> "_1811.CustomReportItem":
        from mastapy._private.utility.report import _1811

        return self.__parent__._cast(_1811.CustomReportItem)

    @property
    def cylindrical_gear_table_with_mg_charts(
        self: "CastSelf",
    ) -> "_1065.CylindricalGearTableWithMGCharts":
        from mastapy._private.gears.gear_designs.cylindrical import _1065

        return self.__parent__._cast(_1065.CylindricalGearTableWithMGCharts)

    @property
    def custom_table_and_chart(self: "CastSelf") -> "_1907.CustomTableAndChart":
        from mastapy._private.utility_gui.charts import _1907

        return self.__parent__._cast(_1907.CustomTableAndChart)

    @property
    def custom_table(self: "CastSelf") -> "CustomTable":
        return self.__parent__

    def __getattr__(self: "CastSelf", name: str) -> "Any":
        try:
            return self.__getattribute__(name)
        except AttributeError:
            class_name = utility.camel(name)
            raise CastException(
                f'Detected an invalid cast. Cannot cast to type "{class_name}"'
            ) from None


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class CustomTable(_1817.CustomReportMultiPropertyItem[_1826.CustomRow]):
    """CustomTable

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CUSTOM_TABLE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def is_main_report_item(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IsMainReportItem

        if temp is None:
            return False

        return temp

    @is_main_report_item.setter
    @enforce_parameter_types
    def is_main_report_item(self: "Self", value: "bool") -> None:
        self.wrapped.IsMainReportItem = bool(value) if value is not None else False

    @property
    def cast_to(self: "Self") -> "_Cast_CustomTable":
        """Cast to another type.

        Returns:
            _Cast_CustomTable
        """
        return _Cast_CustomTable(self)
