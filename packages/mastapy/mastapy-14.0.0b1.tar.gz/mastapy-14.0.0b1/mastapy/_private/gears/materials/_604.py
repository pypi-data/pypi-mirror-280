"""CylindricalGearMaterial"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import list_with_selected_item, overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.gears.materials import _608
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearMaterial"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.gears.materials import _622, _594, _616, _625
    from mastapy._private.materials import _280
    from mastapy._private.utility.databases import _1879

    Self = TypeVar("Self", bound="CylindricalGearMaterial")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalGearMaterial._Cast_CylindricalGearMaterial"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMaterial",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearMaterial:
    """Special nested class for casting CylindricalGearMaterial to subclasses."""

    __parent__: "CylindricalGearMaterial"

    @property
    def gear_material(self: "CastSelf") -> "_608.GearMaterial":
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
    def agma_cylindrical_gear_material(
        self: "CastSelf",
    ) -> "_594.AGMACylindricalGearMaterial":
        from mastapy._private.gears.materials import _594

        return self.__parent__._cast(_594.AGMACylindricalGearMaterial)

    @property
    def iso_cylindrical_gear_material(
        self: "CastSelf",
    ) -> "_616.ISOCylindricalGearMaterial":
        from mastapy._private.gears.materials import _616

        return self.__parent__._cast(_616.ISOCylindricalGearMaterial)

    @property
    def plastic_cylindrical_gear_material(
        self: "CastSelf",
    ) -> "_625.PlasticCylindricalGearMaterial":
        from mastapy._private.gears.materials import _625

        return self.__parent__._cast(_625.PlasticCylindricalGearMaterial)

    @property
    def cylindrical_gear_material(self: "CastSelf") -> "CylindricalGearMaterial":
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
class CylindricalGearMaterial(_608.GearMaterial):
    """CylindricalGearMaterial

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_MATERIAL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def allowable_stress_number_bending(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @allowable_stress_number_bending.setter
    @enforce_parameter_types
    def allowable_stress_number_bending(self: "Self", value: "float") -> None:
        self.wrapped.AllowableStressNumberBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def allowable_stress_number_contact(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AllowableStressNumberContact

        if temp is None:
            return 0.0

        return temp

    @allowable_stress_number_contact.setter
    @enforce_parameter_types
    def allowable_stress_number_contact(self: "Self", value: "float") -> None:
        self.wrapped.AllowableStressNumberContact = (
            float(value) if value is not None else 0.0
        )

    @property
    def heat_treatment_distortion_control(self: "Self") -> "_622.ManufactureRating":
        """mastapy._private.gears.materials.ManufactureRating"""
        temp = self.wrapped.HeatTreatmentDistortionControl

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.materials._622", "ManufactureRating"
        )(value)

    @heat_treatment_distortion_control.setter
    @enforce_parameter_types
    def heat_treatment_distortion_control(
        self: "Self", value: "_622.ManufactureRating"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )
        self.wrapped.HeatTreatmentDistortionControl = value

    @property
    def heat_treatment_process_development(self: "Self") -> "_622.ManufactureRating":
        """mastapy._private.gears.materials.ManufactureRating"""
        temp = self.wrapped.HeatTreatmentProcessDevelopment

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.materials._622", "ManufactureRating"
        )(value)

    @heat_treatment_process_development.setter
    @enforce_parameter_types
    def heat_treatment_process_development(
        self: "Self", value: "_622.ManufactureRating"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )
        self.wrapped.HeatTreatmentProcessDevelopment = value

    @property
    def machine_process_development(self: "Self") -> "_622.ManufactureRating":
        """mastapy._private.gears.materials.ManufactureRating"""
        temp = self.wrapped.MachineProcessDevelopment

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.materials._622", "ManufactureRating"
        )(value)

    @machine_process_development.setter
    @enforce_parameter_types
    def machine_process_development(
        self: "Self", value: "_622.ManufactureRating"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )
        self.wrapped.MachineProcessDevelopment = value

    @property
    def manufacturability(self: "Self") -> "_622.ManufactureRating":
        """mastapy._private.gears.materials.ManufactureRating"""
        temp = self.wrapped.Manufacturability

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.materials._622", "ManufactureRating"
        )(value)

    @manufacturability.setter
    @enforce_parameter_types
    def manufacturability(self: "Self", value: "_622.ManufactureRating") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )
        self.wrapped.Manufacturability = value

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
    def nominal_stress_number_bending(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NominalStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @nominal_stress_number_bending.setter
    @enforce_parameter_types
    def nominal_stress_number_bending(self: "Self", value: "float") -> None:
        self.wrapped.NominalStressNumberBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def retained_austenite(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RetainedAustenite

        if temp is None:
            return 0.0

        return temp

    @retained_austenite.setter
    @enforce_parameter_types
    def retained_austenite(self: "Self", value: "float") -> None:
        self.wrapped.RetainedAustenite = float(value) if value is not None else 0.0

    @property
    def sn_curve_bending_allowable_stress_point_selector(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.SNCurveBendingAllowableStressPointSelector

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @sn_curve_bending_allowable_stress_point_selector.setter
    @enforce_parameter_types
    def sn_curve_bending_allowable_stress_point_selector(
        self: "Self", value: "str"
    ) -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.SNCurveBendingAllowableStressPointSelector = value

    @property
    def sn_curve_contact_allowable_stress_point_selector(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.SNCurveContactAllowableStressPointSelector

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @sn_curve_contact_allowable_stress_point_selector.setter
    @enforce_parameter_types
    def sn_curve_contact_allowable_stress_point_selector(
        self: "Self", value: "str"
    ) -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.SNCurveContactAllowableStressPointSelector = value

    @property
    def shot_peened(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ShotPeened

        if temp is None:
            return False

        return temp

    @shot_peened.setter
    @enforce_parameter_types
    def shot_peened(self: "Self", value: "bool") -> None:
        self.wrapped.ShotPeened = bool(value) if value is not None else False

    @property
    def specify_allowable_stress_number_bending(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyAllowableStressNumberBending

        if temp is None:
            return False

        return temp

    @specify_allowable_stress_number_bending.setter
    @enforce_parameter_types
    def specify_allowable_stress_number_bending(self: "Self", value: "bool") -> None:
        self.wrapped.SpecifyAllowableStressNumberBending = (
            bool(value) if value is not None else False
        )

    @property
    def specify_allowable_stress_number_contact(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyAllowableStressNumberContact

        if temp is None:
            return False

        return temp

    @specify_allowable_stress_number_contact.setter
    @enforce_parameter_types
    def specify_allowable_stress_number_contact(self: "Self", value: "bool") -> None:
        self.wrapped.SpecifyAllowableStressNumberContact = (
            bool(value) if value is not None else False
        )

    @property
    def welding_structural_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WeldingStructuralFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @welding_structural_factor.setter
    @enforce_parameter_types
    def welding_structural_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WeldingStructuralFactor = value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearMaterial":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearMaterial
        """
        return _Cast_CylindricalGearMaterial(self)
