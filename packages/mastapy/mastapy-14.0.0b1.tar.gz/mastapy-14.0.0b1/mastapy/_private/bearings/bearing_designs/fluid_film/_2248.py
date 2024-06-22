"""TiltingPadThrustBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.bearings.bearing_designs.fluid_film import _2240
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_TILTING_PAD_THRUST_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "TiltingPadThrustBearing"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.bearings import _1952
    from mastapy._private.bearings.bearing_designs import _2184, _2187, _2183

    Self = TypeVar("Self", bound="TiltingPadThrustBearing")
    CastSelf = TypeVar(
        "CastSelf", bound="TiltingPadThrustBearing._Cast_TiltingPadThrustBearing"
    )


__docformat__ = "restructuredtext en"
__all__ = ("TiltingPadThrustBearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_TiltingPadThrustBearing:
    """Special nested class for casting TiltingPadThrustBearing to subclasses."""

    __parent__: "TiltingPadThrustBearing"

    @property
    def pad_fluid_film_bearing(self: "CastSelf") -> "_2240.PadFluidFilmBearing":
        return self.__parent__._cast(_2240.PadFluidFilmBearing)

    @property
    def detailed_bearing(self: "CastSelf") -> "_2184.DetailedBearing":
        from mastapy._private.bearings.bearing_designs import _2184

        return self.__parent__._cast(_2184.DetailedBearing)

    @property
    def non_linear_bearing(self: "CastSelf") -> "_2187.NonLinearBearing":
        from mastapy._private.bearings.bearing_designs import _2187

        return self.__parent__._cast(_2187.NonLinearBearing)

    @property
    def bearing_design(self: "CastSelf") -> "_2183.BearingDesign":
        from mastapy._private.bearings.bearing_designs import _2183

        return self.__parent__._cast(_2183.BearingDesign)

    @property
    def tilting_pad_thrust_bearing(self: "CastSelf") -> "TiltingPadThrustBearing":
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
class TiltingPadThrustBearing(_2240.PadFluidFilmBearing):
    """TiltingPadThrustBearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _TILTING_PAD_THRUST_BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def non_dimensional_friction(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalFriction

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_friction.setter
    @enforce_parameter_types
    def non_dimensional_friction(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalFriction = value

    @property
    def non_dimensional_inlet_flow(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalInletFlow

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_inlet_flow.setter
    @enforce_parameter_types
    def non_dimensional_inlet_flow(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalInletFlow = value

    @property
    def non_dimensional_load(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_load.setter
    @enforce_parameter_types
    def non_dimensional_load(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalLoad = value

    @property
    def non_dimensional_minimum_film_thickness(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalMinimumFilmThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_minimum_film_thickness.setter
    @enforce_parameter_types
    def non_dimensional_minimum_film_thickness(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalMinimumFilmThickness = value

    @property
    def non_dimensional_side_flow(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalSideFlow

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_side_flow.setter
    @enforce_parameter_types
    def non_dimensional_side_flow(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalSideFlow = value

    @property
    def pad_circumferential_width(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadCircumferentialWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_height(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_height_aspect_ratio(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadHeightAspectRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_inner_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PadInnerDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pad_inner_diameter.setter
    @enforce_parameter_types
    def pad_inner_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PadInnerDiameter = value

    @property
    def pad_outer_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PadOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pad_outer_diameter.setter
    @enforce_parameter_types
    def pad_outer_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PadOuterDiameter = value

    @property
    def pad_width_aspect_ratio(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadWidthAspectRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def pivot_angular_offset(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PivotAngularOffset

        if temp is None:
            return 0.0

        return temp

    @pivot_angular_offset.setter
    @enforce_parameter_types
    def pivot_angular_offset(self: "Self", value: "float") -> None:
        self.wrapped.PivotAngularOffset = float(value) if value is not None else 0.0

    @property
    def tilting_pad_type(self: "Self") -> "_1952.TiltingPadTypes":
        """mastapy._private.bearings.TiltingPadTypes"""
        temp = self.wrapped.TiltingPadType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bearings.TiltingPadTypes")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings._1952", "TiltingPadTypes"
        )(value)

    @tilting_pad_type.setter
    @enforce_parameter_types
    def tilting_pad_type(self: "Self", value: "_1952.TiltingPadTypes") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bearings.TiltingPadTypes")
        self.wrapped.TiltingPadType = value

    @property
    def width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: "Self", value: "float") -> None:
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_TiltingPadThrustBearing":
        """Cast to another type.

        Returns:
            _Cast_TiltingPadThrustBearing
        """
        return _Cast_TiltingPadThrustBearing(self)
