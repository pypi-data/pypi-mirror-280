"""SKFModuleResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SKF_MODULE_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "SKFModuleResults"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.bearings.bearing_results.rolling.skf_module import (
        _2129,
        _2131,
        _2132,
        _2133,
        _2134,
        _2136,
        _2140,
        _2144,
        _2152,
        _2153,
    )

    Self = TypeVar("Self", bound="SKFModuleResults")
    CastSelf = TypeVar("CastSelf", bound="SKFModuleResults._Cast_SKFModuleResults")


__docformat__ = "restructuredtext en"
__all__ = ("SKFModuleResults",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SKFModuleResults:
    """Special nested class for casting SKFModuleResults to subclasses."""

    __parent__: "SKFModuleResults"

    @property
    def skf_module_results(self: "CastSelf") -> "SKFModuleResults":
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
class SKFModuleResults(_0.APIBase):
    """SKFModuleResults

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SKF_MODULE_RESULTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def adjusted_speed(self: "Self") -> "_2129.AdjustedSpeed":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.AdjustedSpeed

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_loads(self: "Self") -> "_2131.BearingLoads":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.BearingLoads

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_rating_life(self: "Self") -> "_2132.BearingRatingLife":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.BearingRatingLife

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingRatingLife

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_axial_load_carrying_capacity(
        self: "Self",
    ) -> "_2133.DynamicAxialLoadCarryingCapacity":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.DynamicAxialLoadCarryingCapacity

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAxialLoadCarryingCapacity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def frequencies(self: "Self") -> "_2134.Frequencies":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.Frequencies

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Frequencies

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def friction(self: "Self") -> "_2136.Friction":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.Friction

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Friction

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def grease_life_and_relubrication_interval(
        self: "Self",
    ) -> "_2140.GreaseLifeAndRelubricationInterval":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.GreaseLifeAndRelubricationInterval

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GreaseLifeAndRelubricationInterval

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_load(self: "Self") -> "_2144.MinimumLoad":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.MinimumLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_safety_factors(self: "Self") -> "_2152.StaticSafetyFactors":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.StaticSafetyFactors

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def viscosities(self: "Self") -> "_2153.Viscosities":
        """mastapy._private.bearings.bearing_results.rolling.skf_module.Viscosities

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Viscosities

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: "Self") -> "_Cast_SKFModuleResults":
        """Cast to another type.

        Returns:
            _Cast_SKFModuleResults
        """
        return _Cast_SKFModuleResults(self)
