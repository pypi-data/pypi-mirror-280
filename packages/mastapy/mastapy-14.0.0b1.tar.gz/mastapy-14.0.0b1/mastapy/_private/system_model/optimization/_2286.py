"""OptimizationStep"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_OPTIMIZATION_STEP = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "OptimizationStep"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.optimization import _2285, _2280, _2283

    Self = TypeVar("Self", bound="OptimizationStep")
    CastSelf = TypeVar("CastSelf", bound="OptimizationStep._Cast_OptimizationStep")


__docformat__ = "restructuredtext en"
__all__ = ("OptimizationStep",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_OptimizationStep:
    """Special nested class for casting OptimizationStep to subclasses."""

    __parent__: "OptimizationStep"

    @property
    def conical_gear_optimization_step(
        self: "CastSelf",
    ) -> "_2280.ConicalGearOptimizationStep":
        from mastapy._private.system_model.optimization import _2280

        return self.__parent__._cast(_2280.ConicalGearOptimizationStep)

    @property
    def cylindrical_gear_optimization_step(
        self: "CastSelf",
    ) -> "_2283.CylindricalGearOptimizationStep":
        from mastapy._private.system_model.optimization import _2283

        return self.__parent__._cast(_2283.CylindricalGearOptimizationStep)

    @property
    def optimization_step(self: "CastSelf") -> "OptimizationStep":
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
class OptimizationStep(_0.APIBase):
    """OptimizationStep

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _OPTIMIZATION_STEP

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def name(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: "Self", value: "str") -> None:
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def optimisation_target(self: "Self") -> "_2285.MicroGeometryOptimisationTarget":
        """mastapy._private.system_model.optimization.MicroGeometryOptimisationTarget"""
        temp = self.wrapped.OptimisationTarget

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.Optimization.MicroGeometryOptimisationTarget",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model.optimization._2285",
            "MicroGeometryOptimisationTarget",
        )(value)

    @optimisation_target.setter
    @enforce_parameter_types
    def optimisation_target(
        self: "Self", value: "_2285.MicroGeometryOptimisationTarget"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.Optimization.MicroGeometryOptimisationTarget",
        )
        self.wrapped.OptimisationTarget = value

    @property
    def target_edge_stress_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TargetEdgeStressFactor

        if temp is None:
            return 0.0

        return temp

    @target_edge_stress_factor.setter
    @enforce_parameter_types
    def target_edge_stress_factor(self: "Self", value: "float") -> None:
        self.wrapped.TargetEdgeStressFactor = float(value) if value is not None else 0.0

    @property
    def tolerance(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Tolerance

        if temp is None:
            return 0.0

        return temp

    @tolerance.setter
    @enforce_parameter_types
    def tolerance(self: "Self", value: "float") -> None:
        self.wrapped.Tolerance = float(value) if value is not None else 0.0

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
    def cast_to(self: "Self") -> "_Cast_OptimizationStep":
        """Cast to another type.

        Returns:
            _Cast_OptimizationStep
        """
        return _Cast_OptimizationStep(self)
