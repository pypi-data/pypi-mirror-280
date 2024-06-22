"""BoltMaterial"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.bolts import _1512
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BOLT_MATERIAL = python_net_import("SMT.MastaAPI.Bolts", "BoltMaterial")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bolts import _1531
    from mastapy._private.materials import _280
    from mastapy._private.utility.databases import _1879

    Self = TypeVar("Self", bound="BoltMaterial")
    CastSelf = TypeVar("CastSelf", bound="BoltMaterial._Cast_BoltMaterial")


__docformat__ = "restructuredtext en"
__all__ = ("BoltMaterial",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BoltMaterial:
    """Special nested class for casting BoltMaterial to subclasses."""

    __parent__: "BoltMaterial"

    @property
    def bolted_joint_material(self: "CastSelf") -> "_1512.BoltedJointMaterial":
        return self.__parent__._cast(_1512.BoltedJointMaterial)

    @property
    def material(self: "CastSelf") -> "_280.Material":
        from mastapy._private.materials import _280

        return self.__parent__._cast(_280.Material)

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        from mastapy._private.utility.databases import _1879

        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def bolt_material(self: "CastSelf") -> "BoltMaterial":
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
class BoltMaterial(_1512.BoltedJointMaterial):
    """BoltMaterial

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BOLT_MATERIAL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def minimum_tensile_strength(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumTensileStrength

        if temp is None:
            return 0.0

        return temp

    @minimum_tensile_strength.setter
    @enforce_parameter_types
    def minimum_tensile_strength(self: "Self", value: "float") -> None:
        self.wrapped.MinimumTensileStrength = float(value) if value is not None else 0.0

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
    def shearing_strength(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ShearingStrength

        if temp is None:
            return 0.0

        return temp

    @shearing_strength.setter
    @enforce_parameter_types
    def shearing_strength(self: "Self", value: "float") -> None:
        self.wrapped.ShearingStrength = float(value) if value is not None else 0.0

    @property
    def strength_grade(self: "Self") -> "_1531.StrengthGrades":
        """mastapy._private.bolts.StrengthGrades"""
        temp = self.wrapped.StrengthGrade

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bolts.StrengthGrades")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bolts._1531", "StrengthGrades"
        )(value)

    @strength_grade.setter
    @enforce_parameter_types
    def strength_grade(self: "Self", value: "_1531.StrengthGrades") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bolts.StrengthGrades")
        self.wrapped.StrengthGrade = value

    @property
    def cast_to(self: "Self") -> "_Cast_BoltMaterial":
        """Cast to another type.

        Returns:
            _Cast_BoltMaterial
        """
        return _Cast_BoltMaterial(self)
