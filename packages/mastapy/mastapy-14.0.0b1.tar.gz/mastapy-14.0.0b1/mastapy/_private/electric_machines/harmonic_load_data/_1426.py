"""HarmonicLoadDataBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.electric_machines.harmonic_load_data import _1428
from mastapy._private._internal import (
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.python_net import python_net_import
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_DOUBLE = python_net_import("System", "Double")
_STRING = python_net_import("System", "String")
_FOURIER_SERIES = python_net_import("SMT.MastaAPI.MathUtility", "FourierSeries")
_LIST = python_net_import("System.Collections.Generic", "List")
_MEASUREMENT_TYPE = python_net_import(
    "SMT.MastaAPIUtility.UnitsAndMeasurements", "MeasurementType"
)
_HARMONIC_LOAD_DATA_BASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "HarmonicLoadDataBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.math_utility import _1559
    from mastapy._private.units_and_measurements import _7725
    from mastapy._private.electric_machines.results import _1367
    from mastapy._private.electric_machines.harmonic_load_data import _1424, _1429
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _6994,
        _7011,
        _7018,
        _7019,
        _7020,
        _7021,
        _7022,
        _7023,
        _7024,
        _7041,
        _7086,
        _7128,
    )

    Self = TypeVar("Self", bound="HarmonicLoadDataBase")
    CastSelf = TypeVar(
        "CastSelf", bound="HarmonicLoadDataBase._Cast_HarmonicLoadDataBase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HarmonicLoadDataBase:
    """Special nested class for casting HarmonicLoadDataBase to subclasses."""

    __parent__: "HarmonicLoadDataBase"

    @property
    def dynamic_force_results(self: "CastSelf") -> "_1367.DynamicForceResults":
        from mastapy._private.electric_machines.results import _1367

        return self.__parent__._cast(_1367.DynamicForceResults)

    @property
    def electric_machine_harmonic_load_data_base(
        self: "CastSelf",
    ) -> "_1424.ElectricMachineHarmonicLoadDataBase":
        from mastapy._private.electric_machines.harmonic_load_data import _1424

        return self.__parent__._cast(_1424.ElectricMachineHarmonicLoadDataBase)

    @property
    def speed_dependent_harmonic_load_data(
        self: "CastSelf",
    ) -> "_1429.SpeedDependentHarmonicLoadData":
        from mastapy._private.electric_machines.harmonic_load_data import _1429

        return self.__parent__._cast(_1429.SpeedDependentHarmonicLoadData)

    @property
    def conical_gear_set_harmonic_load_data(
        self: "CastSelf",
    ) -> "_6994.ConicalGearSetHarmonicLoadData":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6994,
        )

        return self.__parent__._cast(_6994.ConicalGearSetHarmonicLoadData)

    @property
    def cylindrical_gear_set_harmonic_load_data(
        self: "CastSelf",
    ) -> "_7011.CylindricalGearSetHarmonicLoadData":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7011,
        )

        return self.__parent__._cast(_7011.CylindricalGearSetHarmonicLoadData)

    @property
    def electric_machine_harmonic_load_data(
        self: "CastSelf",
    ) -> "_7018.ElectricMachineHarmonicLoadData":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7018,
        )

        return self.__parent__._cast(_7018.ElectricMachineHarmonicLoadData)

    @property
    def electric_machine_harmonic_load_data_from_excel(
        self: "CastSelf",
    ) -> "_7019.ElectricMachineHarmonicLoadDataFromExcel":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7019,
        )

        return self.__parent__._cast(_7019.ElectricMachineHarmonicLoadDataFromExcel)

    @property
    def electric_machine_harmonic_load_data_from_flux(
        self: "CastSelf",
    ) -> "_7020.ElectricMachineHarmonicLoadDataFromFlux":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7020,
        )

        return self.__parent__._cast(_7020.ElectricMachineHarmonicLoadDataFromFlux)

    @property
    def electric_machine_harmonic_load_data_from_jmag(
        self: "CastSelf",
    ) -> "_7021.ElectricMachineHarmonicLoadDataFromJMAG":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7021,
        )

        return self.__parent__._cast(_7021.ElectricMachineHarmonicLoadDataFromJMAG)

    @property
    def electric_machine_harmonic_load_data_from_masta(
        self: "CastSelf",
    ) -> "_7022.ElectricMachineHarmonicLoadDataFromMASTA":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7022,
        )

        return self.__parent__._cast(_7022.ElectricMachineHarmonicLoadDataFromMASTA)

    @property
    def electric_machine_harmonic_load_data_from_motor_cad(
        self: "CastSelf",
    ) -> "_7023.ElectricMachineHarmonicLoadDataFromMotorCAD":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7023,
        )

        return self.__parent__._cast(_7023.ElectricMachineHarmonicLoadDataFromMotorCAD)

    @property
    def electric_machine_harmonic_load_data_from_motor_packages(
        self: "CastSelf",
    ) -> "_7024.ElectricMachineHarmonicLoadDataFromMotorPackages":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7024,
        )

        return self.__parent__._cast(
            _7024.ElectricMachineHarmonicLoadDataFromMotorPackages
        )

    @property
    def gear_set_harmonic_load_data(
        self: "CastSelf",
    ) -> "_7041.GearSetHarmonicLoadData":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7041,
        )

        return self.__parent__._cast(_7041.GearSetHarmonicLoadData)

    @property
    def point_load_harmonic_load_data(
        self: "CastSelf",
    ) -> "_7086.PointLoadHarmonicLoadData":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7086,
        )

        return self.__parent__._cast(_7086.PointLoadHarmonicLoadData)

    @property
    def unbalanced_mass_harmonic_load_data(
        self: "CastSelf",
    ) -> "_7128.UnbalancedMassHarmonicLoadData":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7128,
        )

        return self.__parent__._cast(_7128.UnbalancedMassHarmonicLoadData)

    @property
    def harmonic_load_data_base(self: "CastSelf") -> "HarmonicLoadDataBase":
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
class HarmonicLoadDataBase(_0.APIBase):
    """HarmonicLoadDataBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HARMONIC_LOAD_DATA_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def data_type(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType":
        """EnumWithSelectedValue[mastapy._private.electric_machines.harmonic_load_data.HarmonicLoadDataType]"""
        temp = self.wrapped.DataType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @data_type.setter
    @enforce_parameter_types
    def data_type(self: "Self", value: "_1428.HarmonicLoadDataType") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataType = value

    @property
    def excitation_order_as_rotational_order_of_shaft(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ExcitationOrderAsRotationalOrderOfShaft

        if temp is None:
            return 0.0

        return temp

    @excitation_order_as_rotational_order_of_shaft.setter
    @enforce_parameter_types
    def excitation_order_as_rotational_order_of_shaft(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.ExcitationOrderAsRotationalOrderOfShaft = (
            float(value) if value is not None else 0.0
        )

    @property
    def number_of_cycles_in_signal(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NumberOfCyclesInSignal

        if temp is None:
            return 0.0

        return temp

    @number_of_cycles_in_signal.setter
    @enforce_parameter_types
    def number_of_cycles_in_signal(self: "Self", value: "float") -> None:
        self.wrapped.NumberOfCyclesInSignal = float(value) if value is not None else 0.0

    @property
    def number_of_harmonics(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfHarmonics

        if temp is None:
            return 0

        return temp

    @number_of_harmonics.setter
    @enforce_parameter_types
    def number_of_harmonics(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfHarmonics = int(value) if value is not None else 0

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
    def excitations(self: "Self") -> "List[_1559.FourierSeries]":
        """List[mastapy._private.math_utility.FourierSeries]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    def peak_to_peak(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeak

        if temp is None:
            return 0.0

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

    def clear_all_data(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ClearAllData()

    def clear_selected_data(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ClearSelectedData()

    @enforce_parameter_types
    def set_selected_harmonic_load_data_with_fourier_series(
        self: "Self", fourier_series: "_1559.FourierSeries"
    ) -> None:
        """Method does not return.

        Args:
            fourier_series (mastapy._private.math_utility.FourierSeries)
        """
        self.wrapped.SetSelectedHarmonicLoadData.Overloads[_FOURIER_SERIES](
            fourier_series.wrapped if fourier_series else None
        )

    @enforce_parameter_types
    def set_selected_harmonic_load_data_extended(
        self: "Self",
        amplitudes: "List[float]",
        phases: "List[float]",
        mean_value: "float",
        fourier_series_name: "str",
        fourier_series_measurement_type: "_7725.MeasurementType",
    ) -> None:
        """Method does not return.

        Args:
            amplitudes (List[float])
            phases (List[float])
            mean_value (float)
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy._private.units_and_measurements.MeasurementType)
        """
        amplitudes = conversion.mp_to_pn_list_float(amplitudes)
        phases = conversion.mp_to_pn_list_float(phases)
        mean_value = float(mean_value)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(
            fourier_series_measurement_type,
            "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType",
        )
        self.wrapped.SetSelectedHarmonicLoadData.Overloads[
            _LIST[_DOUBLE], _LIST[_DOUBLE], _DOUBLE, _STRING, _MEASUREMENT_TYPE
        ](
            amplitudes,
            phases,
            mean_value if mean_value else 0.0,
            fourier_series_name if fourier_series_name else "",
            fourier_series_measurement_type,
        )

    @enforce_parameter_types
    def set_selected_harmonic_load_data(
        self: "Self",
        fourier_series_values: "List[float]",
        fourier_series_name: "str",
        fourier_series_measurement_type: "_7725.MeasurementType",
    ) -> None:
        """Method does not return.

        Args:
            fourier_series_values (List[float])
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy._private.units_and_measurements.MeasurementType)
        """
        fourier_series_values = conversion.mp_to_pn_array_float(fourier_series_values)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(
            fourier_series_measurement_type,
            "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType",
        )
        self.wrapped.SetSelectedHarmonicLoadData.Overloads[
            _ARRAY[_DOUBLE], _STRING, _MEASUREMENT_TYPE
        ](
            fourier_series_values,
            fourier_series_name if fourier_series_name else "",
            fourier_series_measurement_type,
        )

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
    def cast_to(self: "Self") -> "_Cast_HarmonicLoadDataBase":
        """Cast to another type.

        Returns:
            _Cast_HarmonicLoadDataBase
        """
        return _Cast_HarmonicLoadDataBase(self)
