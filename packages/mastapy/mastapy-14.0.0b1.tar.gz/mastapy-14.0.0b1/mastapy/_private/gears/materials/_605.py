"""CylindricalGearMaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.materials import _281
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_CYLINDRICAL_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearMaterialDatabase"
)

if TYPE_CHECKING:
    from typing import Any, Type

    from mastapy._private.gears.materials import _604, _602, _603, _606
    from mastapy._private.utility.databases import _1878, _1881, _1874

    Self = TypeVar("Self", bound="CylindricalGearMaterialDatabase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
    )

T = TypeVar("T", bound="_604.CylindricalGearMaterial")

__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMaterialDatabase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearMaterialDatabase:
    """Special nested class for casting CylindricalGearMaterialDatabase to subclasses."""

    __parent__: "CylindricalGearMaterialDatabase"

    @property
    def material_database(self: "CastSelf") -> "_281.MaterialDatabase":
        return self.__parent__._cast(_281.MaterialDatabase)

    @property
    def named_database(self: "CastSelf") -> "_1878.NamedDatabase":
        from mastapy._private.utility.databases import _1878

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
    def cylindrical_gear_plastic_material_database(
        self: "CastSelf",
    ) -> "_606.CylindricalGearPlasticMaterialDatabase":
        from mastapy._private.gears.materials import _606

        return self.__parent__._cast(_606.CylindricalGearPlasticMaterialDatabase)

    @property
    def cylindrical_gear_material_database(
        self: "CastSelf",
    ) -> "CylindricalGearMaterialDatabase":
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
class CylindricalGearMaterialDatabase(_281.MaterialDatabase[T]):
    """CylindricalGearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_MATERIAL_DATABASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearMaterialDatabase":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearMaterialDatabase
        """
        return _Cast_CylindricalGearMaterialDatabase(self)
