"""DataInputFileOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable, list_with_selected_item
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_DATA_INPUT_FILE_OPTIONS = python_net_import(
    "SMT.MastaAPI.UtilityGUI", "DataInputFileOptions"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
        _2614,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _7145,
    )

    Self = TypeVar("Self", bound="DataInputFileOptions")
    CastSelf = TypeVar(
        "CastSelf", bound="DataInputFileOptions._Cast_DataInputFileOptions"
    )


__docformat__ = "restructuredtext en"
__all__ = ("DataInputFileOptions",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_DataInputFileOptions:
    """Special nested class for casting DataInputFileOptions to subclasses."""

    __parent__: "DataInputFileOptions"

    @property
    def rotor_set_data_input_file_options(
        self: "CastSelf",
    ) -> "_2614.RotorSetDataInputFileOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2614,
        )

        return self.__parent__._cast(_2614.RotorSetDataInputFileOptions)

    @property
    def multi_time_series_data_input_file_options(
        self: "CastSelf",
    ) -> "_7145.MultiTimeSeriesDataInputFileOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7145,
        )

        return self.__parent__._cast(_7145.MultiTimeSeriesDataInputFileOptions)

    @property
    def data_input_file_options(self: "CastSelf") -> "DataInputFileOptions":
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
class DataInputFileOptions(_0.APIBase):
    """DataInputFileOptions

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _DATA_INPUT_FILE_OPTIONS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def column_headers_row(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.ColumnHeadersRow

        if temp is None:
            return 0

        return temp

    @column_headers_row.setter
    @enforce_parameter_types
    def column_headers_row(self: "Self", value: "int") -> None:
        self.wrapped.ColumnHeadersRow = int(value) if value is not None else 0

    @property
    def data_end_row(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.DataEndRow

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @data_end_row.setter
    @enforce_parameter_types
    def data_end_row(self: "Self", value: "Union[int, Tuple[int, bool]]") -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.DataEndRow = value

    @property
    def data_start_row(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.DataStartRow

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @data_start_row.setter
    @enforce_parameter_types
    def data_start_row(self: "Self", value: "Union[int, Tuple[int, bool]]") -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.DataStartRow = value

    @property
    def selected_file_name(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.SelectedFileName

        if temp is None:
            return ""

        return temp

    @selected_file_name.setter
    @enforce_parameter_types
    def selected_file_name(self: "Self", value: "str") -> None:
        self.wrapped.SelectedFileName = str(value) if value is not None else ""

    @property
    def sheet(self: "Self") -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.Sheet

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @sheet.setter
    @enforce_parameter_types
    def sheet(self: "Self", value: "str") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.Sheet = value

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
    def open_file(self: "Self", filename: "str") -> None:
        """Method does not return.

        Args:
            filename (str)
        """
        filename = str(filename)
        self.wrapped.OpenFile(filename if filename else "")

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
    def cast_to(self: "Self") -> "_Cast_DataInputFileOptions":
        """Cast to another type.

        Returns:
            _Cast_DataInputFileOptions
        """
        return _Cast_DataInputFileOptions(self)
