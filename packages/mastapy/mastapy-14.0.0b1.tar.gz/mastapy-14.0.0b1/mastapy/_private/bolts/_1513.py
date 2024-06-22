"""BoltedJointMaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypeVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.utility.databases import _1878
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_BOLTED_JOINT_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Bolts", "BoltedJointMaterialDatabase"
)

if TYPE_CHECKING:
    from typing import Any, Type

    from mastapy._private.bolts import _1512, _1517, _1522
    from mastapy._private.utility.databases import _1881, _1874

    Self = TypeVar("Self", bound="BoltedJointMaterialDatabase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
    )

T = TypeVar("T", bound="_1512.BoltedJointMaterial")

__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointMaterialDatabase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BoltedJointMaterialDatabase:
    """Special nested class for casting BoltedJointMaterialDatabase to subclasses."""

    __parent__: "BoltedJointMaterialDatabase"

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
    def bolt_material_database(self: "CastSelf") -> "_1517.BoltMaterialDatabase":
        from mastapy._private.bolts import _1517

        return self.__parent__._cast(_1517.BoltMaterialDatabase)

    @property
    def clamped_section_material_database(
        self: "CastSelf",
    ) -> "_1522.ClampedSectionMaterialDatabase":
        from mastapy._private.bolts import _1522

        return self.__parent__._cast(_1522.ClampedSectionMaterialDatabase)

    @property
    def bolted_joint_material_database(
        self: "CastSelf",
    ) -> "BoltedJointMaterialDatabase":
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
class BoltedJointMaterialDatabase(_1878.NamedDatabase[T]):
    """BoltedJointMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE: ClassVar["Type"] = _BOLTED_JOINT_MATERIAL_DATABASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_BoltedJointMaterialDatabase":
        """Cast to another type.

        Returns:
            _Cast_BoltedJointMaterialDatabase
        """
        return _Cast_BoltedJointMaterialDatabase(self)
