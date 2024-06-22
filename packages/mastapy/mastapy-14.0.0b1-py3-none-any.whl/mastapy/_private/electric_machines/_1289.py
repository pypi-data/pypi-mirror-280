"""CADRotor"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.electric_machines import _1338
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CAD_ROTOR = python_net_import("SMT.MastaAPI.ElectricMachines", "CADRotor")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.electric_machines import _1288, _1292

    Self = TypeVar("Self", bound="CADRotor")
    CastSelf = TypeVar("CastSelf", bound="CADRotor._Cast_CADRotor")


__docformat__ = "restructuredtext en"
__all__ = ("CADRotor",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CADRotor:
    """Special nested class for casting CADRotor to subclasses."""

    __parent__: "CADRotor"

    @property
    def rotor(self: "CastSelf") -> "_1338.Rotor":
        return self.__parent__._cast(_1338.Rotor)

    @property
    def cad_wound_field_synchronous_rotor(
        self: "CastSelf",
    ) -> "_1292.CADWoundFieldSynchronousRotor":
        from mastapy._private.electric_machines import _1292

        return self.__parent__._cast(_1292.CADWoundFieldSynchronousRotor)

    @property
    def cad_rotor(self: "CastSelf") -> "CADRotor":
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
class CADRotor(_1338.Rotor):
    """CADRotor

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CAD_ROTOR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def importing_full_rotor(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ImportingFullRotor

        if temp is None:
            return False

        return temp

    @importing_full_rotor.setter
    @enforce_parameter_types
    def importing_full_rotor(self: "Self", value: "bool") -> None:
        self.wrapped.ImportingFullRotor = bool(value) if value is not None else False

    @property
    def number_of_imported_poles(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfImportedPoles

        if temp is None:
            return 0

        return temp

    @number_of_imported_poles.setter
    @enforce_parameter_types
    def number_of_imported_poles(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfImportedPoles = int(value) if value is not None else 0

    @property
    def number_of_magnet_layers(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfMagnetLayers

        if temp is None:
            return 0

        return temp

    @number_of_magnet_layers.setter
    @enforce_parameter_types
    def number_of_magnet_layers(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfMagnetLayers = int(value) if value is not None else 0

    @property
    def offset_of_additional_line_used_for_estimating_kair(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OffsetOfAdditionalLineUsedForEstimatingKair

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @offset_of_additional_line_used_for_estimating_kair.setter
    @enforce_parameter_types
    def offset_of_additional_line_used_for_estimating_kair(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OffsetOfAdditionalLineUsedForEstimatingKair = value

    @property
    def magnet_layers(self: "Self") -> "List[_1288.CADMagnetsForLayer]":
        """List[mastapy._private.electric_machines.CADMagnetsForLayer]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagnetLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CADRotor":
        """Cast to another type.

        Returns:
            _Cast_CADRotor
        """
        return _Cast_CADRotor(self)
