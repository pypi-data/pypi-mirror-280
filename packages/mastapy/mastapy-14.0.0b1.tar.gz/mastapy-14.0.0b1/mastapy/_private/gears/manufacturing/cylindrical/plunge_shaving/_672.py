"""PlungeShaverGeneration"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PLUNGE_SHAVER_GENERATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "PlungeShaverGeneration",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.math_utility import _1535
    from mastapy._private.gears.gear_designs.cylindrical import _1028
    from mastapy._private.gears.manufacturing.cylindrical.plunge_shaving import (
        _665,
        _679,
    )

    Self = TypeVar("Self", bound="PlungeShaverGeneration")
    CastSelf = TypeVar(
        "CastSelf", bound="PlungeShaverGeneration._Cast_PlungeShaverGeneration"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverGeneration",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PlungeShaverGeneration:
    """Special nested class for casting PlungeShaverGeneration to subclasses."""

    __parent__: "PlungeShaverGeneration"

    @property
    def plunge_shaver_generation(self: "CastSelf") -> "PlungeShaverGeneration":
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
class PlungeShaverGeneration(_0.APIBase):
    """PlungeShaverGeneration

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PLUNGE_SHAVER_GENERATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def calculated_conjugate_face_width(self: "Self") -> "_1535.Range":
        """mastapy._private.math_utility.Range

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedConjugateFaceWidth

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_start_of_active_profile_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def manufactured_end_of_active_profile_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturedEndOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def manufactured_start_of_active_profile_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturedStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_angle_unsigned(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftAngleUnsigned

        if temp is None:
            return 0.0

        return temp

    @property
    def crossed_axis_calculation_details(
        self: "Self",
    ) -> "_1028.CrossedAxisCylindricalGearPairLineContact":
        """mastapy._private.gears.gear_designs.cylindrical.CrossedAxisCylindricalGearPairLineContact

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrossedAxisCalculationDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def calculation_errors(self: "Self") -> "List[_665.CalculationError]":
        """List[mastapy._private.gears.manufacturing.cylindrical.plunge_shaving.CalculationError]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculationErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def points_of_interest_on_the_shaver(
        self: "Self",
    ) -> "List[_679.ShaverPointOfInterest]":
        """List[mastapy._private.gears.manufacturing.cylindrical.plunge_shaving.ShaverPointOfInterest]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointsOfInterestOnTheShaver

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
    def cast_to(self: "Self") -> "_Cast_PlungeShaverGeneration":
        """Cast to another type.

        Returns:
            _Cast_PlungeShaverGeneration
        """
        return _Cast_PlungeShaverGeneration(self)
