"""CylindricalGearSpecifiedMicroGeometry"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SPECIFIED_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "CylindricalGearSpecifiedMicroGeometry",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical.plunge_shaving import _668
    from mastapy._private.gears.manufacturing.cylindrical import _657, _658

    Self = TypeVar("Self", bound="CylindricalGearSpecifiedMicroGeometry")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearSpecifiedMicroGeometry._Cast_CylindricalGearSpecifiedMicroGeometry",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSpecifiedMicroGeometry",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearSpecifiedMicroGeometry:
    """Special nested class for casting CylindricalGearSpecifiedMicroGeometry to subclasses."""

    __parent__: "CylindricalGearSpecifiedMicroGeometry"

    @property
    def cylindrical_gear_specified_micro_geometry(
        self: "CastSelf",
    ) -> "CylindricalGearSpecifiedMicroGeometry":
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
class CylindricalGearSpecifiedMicroGeometry(_0.APIBase):
    """CylindricalGearSpecifiedMicroGeometry

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SPECIFIED_MICRO_GEOMETRY

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def lead_measurement_method(self: "Self") -> "_668.MicroGeometryDefinitionMethod":
        """mastapy._private.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod"""
        temp = self.wrapped.LeadMeasurementMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.manufacturing.cylindrical.plunge_shaving._668",
            "MicroGeometryDefinitionMethod",
        )(value)

    @lead_measurement_method.setter
    @enforce_parameter_types
    def lead_measurement_method(
        self: "Self", value: "_668.MicroGeometryDefinitionMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )
        self.wrapped.LeadMeasurementMethod = value

    @property
    def name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def number_of_transverse_planes(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfTransversePlanes

        if temp is None:
            return 0

        return temp

    @number_of_transverse_planes.setter
    @enforce_parameter_types
    def number_of_transverse_planes(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfTransversePlanes = int(value) if value is not None else 0

    @property
    def profile_measurement_method(
        self: "Self",
    ) -> "_668.MicroGeometryDefinitionMethod":
        """mastapy._private.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod"""
        temp = self.wrapped.ProfileMeasurementMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.manufacturing.cylindrical.plunge_shaving._668",
            "MicroGeometryDefinitionMethod",
        )(value)

    @profile_measurement_method.setter
    @enforce_parameter_types
    def profile_measurement_method(
        self: "Self", value: "_668.MicroGeometryDefinitionMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )
        self.wrapped.ProfileMeasurementMethod = value

    @property
    def lead_micro_geometry(self: "Self") -> "_657.MicroGeometryInputsLead":
        """mastapy._private.gears.manufacturing.cylindrical.MicroGeometryInputsLead

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_micro_geometry(self: "Self") -> "List[_658.MicroGeometryInputsProfile]":
        """List[mastapy._private.gears.manufacturing.cylindrical.MicroGeometryInputsProfile]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileMicroGeometry

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    def cast_to(self: "Self") -> "_Cast_CylindricalGearSpecifiedMicroGeometry":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearSpecifiedMicroGeometry
        """
        return _Cast_CylindricalGearSpecifiedMicroGeometry(self)
