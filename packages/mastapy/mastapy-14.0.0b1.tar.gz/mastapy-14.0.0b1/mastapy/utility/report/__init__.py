"""Subpackage."""

from typing import TYPE_CHECKING as __tc


if __tc:
    from mastapy._private.utility.report._1790 import AdHocCustomTable
    from mastapy._private.utility.report._1791 import AxisSettings
    from mastapy._private.utility.report._1792 import BlankRow
    from mastapy._private.utility.report._1793 import CadPageOrientation
    from mastapy._private.utility.report._1794 import CadPageSize
    from mastapy._private.utility.report._1795 import CadTableBorderType
    from mastapy._private.utility.report._1796 import ChartDefinition
    from mastapy._private.utility.report._1797 import SMTChartPointShape
    from mastapy._private.utility.report._1798 import CustomChart
    from mastapy._private.utility.report._1799 import CustomDrawing
    from mastapy._private.utility.report._1800 import CustomGraphic
    from mastapy._private.utility.report._1801 import CustomImage
    from mastapy._private.utility.report._1802 import CustomReport
    from mastapy._private.utility.report._1803 import CustomReportCadDrawing
    from mastapy._private.utility.report._1804 import CustomReportChart
    from mastapy._private.utility.report._1805 import CustomReportChartItem
    from mastapy._private.utility.report._1806 import CustomReportColumn
    from mastapy._private.utility.report._1807 import CustomReportColumns
    from mastapy._private.utility.report._1808 import CustomReportDefinitionItem
    from mastapy._private.utility.report._1809 import CustomReportHorizontalLine
    from mastapy._private.utility.report._1810 import CustomReportHtmlItem
    from mastapy._private.utility.report._1811 import CustomReportItem
    from mastapy._private.utility.report._1812 import CustomReportItemContainer
    from mastapy._private.utility.report._1813 import (
        CustomReportItemContainerCollection,
    )
    from mastapy._private.utility.report._1814 import (
        CustomReportItemContainerCollectionBase,
    )
    from mastapy._private.utility.report._1815 import (
        CustomReportItemContainerCollectionItem,
    )
    from mastapy._private.utility.report._1816 import CustomReportKey
    from mastapy._private.utility.report._1817 import CustomReportMultiPropertyItem
    from mastapy._private.utility.report._1818 import CustomReportMultiPropertyItemBase
    from mastapy._private.utility.report._1819 import CustomReportNameableItem
    from mastapy._private.utility.report._1820 import CustomReportNamedItem
    from mastapy._private.utility.report._1821 import CustomReportPropertyItem
    from mastapy._private.utility.report._1822 import CustomReportStatusItem
    from mastapy._private.utility.report._1823 import CustomReportTab
    from mastapy._private.utility.report._1824 import CustomReportTabs
    from mastapy._private.utility.report._1825 import CustomReportText
    from mastapy._private.utility.report._1826 import CustomRow
    from mastapy._private.utility.report._1827 import CustomSubReport
    from mastapy._private.utility.report._1828 import CustomTable
    from mastapy._private.utility.report._1829 import DefinitionBooleanCheckOptions
    from mastapy._private.utility.report._1830 import DynamicCustomReportItem
    from mastapy._private.utility.report._1831 import FontStyle
    from mastapy._private.utility.report._1832 import FontWeight
    from mastapy._private.utility.report._1833 import HeadingSize
    from mastapy._private.utility.report._1834 import SimpleChartDefinition
    from mastapy._private.utility.report._1835 import UserTextRow
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.utility.report._1790": ["AdHocCustomTable"],
        "_private.utility.report._1791": ["AxisSettings"],
        "_private.utility.report._1792": ["BlankRow"],
        "_private.utility.report._1793": ["CadPageOrientation"],
        "_private.utility.report._1794": ["CadPageSize"],
        "_private.utility.report._1795": ["CadTableBorderType"],
        "_private.utility.report._1796": ["ChartDefinition"],
        "_private.utility.report._1797": ["SMTChartPointShape"],
        "_private.utility.report._1798": ["CustomChart"],
        "_private.utility.report._1799": ["CustomDrawing"],
        "_private.utility.report._1800": ["CustomGraphic"],
        "_private.utility.report._1801": ["CustomImage"],
        "_private.utility.report._1802": ["CustomReport"],
        "_private.utility.report._1803": ["CustomReportCadDrawing"],
        "_private.utility.report._1804": ["CustomReportChart"],
        "_private.utility.report._1805": ["CustomReportChartItem"],
        "_private.utility.report._1806": ["CustomReportColumn"],
        "_private.utility.report._1807": ["CustomReportColumns"],
        "_private.utility.report._1808": ["CustomReportDefinitionItem"],
        "_private.utility.report._1809": ["CustomReportHorizontalLine"],
        "_private.utility.report._1810": ["CustomReportHtmlItem"],
        "_private.utility.report._1811": ["CustomReportItem"],
        "_private.utility.report._1812": ["CustomReportItemContainer"],
        "_private.utility.report._1813": ["CustomReportItemContainerCollection"],
        "_private.utility.report._1814": ["CustomReportItemContainerCollectionBase"],
        "_private.utility.report._1815": ["CustomReportItemContainerCollectionItem"],
        "_private.utility.report._1816": ["CustomReportKey"],
        "_private.utility.report._1817": ["CustomReportMultiPropertyItem"],
        "_private.utility.report._1818": ["CustomReportMultiPropertyItemBase"],
        "_private.utility.report._1819": ["CustomReportNameableItem"],
        "_private.utility.report._1820": ["CustomReportNamedItem"],
        "_private.utility.report._1821": ["CustomReportPropertyItem"],
        "_private.utility.report._1822": ["CustomReportStatusItem"],
        "_private.utility.report._1823": ["CustomReportTab"],
        "_private.utility.report._1824": ["CustomReportTabs"],
        "_private.utility.report._1825": ["CustomReportText"],
        "_private.utility.report._1826": ["CustomRow"],
        "_private.utility.report._1827": ["CustomSubReport"],
        "_private.utility.report._1828": ["CustomTable"],
        "_private.utility.report._1829": ["DefinitionBooleanCheckOptions"],
        "_private.utility.report._1830": ["DynamicCustomReportItem"],
        "_private.utility.report._1831": ["FontStyle"],
        "_private.utility.report._1832": ["FontWeight"],
        "_private.utility.report._1833": ["HeadingSize"],
        "_private.utility.report._1834": ["SimpleChartDefinition"],
        "_private.utility.report._1835": ["UserTextRow"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AdHocCustomTable",
    "AxisSettings",
    "BlankRow",
    "CadPageOrientation",
    "CadPageSize",
    "CadTableBorderType",
    "ChartDefinition",
    "SMTChartPointShape",
    "CustomChart",
    "CustomDrawing",
    "CustomGraphic",
    "CustomImage",
    "CustomReport",
    "CustomReportCadDrawing",
    "CustomReportChart",
    "CustomReportChartItem",
    "CustomReportColumn",
    "CustomReportColumns",
    "CustomReportDefinitionItem",
    "CustomReportHorizontalLine",
    "CustomReportHtmlItem",
    "CustomReportItem",
    "CustomReportItemContainer",
    "CustomReportItemContainerCollection",
    "CustomReportItemContainerCollectionBase",
    "CustomReportItemContainerCollectionItem",
    "CustomReportKey",
    "CustomReportMultiPropertyItem",
    "CustomReportMultiPropertyItemBase",
    "CustomReportNameableItem",
    "CustomReportNamedItem",
    "CustomReportPropertyItem",
    "CustomReportStatusItem",
    "CustomReportTab",
    "CustomReportTabs",
    "CustomReportText",
    "CustomRow",
    "CustomSubReport",
    "CustomTable",
    "DefinitionBooleanCheckOptions",
    "DynamicCustomReportItem",
    "FontStyle",
    "FontWeight",
    "HeadingSize",
    "SimpleChartDefinition",
    "UserTextRow",
)
