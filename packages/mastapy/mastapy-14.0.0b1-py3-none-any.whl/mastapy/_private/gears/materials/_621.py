"""KlingelnbergCycloPalloidConicalGearMaterial"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.gears.materials import _608
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "KlingelnbergCycloPalloidConicalGearMaterial"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.materials import _280
    from mastapy._private.utility.databases import _1879

    Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMaterial")
    CastSelf = TypeVar(
        "CastSelf",
        bound="KlingelnbergCycloPalloidConicalGearMaterial._Cast_KlingelnbergCycloPalloidConicalGearMaterial",
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMaterial",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_KlingelnbergCycloPalloidConicalGearMaterial:
    """Special nested class for casting KlingelnbergCycloPalloidConicalGearMaterial to subclasses."""

    __parent__: "KlingelnbergCycloPalloidConicalGearMaterial"

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
    def klingelnberg_cyclo_palloid_conical_gear_material(
        self: "CastSelf",
    ) -> "KlingelnbergCycloPalloidConicalGearMaterial":
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
class KlingelnbergCycloPalloidConicalGearMaterial(_608.GearMaterial):
    """KlingelnbergCycloPalloidConicalGearMaterial

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MATERIAL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def specify_allowable_stress_numbers(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyAllowableStressNumbers

        if temp is None:
            return False

        return temp

    @specify_allowable_stress_numbers.setter
    @enforce_parameter_types
    def specify_allowable_stress_numbers(self: "Self", value: "bool") -> None:
        self.wrapped.SpecifyAllowableStressNumbers = (
            bool(value) if value is not None else False
        )

    @property
    def stress_number_bending(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StressNumberBending

        if temp is None:
            return 0.0

        return temp

    @stress_number_bending.setter
    @enforce_parameter_types
    def stress_number_bending(self: "Self", value: "float") -> None:
        self.wrapped.StressNumberBending = float(value) if value is not None else 0.0

    @property
    def stress_number_contact(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StressNumberContact

        if temp is None:
            return 0.0

        return temp

    @stress_number_contact.setter
    @enforce_parameter_types
    def stress_number_contact(self: "Self", value: "float") -> None:
        self.wrapped.StressNumberContact = float(value) if value is not None else 0.0

    @property
    def stress_number_static_bending(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StressNumberStaticBending

        if temp is None:
            return 0.0

        return temp

    @stress_number_static_bending.setter
    @enforce_parameter_types
    def stress_number_static_bending(self: "Self", value: "float") -> None:
        self.wrapped.StressNumberStaticBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def stress_number_static_contact(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StressNumberStaticContact

        if temp is None:
            return 0.0

        return temp

    @stress_number_static_contact.setter
    @enforce_parameter_types
    def stress_number_static_contact(self: "Self", value: "float") -> None:
        self.wrapped.StressNumberStaticContact = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: "Self") -> "_Cast_KlingelnbergCycloPalloidConicalGearMaterial":
        """Cast to another type.

        Returns:
            _Cast_KlingelnbergCycloPalloidConicalGearMaterial
        """
        return _Cast_KlingelnbergCycloPalloidConicalGearMaterial(self)
