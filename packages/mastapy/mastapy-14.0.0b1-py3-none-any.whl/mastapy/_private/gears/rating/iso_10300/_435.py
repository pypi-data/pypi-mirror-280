"""ISO10300MeshSingleFlankRatingHypoidMethodB2"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.rating.iso_10300 import _437
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ISO10300_MESH_SINGLE_FLANK_RATING_HYPOID_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300MeshSingleFlankRatingHypoidMethodB2"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.iso_10300 import _433
    from mastapy._private.gears.rating.conical import _557
    from mastapy._private.gears.rating import _377

    Self = TypeVar("Self", bound="ISO10300MeshSingleFlankRatingHypoidMethodB2")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300MeshSingleFlankRatingHypoidMethodB2",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2:
    """Special nested class for casting ISO10300MeshSingleFlankRatingHypoidMethodB2 to subclasses."""

    __parent__: "ISO10300MeshSingleFlankRatingHypoidMethodB2"

    @property
    def iso10300_mesh_single_flank_rating_method_b2(
        self: "CastSelf",
    ) -> "_437.ISO10300MeshSingleFlankRatingMethodB2":
        return self.__parent__._cast(_437.ISO10300MeshSingleFlankRatingMethodB2)

    @property
    def iso10300_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "_433.ISO10300MeshSingleFlankRating":
        pass

        from mastapy._private.gears.rating.iso_10300 import _433

        return self.__parent__._cast(_433.ISO10300MeshSingleFlankRating)

    @property
    def conical_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "_557.ConicalMeshSingleFlankRating":
        from mastapy._private.gears.rating.conical import _557

        return self.__parent__._cast(_557.ConicalMeshSingleFlankRating)

    @property
    def mesh_single_flank_rating(self: "CastSelf") -> "_377.MeshSingleFlankRating":
        from mastapy._private.gears.rating import _377

        return self.__parent__._cast(_377.MeshSingleFlankRating)

    @property
    def iso10300_mesh_single_flank_rating_hypoid_method_b2(
        self: "CastSelf",
    ) -> "ISO10300MeshSingleFlankRatingHypoidMethodB2":
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
class ISO10300MeshSingleFlankRatingHypoidMethodB2(
    _437.ISO10300MeshSingleFlankRatingMethodB2
):
    """ISO10300MeshSingleFlankRatingHypoidMethodB2

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ISO10300_MESH_SINGLE_FLANK_RATING_HYPOID_METHOD_B2

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def length_of_action_from_pinion_tip_to_point_of_load_application(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfActionFromPinionTipToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_action_from_wheel_tip_to_point_of_load_application(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfActionFromWheelTipToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def lengthwise_load_sharing_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthwiseLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_length_of_action_point_of_load_application(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionLengthOfActionPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_load_sharing_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_length_of_action_point_of_load_application(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelLengthOfActionPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2":
        """Cast to another type.

        Returns:
            _Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2
        """
        return _Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2(self)
