"""Modification"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MODIFICATION = python_net_import("SMT.MastaAPI.Gears.MicroGeometry", "Modification")

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.cylindrical import _1052
    from mastapy._private.gears.micro_geometry import _580, _583, _593
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1125,
        _1128,
        _1129,
        _1137,
        _1138,
        _1142,
    )
    from mastapy._private.gears.gear_designs.conical.micro_geometry import (
        _1210,
        _1212,
        _1213,
    )

    Self = TypeVar("Self", bound="Modification")
    CastSelf = TypeVar("CastSelf", bound="Modification._Cast_Modification")


__docformat__ = "restructuredtext en"
__all__ = ("Modification",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Modification:
    """Special nested class for casting Modification to subclasses."""

    __parent__: "Modification"

    @property
    def bias_modification(self: "CastSelf") -> "_580.BiasModification":
        from mastapy._private.gears.micro_geometry import _580

        return self.__parent__._cast(_580.BiasModification)

    @property
    def lead_modification(self: "CastSelf") -> "_583.LeadModification":
        from mastapy._private.gears.micro_geometry import _583

        return self.__parent__._cast(_583.LeadModification)

    @property
    def profile_modification(self: "CastSelf") -> "_593.ProfileModification":
        from mastapy._private.gears.micro_geometry import _593

        return self.__parent__._cast(_593.ProfileModification)

    @property
    def cylindrical_gear_bias_modification(
        self: "CastSelf",
    ) -> "_1125.CylindricalGearBiasModification":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1125

        return self.__parent__._cast(_1125.CylindricalGearBiasModification)

    @property
    def cylindrical_gear_lead_modification(
        self: "CastSelf",
    ) -> "_1128.CylindricalGearLeadModification":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1128

        return self.__parent__._cast(_1128.CylindricalGearLeadModification)

    @property
    def cylindrical_gear_lead_modification_at_profile_position(
        self: "CastSelf",
    ) -> "_1129.CylindricalGearLeadModificationAtProfilePosition":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1129

        return self.__parent__._cast(
            _1129.CylindricalGearLeadModificationAtProfilePosition
        )

    @property
    def cylindrical_gear_profile_modification(
        self: "CastSelf",
    ) -> "_1137.CylindricalGearProfileModification":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1137

        return self.__parent__._cast(_1137.CylindricalGearProfileModification)

    @property
    def cylindrical_gear_profile_modification_at_face_width_position(
        self: "CastSelf",
    ) -> "_1138.CylindricalGearProfileModificationAtFaceWidthPosition":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1138

        return self.__parent__._cast(
            _1138.CylindricalGearProfileModificationAtFaceWidthPosition
        )

    @property
    def cylindrical_gear_triangular_end_modification(
        self: "CastSelf",
    ) -> "_1142.CylindricalGearTriangularEndModification":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1142

        return self.__parent__._cast(_1142.CylindricalGearTriangularEndModification)

    @property
    def conical_gear_bias_modification(
        self: "CastSelf",
    ) -> "_1210.ConicalGearBiasModification":
        from mastapy._private.gears.gear_designs.conical.micro_geometry import _1210

        return self.__parent__._cast(_1210.ConicalGearBiasModification)

    @property
    def conical_gear_lead_modification(
        self: "CastSelf",
    ) -> "_1212.ConicalGearLeadModification":
        from mastapy._private.gears.gear_designs.conical.micro_geometry import _1212

        return self.__parent__._cast(_1212.ConicalGearLeadModification)

    @property
    def conical_gear_profile_modification(
        self: "CastSelf",
    ) -> "_1213.ConicalGearProfileModification":
        from mastapy._private.gears.gear_designs.conical.micro_geometry import _1213

        return self.__parent__._cast(_1213.ConicalGearProfileModification)

    @property
    def modification(self: "CastSelf") -> "Modification":
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
class Modification(_0.APIBase):
    """Modification

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MODIFICATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def settings(self: "Self") -> "_1052.CylindricalGearMicroGeometrySettingsItem":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearMicroGeometrySettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Settings

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
    def cast_to(self: "Self") -> "_Cast_Modification":
        """Cast to another type.

        Returns:
            _Cast_Modification
        """
        return _Cast_Modification(self)
