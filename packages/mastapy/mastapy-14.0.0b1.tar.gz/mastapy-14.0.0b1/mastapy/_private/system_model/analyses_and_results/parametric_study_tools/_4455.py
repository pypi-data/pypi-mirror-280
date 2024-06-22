"""DesignOfExperimentsVariableSetter"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
    _4456,
)
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_DESIGN_OF_EXPERIMENTS_VARIABLE_SETTER = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "DesignOfExperimentsVariableSetter",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    Self = TypeVar("Self", bound="DesignOfExperimentsVariableSetter")
    CastSelf = TypeVar(
        "CastSelf",
        bound="DesignOfExperimentsVariableSetter._Cast_DesignOfExperimentsVariableSetter",
    )


__docformat__ = "restructuredtext en"
__all__ = ("DesignOfExperimentsVariableSetter",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_DesignOfExperimentsVariableSetter:
    """Special nested class for casting DesignOfExperimentsVariableSetter to subclasses."""

    __parent__: "DesignOfExperimentsVariableSetter"

    @property
    def design_of_experiments_variable_setter(
        self: "CastSelf",
    ) -> "DesignOfExperimentsVariableSetter":
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
class DesignOfExperimentsVariableSetter(_0.APIBase):
    """DesignOfExperimentsVariableSetter

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _DESIGN_OF_EXPERIMENTS_VARIABLE_SETTER

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def current_design_value(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentDesignValue

        if temp is None:
            return 0.0

        return temp

    @property
    def define_using_range(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.DefineUsingRange

        if temp is None:
            return False

        return temp

    @define_using_range.setter
    @enforce_parameter_types
    def define_using_range(self: "Self", value: "bool") -> None:
        self.wrapped.DefineUsingRange = bool(value) if value is not None else False

    @property
    def end_value(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EndValue

        if temp is None:
            return 0.0

        return temp

    @end_value.setter
    @enforce_parameter_types
    def end_value(self: "Self", value: "float") -> None:
        self.wrapped.EndValue = float(value) if value is not None else 0.0

    @property
    def integer_end_value(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.IntegerEndValue

        if temp is None:
            return 0

        return temp

    @integer_end_value.setter
    @enforce_parameter_types
    def integer_end_value(self: "Self", value: "int") -> None:
        self.wrapped.IntegerEndValue = int(value) if value is not None else 0

    @property
    def integer_start_value(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.IntegerStartValue

        if temp is None:
            return 0

        return temp

    @integer_start_value.setter
    @enforce_parameter_types
    def integer_start_value(self: "Self", value: "int") -> None:
        self.wrapped.IntegerStartValue = int(value) if value is not None else 0

    @property
    def integer_value(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.IntegerValue

        if temp is None:
            return 0

        return temp

    @integer_value.setter
    @enforce_parameter_types
    def integer_value(self: "Self", value: "int") -> None:
        self.wrapped.IntegerValue = int(value) if value is not None else 0

    @property
    def mean_value(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MeanValue

        if temp is None:
            return 0.0

        return temp

    @mean_value.setter
    @enforce_parameter_types
    def mean_value(self: "Self", value: "float") -> None:
        self.wrapped.MeanValue = float(value) if value is not None else 0.0

    @property
    def number_of_values(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfValues

        if temp is None:
            return 0

        return temp

    @number_of_values.setter
    @enforce_parameter_types
    def number_of_values(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfValues = int(value) if value is not None else 0

    @property
    def standard_deviation(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StandardDeviation

        if temp is None:
            return 0.0

        return temp

    @standard_deviation.setter
    @enforce_parameter_types
    def standard_deviation(self: "Self", value: "float") -> None:
        self.wrapped.StandardDeviation = float(value) if value is not None else 0.0

    @property
    def start_value(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartValue

        if temp is None:
            return 0.0

        return temp

    @start_value.setter
    @enforce_parameter_types
    def start_value(self: "Self", value: "float") -> None:
        self.wrapped.StartValue = float(value) if value is not None else 0.0

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
    def value(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @value.setter
    @enforce_parameter_types
    def value(self: "Self", value: "float") -> None:
        self.wrapped.Value = float(value) if value is not None else 0.0

    @property
    def value_specification_type(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DoeValueSpecificationOption":
        """EnumWithSelectedValue[mastapy._private.system_model.analyses_and_results.parametric_study_tools.DoeValueSpecificationOption]"""
        temp = self.wrapped.ValueSpecificationType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DoeValueSpecificationOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @value_specification_type.setter
    @enforce_parameter_types
    def value_specification_type(
        self: "Self", value: "_4456.DoeValueSpecificationOption"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DoeValueSpecificationOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ValueSpecificationType = value

    @property
    def doe_variable_values_in_si_units(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DOEVariableValuesInSIUnits

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def end_value_in_si_units(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EndValueInSIUnits

        if temp is None:
            return 0.0

        return temp

    @end_value_in_si_units.setter
    @enforce_parameter_types
    def end_value_in_si_units(self: "Self", value: "float") -> None:
        self.wrapped.EndValueInSIUnits = float(value) if value is not None else 0.0

    @property
    def integer_end_value_in_si_units(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.IntegerEndValueInSIUnits

        if temp is None:
            return 0

        return temp

    @integer_end_value_in_si_units.setter
    @enforce_parameter_types
    def integer_end_value_in_si_units(self: "Self", value: "int") -> None:
        self.wrapped.IntegerEndValueInSIUnits = int(value) if value is not None else 0

    @property
    def integer_start_value_in_si_units(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.IntegerStartValueInSIUnits

        if temp is None:
            return 0

        return temp

    @integer_start_value_in_si_units.setter
    @enforce_parameter_types
    def integer_start_value_in_si_units(self: "Self", value: "int") -> None:
        self.wrapped.IntegerStartValueInSIUnits = int(value) if value is not None else 0

    @property
    def integer_value_in_si_units(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.IntegerValueInSIUnits

        if temp is None:
            return 0

        return temp

    @integer_value_in_si_units.setter
    @enforce_parameter_types
    def integer_value_in_si_units(self: "Self", value: "int") -> None:
        self.wrapped.IntegerValueInSIUnits = int(value) if value is not None else 0

    @property
    def mean_value_in_si_units(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MeanValueInSIUnits

        if temp is None:
            return 0.0

        return temp

    @mean_value_in_si_units.setter
    @enforce_parameter_types
    def mean_value_in_si_units(self: "Self", value: "float") -> None:
        self.wrapped.MeanValueInSIUnits = float(value) if value is not None else 0.0

    @property
    def standard_deviation_in_si_units(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StandardDeviationInSIUnits

        if temp is None:
            return 0.0

        return temp

    @standard_deviation_in_si_units.setter
    @enforce_parameter_types
    def standard_deviation_in_si_units(self: "Self", value: "float") -> None:
        self.wrapped.StandardDeviationInSIUnits = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_value_in_si_units(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartValueInSIUnits

        if temp is None:
            return 0.0

        return temp

    @start_value_in_si_units.setter
    @enforce_parameter_types
    def start_value_in_si_units(self: "Self", value: "float") -> None:
        self.wrapped.StartValueInSIUnits = float(value) if value is not None else 0.0

    @property
    def value_in_si_units(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ValueInSIUnits

        if temp is None:
            return 0.0

        return temp

    @value_in_si_units.setter
    @enforce_parameter_types
    def value_in_si_units(self: "Self", value: "float") -> None:
        self.wrapped.ValueInSIUnits = float(value) if value is not None else 0.0

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
    def set_values(self: "Self", values: "List[float]") -> None:
        """Method does not return.

        Args:
            values (List[float])
        """
        values = conversion.mp_to_pn_list_float(values)
        self.wrapped.SetValues(values)

    @enforce_parameter_types
    def set_values_in_si_units(self: "Self", values: "List[float]") -> None:
        """Method does not return.

        Args:
            values (List[float])
        """
        values = conversion.mp_to_pn_list_float(values)
        self.wrapped.SetValuesInSIUnits(values)

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
    def cast_to(self: "Self") -> "_Cast_DesignOfExperimentsVariableSetter":
        """Cast to another type.

        Returns:
            _Cast_DesignOfExperimentsVariableSetter
        """
        return _Cast_DesignOfExperimentsVariableSetter(self)
