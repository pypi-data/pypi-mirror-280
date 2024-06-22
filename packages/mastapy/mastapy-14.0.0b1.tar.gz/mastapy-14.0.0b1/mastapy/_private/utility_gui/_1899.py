"""ColumnInputOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal.implicit import list_with_selected_item
from mastapy._private.utility.file_access_helpers import _1867
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility.units_and_measurements import _1657
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COLUMN_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.UtilityGUI", "ColumnInputOptions"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
        _2611,
        _2612,
        _2613,
        _2616,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _7138,
        _7139,
        _7141,
        _7142,
        _7143,
        _7144,
        _7146,
        _7147,
        _7148,
        _7149,
        _7151,
        _7152,
    )

    Self = TypeVar("Self", bound="ColumnInputOptions")
    CastSelf = TypeVar("CastSelf", bound="ColumnInputOptions._Cast_ColumnInputOptions")


__docformat__ = "restructuredtext en"
__all__ = ("ColumnInputOptions",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ColumnInputOptions:
    """Special nested class for casting ColumnInputOptions to subclasses."""

    __parent__: "ColumnInputOptions"

    @property
    def boost_pressure_input_options(
        self: "CastSelf",
    ) -> "_2611.BoostPressureInputOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2611,
        )

        return self.__parent__._cast(_2611.BoostPressureInputOptions)

    @property
    def input_power_input_options(self: "CastSelf") -> "_2612.InputPowerInputOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2612,
        )

        return self.__parent__._cast(_2612.InputPowerInputOptions)

    @property
    def pressure_ratio_input_options(
        self: "CastSelf",
    ) -> "_2613.PressureRatioInputOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2613,
        )

        return self.__parent__._cast(_2613.PressureRatioInputOptions)

    @property
    def rotor_speed_input_options(self: "CastSelf") -> "_2616.RotorSpeedInputOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2616,
        )

        return self.__parent__._cast(_2616.RotorSpeedInputOptions)

    @property
    def boost_pressure_load_case_input_options(
        self: "CastSelf",
    ) -> "_7138.BoostPressureLoadCaseInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7138,
        )

        return self.__parent__._cast(_7138.BoostPressureLoadCaseInputOptions)

    @property
    def design_state_options(self: "CastSelf") -> "_7139.DesignStateOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7139,
        )

        return self.__parent__._cast(_7139.DesignStateOptions)

    @property
    def force_input_options(self: "CastSelf") -> "_7141.ForceInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7141,
        )

        return self.__parent__._cast(_7141.ForceInputOptions)

    @property
    def gear_ratio_input_options(self: "CastSelf") -> "_7142.GearRatioInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7142,
        )

        return self.__parent__._cast(_7142.GearRatioInputOptions)

    @property
    def load_case_name_options(self: "CastSelf") -> "_7143.LoadCaseNameOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7143,
        )

        return self.__parent__._cast(_7143.LoadCaseNameOptions)

    @property
    def moment_input_options(self: "CastSelf") -> "_7144.MomentInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7144,
        )

        return self.__parent__._cast(_7144.MomentInputOptions)

    @property
    def point_load_input_options(self: "CastSelf") -> "_7146.PointLoadInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7146,
        )

        return self.__parent__._cast(_7146.PointLoadInputOptions)

    @property
    def power_load_input_options(self: "CastSelf") -> "_7147.PowerLoadInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7147,
        )

        return self.__parent__._cast(_7147.PowerLoadInputOptions)

    @property
    def ramp_or_steady_state_input_options(
        self: "CastSelf",
    ) -> "_7148.RampOrSteadyStateInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7148,
        )

        return self.__parent__._cast(_7148.RampOrSteadyStateInputOptions)

    @property
    def speed_input_options(self: "CastSelf") -> "_7149.SpeedInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7149,
        )

        return self.__parent__._cast(_7149.SpeedInputOptions)

    @property
    def time_step_input_options(self: "CastSelf") -> "_7151.TimeStepInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7151,
        )

        return self.__parent__._cast(_7151.TimeStepInputOptions)

    @property
    def torque_input_options(self: "CastSelf") -> "_7152.TorqueInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7152,
        )

        return self.__parent__._cast(_7152.TorqueInputOptions)

    @property
    def column_input_options(self: "CastSelf") -> "ColumnInputOptions":
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
class ColumnInputOptions(_0.APIBase):
    """ColumnInputOptions

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COLUMN_INPUT_OPTIONS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def column(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_ColumnTitle":
        """ListWithSelectedItem[mastapy._private.utility.file_access_helpers.ColumnTitle]"""
        temp = self.wrapped.Column

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ColumnTitle",
        )(temp)

    @column.setter
    @enforce_parameter_types
    def column(self: "Self", value: "_1867.ColumnTitle") -> None:
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Column = value

    @property
    def unit(self: "Self") -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy._private.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.Unit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @unit.setter
    @enforce_parameter_types
    def unit(self: "Self", value: "_1657.Unit") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Unit = value

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
    def cast_to(self: "Self") -> "_Cast_ColumnInputOptions":
        """Cast to another type.

        Returns:
            _Cast_ColumnInputOptions
        """
        return _Cast_ColumnInputOptions(self)
