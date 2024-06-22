"""AbstractStator"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ABSTRACT_STATOR = python_net_import("SMT.MastaAPI.ElectricMachines", "AbstractStator")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.electric_machines import _1283, _1361, _1290, _1344

    Self = TypeVar("Self", bound="AbstractStator")
    CastSelf = TypeVar("CastSelf", bound="AbstractStator._Cast_AbstractStator")


__docformat__ = "restructuredtext en"
__all__ = ("AbstractStator",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractStator:
    """Special nested class for casting AbstractStator to subclasses."""

    __parent__: "AbstractStator"

    @property
    def cad_stator(self: "CastSelf") -> "_1290.CADStator":
        from mastapy._private.electric_machines import _1290

        return self.__parent__._cast(_1290.CADStator)

    @property
    def stator(self: "CastSelf") -> "_1344.Stator":
        from mastapy._private.electric_machines import _1344

        return self.__parent__._cast(_1344.Stator)

    @property
    def abstract_stator(self: "CastSelf") -> "AbstractStator":
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
class AbstractStator(_0.APIBase):
    """AbstractStator

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_STATOR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def angle_between_stator_partitioning_lines(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AngleBetweenStatorPartitioningLines

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle_between_stator_partitioning_lines.setter
    @enforce_parameter_types
    def angle_between_stator_partitioning_lines(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AngleBetweenStatorPartitioningLines = value

    @property
    def back_iron_inner_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BackIronInnerRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def back_iron_mid_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BackIronMidRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_diameter_of_stator_teeth(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.InnerDiameterOfStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @inner_diameter_of_stator_teeth.setter
    @enforce_parameter_types
    def inner_diameter_of_stator_teeth(self: "Self", value: "float") -> None:
        self.wrapped.InnerDiameterOfStatorTeeth = (
            float(value) if value is not None else 0.0
        )

    @property
    def mid_tooth_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MidToothRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_slots(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfSlots

        if temp is None:
            return 0

        return temp

    @number_of_slots.setter
    @enforce_parameter_types
    def number_of_slots(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfSlots = int(value) if value is not None else 0

    @property
    def outer_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: "Self", value: "float") -> None:
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def outer_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def split_ratio(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SplitRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def stator_length(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StatorLength

        if temp is None:
            return 0.0

        return temp

    @stator_length.setter
    @enforce_parameter_types
    def stator_length(self: "Self", value: "float") -> None:
        self.wrapped.StatorLength = float(value) if value is not None else 0.0

    @property
    def stator_material_database(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.StatorMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @stator_material_database.setter
    @enforce_parameter_types
    def stator_material_database(self: "Self", value: "str") -> None:
        self.wrapped.StatorMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def tooth_and_slot(self: "Self") -> "_1283.AbstractToothAndSlot":
        """mastapy._private.electric_machines.AbstractToothAndSlot

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def windings(self: "Self") -> "_1361.Windings":
        """mastapy._private.electric_machines.Windings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Windings

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
    def cast_to(self: "Self") -> "_Cast_AbstractStator":
        """Cast to another type.

        Returns:
            _Cast_AbstractStator
        """
        return _Cast_AbstractStator(self)
