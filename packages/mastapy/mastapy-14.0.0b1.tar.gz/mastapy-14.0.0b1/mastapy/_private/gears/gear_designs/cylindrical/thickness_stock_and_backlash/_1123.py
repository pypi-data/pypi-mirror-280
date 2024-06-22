"""NominalValueSpecification"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.gear_designs.cylindrical import _1115
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_NOMINAL_VALUE_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash",
    "NominalValueSpecification",
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple

    from mastapy._private.gears.gear_designs.cylindrical import _1098

    Self = TypeVar("Self", bound="NominalValueSpecification")
    CastSelf = TypeVar(
        "CastSelf", bound="NominalValueSpecification._Cast_NominalValueSpecification"
    )

T = TypeVar("T")

__docformat__ = "restructuredtext en"
__all__ = ("NominalValueSpecification",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_NominalValueSpecification:
    """Special nested class for casting NominalValueSpecification to subclasses."""

    __parent__: "NominalValueSpecification"

    @property
    def toleranced_value_specification(
        self: "CastSelf",
    ) -> "_1115.TolerancedValueSpecification":
        return self.__parent__._cast(_1115.TolerancedValueSpecification)

    @property
    def relative_measurement_view_model(
        self: "CastSelf",
    ) -> "_1098.RelativeMeasurementViewModel":
        from mastapy._private.gears.gear_designs.cylindrical import _1098

        return self.__parent__._cast(_1098.RelativeMeasurementViewModel)

    @property
    def nominal_value_specification(self: "CastSelf") -> "NominalValueSpecification":
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
class NominalValueSpecification(_1115.TolerancedValueSpecification[T]):
    """NominalValueSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _NOMINAL_VALUE_SPECIFICATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def design(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Design

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @design.setter
    @enforce_parameter_types
    def design(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Design = value

    @property
    def cast_to(self: "Self") -> "_Cast_NominalValueSpecification":
        """Cast to another type.

        Returns:
            _Cast_NominalValueSpecification
        """
        return _Cast_NominalValueSpecification(self)
