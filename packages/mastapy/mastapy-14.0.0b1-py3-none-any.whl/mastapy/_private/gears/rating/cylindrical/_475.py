"""CylindricalGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.rating import _374
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearSetRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.materials import _262
    from mastapy._private.gears.gear_designs.cylindrical import _1058
    from mastapy._private.gears.rating.cylindrical.optimisation import _512
    from mastapy._private.gears.rating.cylindrical import _465, _471, _469
    from mastapy._private.gears.rating.cylindrical.vdi import _500
    from mastapy._private.gears.rating import _365
    from mastapy._private.gears.analysis import _1255

    Self = TypeVar("Self", bound="CylindricalGearSetRating")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalGearSetRating._Cast_CylindricalGearSetRating"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearSetRating:
    """Special nested class for casting CylindricalGearSetRating to subclasses."""

    __parent__: "CylindricalGearSetRating"

    @property
    def gear_set_rating(self: "CastSelf") -> "_374.GearSetRating":
        return self.__parent__._cast(_374.GearSetRating)

    @property
    def abstract_gear_set_rating(self: "CastSelf") -> "_365.AbstractGearSetRating":
        from mastapy._private.gears.rating import _365

        return self.__parent__._cast(_365.AbstractGearSetRating)

    @property
    def abstract_gear_set_analysis(self: "CastSelf") -> "_1255.AbstractGearSetAnalysis":
        from mastapy._private.gears.analysis import _1255

        return self.__parent__._cast(_1255.AbstractGearSetAnalysis)

    @property
    def cylindrical_gear_set_rating(self: "CastSelf") -> "CylindricalGearSetRating":
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
class CylindricalGearSetRating(_374.GearSetRating):
    """CylindricalGearSetRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SET_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def rating_method(self: "Self") -> "_262.CylindricalGearRatingMethods":
        """mastapy._private.materials.CylindricalGearRatingMethods

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.CylindricalGearRatingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.materials._262", "CylindricalGearRatingMethods"
        )(value)

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
    def cylindrical_gear_set(self: "Self") -> "_1058.CylindricalGearSetDesign":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def optimisations(
        self: "Self",
    ) -> "_512.CylindricalGearSetRatingOptimisationHelper":
        """mastapy._private.gears.rating.cylindrical.optimisation.CylindricalGearSetRatingOptimisationHelper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Optimisations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating_settings(
        self: "Self",
    ) -> "_465.CylindricalGearDesignAndRatingSettingsItem":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: "Self") -> "List[_471.CylindricalGearRating]":
        """List[mastapy._private.gears.rating.cylindrical.CylindricalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_ratings(self: "Self") -> "List[_471.CylindricalGearRating]":
        """List[mastapy._private.gears.rating.cylindrical.CylindricalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_ratings(self: "Self") -> "List[_469.CylindricalGearMeshRating]":
        """List[mastapy._private.gears.rating.cylindrical.CylindricalGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_mesh_ratings(
        self: "Self",
    ) -> "List[_469.CylindricalGearMeshRating]":
        """List[mastapy._private.gears.rating.cylindrical.CylindricalGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def vdi_cylindrical_gear_single_flank_ratings(
        self: "Self",
    ) -> "List[_500.VDI2737InternalGearSingleFlankRating]":
        """List[mastapy._private.gears.rating.cylindrical.vdi.VDI2737InternalGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VDICylindricalGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearSetRating":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearSetRating
        """
        return _Cast_CylindricalGearSetRating(self)
