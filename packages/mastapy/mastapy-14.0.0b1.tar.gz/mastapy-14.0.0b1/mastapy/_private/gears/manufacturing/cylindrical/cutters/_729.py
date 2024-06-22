"""CylindricalGearAbstractCutterDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.utility.databases import _1879
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ABSTRACT_CUTTER_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalGearAbstractCutterDesign",
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical.cutters import (
        _730,
        _731,
        _732,
        _733,
        _735,
        _736,
        _737,
        _738,
        _741,
    )

    Self = TypeVar("Self", bound="CylindricalGearAbstractCutterDesign")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearAbstractCutterDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearAbstractCutterDesign:
    """Special nested class for casting CylindricalGearAbstractCutterDesign to subclasses."""

    __parent__: "CylindricalGearAbstractCutterDesign"

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def cylindrical_gear_form_grinding_wheel(
        self: "CastSelf",
    ) -> "_730.CylindricalGearFormGrindingWheel":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _730

        return self.__parent__._cast(_730.CylindricalGearFormGrindingWheel)

    @property
    def cylindrical_gear_grinding_worm(
        self: "CastSelf",
    ) -> "_731.CylindricalGearGrindingWorm":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _731

        return self.__parent__._cast(_731.CylindricalGearGrindingWorm)

    @property
    def cylindrical_gear_hob_design(
        self: "CastSelf",
    ) -> "_732.CylindricalGearHobDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _732

        return self.__parent__._cast(_732.CylindricalGearHobDesign)

    @property
    def cylindrical_gear_plunge_shaver(
        self: "CastSelf",
    ) -> "_733.CylindricalGearPlungeShaver":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _733

        return self.__parent__._cast(_733.CylindricalGearPlungeShaver)

    @property
    def cylindrical_gear_rack_design(
        self: "CastSelf",
    ) -> "_735.CylindricalGearRackDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _735

        return self.__parent__._cast(_735.CylindricalGearRackDesign)

    @property
    def cylindrical_gear_real_cutter_design(
        self: "CastSelf",
    ) -> "_736.CylindricalGearRealCutterDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _736

        return self.__parent__._cast(_736.CylindricalGearRealCutterDesign)

    @property
    def cylindrical_gear_shaper(self: "CastSelf") -> "_737.CylindricalGearShaper":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _737

        return self.__parent__._cast(_737.CylindricalGearShaper)

    @property
    def cylindrical_gear_shaver(self: "CastSelf") -> "_738.CylindricalGearShaver":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _738

        return self.__parent__._cast(_738.CylindricalGearShaver)

    @property
    def involute_cutter_design(self: "CastSelf") -> "_741.InvoluteCutterDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _741

        return self.__parent__._cast(_741.InvoluteCutterDesign)

    @property
    def cylindrical_gear_abstract_cutter_design(
        self: "CastSelf",
    ) -> "CylindricalGearAbstractCutterDesign":
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
class CylindricalGearAbstractCutterDesign(_1879.NamedDatabaseItem):
    """CylindricalGearAbstractCutterDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_ABSTRACT_CUTTER_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cutter_type(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterType

        if temp is None:
            return ""

        return temp

    @property
    def edge_radius(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @edge_radius.setter
    @enforce_parameter_types
    def edge_radius(self: "Self", value: "float") -> None:
        self.wrapped.EdgeRadius = float(value) if value is not None else 0.0

    @property
    def nominal_normal_pressure_angle(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NominalNormalPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @nominal_normal_pressure_angle.setter
    @enforce_parameter_types
    def nominal_normal_pressure_angle(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NominalNormalPressureAngle = value

    @property
    def normal_module(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @normal_module.setter
    @enforce_parameter_types
    def normal_module(self: "Self", value: "float") -> None:
        self.wrapped.NormalModule = float(value) if value is not None else 0.0

    @property
    def normal_pressure_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    @enforce_parameter_types
    def normal_pressure_angle(self: "Self", value: "float") -> None:
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearAbstractCutterDesign":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearAbstractCutterDesign
        """
        return _Cast_CylindricalGearAbstractCutterDesign(self)
