"""CylindricalGearLeadModification"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.micro_geometry import _583
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LEAD_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearLeadModification",
)

if TYPE_CHECKING:
    from typing import Any, Type, Optional, TypeVar

    from mastapy._private.utility_gui.charts import _1919
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1147,
        _1129,
    )
    from mastapy._private.gears.micro_geometry import _590

    Self = TypeVar("Self", bound="CylindricalGearLeadModification")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearLeadModification._Cast_CylindricalGearLeadModification",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearLeadModification",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearLeadModification:
    """Special nested class for casting CylindricalGearLeadModification to subclasses."""

    __parent__: "CylindricalGearLeadModification"

    @property
    def lead_modification(self: "CastSelf") -> "_583.LeadModification":
        return self.__parent__._cast(_583.LeadModification)

    @property
    def modification(self: "CastSelf") -> "_590.Modification":
        from mastapy._private.gears.micro_geometry import _590

        return self.__parent__._cast(_590.Modification)

    @property
    def cylindrical_gear_lead_modification_at_profile_position(
        self: "CastSelf",
    ) -> "_1129.CylindricalGearLeadModificationAtProfilePosition":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1129

        return self.__parent__._cast(
            _1129.CylindricalGearLeadModificationAtProfilePosition
        )

    @property
    def cylindrical_gear_lead_modification(
        self: "CastSelf",
    ) -> "CylindricalGearLeadModification":
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
class CylindricalGearLeadModification(_583.LeadModification):
    """CylindricalGearLeadModification

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_LEAD_MODIFICATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def evaluation_left_limit(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationLeftLimit

        if temp is None:
            return 0.0

        return temp

    @evaluation_left_limit.setter
    @enforce_parameter_types
    def evaluation_left_limit(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationLeftLimit = float(value) if value is not None else 0.0

    @property
    def evaluation_of_linear_left_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearLeftRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_left_relief.setter
    @enforce_parameter_types
    def evaluation_of_linear_left_relief(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationOfLinearLeftRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_right_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRightRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_right_relief.setter
    @enforce_parameter_types
    def evaluation_of_linear_right_relief(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationOfLinearRightRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_left_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicLeftRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_left_relief.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_left_relief(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationOfParabolicLeftRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_right_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRightRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_right_relief.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_right_relief(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationOfParabolicRightRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_right_limit(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationRightLimit

        if temp is None:
            return 0.0

        return temp

    @evaluation_right_limit.setter
    @enforce_parameter_types
    def evaluation_right_limit(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationRightLimit = float(value) if value is not None else 0.0

    @property
    def evaluation_side_limit(self: "Self") -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationSideLimit

        if temp is None:
            return None

        return temp

    @evaluation_side_limit.setter
    @enforce_parameter_types
    def evaluation_side_limit(self: "Self", value: "Optional[float]") -> None:
        self.wrapped.EvaluationSideLimit = value

    @property
    def evaluation_of_linear_side_relief(self: "Self") -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationOfLinearSideRelief

        if temp is None:
            return None

        return temp

    @evaluation_of_linear_side_relief.setter
    @enforce_parameter_types
    def evaluation_of_linear_side_relief(
        self: "Self", value: "Optional[float]"
    ) -> None:
        self.wrapped.EvaluationOfLinearSideRelief = value

    @property
    def evaluation_of_parabolic_side_relief(self: "Self") -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationOfParabolicSideRelief

        if temp is None:
            return None

        return temp

    @evaluation_of_parabolic_side_relief.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_side_relief(
        self: "Self", value: "Optional[float]"
    ) -> None:
        self.wrapped.EvaluationOfParabolicSideRelief = value

    @property
    def helix_angle_modification_at_original_reference_diameter(
        self: "Self",
    ) -> "float":
        """float"""
        temp = self.wrapped.HelixAngleModificationAtOriginalReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @helix_angle_modification_at_original_reference_diameter.setter
    @enforce_parameter_types
    def helix_angle_modification_at_original_reference_diameter(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.HelixAngleModificationAtOriginalReferenceDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def lead_modification_chart(self: "Self") -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_relief_isodinagmavdi(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearReliefISODINAGMAVDI

        if temp is None:
            return 0.0

        return temp

    @linear_relief_isodinagmavdi.setter
    @enforce_parameter_types
    def linear_relief_isodinagmavdi(self: "Self", value: "float") -> None:
        self.wrapped.LinearReliefISODINAGMAVDI = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief_isodinagmavdi_across_full_face_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearReliefISODINAGMAVDIAcrossFullFaceWidth

        if temp is None:
            return 0.0

        return temp

    @linear_relief_isodinagmavdi_across_full_face_width.setter
    @enforce_parameter_types
    def linear_relief_isodinagmavdi_across_full_face_width(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.LinearReliefISODINAGMAVDIAcrossFullFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief_ldp(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearReliefLDP

        if temp is None:
            return 0.0

        return temp

    @linear_relief_ldp.setter
    @enforce_parameter_types
    def linear_relief_ldp(self: "Self", value: "float") -> None:
        self.wrapped.LinearReliefLDP = float(value) if value is not None else 0.0

    @property
    def linear_relief_ldp_across_full_face_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearReliefLDPAcrossFullFaceWidth

        if temp is None:
            return 0.0

        return temp

    @linear_relief_ldp_across_full_face_width.setter
    @enforce_parameter_types
    def linear_relief_ldp_across_full_face_width(self: "Self", value: "float") -> None:
        self.wrapped.LinearReliefLDPAcrossFullFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief_across_full_face_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearReliefAcrossFullFaceWidth

        if temp is None:
            return 0.0

        return temp

    @linear_relief_across_full_face_width.setter
    @enforce_parameter_types
    def linear_relief_across_full_face_width(self: "Self", value: "float") -> None:
        self.wrapped.LinearReliefAcrossFullFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def modified_base_helix_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ModifiedBaseHelixAngle

        if temp is None:
            return 0.0

        return temp

    @modified_base_helix_angle.setter
    @enforce_parameter_types
    def modified_base_helix_angle(self: "Self", value: "float") -> None:
        self.wrapped.ModifiedBaseHelixAngle = float(value) if value is not None else 0.0

    @property
    def modified_helix_angle_assuming_unmodified_normal_module(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ModifiedHelixAngleAssumingUnmodifiedNormalModule

        if temp is None:
            return 0.0

        return temp

    @modified_helix_angle_assuming_unmodified_normal_module.setter
    @enforce_parameter_types
    def modified_helix_angle_assuming_unmodified_normal_module(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.ModifiedHelixAngleAssumingUnmodifiedNormalModule = (
            float(value) if value is not None else 0.0
        )

    @property
    def modified_helix_angle_at_original_reference_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ModifiedHelixAngleAtOriginalReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @modified_helix_angle_at_original_reference_diameter.setter
    @enforce_parameter_types
    def modified_helix_angle_at_original_reference_diameter(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.ModifiedHelixAngleAtOriginalReferenceDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def modified_normal_pressure_angle_due_to_helix_angle_modification_assuming_unmodified_normal_module(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ModifiedNormalPressureAngleDueToHelixAngleModificationAssumingUnmodifiedNormalModule
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_normal_pressure_angle_due_to_helix_angle_modification_at_original_reference_diameter(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ModifiedNormalPressureAngleDueToHelixAngleModificationAtOriginalReferenceDiameter
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def start_of_linear_left_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearLeftRelief

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_left_relief.setter
    @enforce_parameter_types
    def start_of_linear_left_relief(self: "Self", value: "float") -> None:
        self.wrapped.StartOfLinearLeftRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_right_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRightRelief

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_right_relief.setter
    @enforce_parameter_types
    def start_of_linear_right_relief(self: "Self", value: "float") -> None:
        self.wrapped.StartOfLinearRightRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_side_relief(self: "Self") -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.StartOfLinearSideRelief

        if temp is None:
            return None

        return temp

    @start_of_linear_side_relief.setter
    @enforce_parameter_types
    def start_of_linear_side_relief(self: "Self", value: "Optional[float]") -> None:
        self.wrapped.StartOfLinearSideRelief = value

    @property
    def start_of_parabolic_left_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicLeftRelief

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_left_relief.setter
    @enforce_parameter_types
    def start_of_parabolic_left_relief(self: "Self", value: "float") -> None:
        self.wrapped.StartOfParabolicLeftRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_right_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRightRelief

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_right_relief.setter
    @enforce_parameter_types
    def start_of_parabolic_right_relief(self: "Self", value: "float") -> None:
        self.wrapped.StartOfParabolicRightRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_side_relief(self: "Self") -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.StartOfParabolicSideRelief

        if temp is None:
            return None

        return temp

    @start_of_parabolic_side_relief.setter
    @enforce_parameter_types
    def start_of_parabolic_side_relief(self: "Self", value: "Optional[float]") -> None:
        self.wrapped.StartOfParabolicSideRelief = value

    @property
    def use_measured_data(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseMeasuredData

        if temp is None:
            return False

        return temp

    @use_measured_data.setter
    @enforce_parameter_types
    def use_measured_data(self: "Self", value: "bool") -> None:
        self.wrapped.UseMeasuredData = bool(value) if value is not None else False

    @property
    def lead_modification_for_customer_102cad(
        self: "Self",
    ) -> "_1147.LeadModificationForCustomer102CAD":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.LeadModificationForCustomer102CAD

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadModificationForCustomer102CAD

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def relief_of(self: "Self", face_width: "float") -> "float":
        """float

        Args:
            face_width (float)
        """
        face_width = float(face_width)
        method_result = self.wrapped.ReliefOf(face_width if face_width else 0.0)
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearLeadModification":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearLeadModification
        """
        return _Cast_CylindricalGearLeadModification(self)
