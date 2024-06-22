"""GearSetCreationOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_SET_CREATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.CreationOptions", "GearSetCreationOptions"
)

if TYPE_CHECKING:
    from typing import Any, Type, List

    from mastapy._private.gears.gear_designs import _974
    from mastapy._private.gears.gear_designs.creation_options import _1184, _1186, _1187

    Self = TypeVar("Self", bound="GearSetCreationOptions")
    CastSelf = TypeVar(
        "CastSelf", bound="GearSetCreationOptions._Cast_GearSetCreationOptions"
    )

T = TypeVar("T", bound="_974.GearSetDesign")

__docformat__ = "restructuredtext en"
__all__ = ("GearSetCreationOptions",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearSetCreationOptions:
    """Special nested class for casting GearSetCreationOptions to subclasses."""

    __parent__: "GearSetCreationOptions"

    @property
    def cylindrical_gear_pair_creation_options(
        self: "CastSelf",
    ) -> "_1184.CylindricalGearPairCreationOptions":
        from mastapy._private.gears.gear_designs.creation_options import _1184

        return self.__parent__._cast(_1184.CylindricalGearPairCreationOptions)

    @property
    def hypoid_gear_set_creation_options(
        self: "CastSelf",
    ) -> "_1186.HypoidGearSetCreationOptions":
        from mastapy._private.gears.gear_designs.creation_options import _1186

        return self.__parent__._cast(_1186.HypoidGearSetCreationOptions)

    @property
    def spiral_bevel_gear_set_creation_options(
        self: "CastSelf",
    ) -> "_1187.SpiralBevelGearSetCreationOptions":
        from mastapy._private.gears.gear_designs.creation_options import _1187

        return self.__parent__._cast(_1187.SpiralBevelGearSetCreationOptions)

    @property
    def gear_set_creation_options(self: "CastSelf") -> "GearSetCreationOptions":
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
class GearSetCreationOptions(_0.APIBase, Generic[T]):
    """GearSetCreationOptions

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _GEAR_SET_CREATION_OPTIONS

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
    def gear_set_design(self: "Self") -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesign

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
    def cast_to(self: "Self") -> "_Cast_GearSetCreationOptions":
        """Cast to another type.

        Returns:
            _Cast_GearSetCreationOptions
        """
        return _Cast_GearSetCreationOptions(self)
