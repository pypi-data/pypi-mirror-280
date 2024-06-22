"""ParetoOptimisationVariableBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PARETO_OPTIMISATION_VARIABLE_BASE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationVariableBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility import _1635
    from mastapy._private.math_utility import _1535
    from mastapy._private.math_utility.optimisation import (
        _1604,
        _1603,
        _1593,
        _1594,
        _1599,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4493,
    )

    Self = TypeVar("Self", bound="ParetoOptimisationVariableBase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationVariableBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ParetoOptimisationVariableBase:
    """Special nested class for casting ParetoOptimisationVariableBase to subclasses."""

    __parent__: "ParetoOptimisationVariableBase"

    @property
    def pareto_optimisation_input(self: "CastSelf") -> "_1593.ParetoOptimisationInput":
        from mastapy._private.math_utility.optimisation import _1593

        return self.__parent__._cast(_1593.ParetoOptimisationInput)

    @property
    def pareto_optimisation_output(
        self: "CastSelf",
    ) -> "_1594.ParetoOptimisationOutput":
        from mastapy._private.math_utility.optimisation import _1594

        return self.__parent__._cast(_1594.ParetoOptimisationOutput)

    @property
    def pareto_optimisation_variable(
        self: "CastSelf",
    ) -> "_1599.ParetoOptimisationVariable":
        from mastapy._private.math_utility.optimisation import _1599

        return self.__parent__._cast(_1599.ParetoOptimisationVariable)

    @property
    def parametric_study_doe_result_variable(
        self: "CastSelf",
    ) -> "_4493.ParametricStudyDOEResultVariable":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4493,
        )

        return self.__parent__._cast(_4493.ParametricStudyDOEResultVariable)

    @property
    def pareto_optimisation_variable_base(
        self: "CastSelf",
    ) -> "ParetoOptimisationVariableBase":
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
class ParetoOptimisationVariableBase(_0.APIBase):
    """ParetoOptimisationVariableBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PARETO_OPTIMISATION_VARIABLE_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def percent(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Percent

        if temp is None:
            return 0.0

        return temp

    @percent.setter
    @enforce_parameter_types
    def percent(self: "Self", value: "float") -> None:
        self.wrapped.Percent = float(value) if value is not None else 0.0

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
    def specification_type(self: "Self") -> "_1604.TargetingPropertyTo":
        """mastapy._private.math_utility.optimisation.TargetingPropertyTo"""
        temp = self.wrapped.SpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.Optimisation.TargetingPropertyTo"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.math_utility.optimisation._1604", "TargetingPropertyTo"
        )(value)

    @specification_type.setter
    @enforce_parameter_types
    def specification_type(self: "Self", value: "_1604.TargetingPropertyTo") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.Optimisation.TargetingPropertyTo"
        )
        self.wrapped.SpecificationType = value

    @property
    def specify_input_range_as(self: "Self") -> "_1603.SpecifyOptimisationInputAs":
        """mastapy._private.math_utility.optimisation.SpecifyOptimisationInputAs"""
        temp = self.wrapped.SpecifyInputRangeAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.Optimisation.SpecifyOptimisationInputAs"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.math_utility.optimisation._1603",
            "SpecifyOptimisationInputAs",
        )(value)

    @specify_input_range_as.setter
    @enforce_parameter_types
    def specify_input_range_as(
        self: "Self", value: "_1603.SpecifyOptimisationInputAs"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.Optimisation.SpecifyOptimisationInputAs"
        )
        self.wrapped.SpecifyInputRangeAs = value

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
    def cast_to(self: "Self") -> "_Cast_ParetoOptimisationVariableBase":
        """Cast to another type.

        Returns:
            _Cast_ParetoOptimisationVariableBase
        """
        return _Cast_ParetoOptimisationVariableBase(self)
