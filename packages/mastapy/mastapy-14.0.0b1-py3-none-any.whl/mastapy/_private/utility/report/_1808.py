"""CustomReportDefinitionItem"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.utility.report import _1819
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_CUSTOM_REPORT_DEFINITION_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportDefinitionItem"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.report import (
        _1790,
        _1798,
        _1799,
        _1800,
        _1801,
        _1810,
        _1822,
        _1825,
        _1827,
        _1811,
    )
    from mastapy._private.bearings.bearing_results import _2000
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4495,
    )

    Self = TypeVar("Self", bound="CustomReportDefinitionItem")
    CastSelf = TypeVar(
        "CastSelf", bound="CustomReportDefinitionItem._Cast_CustomReportDefinitionItem"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportDefinitionItem",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CustomReportDefinitionItem:
    """Special nested class for casting CustomReportDefinitionItem to subclasses."""

    __parent__: "CustomReportDefinitionItem"

    @property
    def custom_report_nameable_item(
        self: "CastSelf",
    ) -> "_1819.CustomReportNameableItem":
        return self.__parent__._cast(_1819.CustomReportNameableItem)

    @property
    def custom_report_item(self: "CastSelf") -> "_1811.CustomReportItem":
        from mastapy._private.utility.report import _1811

        return self.__parent__._cast(_1811.CustomReportItem)

    @property
    def ad_hoc_custom_table(self: "CastSelf") -> "_1790.AdHocCustomTable":
        from mastapy._private.utility.report import _1790

        return self.__parent__._cast(_1790.AdHocCustomTable)

    @property
    def custom_chart(self: "CastSelf") -> "_1798.CustomChart":
        from mastapy._private.utility.report import _1798

        return self.__parent__._cast(_1798.CustomChart)

    @property
    def custom_drawing(self: "CastSelf") -> "_1799.CustomDrawing":
        from mastapy._private.utility.report import _1799

        return self.__parent__._cast(_1799.CustomDrawing)

    @property
    def custom_graphic(self: "CastSelf") -> "_1800.CustomGraphic":
        from mastapy._private.utility.report import _1800

        return self.__parent__._cast(_1800.CustomGraphic)

    @property
    def custom_image(self: "CastSelf") -> "_1801.CustomImage":
        from mastapy._private.utility.report import _1801

        return self.__parent__._cast(_1801.CustomImage)

    @property
    def custom_report_html_item(self: "CastSelf") -> "_1810.CustomReportHtmlItem":
        from mastapy._private.utility.report import _1810

        return self.__parent__._cast(_1810.CustomReportHtmlItem)

    @property
    def custom_report_status_item(self: "CastSelf") -> "_1822.CustomReportStatusItem":
        from mastapy._private.utility.report import _1822

        return self.__parent__._cast(_1822.CustomReportStatusItem)

    @property
    def custom_report_text(self: "CastSelf") -> "_1825.CustomReportText":
        from mastapy._private.utility.report import _1825

        return self.__parent__._cast(_1825.CustomReportText)

    @property
    def custom_sub_report(self: "CastSelf") -> "_1827.CustomSubReport":
        from mastapy._private.utility.report import _1827

        return self.__parent__._cast(_1827.CustomSubReport)

    @property
    def loaded_bearing_chart_reporter(
        self: "CastSelf",
    ) -> "_2000.LoadedBearingChartReporter":
        from mastapy._private.bearings.bearing_results import _2000

        return self.__parent__._cast(_2000.LoadedBearingChartReporter)

    @property
    def parametric_study_histogram(
        self: "CastSelf",
    ) -> "_4495.ParametricStudyHistogram":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4495,
        )

        return self.__parent__._cast(_4495.ParametricStudyHistogram)

    @property
    def custom_report_definition_item(self: "CastSelf") -> "CustomReportDefinitionItem":
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
class CustomReportDefinitionItem(_1819.CustomReportNameableItem):
    """CustomReportDefinitionItem

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CUSTOM_REPORT_DEFINITION_ITEM

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CustomReportDefinitionItem":
        """Cast to another type.

        Returns:
            _Cast_CustomReportDefinitionItem
        """
        return _Cast_CustomReportDefinitionItem(self)
