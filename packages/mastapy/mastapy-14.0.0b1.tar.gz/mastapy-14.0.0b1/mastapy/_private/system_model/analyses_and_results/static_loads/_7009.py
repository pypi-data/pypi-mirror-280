"""CylindricalGearManufactureError"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _7038
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MANUFACTURE_ERROR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearManufactureError",
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.math_utility import _1581

    Self = TypeVar("Self", bound="CylindricalGearManufactureError")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearManufactureError._Cast_CylindricalGearManufactureError",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearManufactureError",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearManufactureError:
    """Special nested class for casting CylindricalGearManufactureError to subclasses."""

    __parent__: "CylindricalGearManufactureError"

    @property
    def gear_manufacture_error(self: "CastSelf") -> "_7038.GearManufactureError":
        return self.__parent__._cast(_7038.GearManufactureError)

    @property
    def cylindrical_gear_manufacture_error(
        self: "CastSelf",
    ) -> "CylindricalGearManufactureError":
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
class CylindricalGearManufactureError(_7038.GearManufactureError):
    """CylindricalGearManufactureError

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_MANUFACTURE_ERROR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def clocking_angle_error(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ClockingAngleError

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @clocking_angle_error.setter
    @enforce_parameter_types
    def clocking_angle_error(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ClockingAngleError = value

    @property
    def extra_backlash(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ExtraBacklash

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @extra_backlash.setter
    @enforce_parameter_types
    def extra_backlash(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ExtraBacklash = value

    @property
    def pitch_error_measurement_diameter(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PitchErrorMeasurementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pitch_error_measurement_diameter.setter
    @enforce_parameter_types
    def pitch_error_measurement_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PitchErrorMeasurementDiameter = value

    @property
    def pitch_error_measurement_face_width(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PitchErrorMeasurementFaceWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pitch_error_measurement_face_width.setter
    @enforce_parameter_types
    def pitch_error_measurement_face_width(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PitchErrorMeasurementFaceWidth = value

    @property
    def pitch_error_phase_shift_on_left_flank(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PitchErrorPhaseShiftOnLeftFlank

        if temp is None:
            return 0.0

        return temp

    @pitch_error_phase_shift_on_left_flank.setter
    @enforce_parameter_types
    def pitch_error_phase_shift_on_left_flank(self: "Self", value: "float") -> None:
        self.wrapped.PitchErrorPhaseShiftOnLeftFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def pitch_error_phase_shift_on_right_flank(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PitchErrorPhaseShiftOnRightFlank

        if temp is None:
            return 0.0

        return temp

    @pitch_error_phase_shift_on_right_flank.setter
    @enforce_parameter_types
    def pitch_error_phase_shift_on_right_flank(self: "Self", value: "float") -> None:
        self.wrapped.PitchErrorPhaseShiftOnRightFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def pitch_errors_left_flank(self: "Self") -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.PitchErrorsLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @pitch_errors_left_flank.setter
    @enforce_parameter_types
    def pitch_errors_left_flank(
        self: "Self", value: "_1581.Vector2DListAccessor"
    ) -> None:
        self.wrapped.PitchErrorsLeftFlank = value.wrapped

    @property
    def pitch_errors_right_flank(self: "Self") -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.PitchErrorsRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @pitch_errors_right_flank.setter
    @enforce_parameter_types
    def pitch_errors_right_flank(
        self: "Self", value: "_1581.Vector2DListAccessor"
    ) -> None:
        self.wrapped.PitchErrorsRightFlank = value.wrapped

    @property
    def runout(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Runout

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @runout.setter
    @enforce_parameter_types
    def runout(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Runout = value

    @property
    def runout_reference_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RunoutReferenceAngle

        if temp is None:
            return 0.0

        return temp

    @runout_reference_angle.setter
    @enforce_parameter_types
    def runout_reference_angle(self: "Self", value: "float") -> None:
        self.wrapped.RunoutReferenceAngle = float(value) if value is not None else 0.0

    @property
    def separation_on_left_flank(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SeparationOnLeftFlank

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @separation_on_left_flank.setter
    @enforce_parameter_types
    def separation_on_left_flank(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SeparationOnLeftFlank = value

    @property
    def separation_on_right_flank(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SeparationOnRightFlank

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @separation_on_right_flank.setter
    @enforce_parameter_types
    def separation_on_right_flank(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SeparationOnRightFlank = value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearManufactureError":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearManufactureError
        """
        return _Cast_CylindricalGearManufactureError(self)
