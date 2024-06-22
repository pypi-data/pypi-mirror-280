"""CustomReportNameableItem"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.utility.report import _1811
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CUSTOM_REPORT_NAMEABLE_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportNameableItem"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.shafts import _20
    from mastapy._private.gears.gear_designs.cylindrical import _1065
    from mastapy._private.utility.report import (
        _1790,
        _1798,
        _1799,
        _1800,
        _1801,
        _1803,
        _1804,
        _1808,
        _1810,
        _1817,
        _1818,
        _1820,
        _1822,
        _1825,
        _1827,
        _1828,
        _1830,
    )
    from mastapy._private.utility_gui.charts import _1906, _1907
    from mastapy._private.bearings.bearing_results import _1999, _2000, _2003, _2011
    from mastapy._private.system_model.analyses_and_results.system_deflections.reporting import (
        _2934,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4495,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses.reporting import (
        _4830,
        _4834,
    )

    Self = TypeVar("Self", bound="CustomReportNameableItem")
    CastSelf = TypeVar(
        "CastSelf", bound="CustomReportNameableItem._Cast_CustomReportNameableItem"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportNameableItem",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CustomReportNameableItem:
    """Special nested class for casting CustomReportNameableItem to subclasses."""

    __parent__: "CustomReportNameableItem"

    @property
    def custom_report_item(self: "CastSelf") -> "_1811.CustomReportItem":
        return self.__parent__._cast(_1811.CustomReportItem)

    @property
    def shaft_damage_results_table_and_chart(
        self: "CastSelf",
    ) -> "_20.ShaftDamageResultsTableAndChart":
        from mastapy._private.shafts import _20

        return self.__parent__._cast(_20.ShaftDamageResultsTableAndChart)

    @property
    def cylindrical_gear_table_with_mg_charts(
        self: "CastSelf",
    ) -> "_1065.CylindricalGearTableWithMGCharts":
        from mastapy._private.gears.gear_designs.cylindrical import _1065

        return self.__parent__._cast(_1065.CylindricalGearTableWithMGCharts)

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
    def custom_report_cad_drawing(self: "CastSelf") -> "_1803.CustomReportCadDrawing":
        from mastapy._private.utility.report import _1803

        return self.__parent__._cast(_1803.CustomReportCadDrawing)

    @property
    def custom_report_chart(self: "CastSelf") -> "_1804.CustomReportChart":
        from mastapy._private.utility.report import _1804

        return self.__parent__._cast(_1804.CustomReportChart)

    @property
    def custom_report_definition_item(
        self: "CastSelf",
    ) -> "_1808.CustomReportDefinitionItem":
        from mastapy._private.utility.report import _1808

        return self.__parent__._cast(_1808.CustomReportDefinitionItem)

    @property
    def custom_report_html_item(self: "CastSelf") -> "_1810.CustomReportHtmlItem":
        from mastapy._private.utility.report import _1810

        return self.__parent__._cast(_1810.CustomReportHtmlItem)

    @property
    def custom_report_multi_property_item(
        self: "CastSelf",
    ) -> "_1817.CustomReportMultiPropertyItem":
        from mastapy._private.utility.report import _1817

        return self.__parent__._cast(_1817.CustomReportMultiPropertyItem)

    @property
    def custom_report_multi_property_item_base(
        self: "CastSelf",
    ) -> "_1818.CustomReportMultiPropertyItemBase":
        from mastapy._private.utility.report import _1818

        return self.__parent__._cast(_1818.CustomReportMultiPropertyItemBase)

    @property
    def custom_report_named_item(self: "CastSelf") -> "_1820.CustomReportNamedItem":
        from mastapy._private.utility.report import _1820

        return self.__parent__._cast(_1820.CustomReportNamedItem)

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
    def custom_table(self: "CastSelf") -> "_1828.CustomTable":
        from mastapy._private.utility.report import _1828

        return self.__parent__._cast(_1828.CustomTable)

    @property
    def dynamic_custom_report_item(self: "CastSelf") -> "_1830.DynamicCustomReportItem":
        from mastapy._private.utility.report import _1830

        return self.__parent__._cast(_1830.DynamicCustomReportItem)

    @property
    def custom_line_chart(self: "CastSelf") -> "_1906.CustomLineChart":
        from mastapy._private.utility_gui.charts import _1906

        return self.__parent__._cast(_1906.CustomLineChart)

    @property
    def custom_table_and_chart(self: "CastSelf") -> "_1907.CustomTableAndChart":
        from mastapy._private.utility_gui.charts import _1907

        return self.__parent__._cast(_1907.CustomTableAndChart)

    @property
    def loaded_ball_element_chart_reporter(
        self: "CastSelf",
    ) -> "_1999.LoadedBallElementChartReporter":
        from mastapy._private.bearings.bearing_results import _1999

        return self.__parent__._cast(_1999.LoadedBallElementChartReporter)

    @property
    def loaded_bearing_chart_reporter(
        self: "CastSelf",
    ) -> "_2000.LoadedBearingChartReporter":
        from mastapy._private.bearings.bearing_results import _2000

        return self.__parent__._cast(_2000.LoadedBearingChartReporter)

    @property
    def loaded_bearing_temperature_chart(
        self: "CastSelf",
    ) -> "_2003.LoadedBearingTemperatureChart":
        from mastapy._private.bearings.bearing_results import _2003

        return self.__parent__._cast(_2003.LoadedBearingTemperatureChart)

    @property
    def loaded_roller_element_chart_reporter(
        self: "CastSelf",
    ) -> "_2011.LoadedRollerElementChartReporter":
        from mastapy._private.bearings.bearing_results import _2011

        return self.__parent__._cast(_2011.LoadedRollerElementChartReporter)

    @property
    def shaft_system_deflection_sections_report(
        self: "CastSelf",
    ) -> "_2934.ShaftSystemDeflectionSectionsReport":
        from mastapy._private.system_model.analyses_and_results.system_deflections.reporting import (
            _2934,
        )

        return self.__parent__._cast(_2934.ShaftSystemDeflectionSectionsReport)

    @property
    def parametric_study_histogram(
        self: "CastSelf",
    ) -> "_4495.ParametricStudyHistogram":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4495,
        )

        return self.__parent__._cast(_4495.ParametricStudyHistogram)

    @property
    def campbell_diagram_report(self: "CastSelf") -> "_4830.CampbellDiagramReport":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.reporting import (
            _4830,
        )

        return self.__parent__._cast(_4830.CampbellDiagramReport)

    @property
    def per_mode_results_report(self: "CastSelf") -> "_4834.PerModeResultsReport":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.reporting import (
            _4834,
        )

        return self.__parent__._cast(_4834.PerModeResultsReport)

    @property
    def custom_report_nameable_item(self: "CastSelf") -> "CustomReportNameableItem":
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
class CustomReportNameableItem(_1811.CustomReportItem):
    """CustomReportNameableItem

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CUSTOM_REPORT_NAMEABLE_ITEM

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def name(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: "Self", value: "str") -> None:
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def x_position_for_cad(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.XPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @x_position_for_cad.setter
    @enforce_parameter_types
    def x_position_for_cad(self: "Self", value: "float") -> None:
        self.wrapped.XPositionForCAD = float(value) if value is not None else 0.0

    @property
    def y_position_for_cad(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.YPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @y_position_for_cad.setter
    @enforce_parameter_types
    def y_position_for_cad(self: "Self", value: "float") -> None:
        self.wrapped.YPositionForCAD = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_CustomReportNameableItem":
        """Cast to another type.

        Returns:
            _Cast_CustomReportNameableItem
        """
        return _Cast_CustomReportNameableItem(self)
