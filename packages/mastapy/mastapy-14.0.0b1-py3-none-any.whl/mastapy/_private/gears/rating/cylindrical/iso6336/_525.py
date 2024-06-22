"""ISO63362006MeshSingleFlankRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.rating.cylindrical.iso6336 import _531
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ISO63362006_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO63362006MeshSingleFlankRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.cylindrical.iso6336 import _527, _529
    from mastapy._private.gears.rating.cylindrical import _478
    from mastapy._private.gears.rating import _377

    Self = TypeVar("Self", bound="ISO63362006MeshSingleFlankRating")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ISO63362006MeshSingleFlankRating._Cast_ISO63362006MeshSingleFlankRating",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISO63362006MeshSingleFlankRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ISO63362006MeshSingleFlankRating:
    """Special nested class for casting ISO63362006MeshSingleFlankRating to subclasses."""

    __parent__: "ISO63362006MeshSingleFlankRating"

    @property
    def iso6336_abstract_metal_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "_531.ISO6336AbstractMetalMeshSingleFlankRating":
        return self.__parent__._cast(_531.ISO6336AbstractMetalMeshSingleFlankRating)

    @property
    def iso6336_abstract_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "_529.ISO6336AbstractMeshSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _529

        return self.__parent__._cast(_529.ISO6336AbstractMeshSingleFlankRating)

    @property
    def cylindrical_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "_478.CylindricalMeshSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical import _478

        return self.__parent__._cast(_478.CylindricalMeshSingleFlankRating)

    @property
    def mesh_single_flank_rating(self: "CastSelf") -> "_377.MeshSingleFlankRating":
        from mastapy._private.gears.rating import _377

        return self.__parent__._cast(_377.MeshSingleFlankRating)

    @property
    def iso63362019_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "_527.ISO63362019MeshSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _527

        return self.__parent__._cast(_527.ISO63362019MeshSingleFlankRating)

    @property
    def iso63362006_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "ISO63362006MeshSingleFlankRating":
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
class ISO63362006MeshSingleFlankRating(_531.ISO6336AbstractMetalMeshSingleFlankRating):
    """ISO63362006MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ISO63362006_MESH_SINGLE_FLANK_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def deep_tooth_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeepToothFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor_source(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicFactorSource

        if temp is None:
            return ""

        return temp

    @property
    def helix_angle_factor_contact(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_stiffness_face(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshStiffnessFace

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_stiffness_transverse(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshStiffnessTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def transverse_load_factor_bending(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_ISO63362006MeshSingleFlankRating":
        """Cast to another type.

        Returns:
            _Cast_ISO63362006MeshSingleFlankRating
        """
        return _Cast_ISO63362006MeshSingleFlankRating(self)
