"""ISOCylindricalGearMaterial"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import list_with_selected_item, overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.gears.materials import _604
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ISO_CYLINDRICAL_GEAR_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "ISOCylindricalGearMaterial"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.materials import _289, _280
    from mastapy._private.gears.materials import _608
    from mastapy._private.utility.databases import _1879

    Self = TypeVar("Self", bound="ISOCylindricalGearMaterial")
    CastSelf = TypeVar(
        "CastSelf", bound="ISOCylindricalGearMaterial._Cast_ISOCylindricalGearMaterial"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISOCylindricalGearMaterial",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ISOCylindricalGearMaterial:
    """Special nested class for casting ISOCylindricalGearMaterial to subclasses."""

    __parent__: "ISOCylindricalGearMaterial"

    @property
    def cylindrical_gear_material(self: "CastSelf") -> "_604.CylindricalGearMaterial":
        return self.__parent__._cast(_604.CylindricalGearMaterial)

    @property
    def gear_material(self: "CastSelf") -> "_608.GearMaterial":
        from mastapy._private.gears.materials import _608

        return self.__parent__._cast(_608.GearMaterial)

    @property
    def material(self: "CastSelf") -> "_280.Material":
        from mastapy._private.materials import _280

        return self.__parent__._cast(_280.Material)

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        from mastapy._private.utility.databases import _1879

        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def iso_cylindrical_gear_material(self: "CastSelf") -> "ISOCylindricalGearMaterial":
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
class ISOCylindricalGearMaterial(_604.CylindricalGearMaterial):
    """ISOCylindricalGearMaterial

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ISO_CYLINDRICAL_GEAR_MATERIAL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def limited_pitting_allowed(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.LimitedPittingAllowed

        if temp is None:
            return False

        return temp

    @limited_pitting_allowed.setter
    @enforce_parameter_types
    def limited_pitting_allowed(self: "Self", value: "bool") -> None:
        self.wrapped.LimitedPittingAllowed = bool(value) if value is not None else False

    @property
    def long_life_life_factor_bending(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LongLifeLifeFactorBending

        if temp is None:
            return 0.0

        return temp

    @long_life_life_factor_bending.setter
    @enforce_parameter_types
    def long_life_life_factor_bending(self: "Self", value: "float") -> None:
        self.wrapped.LongLifeLifeFactorBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def long_life_life_factor_contact(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LongLifeLifeFactorContact

        if temp is None:
            return 0.0

        return temp

    @long_life_life_factor_contact.setter
    @enforce_parameter_types
    def long_life_life_factor_contact(self: "Self", value: "float") -> None:
        self.wrapped.LongLifeLifeFactorContact = (
            float(value) if value is not None else 0.0
        )

    @property
    def material_has_a_well_defined_yield_point(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.MaterialHasAWellDefinedYieldPoint

        if temp is None:
            return False

        return temp

    @material_has_a_well_defined_yield_point.setter
    @enforce_parameter_types
    def material_has_a_well_defined_yield_point(self: "Self", value: "bool") -> None:
        self.wrapped.MaterialHasAWellDefinedYieldPoint = (
            bool(value) if value is not None else False
        )

    @property
    def material_type(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.MaterialType

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @material_type.setter
    @enforce_parameter_types
    def material_type(self: "Self", value: "str") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.MaterialType = value

    @property
    def n0_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.N0Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def n0_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.N0Contact

        if temp is None:
            return 0.0

        return temp

    @property
    def proof_stress(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ProofStress

        if temp is None:
            return 0.0

        return temp

    @proof_stress.setter
    @enforce_parameter_types
    def proof_stress(self: "Self", value: "float") -> None:
        self.wrapped.ProofStress = float(value) if value is not None else 0.0

    @property
    def quality_grade(self: "Self") -> "_289.QualityGrade":
        """mastapy._private.materials.QualityGrade"""
        temp = self.wrapped.QualityGrade

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Materials.QualityGrade")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._289", "QualityGrade"
        )(value)

    @quality_grade.setter
    @enforce_parameter_types
    def quality_grade(self: "Self", value: "_289.QualityGrade") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Materials.QualityGrade")
        self.wrapped.QualityGrade = value

    @property
    def shot_peening_bending_stress_benefit(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ShotPeeningBendingStressBenefit

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @shot_peening_bending_stress_benefit.setter
    @enforce_parameter_types
    def shot_peening_bending_stress_benefit(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ShotPeeningBendingStressBenefit = value

    @property
    def use_custom_material_for_bending(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseCustomMaterialForBending

        if temp is None:
            return False

        return temp

    @use_custom_material_for_bending.setter
    @enforce_parameter_types
    def use_custom_material_for_bending(self: "Self", value: "bool") -> None:
        self.wrapped.UseCustomMaterialForBending = (
            bool(value) if value is not None else False
        )

    @property
    def use_custom_material_for_contact(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseCustomMaterialForContact

        if temp is None:
            return False

        return temp

    @use_custom_material_for_contact.setter
    @enforce_parameter_types
    def use_custom_material_for_contact(self: "Self", value: "bool") -> None:
        self.wrapped.UseCustomMaterialForContact = (
            bool(value) if value is not None else False
        )

    @property
    def use_iso633652003_material_definitions(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseISO633652003MaterialDefinitions

        if temp is None:
            return False

        return temp

    @use_iso633652003_material_definitions.setter
    @enforce_parameter_types
    def use_iso633652003_material_definitions(self: "Self", value: "bool") -> None:
        self.wrapped.UseISO633652003MaterialDefinitions = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: "Self") -> "_Cast_ISOCylindricalGearMaterial":
        """Cast to another type.

        Returns:
            _Cast_ISOCylindricalGearMaterial
        """
        return _Cast_ISOCylindricalGearMaterial(self)
