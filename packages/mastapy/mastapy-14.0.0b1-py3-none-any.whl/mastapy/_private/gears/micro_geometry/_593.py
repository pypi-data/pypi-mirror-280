"""ProfileModification"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    enum_with_selected_value_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import enum_with_selected_value
from mastapy._private.gears.micro_geometry import _584, _585, _586, _587, _590
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PROFILE_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry", "ProfileModification"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.micro_geometry import _588, _589, _591, _592
    from mastapy._private.math_utility import _1581
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1137,
        _1138,
    )
    from mastapy._private.gears.gear_designs.conical.micro_geometry import _1213

    Self = TypeVar("Self", bound="ProfileModification")
    CastSelf = TypeVar(
        "CastSelf", bound="ProfileModification._Cast_ProfileModification"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ProfileModification",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ProfileModification:
    """Special nested class for casting ProfileModification to subclasses."""

    __parent__: "ProfileModification"

    @property
    def modification(self: "CastSelf") -> "_590.Modification":
        return self.__parent__._cast(_590.Modification)

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
    def conical_gear_profile_modification(
        self: "CastSelf",
    ) -> "_1213.ConicalGearProfileModification":
        from mastapy._private.gears.gear_designs.conical.micro_geometry import _1213

        return self.__parent__._cast(_1213.ConicalGearProfileModification)

    @property
    def profile_modification(self: "CastSelf") -> "ProfileModification":
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
class ProfileModification(_590.Modification):
    """ProfileModification

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PROFILE_MODIFICATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def barrelling_peak_point_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BarrellingPeakPointFactor

        if temp is None:
            return 0.0

        return temp

    @barrelling_peak_point_factor.setter
    @enforce_parameter_types
    def barrelling_peak_point_factor(self: "Self", value: "float") -> None:
        self.wrapped.BarrellingPeakPointFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def barrelling_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BarrellingRelief

        if temp is None:
            return 0.0

        return temp

    @barrelling_relief.setter
    @enforce_parameter_types
    def barrelling_relief(self: "Self", value: "float") -> None:
        self.wrapped.BarrellingRelief = float(value) if value is not None else 0.0

    @property
    def evaluation_lower_limit_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_factor.setter
    @enforce_parameter_types
    def evaluation_lower_limit_factor(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationLowerLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_factor_for_zero_root_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitFactorForZeroRootRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_factor_for_zero_root_relief.setter
    @enforce_parameter_types
    def evaluation_lower_limit_factor_for_zero_root_relief(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.EvaluationLowerLimitFactorForZeroRootRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_factor.setter
    @enforce_parameter_types
    def evaluation_upper_limit_factor(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationUpperLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_factor_for_zero_tip_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitFactorForZeroTipRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_factor_for_zero_tip_relief.setter
    @enforce_parameter_types
    def evaluation_upper_limit_factor_for_zero_tip_relief(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.EvaluationUpperLimitFactorForZeroTipRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_root_relief_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRootReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_root_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_linear_root_relief_factor(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationOfLinearRootReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_tip_relief_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearTipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_tip_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_linear_tip_relief_factor(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationOfLinearTipReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_root_relief_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRootReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_root_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_root_relief_factor(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.EvaluationOfParabolicRootReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_tip_relief_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicTipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_tip_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_tip_relief_factor(self: "Self", value: "float") -> None:
        self.wrapped.EvaluationOfParabolicTipReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearRelief

        if temp is None:
            return 0.0

        return temp

    @linear_relief.setter
    @enforce_parameter_types
    def linear_relief(self: "Self", value: "float") -> None:
        self.wrapped.LinearRelief = float(value) if value is not None else 0.0

    @property
    def linear_root_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearRootRelief

        if temp is None:
            return 0.0

        return temp

    @linear_root_relief.setter
    @enforce_parameter_types
    def linear_root_relief(self: "Self", value: "float") -> None:
        self.wrapped.LinearRootRelief = float(value) if value is not None else 0.0

    @property
    def linear_tip_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LinearTipRelief

        if temp is None:
            return 0.0

        return temp

    @linear_tip_relief.setter
    @enforce_parameter_types
    def linear_tip_relief(self: "Self", value: "float") -> None:
        self.wrapped.LinearTipRelief = float(value) if value is not None else 0.0

    @property
    def location_of_evaluation_lower_limit(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfEvaluationLowerLimit]"""
        temp = self.wrapped.LocationOfEvaluationLowerLimit

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_evaluation_lower_limit.setter
    @enforce_parameter_types
    def location_of_evaluation_lower_limit(
        self: "Self", value: "_584.LocationOfEvaluationLowerLimit"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfEvaluationLowerLimit = value

    @property
    def location_of_evaluation_lower_limit_for_zero_root_relief(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfEvaluationLowerLimit]"""
        temp = self.wrapped.LocationOfEvaluationLowerLimitForZeroRootRelief

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_evaluation_lower_limit_for_zero_root_relief.setter
    @enforce_parameter_types
    def location_of_evaluation_lower_limit_for_zero_root_relief(
        self: "Self", value: "_584.LocationOfEvaluationLowerLimit"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfEvaluationLowerLimitForZeroRootRelief = value

    @property
    def location_of_evaluation_upper_limit(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfEvaluationUpperLimit]"""
        temp = self.wrapped.LocationOfEvaluationUpperLimit

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_evaluation_upper_limit.setter
    @enforce_parameter_types
    def location_of_evaluation_upper_limit(
        self: "Self", value: "_585.LocationOfEvaluationUpperLimit"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfEvaluationUpperLimit = value

    @property
    def location_of_evaluation_upper_limit_for_zero_tip_relief(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfEvaluationUpperLimit]"""
        temp = self.wrapped.LocationOfEvaluationUpperLimitForZeroTipRelief

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_evaluation_upper_limit_for_zero_tip_relief.setter
    @enforce_parameter_types
    def location_of_evaluation_upper_limit_for_zero_tip_relief(
        self: "Self", value: "_585.LocationOfEvaluationUpperLimit"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfEvaluationUpperLimitForZeroTipRelief = value

    @property
    def location_of_root_modification_start(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfRootReliefEvaluation]"""
        temp = self.wrapped.LocationOfRootModificationStart

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_root_modification_start.setter
    @enforce_parameter_types
    def location_of_root_modification_start(
        self: "Self", value: "_586.LocationOfRootReliefEvaluation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfRootModificationStart = value

    @property
    def location_of_root_relief_evaluation(
        self: "Self",
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation"
    ):
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfRootReliefEvaluation]"""
        temp = self.wrapped.LocationOfRootReliefEvaluation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_root_relief_evaluation.setter
    @enforce_parameter_types
    def location_of_root_relief_evaluation(
        self: "Self", value: "_586.LocationOfRootReliefEvaluation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfRootReliefEvaluation = value

    @property
    def location_of_tip_relief_evaluation(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation":
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfTipReliefEvaluation]"""
        temp = self.wrapped.LocationOfTipReliefEvaluation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_tip_relief_evaluation.setter
    @enforce_parameter_types
    def location_of_tip_relief_evaluation(
        self: "Self", value: "_587.LocationOfTipReliefEvaluation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfTipReliefEvaluation = value

    @property
    def location_of_tip_relief_start(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation":
        """EnumWithSelectedValue[mastapy._private.gears.micro_geometry.LocationOfTipReliefEvaluation]"""
        temp = self.wrapped.LocationOfTipReliefStart

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_tip_relief_start.setter
    @enforce_parameter_types
    def location_of_tip_relief_start(
        self: "Self", value: "_587.LocationOfTipReliefEvaluation"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfTipReliefStart = value

    @property
    def main_profile_modification_ends_at_the_start_of_root_relief(
        self: "Self",
    ) -> "_588.MainProfileReliefEndsAtTheStartOfRootReliefOption":
        """mastapy._private.gears.micro_geometry.MainProfileReliefEndsAtTheStartOfRootReliefOption"""
        temp = self.wrapped.MainProfileModificationEndsAtTheStartOfRootRelief

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._588",
            "MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )(value)

    @main_profile_modification_ends_at_the_start_of_root_relief.setter
    @enforce_parameter_types
    def main_profile_modification_ends_at_the_start_of_root_relief(
        self: "Self", value: "_588.MainProfileReliefEndsAtTheStartOfRootReliefOption"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )
        self.wrapped.MainProfileModificationEndsAtTheStartOfRootRelief = value

    @property
    def main_profile_modification_ends_at_the_start_of_tip_relief(
        self: "Self",
    ) -> "_589.MainProfileReliefEndsAtTheStartOfTipReliefOption":
        """mastapy._private.gears.micro_geometry.MainProfileReliefEndsAtTheStartOfTipReliefOption"""
        temp = self.wrapped.MainProfileModificationEndsAtTheStartOfTipRelief

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._589",
            "MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )(value)

    @main_profile_modification_ends_at_the_start_of_tip_relief.setter
    @enforce_parameter_types
    def main_profile_modification_ends_at_the_start_of_tip_relief(
        self: "Self", value: "_589.MainProfileReliefEndsAtTheStartOfTipReliefOption"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )
        self.wrapped.MainProfileModificationEndsAtTheStartOfTipRelief = value

    @property
    def measure_root_reliefs_from_extrapolated_linear_relief(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.MeasureRootReliefsFromExtrapolatedLinearRelief

        if temp is None:
            return False

        return temp

    @measure_root_reliefs_from_extrapolated_linear_relief.setter
    @enforce_parameter_types
    def measure_root_reliefs_from_extrapolated_linear_relief(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.MeasureRootReliefsFromExtrapolatedLinearRelief = (
            bool(value) if value is not None else False
        )

    @property
    def measure_tip_reliefs_from_extrapolated_linear_relief(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.MeasureTipReliefsFromExtrapolatedLinearRelief

        if temp is None:
            return False

        return temp

    @measure_tip_reliefs_from_extrapolated_linear_relief.setter
    @enforce_parameter_types
    def measure_tip_reliefs_from_extrapolated_linear_relief(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.MeasureTipReliefsFromExtrapolatedLinearRelief = (
            bool(value) if value is not None else False
        )

    @property
    def measured_data(self: "Self") -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.MeasuredData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @measured_data.setter
    @enforce_parameter_types
    def measured_data(self: "Self", value: "_1581.Vector2DListAccessor") -> None:
        self.wrapped.MeasuredData = value.wrapped

    @property
    def parabolic_root_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ParabolicRootRelief

        if temp is None:
            return 0.0

        return temp

    @parabolic_root_relief.setter
    @enforce_parameter_types
    def parabolic_root_relief(self: "Self", value: "float") -> None:
        self.wrapped.ParabolicRootRelief = float(value) if value is not None else 0.0

    @property
    def parabolic_root_relief_starts_tangent_to_main_profile_relief(
        self: "Self",
    ) -> "_591.ParabolicRootReliefStartsTangentToMainProfileRelief":
        """mastapy._private.gears.micro_geometry.ParabolicRootReliefStartsTangentToMainProfileRelief"""
        temp = self.wrapped.ParabolicRootReliefStartsTangentToMainProfileRelief

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicRootReliefStartsTangentToMainProfileRelief",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._591",
            "ParabolicRootReliefStartsTangentToMainProfileRelief",
        )(value)

    @parabolic_root_relief_starts_tangent_to_main_profile_relief.setter
    @enforce_parameter_types
    def parabolic_root_relief_starts_tangent_to_main_profile_relief(
        self: "Self", value: "_591.ParabolicRootReliefStartsTangentToMainProfileRelief"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicRootReliefStartsTangentToMainProfileRelief",
        )
        self.wrapped.ParabolicRootReliefStartsTangentToMainProfileRelief = value

    @property
    def parabolic_tip_relief(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ParabolicTipRelief

        if temp is None:
            return 0.0

        return temp

    @parabolic_tip_relief.setter
    @enforce_parameter_types
    def parabolic_tip_relief(self: "Self", value: "float") -> None:
        self.wrapped.ParabolicTipRelief = float(value) if value is not None else 0.0

    @property
    def parabolic_tip_relief_starts_tangent_to_main_profile_relief(
        self: "Self",
    ) -> "_592.ParabolicTipReliefStartsTangentToMainProfileRelief":
        """mastapy._private.gears.micro_geometry.ParabolicTipReliefStartsTangentToMainProfileRelief"""
        temp = self.wrapped.ParabolicTipReliefStartsTangentToMainProfileRelief

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicTipReliefStartsTangentToMainProfileRelief",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.micro_geometry._592",
            "ParabolicTipReliefStartsTangentToMainProfileRelief",
        )(value)

    @parabolic_tip_relief_starts_tangent_to_main_profile_relief.setter
    @enforce_parameter_types
    def parabolic_tip_relief_starts_tangent_to_main_profile_relief(
        self: "Self", value: "_592.ParabolicTipReliefStartsTangentToMainProfileRelief"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicTipReliefStartsTangentToMainProfileRelief",
        )
        self.wrapped.ParabolicTipReliefStartsTangentToMainProfileRelief = value

    @property
    def start_of_linear_root_relief_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRootReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_root_relief_factor.setter
    @enforce_parameter_types
    def start_of_linear_root_relief_factor(self: "Self", value: "float") -> None:
        self.wrapped.StartOfLinearRootReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_tip_relief_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearTipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_tip_relief_factor.setter
    @enforce_parameter_types
    def start_of_linear_tip_relief_factor(self: "Self", value: "float") -> None:
        self.wrapped.StartOfLinearTipReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_root_relief_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRootReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_root_relief_factor.setter
    @enforce_parameter_types
    def start_of_parabolic_root_relief_factor(self: "Self", value: "float") -> None:
        self.wrapped.StartOfParabolicRootReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_tip_relief_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicTipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_tip_relief_factor.setter
    @enforce_parameter_types
    def start_of_parabolic_tip_relief_factor(self: "Self", value: "float") -> None:
        self.wrapped.StartOfParabolicTipReliefFactor = (
            float(value) if value is not None else 0.0
        )

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
    def use_user_specified_barrelling_peak_point(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseUserSpecifiedBarrellingPeakPoint

        if temp is None:
            return False

        return temp

    @use_user_specified_barrelling_peak_point.setter
    @enforce_parameter_types
    def use_user_specified_barrelling_peak_point(self: "Self", value: "bool") -> None:
        self.wrapped.UseUserSpecifiedBarrellingPeakPoint = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: "Self") -> "_Cast_ProfileModification":
        """Cast to another type.

        Returns:
            _Cast_ProfileModification
        """
        return _Cast_ProfileModification(self)
