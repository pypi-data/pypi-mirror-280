"""PadFluidFilmBearing"""
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
from mastapy._private._internal.implicit import overridable, enum_with_selected_value
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.bearings import _1949
from mastapy._private.bearings.bearing_designs import _2184
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PAD_FLUID_FILM_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "PadFluidFilmBearing"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.bearings.bearing_designs.fluid_film import _2247, _2248
    from mastapy._private.bearings.bearing_designs import _2187, _2183

    Self = TypeVar("Self", bound="PadFluidFilmBearing")
    CastSelf = TypeVar(
        "CastSelf", bound="PadFluidFilmBearing._Cast_PadFluidFilmBearing"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PadFluidFilmBearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PadFluidFilmBearing:
    """Special nested class for casting PadFluidFilmBearing to subclasses."""

    __parent__: "PadFluidFilmBearing"

    @property
    def detailed_bearing(self: "CastSelf") -> "_2184.DetailedBearing":
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
    def tilting_pad_journal_bearing(
        self: "CastSelf",
    ) -> "_2247.TiltingPadJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2247

        return self.__parent__._cast(_2247.TiltingPadJournalBearing)

    @property
    def tilting_pad_thrust_bearing(self: "CastSelf") -> "_2248.TiltingPadThrustBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2248

        return self.__parent__._cast(_2248.TiltingPadThrustBearing)

    @property
    def pad_fluid_film_bearing(self: "CastSelf") -> "PadFluidFilmBearing":
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
class PadFluidFilmBearing(_2184.DetailedBearing):
    """PadFluidFilmBearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PAD_FLUID_FILM_BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def collar_surface_roughness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.CollarSurfaceRoughness

        if temp is None:
            return 0.0

        return temp

    @collar_surface_roughness.setter
    @enforce_parameter_types
    def collar_surface_roughness(self: "Self", value: "float") -> None:
        self.wrapped.CollarSurfaceRoughness = float(value) if value is not None else 0.0

    @property
    def limiting_film_thickness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitingFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_pads(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfPads

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_pads.setter
    @enforce_parameter_types
    def number_of_pads(self: "Self", value: "Union[int, Tuple[int, bool]]") -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfPads = value

    @property
    def pad_angular_extent(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PadAngularExtent

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pad_angular_extent.setter
    @enforce_parameter_types
    def pad_angular_extent(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PadAngularExtent = value

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
    def rotational_direction(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RotationalDirections":
        """EnumWithSelectedValue[mastapy._private.bearings.RotationalDirections]"""
        temp = self.wrapped.RotationalDirection

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RotationalDirections.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @rotational_direction.setter
    @enforce_parameter_types
    def rotational_direction(self: "Self", value: "_1949.RotationalDirections") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RotationalDirections.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RotationalDirection = value

    @property
    def cast_to(self: "Self") -> "_Cast_PadFluidFilmBearing":
        """Cast to another type.

        Returns:
            _Cast_PadFluidFilmBearing
        """
        return _Cast_PadFluidFilmBearing(self)
