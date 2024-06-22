"""MicroGeometryInputs"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "MicroGeometryInputs"
)

if TYPE_CHECKING:
    from typing import Any, Type, List

    from mastapy._private.gears.manufacturing.cylindrical import _659, _657, _658

    Self = TypeVar("Self", bound="MicroGeometryInputs")
    CastSelf = TypeVar(
        "CastSelf", bound="MicroGeometryInputs._Cast_MicroGeometryInputs"
    )

T = TypeVar("T", bound="_659.ModificationSegment")

__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryInputs",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MicroGeometryInputs:
    """Special nested class for casting MicroGeometryInputs to subclasses."""

    __parent__: "MicroGeometryInputs"

    @property
    def micro_geometry_inputs_lead(self: "CastSelf") -> "_657.MicroGeometryInputsLead":
        from mastapy._private.gears.manufacturing.cylindrical import _657

        return self.__parent__._cast(_657.MicroGeometryInputsLead)

    @property
    def micro_geometry_inputs_profile(
        self: "CastSelf",
    ) -> "_658.MicroGeometryInputsProfile":
        from mastapy._private.gears.manufacturing.cylindrical import _658

        return self.__parent__._cast(_658.MicroGeometryInputsProfile)

    @property
    def micro_geometry_inputs(self: "CastSelf") -> "MicroGeometryInputs":
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
class MicroGeometryInputs(_0.APIBase, Generic[T]):
    """MicroGeometryInputs

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _MICRO_GEOMETRY_INPUTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def modification_at_starting_point(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ModificationAtStartingPoint

        if temp is None:
            return 0.0

        return temp

    @modification_at_starting_point.setter
    @enforce_parameter_types
    def modification_at_starting_point(self: "Self", value: "float") -> None:
        self.wrapped.ModificationAtStartingPoint = (
            float(value) if value is not None else 0.0
        )

    @property
    def micro_geometry_segments(self: "Self") -> "List[T]":
        """List[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometrySegments

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
    def cast_to(self: "Self") -> "_Cast_MicroGeometryInputs":
        """Cast to another type.

        Returns:
            _Cast_MicroGeometryInputs
        """
        return _Cast_MicroGeometryInputs(self)
