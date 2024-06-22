"""CylindricalWormGrinderDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.manufacturing.cylindrical import _633
from mastapy._private.gears.manufacturing.cylindrical.cutters import _731
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_CYLINDRICAL_WORM_GRINDER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalWormGrinderDatabase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.databases import _1878, _1881, _1874

    Self = TypeVar("Self", bound="CylindricalWormGrinderDatabase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalWormGrinderDatabase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalWormGrinderDatabase:
    """Special nested class for casting CylindricalWormGrinderDatabase to subclasses."""

    __parent__: "CylindricalWormGrinderDatabase"

    @property
    def cylindrical_cutter_database(
        self: "CastSelf",
    ) -> "_633.CylindricalCutterDatabase":
        return self.__parent__._cast(_633.CylindricalCutterDatabase)

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
    def cylindrical_worm_grinder_database(
        self: "CastSelf",
    ) -> "CylindricalWormGrinderDatabase":
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
class CylindricalWormGrinderDatabase(
    _633.CylindricalCutterDatabase[_731.CylindricalGearGrindingWorm]
):
    """CylindricalWormGrinderDatabase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_WORM_GRINDER_DATABASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalWormGrinderDatabase":
        """Cast to another type.

        Returns:
            _Cast_CylindricalWormGrinderDatabase
        """
        return _Cast_CylindricalWormGrinderDatabase(self)
