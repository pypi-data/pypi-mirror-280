"""ShaftDamageResultsTableAndChart"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility.report import _1804
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SHAFT_DAMAGE_RESULTS_TABLE_AND_CHART = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftDamageResultsTableAndChart"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.enums import _1870
    from mastapy._private.utility.report import _1817, _1818, _1819, _1811

    Self = TypeVar("Self", bound="ShaftDamageResultsTableAndChart")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftDamageResultsTableAndChart",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShaftDamageResultsTableAndChart:
    """Special nested class for casting ShaftDamageResultsTableAndChart to subclasses."""

    __parent__: "ShaftDamageResultsTableAndChart"

    @property
    def custom_report_chart(self: "CastSelf") -> "_1804.CustomReportChart":
        return self.__parent__._cast(_1804.CustomReportChart)

    @property
    def custom_report_multi_property_item(
        self: "CastSelf",
    ) -> "_1817.CustomReportMultiPropertyItem":
        pass

        from mastapy._private.utility.report import _1817

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
    def shaft_damage_results_table_and_chart(
        self: "CastSelf",
    ) -> "ShaftDamageResultsTableAndChart":
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
class ShaftDamageResultsTableAndChart(_1804.CustomReportChart):
    """ShaftDamageResultsTableAndChart

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SHAFT_DAMAGE_RESULTS_TABLE_AND_CHART

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def display(self: "Self") -> "_1870.TableAndChartOptions":
        """mastapy._private.utility.enums.TableAndChartOptions"""
        temp = self.wrapped.Display

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Enums.TableAndChartOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.utility.enums._1870", "TableAndChartOptions"
        )(value)

    @display.setter
    @enforce_parameter_types
    def display(self: "Self", value: "_1870.TableAndChartOptions") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Enums.TableAndChartOptions"
        )
        self.wrapped.Display = value

    @property
    def cast_to(self: "Self") -> "_Cast_ShaftDamageResultsTableAndChart":
        """Cast to another type.

        Returns:
            _Cast_ShaftDamageResultsTableAndChart
        """
        return _Cast_ShaftDamageResultsTableAndChart(self)
