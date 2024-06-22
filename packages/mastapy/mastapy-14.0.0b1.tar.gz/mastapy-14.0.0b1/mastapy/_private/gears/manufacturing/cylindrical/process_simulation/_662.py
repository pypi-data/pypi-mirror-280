"""CutterProcessSimulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CUTTER_PROCESS_SIMULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.ProcessSimulation",
    "CutterProcessSimulation",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical.process_simulation import (
        _663,
        _664,
    )

    Self = TypeVar("Self", bound="CutterProcessSimulation")
    CastSelf = TypeVar(
        "CastSelf", bound="CutterProcessSimulation._Cast_CutterProcessSimulation"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CutterProcessSimulation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CutterProcessSimulation:
    """Special nested class for casting CutterProcessSimulation to subclasses."""

    __parent__: "CutterProcessSimulation"

    @property
    def form_wheel_grinding_process_simulation(
        self: "CastSelf",
    ) -> "_663.FormWheelGrindingProcessSimulation":
        from mastapy._private.gears.manufacturing.cylindrical.process_simulation import (
            _663,
        )

        return self.__parent__._cast(_663.FormWheelGrindingProcessSimulation)

    @property
    def shaping_process_simulation(self: "CastSelf") -> "_664.ShapingProcessSimulation":
        from mastapy._private.gears.manufacturing.cylindrical.process_simulation import (
            _664,
        )

        return self.__parent__._cast(_664.ShapingProcessSimulation)

    @property
    def cutter_process_simulation(self: "CastSelf") -> "CutterProcessSimulation":
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
class CutterProcessSimulation(_0.APIBase):
    """CutterProcessSimulation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CUTTER_PROCESS_SIMULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def end_of_measured_lead(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EndOfMeasuredLead

        if temp is None:
            return 0.0

        return temp

    @end_of_measured_lead.setter
    @enforce_parameter_types
    def end_of_measured_lead(self: "Self", value: "float") -> None:
        self.wrapped.EndOfMeasuredLead = float(value) if value is not None else 0.0

    @property
    def end_of_measured_profile(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EndOfMeasuredProfile

        if temp is None:
            return 0.0

        return temp

    @end_of_measured_profile.setter
    @enforce_parameter_types
    def end_of_measured_profile(self: "Self", value: "float") -> None:
        self.wrapped.EndOfMeasuredProfile = float(value) if value is not None else 0.0

    @property
    def lead_distance_per_step(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LeadDistancePerStep

        if temp is None:
            return 0.0

        return temp

    @lead_distance_per_step.setter
    @enforce_parameter_types
    def lead_distance_per_step(self: "Self", value: "float") -> None:
        self.wrapped.LeadDistancePerStep = float(value) if value is not None else 0.0

    @property
    def number_of_teeth_to_calculate(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeethToCalculate

        if temp is None:
            return 0

        return temp

    @number_of_teeth_to_calculate.setter
    @enforce_parameter_types
    def number_of_teeth_to_calculate(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfTeethToCalculate = int(value) if value is not None else 0

    @property
    def rolling_distance_per_step(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RollingDistancePerStep

        if temp is None:
            return 0.0

        return temp

    @rolling_distance_per_step.setter
    @enforce_parameter_types
    def rolling_distance_per_step(self: "Self", value: "float") -> None:
        self.wrapped.RollingDistancePerStep = float(value) if value is not None else 0.0

    @property
    def start_of_measured_lead(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfMeasuredLead

        if temp is None:
            return 0.0

        return temp

    @start_of_measured_lead.setter
    @enforce_parameter_types
    def start_of_measured_lead(self: "Self", value: "float") -> None:
        self.wrapped.StartOfMeasuredLead = float(value) if value is not None else 0.0

    @property
    def start_of_measured_profile(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfMeasuredProfile

        if temp is None:
            return 0.0

        return temp

    @start_of_measured_profile.setter
    @enforce_parameter_types
    def start_of_measured_profile(self: "Self", value: "float") -> None:
        self.wrapped.StartOfMeasuredProfile = float(value) if value is not None else 0.0

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
    def cast_to(self: "Self") -> "_Cast_CutterProcessSimulation":
        """Cast to another type.

        Returns:
            _Cast_CutterProcessSimulation
        """
        return _Cast_CutterProcessSimulation(self)
