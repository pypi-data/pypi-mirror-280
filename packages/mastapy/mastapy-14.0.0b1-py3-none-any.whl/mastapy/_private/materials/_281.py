"""MaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.utility.databases import _1878
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_MATERIAL_DATABASE = python_net_import("SMT.MastaAPI.Materials", "MaterialDatabase")

if TYPE_CHECKING:
    from typing import Any, Type

    from mastapy._private.materials import _280
    from mastapy._private.shafts import _25
    from mastapy._private.gears.materials import _596, _598, _602, _603, _605, _606
    from mastapy._private.electric_machines import _1329, _1347, _1360
    from mastapy._private.cycloidal import _1503, _1510
    from mastapy._private.utility.databases import _1881, _1874

    Self = TypeVar("Self", bound="MaterialDatabase")
    CastSelf = TypeVar("CastSelf", bound="MaterialDatabase._Cast_MaterialDatabase")

T = TypeVar("T", bound="_280.Material")

__docformat__ = "restructuredtext en"
__all__ = ("MaterialDatabase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MaterialDatabase:
    """Special nested class for casting MaterialDatabase to subclasses."""

    __parent__: "MaterialDatabase"

    @property
    def named_database(self: "CastSelf") -> "_1878.NamedDatabase":
        return self.__parent__._cast(_1878.NamedDatabase)

    @property
    def sql_database(self: "CastSelf") -> "_1881.SQLDatabase":
        pass

        from mastapy._private.utility.databases import _1881

        return self.__parent__._cast(_1881.SQLDatabase)

    @property
    def database(self: "CastSelf") -> "_1874.Database":
        pass

        from mastapy._private.utility.databases import _1874

        return self.__parent__._cast(_1874.Database)

    @property
    def shaft_material_database(self: "CastSelf") -> "_25.ShaftMaterialDatabase":
        from mastapy._private.shafts import _25

        return self.__parent__._cast(_25.ShaftMaterialDatabase)

    @property
    def bevel_gear_abstract_material_database(
        self: "CastSelf",
    ) -> "_596.BevelGearAbstractMaterialDatabase":
        from mastapy._private.gears.materials import _596

        return self.__parent__._cast(_596.BevelGearAbstractMaterialDatabase)

    @property
    def bevel_gear_iso_material_database(
        self: "CastSelf",
    ) -> "_598.BevelGearISOMaterialDatabase":
        from mastapy._private.gears.materials import _598

        return self.__parent__._cast(_598.BevelGearISOMaterialDatabase)

    @property
    def cylindrical_gear_agma_material_database(
        self: "CastSelf",
    ) -> "_602.CylindricalGearAGMAMaterialDatabase":
        from mastapy._private.gears.materials import _602

        return self.__parent__._cast(_602.CylindricalGearAGMAMaterialDatabase)

    @property
    def cylindrical_gear_iso_material_database(
        self: "CastSelf",
    ) -> "_603.CylindricalGearISOMaterialDatabase":
        from mastapy._private.gears.materials import _603

        return self.__parent__._cast(_603.CylindricalGearISOMaterialDatabase)

    @property
    def cylindrical_gear_material_database(
        self: "CastSelf",
    ) -> "_605.CylindricalGearMaterialDatabase":
        from mastapy._private.gears.materials import _605

        return self.__parent__._cast(_605.CylindricalGearMaterialDatabase)

    @property
    def cylindrical_gear_plastic_material_database(
        self: "CastSelf",
    ) -> "_606.CylindricalGearPlasticMaterialDatabase":
        from mastapy._private.gears.materials import _606

        return self.__parent__._cast(_606.CylindricalGearPlasticMaterialDatabase)

    @property
    def magnet_material_database(self: "CastSelf") -> "_1329.MagnetMaterialDatabase":
        from mastapy._private.electric_machines import _1329

        return self.__parent__._cast(_1329.MagnetMaterialDatabase)

    @property
    def stator_rotor_material_database(
        self: "CastSelf",
    ) -> "_1347.StatorRotorMaterialDatabase":
        from mastapy._private.electric_machines import _1347

        return self.__parent__._cast(_1347.StatorRotorMaterialDatabase)

    @property
    def winding_material_database(self: "CastSelf") -> "_1360.WindingMaterialDatabase":
        from mastapy._private.electric_machines import _1360

        return self.__parent__._cast(_1360.WindingMaterialDatabase)

    @property
    def cycloidal_disc_material_database(
        self: "CastSelf",
    ) -> "_1503.CycloidalDiscMaterialDatabase":
        from mastapy._private.cycloidal import _1503

        return self.__parent__._cast(_1503.CycloidalDiscMaterialDatabase)

    @property
    def ring_pins_material_database(
        self: "CastSelf",
    ) -> "_1510.RingPinsMaterialDatabase":
        from mastapy._private.cycloidal import _1510

        return self.__parent__._cast(_1510.RingPinsMaterialDatabase)

    @property
    def material_database(self: "CastSelf") -> "MaterialDatabase":
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
class MaterialDatabase(_1878.NamedDatabase[T]):
    """MaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _MATERIAL_DATABASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_MaterialDatabase":
        """Cast to another type.

        Returns:
            _Cast_MaterialDatabase
        """
        return _Cast_MaterialDatabase(self)
