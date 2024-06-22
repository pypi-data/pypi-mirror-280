"""ToothThicknessSpecificationBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility.units_and_measurements.measurements import _1714, _1735
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_TOOTH_THICKNESS_SPECIFICATION_BASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ToothThicknessSpecificationBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.gears.gear_designs.cylindrical import (
        _1066,
        _1076,
        _1097,
        _1117,
    )

    Self = TypeVar("Self", bound="ToothThicknessSpecificationBase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ToothThicknessSpecificationBase._Cast_ToothThicknessSpecificationBase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ToothThicknessSpecificationBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ToothThicknessSpecificationBase:
    """Special nested class for casting ToothThicknessSpecificationBase to subclasses."""

    __parent__: "ToothThicknessSpecificationBase"

    @property
    def finish_tooth_thickness_design_specification(
        self: "CastSelf",
    ) -> "_1076.FinishToothThicknessDesignSpecification":
        from mastapy._private.gears.gear_designs.cylindrical import _1076

        return self.__parent__._cast(_1076.FinishToothThicknessDesignSpecification)

    @property
    def readonly_tooth_thickness_specification(
        self: "CastSelf",
    ) -> "_1097.ReadonlyToothThicknessSpecification":
        from mastapy._private.gears.gear_designs.cylindrical import _1097

        return self.__parent__._cast(_1097.ReadonlyToothThicknessSpecification)

    @property
    def tooth_thickness_specification(
        self: "CastSelf",
    ) -> "_1117.ToothThicknessSpecification":
        from mastapy._private.gears.gear_designs.cylindrical import _1117

        return self.__parent__._cast(_1117.ToothThicknessSpecification)

    @property
    def tooth_thickness_specification_base(
        self: "CastSelf",
    ) -> "ToothThicknessSpecificationBase":
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
class ToothThicknessSpecificationBase(_0.APIBase):
    """ToothThicknessSpecificationBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _TOOTH_THICKNESS_SPECIFICATION_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def ball_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BallDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ball_diameter.setter
    @enforce_parameter_types
    def ball_diameter(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BallDiameter = value

    @property
    def ball_diameter_at_form_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BallDiameterAtFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def ball_diameter_at_tip_form_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BallDiameterAtTipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_at_thickness_measurement(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DiameterAtThicknessMeasurement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter_at_thickness_measurement.setter
    @enforce_parameter_types
    def diameter_at_thickness_measurement(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DiameterAtThicknessMeasurement = value

    @property
    def maximum_number_of_teeth_for_chordal_span_test(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNumberOfTeethForChordalSpanTest

        if temp is None:
            return 0

        return temp

    @property
    def minimum_number_of_teeth_for_chordal_span_test(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumNumberOfTeethForChordalSpanTest

        if temp is None:
            return 0

        return temp

    @property
    def number_of_teeth_for_chordal_span_test(
        self: "Self",
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfTeethForChordalSpanTest

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_teeth_for_chordal_span_test.setter
    @enforce_parameter_types
    def number_of_teeth_for_chordal_span_test(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfTeethForChordalSpanTest = value

    @property
    def chordal_span(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChordalSpan

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def normal_thickness(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def normal_thickness_at_specified_diameter(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThicknessAtSpecifiedDiameter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def over_balls(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverBalls

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def over_two_pins_free_pin_method(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverTwoPinsFreePinMethod

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def over_two_pins_transverse_method(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverTwoPinsTransverseMethod

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def profile_shift(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShift

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def profile_shift_coefficient(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1735.Number]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.Number]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1735.Number](temp)

    @property
    def transverse_thickness(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def transverse_thickness_at_specified_diameter(
        self: "Self",
    ) -> "_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseThicknessAtSpecifiedDiameter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.LengthShort](temp)

    @property
    def tooth_thickness(
        self: "Self",
    ) -> "List[_1066.CylindricalGearToothThicknessSpecification[_1714.LengthShort]]":
        """List[mastapy._private.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy._private.utility.units_and_measurements.measurements.LengthShort]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThickness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ToothThicknessSpecificationBase":
        """Cast to another type.

        Returns:
            _Cast_ToothThicknessSpecificationBase
        """
        return _Cast_ToothThicknessSpecificationBase(self)
