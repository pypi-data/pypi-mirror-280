"""KlingelnbergConicalGearMaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.materials import _609, _621
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "KlingelnbergConicalGearMaterialDatabase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.databases import _1878, _1881, _1874

    Self = TypeVar("Self", bound="KlingelnbergConicalGearMaterialDatabase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalGearMaterialDatabase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_KlingelnbergConicalGearMaterialDatabase:
    """Special nested class for casting KlingelnbergConicalGearMaterialDatabase to subclasses."""

    __parent__: "KlingelnbergConicalGearMaterialDatabase"

    @property
    def gear_material_database(self: "CastSelf") -> "_609.GearMaterialDatabase":
        return self.__parent__._cast(_609.GearMaterialDatabase)

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
    def klingelnberg_conical_gear_material_database(
        self: "CastSelf",
    ) -> "KlingelnbergConicalGearMaterialDatabase":
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
class KlingelnbergConicalGearMaterialDatabase(
    _609.GearMaterialDatabase[_621.KlingelnbergCycloPalloidConicalGearMaterial]
):
    """KlingelnbergConicalGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_KlingelnbergConicalGearMaterialDatabase":
        """Cast to another type.

        Returns:
            _Cast_KlingelnbergConicalGearMaterialDatabase
        """
        return _Cast_KlingelnbergConicalGearMaterialDatabase(self)
