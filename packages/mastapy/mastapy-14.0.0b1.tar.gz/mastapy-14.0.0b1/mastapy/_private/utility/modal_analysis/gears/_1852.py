"""OrderForTE"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ORDER_FOR_TE = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "OrderForTE"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility.modal_analysis.gears import (
        _1847,
        _1848,
        _1850,
        _1851,
        _1853,
        _1854,
        _1855,
        _1856,
        _1857,
    )

    Self = TypeVar("Self", bound="OrderForTE")
    CastSelf = TypeVar("CastSelf", bound="OrderForTE._Cast_OrderForTE")


__docformat__ = "restructuredtext en"
__all__ = ("OrderForTE",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_OrderForTE:
    """Special nested class for casting OrderForTE to subclasses."""

    __parent__: "OrderForTE"

    @property
    def gear_mesh_for_te(self: "CastSelf") -> "_1847.GearMeshForTE":
        from mastapy._private.utility.modal_analysis.gears import _1847

        return self.__parent__._cast(_1847.GearMeshForTE)

    @property
    def gear_order_for_te(self: "CastSelf") -> "_1848.GearOrderForTE":
        from mastapy._private.utility.modal_analysis.gears import _1848

        return self.__parent__._cast(_1848.GearOrderForTE)

    @property
    def harmonic_order_for_te(self: "CastSelf") -> "_1850.HarmonicOrderForTE":
        from mastapy._private.utility.modal_analysis.gears import _1850

        return self.__parent__._cast(_1850.HarmonicOrderForTE)

    @property
    def label_only_order(self: "CastSelf") -> "_1851.LabelOnlyOrder":
        from mastapy._private.utility.modal_analysis.gears import _1851

        return self.__parent__._cast(_1851.LabelOnlyOrder)

    @property
    def order_selector(self: "CastSelf") -> "_1853.OrderSelector":
        from mastapy._private.utility.modal_analysis.gears import _1853

        return self.__parent__._cast(_1853.OrderSelector)

    @property
    def order_with_radius(self: "CastSelf") -> "_1854.OrderWithRadius":
        from mastapy._private.utility.modal_analysis.gears import _1854

        return self.__parent__._cast(_1854.OrderWithRadius)

    @property
    def rolling_bearing_order(self: "CastSelf") -> "_1855.RollingBearingOrder":
        from mastapy._private.utility.modal_analysis.gears import _1855

        return self.__parent__._cast(_1855.RollingBearingOrder)

    @property
    def shaft_order_for_te(self: "CastSelf") -> "_1856.ShaftOrderForTE":
        from mastapy._private.utility.modal_analysis.gears import _1856

        return self.__parent__._cast(_1856.ShaftOrderForTE)

    @property
    def user_defined_order_for_te(self: "CastSelf") -> "_1857.UserDefinedOrderForTE":
        from mastapy._private.utility.modal_analysis.gears import _1857

        return self.__parent__._cast(_1857.UserDefinedOrderForTE)

    @property
    def order_for_te(self: "CastSelf") -> "OrderForTE":
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
class OrderForTE(_0.APIBase):
    """OrderForTE

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ORDER_FOR_TE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def frequency_offset(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.FrequencyOffset

        if temp is None:
            return 0.0

        return temp

    @frequency_offset.setter
    @enforce_parameter_types
    def frequency_offset(self: "Self", value: "float") -> None:
        self.wrapped.FrequencyOffset = float(value) if value is not None else 0.0

    @property
    def name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def order(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Order

        if temp is None:
            return 0.0

        return temp

    @property
    def children(self: "Self") -> "List[OrderForTE]":
        """List[mastapy._private.utility.modal_analysis.gears.OrderForTE]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Children

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: "Self", report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_OrderForTE":
        """Cast to another type.

        Returns:
            _Cast_OrderForTE
        """
        return _Cast_OrderForTE(self)
