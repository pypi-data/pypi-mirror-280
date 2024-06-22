"""ScatterChartDefinition"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.utility_gui.charts import _1919
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SCATTER_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "ScatterChartDefinition"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility_gui.charts import _1904, _1911
    from mastapy._private.utility.report import _1796

    Self = TypeVar("Self", bound="ScatterChartDefinition")
    CastSelf = TypeVar(
        "CastSelf", bound="ScatterChartDefinition._Cast_ScatterChartDefinition"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ScatterChartDefinition",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ScatterChartDefinition:
    """Special nested class for casting ScatterChartDefinition to subclasses."""

    __parent__: "ScatterChartDefinition"

    @property
    def two_d_chart_definition(self: "CastSelf") -> "_1919.TwoDChartDefinition":
        return self.__parent__._cast(_1919.TwoDChartDefinition)

    @property
    def nd_chart_definition(self: "CastSelf") -> "_1911.NDChartDefinition":
        from mastapy._private.utility_gui.charts import _1911

        return self.__parent__._cast(_1911.NDChartDefinition)

    @property
    def chart_definition(self: "CastSelf") -> "_1796.ChartDefinition":
        from mastapy._private.utility.report import _1796

        return self.__parent__._cast(_1796.ChartDefinition)

    @property
    def bubble_chart_definition(self: "CastSelf") -> "_1904.BubbleChartDefinition":
        from mastapy._private.utility_gui.charts import _1904

        return self.__parent__._cast(_1904.BubbleChartDefinition)

    @property
    def scatter_chart_definition(self: "CastSelf") -> "ScatterChartDefinition":
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
class ScatterChartDefinition(_1919.TwoDChartDefinition):
    """ScatterChartDefinition

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SCATTER_CHART_DEFINITION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def x_values(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def y_values(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def z_axis_title(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxisTitle

        if temp is None:
            return ""

        return temp

    @property
    def z_values(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ScatterChartDefinition":
        """Cast to another type.

        Returns:
            _Cast_ScatterChartDefinition
        """
        return _Cast_ScatterChartDefinition(self)
