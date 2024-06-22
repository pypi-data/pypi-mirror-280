"""CylindricalGearDesignConstraint"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.utility.model_validation import _1843
from mastapy._private._internal import (
    enum_with_selected_value_runtime,
    conversion,
    constructor,
    utility,
)
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_CONSTRAINT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearDesignConstraint"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility import _1635
    from mastapy._private.math_utility import _1535

    Self = TypeVar("Self", bound="CylindricalGearDesignConstraint")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearDesignConstraint._Cast_CylindricalGearDesignConstraint",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDesignConstraint",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearDesignConstraint:
    """Special nested class for casting CylindricalGearDesignConstraint to subclasses."""

    __parent__: "CylindricalGearDesignConstraint"

    @property
    def cylindrical_gear_design_constraint(
        self: "CastSelf",
    ) -> "CylindricalGearDesignConstraint":
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
class CylindricalGearDesignConstraint(_0.APIBase):
    """CylindricalGearDesignConstraint

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_DESIGN_CONSTRAINT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def class_of_error(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_StatusItemSeverity":
        """EnumWithSelectedValue[mastapy._private.utility.model_validation.StatusItemSeverity]"""
        temp = self.wrapped.ClassOfError

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_StatusItemSeverity.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @class_of_error.setter
    @enforce_parameter_types
    def class_of_error(self: "Self", value: "_1843.StatusItemSeverity") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_StatusItemSeverity.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ClassOfError = value

    @property
    def integer_range(self: "Self") -> "_1635.IntegerRange":
        """mastapy._private.utility.IntegerRange"""
        temp = self.wrapped.IntegerRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @integer_range.setter
    @enforce_parameter_types
    def integer_range(self: "Self", value: "_1635.IntegerRange") -> None:
        self.wrapped.IntegerRange = value.wrapped

    @property
    def is_active(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IsActive

        if temp is None:
            return False

        return temp

    @is_active.setter
    @enforce_parameter_types
    def is_active(self: "Self", value: "bool") -> None:
        self.wrapped.IsActive = bool(value) if value is not None else False

    @property
    def property_(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Property

        if temp is None:
            return ""

        return temp

    @property
    def range(self: "Self") -> "_1535.Range":
        """mastapy._private.math_utility.Range"""
        temp = self.wrapped.Range

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @range.setter
    @enforce_parameter_types
    def range(self: "Self", value: "_1535.Range") -> None:
        self.wrapped.Range = value.wrapped

    @property
    def unit(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Unit

        if temp is None:
            return ""

        return temp

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

    def delete(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.Delete()

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
    def cast_to(self: "Self") -> "_Cast_CylindricalGearDesignConstraint":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearDesignConstraint
        """
        return _Cast_CylindricalGearDesignConstraint(self)
