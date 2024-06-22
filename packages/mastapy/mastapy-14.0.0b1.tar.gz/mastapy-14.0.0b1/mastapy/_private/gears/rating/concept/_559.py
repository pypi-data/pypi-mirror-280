"""ConceptGearDutyCycleRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.rating import _368
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONCEPT_GEAR_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Concept", "ConceptGearDutyCycleRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating import _369, _364
    from mastapy._private.gears.analysis import _1253

    Self = TypeVar("Self", bound="ConceptGearDutyCycleRating")
    CastSelf = TypeVar(
        "CastSelf", bound="ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearDutyCycleRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConceptGearDutyCycleRating:
    """Special nested class for casting ConceptGearDutyCycleRating to subclasses."""

    __parent__: "ConceptGearDutyCycleRating"

    @property
    def gear_duty_cycle_rating(self: "CastSelf") -> "_368.GearDutyCycleRating":
        return self.__parent__._cast(_368.GearDutyCycleRating)

    @property
    def abstract_gear_rating(self: "CastSelf") -> "_364.AbstractGearRating":
        from mastapy._private.gears.rating import _364

        return self.__parent__._cast(_364.AbstractGearRating)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def concept_gear_duty_cycle_rating(
        self: "CastSelf",
    ) -> "ConceptGearDutyCycleRating":
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
class ConceptGearDutyCycleRating(_368.GearDutyCycleRating):
    """ConceptGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONCEPT_GEAR_DUTY_CYCLE_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def left_flank_rating(self: "Self") -> "_369.GearFlankRating":
        """mastapy._private.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_rating(self: "Self") -> "_369.GearFlankRating":
        """mastapy._private.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConceptGearDutyCycleRating":
        """Cast to another type.

        Returns:
            _Cast_ConceptGearDutyCycleRating
        """
        return _Cast_ConceptGearDutyCycleRating(self)
