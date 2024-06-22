"""CylindricalGearShaper"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.gears.manufacturing.cylindrical.cutters import _741
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAPER = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "CylindricalGearShaper"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.gears.gear_designs.cylindrical import _1106
    from mastapy._private.gears.manufacturing.cylindrical.cutters import _736, _729
    from mastapy._private.utility.databases import _1879

    Self = TypeVar("Self", bound="CylindricalGearShaper")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalGearShaper._Cast_CylindricalGearShaper"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearShaper",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearShaper:
    """Special nested class for casting CylindricalGearShaper to subclasses."""

    __parent__: "CylindricalGearShaper"

    @property
    def involute_cutter_design(self: "CastSelf") -> "_741.InvoluteCutterDesign":
        return self.__parent__._cast(_741.InvoluteCutterDesign)

    @property
    def cylindrical_gear_real_cutter_design(
        self: "CastSelf",
    ) -> "_736.CylindricalGearRealCutterDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _736

        return self.__parent__._cast(_736.CylindricalGearRealCutterDesign)

    @property
    def cylindrical_gear_abstract_cutter_design(
        self: "CastSelf",
    ) -> "_729.CylindricalGearAbstractCutterDesign":
        from mastapy._private.gears.manufacturing.cylindrical.cutters import _729

        return self.__parent__._cast(_729.CylindricalGearAbstractCutterDesign)

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        from mastapy._private.utility.databases import _1879

        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def cylindrical_gear_shaper(self: "CastSelf") -> "CylindricalGearShaper":
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
class CylindricalGearShaper(_741.InvoluteCutterDesign):
    """CylindricalGearShaper

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SHAPER

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def actual_protuberance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualProtuberance

        if temp is None:
            return 0.0

        return temp

    @property
    def blade_control_distance(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BladeControlDistance

        if temp is None:
            return 0.0

        return temp

    @blade_control_distance.setter
    @enforce_parameter_types
    def blade_control_distance(self: "Self", value: "float") -> None:
        self.wrapped.BladeControlDistance = float(value) if value is not None else 0.0

    @property
    def circle_blade_flank_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.CircleBladeFlankAngle

        if temp is None:
            return 0.0

        return temp

    @circle_blade_flank_angle.setter
    @enforce_parameter_types
    def circle_blade_flank_angle(self: "Self", value: "float") -> None:
        self.wrapped.CircleBladeFlankAngle = float(value) if value is not None else 0.0

    @property
    def circle_blade_rake_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.CircleBladeRakeAngle

        if temp is None:
            return 0.0

        return temp

    @circle_blade_rake_angle.setter
    @enforce_parameter_types
    def circle_blade_rake_angle(self: "Self", value: "float") -> None:
        self.wrapped.CircleBladeRakeAngle = float(value) if value is not None else 0.0

    @property
    def diametral_height_at_semi_topping_thickness_measurement(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.DiametralHeightAtSemiToppingThicknessMeasurement

        if temp is None:
            return 0.0

        return temp

    @diametral_height_at_semi_topping_thickness_measurement.setter
    @enforce_parameter_types
    def diametral_height_at_semi_topping_thickness_measurement(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.DiametralHeightAtSemiToppingThicknessMeasurement = (
            float(value) if value is not None else 0.0
        )

    @property
    def edge_height(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EdgeHeight

        if temp is None:
            return 0.0

        return temp

    @edge_height.setter
    @enforce_parameter_types
    def edge_height(self: "Self", value: "float") -> None:
        self.wrapped.EdgeHeight = float(value) if value is not None else 0.0

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
    def has_protuberance(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.HasProtuberance

        if temp is None:
            return False

        return temp

    @has_protuberance.setter
    @enforce_parameter_types
    def has_protuberance(self: "Self", value: "bool") -> None:
        self.wrapped.HasProtuberance = bool(value) if value is not None else False

    @property
    def has_semi_topping_blade(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.HasSemiToppingBlade

        if temp is None:
            return False

        return temp

    @has_semi_topping_blade.setter
    @enforce_parameter_types
    def has_semi_topping_blade(self: "Self", value: "bool") -> None:
        self.wrapped.HasSemiToppingBlade = bool(value) if value is not None else False

    @property
    def nominal_addendum(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NominalAddendum

        if temp is None:
            return 0.0

        return temp

    @nominal_addendum.setter
    @enforce_parameter_types
    def nominal_addendum(self: "Self", value: "float") -> None:
        self.wrapped.NominalAddendum = float(value) if value is not None else 0.0

    @property
    def nominal_addendum_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NominalAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @nominal_addendum_factor.setter
    @enforce_parameter_types
    def nominal_addendum_factor(self: "Self", value: "float") -> None:
        self.wrapped.NominalAddendumFactor = float(value) if value is not None else 0.0

    @property
    def nominal_dedendum(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NominalDedendum

        if temp is None:
            return 0.0

        return temp

    @nominal_dedendum.setter
    @enforce_parameter_types
    def nominal_dedendum(self: "Self", value: "float") -> None:
        self.wrapped.NominalDedendum = float(value) if value is not None else 0.0

    @property
    def nominal_dedendum_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NominalDedendumFactor

        if temp is None:
            return 0.0

        return temp

    @nominal_dedendum_factor.setter
    @enforce_parameter_types
    def nominal_dedendum_factor(self: "Self", value: "float") -> None:
        self.wrapped.NominalDedendumFactor = float(value) if value is not None else 0.0

    @property
    def nominal_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NominalDiameter

        if temp is None:
            return 0.0

        return temp

    @nominal_diameter.setter
    @enforce_parameter_types
    def nominal_diameter(self: "Self", value: "float") -> None:
        self.wrapped.NominalDiameter = float(value) if value is not None else 0.0

    @property
    def normal_thickness_at_specified_diameter_for_semi_topping(
        self: "Self",
    ) -> "float":
        """float"""
        temp = self.wrapped.NormalThicknessAtSpecifiedDiameterForSemiTopping

        if temp is None:
            return 0.0

        return temp

    @normal_thickness_at_specified_diameter_for_semi_topping.setter
    @enforce_parameter_types
    def normal_thickness_at_specified_diameter_for_semi_topping(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.NormalThicknessAtSpecifiedDiameterForSemiTopping = (
            float(value) if value is not None else 0.0
        )

    @property
    def protuberance(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Protuberance

        if temp is None:
            return 0.0

        return temp

    @protuberance.setter
    @enforce_parameter_types
    def protuberance(self: "Self", value: "float") -> None:
        self.wrapped.Protuberance = float(value) if value is not None else 0.0

    @property
    def protuberance_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceAngle

        if temp is None:
            return 0.0

        return temp

    @protuberance_angle.setter
    @enforce_parameter_types
    def protuberance_angle(self: "Self", value: "float") -> None:
        self.wrapped.ProtuberanceAngle = float(value) if value is not None else 0.0

    @property
    def protuberance_height(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceHeight

        if temp is None:
            return 0.0

        return temp

    @protuberance_height.setter
    @enforce_parameter_types
    def protuberance_height(self: "Self", value: "float") -> None:
        self.wrapped.ProtuberanceHeight = float(value) if value is not None else 0.0

    @property
    def radius_to_centre_s_of_tool_tip_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusToCentreSOfToolTipRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def root_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @root_diameter.setter
    @enforce_parameter_types
    def root_diameter(self: "Self", value: "float") -> None:
        self.wrapped.RootDiameter = float(value) if value is not None else 0.0

    @property
    def root_form_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def semi_topping_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SemiToppingAngle

        if temp is None:
            return 0.0

        return temp

    @semi_topping_angle.setter
    @enforce_parameter_types
    def semi_topping_angle(self: "Self", value: "float") -> None:
        self.wrapped.SemiToppingAngle = float(value) if value is not None else 0.0

    @property
    def semi_topping_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SemiToppingDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @semi_topping_diameter.setter
    @enforce_parameter_types
    def semi_topping_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SemiToppingDiameter = value

    @property
    def semi_topping_pressure_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SemiToppingPressureAngle

        if temp is None:
            return 0.0

        return temp

    @semi_topping_pressure_angle.setter
    @enforce_parameter_types
    def semi_topping_pressure_angle(self: "Self", value: "float") -> None:
        self.wrapped.SemiToppingPressureAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def shaper_edge_type(self: "Self") -> "_1106.ShaperEdgeTypes":
        """mastapy._private.gears.gear_designs.cylindrical.ShaperEdgeTypes"""
        temp = self.wrapped.ShaperEdgeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ShaperEdgeTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1106", "ShaperEdgeTypes"
        )(value)

    @shaper_edge_type.setter
    @enforce_parameter_types
    def shaper_edge_type(self: "Self", value: "_1106.ShaperEdgeTypes") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ShaperEdgeTypes"
        )
        self.wrapped.ShaperEdgeType = value

    @property
    def tip_control_distance(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TipControlDistance

        if temp is None:
            return 0.0

        return temp

    @tip_control_distance.setter
    @enforce_parameter_types
    def tip_control_distance(self: "Self", value: "float") -> None:
        self.wrapped.TipControlDistance = float(value) if value is not None else 0.0

    @property
    def tip_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @tip_diameter.setter
    @enforce_parameter_types
    def tip_diameter(self: "Self", value: "float") -> None:
        self.wrapped.TipDiameter = float(value) if value is not None else 0.0

    @property
    def tip_thickness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TipThickness

        if temp is None:
            return 0.0

        return temp

    @tip_thickness.setter
    @enforce_parameter_types
    def tip_thickness(self: "Self", value: "float") -> None:
        self.wrapped.TipThickness = float(value) if value is not None else 0.0

    @property
    def use_maximum_edge_radius(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseMaximumEdgeRadius

        if temp is None:
            return False

        return temp

    @use_maximum_edge_radius.setter
    @enforce_parameter_types
    def use_maximum_edge_radius(self: "Self", value: "bool") -> None:
        self.wrapped.UseMaximumEdgeRadius = bool(value) if value is not None else False

    @property
    def virtual_tooth_number(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualToothNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def whole_depth(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearShaper":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearShaper
        """
        return _Cast_CylindricalGearShaper(self)
