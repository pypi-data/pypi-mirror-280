"""ProcessSimulationNew"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PROCESS_SIMULATION_NEW = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "ProcessSimulationNew",
)

if TYPE_CHECKING:
    from typing import Any, Type, List

    from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _704,
        _705,
        _706,
        _707,
        _711,
        _708,
        _696,
        _723,
    )

    Self = TypeVar("Self", bound="ProcessSimulationNew")
    CastSelf = TypeVar(
        "CastSelf", bound="ProcessSimulationNew._Cast_ProcessSimulationNew"
    )

T = TypeVar("T", bound="_708.ProcessSimulationInput")

__docformat__ = "restructuredtext en"
__all__ = ("ProcessSimulationNew",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ProcessSimulationNew:
    """Special nested class for casting ProcessSimulationNew to subclasses."""

    __parent__: "ProcessSimulationNew"

    @property
    def hobbing_process_simulation_new(
        self: "CastSelf",
    ) -> "_696.HobbingProcessSimulationNew":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _696,
        )

        return self.__parent__._cast(_696.HobbingProcessSimulationNew)

    @property
    def worm_grinding_process_simulation_new(
        self: "CastSelf",
    ) -> "_723.WormGrindingProcessSimulationNew":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _723,
        )

        return self.__parent__._cast(_723.WormGrindingProcessSimulationNew)

    @property
    def process_simulation_new(self: "CastSelf") -> "ProcessSimulationNew":
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
class ProcessSimulationNew(_0.APIBase, Generic[T]):
    """ProcessSimulationNew

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _PROCESS_SIMULATION_NEW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def achieved_agma20151a01_quality_grade(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AchievedAGMA20151A01QualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def achieved_iso132811995e_quality_grade(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AchievedISO132811995EQualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_tooth_shape_calculation(self: "Self") -> "_704.ProcessGearShape":
        """mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessGearShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearToothShapeCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def input(self: "Self") -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Input

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_calculation(self: "Self") -> "_705.ProcessLeadCalculation":
        """mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessLeadCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pitch_calculation(self: "Self") -> "_706.ProcessPitchCalculation":
        """mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessPitchCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_calculation(self: "Self") -> "_707.ProcessProfileCalculation":
        """mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessProfileCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_modification_calculation(
        self: "Self",
    ) -> "_711.ProcessTotalModificationCalculation":
        """mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessTotalModificationCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalModificationCalculation

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
    def cast_to(self: "Self") -> "_Cast_ProcessSimulationNew":
        """Cast to another type.

        Returns:
            _Cast_ProcessSimulationNew
        """
        return _Cast_ProcessSimulationNew(self)
