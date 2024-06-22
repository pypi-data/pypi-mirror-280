"""AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_STRESS_CYCLES_DATA_FOR_AN_SN_CURVE_OF_A_PLASTIC_MATERIAL = python_net_import(
    "SMT.MastaAPI.Materials", "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.materials import _296, _297

    Self = TypeVar(
        "Self", bound="AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial._Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial:
    """Special nested class for casting AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial to subclasses."""

    __parent__: "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"

    @property
    def stress_cycles_data_for_the_bending_sn_curve_of_a_plastic_material(
        self: "CastSelf",
    ) -> "_296.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial":
        from mastapy._private.materials import _296

        return self.__parent__._cast(
            _296.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial
        )

    @property
    def stress_cycles_data_for_the_contact_sn_curve_of_a_plastic_material(
        self: "CastSelf",
    ) -> "_297.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial":
        from mastapy._private.materials import _297

        return self.__parent__._cast(
            _297.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial
        )

    @property
    def abstract_stress_cycles_data_for_an_sn_curve_of_a_plastic_material(
        self: "CastSelf",
    ) -> "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial":
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
class AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial(_0.APIBase):
    """AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _ABSTRACT_STRESS_CYCLES_DATA_FOR_AN_SN_CURVE_OF_A_PLASTIC_MATERIAL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def number_of_load_cycles(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NumberOfLoadCycles

        if temp is None:
            return 0.0

        return temp

    @number_of_load_cycles.setter
    @enforce_parameter_types
    def number_of_load_cycles(self: "Self", value: "float") -> None:
        self.wrapped.NumberOfLoadCycles = float(value) if value is not None else 0.0

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial":
        """Cast to another type.

        Returns:
            _Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
        """
        return _Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial(self)
