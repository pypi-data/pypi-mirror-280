"""CylindricalGearRackDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.gears.manufacturing.cylindrical.cutters import _736
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_RACK_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "CylindricalGearRackDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.gears import _343, _361
    from mastapy._private.gears.manufacturing.cylindrical.cutters.tangibles import _753
    from mastapy._private.gears.manufacturing.cylindrical.cutters import (
        _731,
        _732,
        _729,
    )
    from mastapy._private.utility.databases import _1879

    Self = TypeVar("Self", bound="CylindricalGearRackDesign")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalGearRackDesign._Cast_CylindricalGearRackDesign"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearRackDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearRackDesign:
    """Special nested class for casting CylindricalGearRackDesign to subclasses."""

    __parent__: "CylindricalGearRackDesign"

    @property
    def cylindrical_gear_real_cutter_design(
        self: "CastSelf",
    ) -> "_736.CylindricalGearRealCutterDesign":
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
    def cylindrical_gear_rack_design(self: "CastSelf") -> "CylindricalGearRackDesign":
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
class CylindricalGearRackDesign(_736.CylindricalGearRealCutterDesign):
    """CylindricalGearRackDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_RACK_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def addendum(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @addendum.setter
    @enforce_parameter_types
    def addendum(self: "Self", value: "float") -> None:
        self.wrapped.Addendum = float(value) if value is not None else 0.0

    @property
    def addendum_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AddendumFactor

        if temp is None:
            return 0.0

        return temp

    @addendum_factor.setter
    @enforce_parameter_types
    def addendum_factor(self: "Self", value: "float") -> None:
        self.wrapped.AddendumFactor = float(value) if value is not None else 0.0

    @property
    def addendum_keeping_dedendum_constant(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AddendumKeepingDedendumConstant

        if temp is None:
            return 0.0

        return temp

    @addendum_keeping_dedendum_constant.setter
    @enforce_parameter_types
    def addendum_keeping_dedendum_constant(self: "Self", value: "float") -> None:
        self.wrapped.AddendumKeepingDedendumConstant = (
            float(value) if value is not None else 0.0
        )

    @property
    def dedendum(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @dedendum.setter
    @enforce_parameter_types
    def dedendum(self: "Self", value: "float") -> None:
        self.wrapped.Dedendum = float(value) if value is not None else 0.0

    @property
    def dedendum_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.DedendumFactor

        if temp is None:
            return 0.0

        return temp

    @dedendum_factor.setter
    @enforce_parameter_types
    def dedendum_factor(self: "Self", value: "float") -> None:
        self.wrapped.DedendumFactor = float(value) if value is not None else 0.0

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
    def effective_length(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EffectiveLength

        if temp is None:
            return 0.0

        return temp

    @effective_length.setter
    @enforce_parameter_types
    def effective_length(self: "Self", value: "float") -> None:
        self.wrapped.EffectiveLength = float(value) if value is not None else 0.0

    @property
    def flat_root_width(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlatRootWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def flat_tip_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.FlatTipWidth

        if temp is None:
            return 0.0

        return temp

    @flat_tip_width.setter
    @enforce_parameter_types
    def flat_tip_width(self: "Self", value: "float") -> None:
        self.wrapped.FlatTipWidth = float(value) if value is not None else 0.0

    @property
    def hand(self: "Self") -> "_343.Hand":
        """mastapy._private.gears.Hand"""
        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy._private.gears._343", "Hand")(
            value
        )

    @hand.setter
    @enforce_parameter_types
    def hand(self: "Self", value: "_343.Hand") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.Hand = value

    @property
    def normal_thickness(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @normal_thickness.setter
    @enforce_parameter_types
    def normal_thickness(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NormalThickness = value

    @property
    def number_of_threads(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfThreads

        if temp is None:
            return 0

        return temp

    @number_of_threads.setter
    @enforce_parameter_types
    def number_of_threads(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfThreads = int(value) if value is not None else 0

    @property
    def reference_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

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
    def whole_depth(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @whole_depth.setter
    @enforce_parameter_types
    def whole_depth(self: "Self", value: "float") -> None:
        self.wrapped.WholeDepth = float(value) if value is not None else 0.0

    @property
    def worm_type(self: "Self") -> "_361.WormType":
        """mastapy._private.gears.WormType"""
        temp = self.wrapped.WormType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.WormType")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy._private.gears._361", "WormType")(
            value
        )

    @worm_type.setter
    @enforce_parameter_types
    def worm_type(self: "Self", value: "_361.WormType") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.WormType")
        self.wrapped.WormType = value

    @property
    def nominal_rack_shape(self: "Self") -> "_753.RackShape":
        """mastapy._private.gears.manufacturing.cylindrical.cutters.tangibles.RackShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalRackShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def convert_to_standard_thickness(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ConvertToStandardThickness()

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearRackDesign":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearRackDesign
        """
        return _Cast_CylindricalGearRackDesign(self)
