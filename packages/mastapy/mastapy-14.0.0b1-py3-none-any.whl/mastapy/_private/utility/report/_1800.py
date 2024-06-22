"""CustomGraphic"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.utility.report import _1808
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CUSTOM_GRAPHIC = python_net_import("SMT.MastaAPI.Utility.Report", "CustomGraphic")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.report import _1798, _1799, _1801, _1819, _1811
    from mastapy._private.bearings.bearing_results import _2000

    Self = TypeVar("Self", bound="CustomGraphic")
    CastSelf = TypeVar("CastSelf", bound="CustomGraphic._Cast_CustomGraphic")


__docformat__ = "restructuredtext en"
__all__ = ("CustomGraphic",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CustomGraphic:
    """Special nested class for casting CustomGraphic to subclasses."""

    __parent__: "CustomGraphic"

    @property
    def custom_report_definition_item(
        self: "CastSelf",
    ) -> "_1808.CustomReportDefinitionItem":
        return self.__parent__._cast(_1808.CustomReportDefinitionItem)

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
    def custom_chart(self: "CastSelf") -> "_1798.CustomChart":
        from mastapy._private.utility.report import _1798

        return self.__parent__._cast(_1798.CustomChart)

    @property
    def custom_drawing(self: "CastSelf") -> "_1799.CustomDrawing":
        from mastapy._private.utility.report import _1799

        return self.__parent__._cast(_1799.CustomDrawing)

    @property
    def custom_image(self: "CastSelf") -> "_1801.CustomImage":
        from mastapy._private.utility.report import _1801

        return self.__parent__._cast(_1801.CustomImage)

    @property
    def loaded_bearing_chart_reporter(
        self: "CastSelf",
    ) -> "_2000.LoadedBearingChartReporter":
        from mastapy._private.bearings.bearing_results import _2000

        return self.__parent__._cast(_2000.LoadedBearingChartReporter)

    @property
    def custom_graphic(self: "CastSelf") -> "CustomGraphic":
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
class CustomGraphic(_1808.CustomReportDefinitionItem):
    """CustomGraphic

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CUSTOM_GRAPHIC

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def height(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.Height

        if temp is None:
            return 0

        return temp

    @height.setter
    @enforce_parameter_types
    def height(self: "Self", value: "int") -> None:
        self.wrapped.Height = int(value) if value is not None else 0

    @property
    def height_for_cad(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.HeightForCAD

        if temp is None:
            return 0.0

        return temp

    @height_for_cad.setter
    @enforce_parameter_types
    def height_for_cad(self: "Self", value: "float") -> None:
        self.wrapped.HeightForCAD = float(value) if value is not None else 0.0

    @property
    def transposed(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.Transposed

        if temp is None:
            return False

        return temp

    @transposed.setter
    @enforce_parameter_types
    def transposed(self: "Self", value: "bool") -> None:
        self.wrapped.Transposed = bool(value) if value is not None else False

    @property
    def width(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.Width

        if temp is None:
            return 0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: "Self", value: "int") -> None:
        self.wrapped.Width = int(value) if value is not None else 0

    @property
    def width_for_cad(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WidthForCAD

        if temp is None:
            return 0.0

        return temp

    @width_for_cad.setter
    @enforce_parameter_types
    def width_for_cad(self: "Self", value: "float") -> None:
        self.wrapped.WidthForCAD = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_CustomGraphic":
        """Cast to another type.

        Returns:
            _Cast_CustomGraphic
        """
        return _Cast_CustomGraphic(self)
