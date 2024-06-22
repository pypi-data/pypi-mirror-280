"""CylindricalGearTableWithMGCharts"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility.report import _1828
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TABLE_WITH_MG_CHARTS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearTableWithMGCharts"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.cylindrical import _1064
    from mastapy._private.utility.report import _1817, _1818, _1819, _1811

    Self = TypeVar("Self", bound="CylindricalGearTableWithMGCharts")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearTableWithMGCharts",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearTableWithMGCharts:
    """Special nested class for casting CylindricalGearTableWithMGCharts to subclasses."""

    __parent__: "CylindricalGearTableWithMGCharts"

    @property
    def custom_table(self: "CastSelf") -> "_1828.CustomTable":
        return self.__parent__._cast(_1828.CustomTable)

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
    def cylindrical_gear_table_with_mg_charts(
        self: "CastSelf",
    ) -> "CylindricalGearTableWithMGCharts":
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
class CylindricalGearTableWithMGCharts(_1828.CustomTable):
    """CylindricalGearTableWithMGCharts

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_TABLE_WITH_MG_CHARTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def chart_height(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.ChartHeight

        if temp is None:
            return 0

        return temp

    @chart_height.setter
    @enforce_parameter_types
    def chart_height(self: "Self", value: "int") -> None:
        self.wrapped.ChartHeight = int(value) if value is not None else 0

    @property
    def chart_width(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.ChartWidth

        if temp is None:
            return 0

        return temp

    @chart_width.setter
    @enforce_parameter_types
    def chart_width(self: "Self", value: "int") -> None:
        self.wrapped.ChartWidth = int(value) if value is not None else 0

    @property
    def item_detail(self: "Self") -> "_1064.CylindricalGearTableMGItemDetail":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearTableMGItemDetail"""
        temp = self.wrapped.ItemDetail

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearTableMGItemDetail",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1064",
            "CylindricalGearTableMGItemDetail",
        )(value)

    @item_detail.setter
    @enforce_parameter_types
    def item_detail(
        self: "Self", value: "_1064.CylindricalGearTableMGItemDetail"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearTableMGItemDetail",
        )
        self.wrapped.ItemDetail = value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearTableWithMGCharts":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearTableWithMGCharts
        """
        return _Cast_CylindricalGearTableWithMGCharts(self)
