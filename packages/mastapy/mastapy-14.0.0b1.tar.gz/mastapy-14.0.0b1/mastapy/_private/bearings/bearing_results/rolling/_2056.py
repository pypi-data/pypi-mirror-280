"""LoadedBallBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.bearings.bearing_results.rolling import _2087
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedBallBearingRow"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import (
        _2055,
        _2054,
        _2037,
        _2040,
        _2066,
        _2071,
        _2090,
        _2105,
        _2108,
    )

    Self = TypeVar("Self", bound="LoadedBallBearingRow")
    CastSelf = TypeVar(
        "CastSelf", bound="LoadedBallBearingRow._Cast_LoadedBallBearingRow"
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBallBearingRow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedBallBearingRow:
    """Special nested class for casting LoadedBallBearingRow to subclasses."""

    __parent__: "LoadedBallBearingRow"

    @property
    def loaded_rolling_bearing_row(self: "CastSelf") -> "_2087.LoadedRollingBearingRow":
        return self.__parent__._cast(_2087.LoadedRollingBearingRow)

    @property
    def loaded_angular_contact_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2037.LoadedAngularContactBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2037

        return self.__parent__._cast(_2037.LoadedAngularContactBallBearingRow)

    @property
    def loaded_angular_contact_thrust_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2040.LoadedAngularContactThrustBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2040

        return self.__parent__._cast(_2040.LoadedAngularContactThrustBallBearingRow)

    @property
    def loaded_deep_groove_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2066.LoadedDeepGrooveBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2066

        return self.__parent__._cast(_2066.LoadedDeepGrooveBallBearingRow)

    @property
    def loaded_four_point_contact_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2071.LoadedFourPointContactBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2071

        return self.__parent__._cast(_2071.LoadedFourPointContactBallBearingRow)

    @property
    def loaded_self_aligning_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2090.LoadedSelfAligningBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2090

        return self.__parent__._cast(_2090.LoadedSelfAligningBallBearingRow)

    @property
    def loaded_three_point_contact_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2105.LoadedThreePointContactBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2105

        return self.__parent__._cast(_2105.LoadedThreePointContactBallBearingRow)

    @property
    def loaded_thrust_ball_bearing_row(
        self: "CastSelf",
    ) -> "_2108.LoadedThrustBallBearingRow":
        from mastapy._private.bearings.bearing_results.rolling import _2108

        return self.__parent__._cast(_2108.LoadedThrustBallBearingRow)

    @property
    def loaded_ball_bearing_row(self: "CastSelf") -> "LoadedBallBearingRow":
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
class LoadedBallBearingRow(_2087.LoadedRollingBearingRow):
    """LoadedBallBearingRow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_BALL_BEARING_ROW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def axial_ball_movement(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialBallMovement

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_with_worst_track_truncation(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementWithWorstTrackTruncation

        if temp is None:
            return ""

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_arc_distance_of_raceway_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallestArcDistanceOfRacewayEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def track_truncation_occurring_beyond_permissible_limit(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TrackTruncationOccurringBeyondPermissibleLimit

        if temp is None:
            return False

        return temp

    @property
    def truncation_warning(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TruncationWarning

        if temp is None:
            return ""

        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncation

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_bearing(self: "Self") -> "_2055.LoadedBallBearingResults":
        """mastapy._private.bearings.bearing_results.rolling.LoadedBallBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def race_results(self: "Self") -> "List[_2054.LoadedBallBearingRaceResults]":
        """List[mastapy._private.bearings.bearing_results.rolling.LoadedBallBearingRaceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedBallBearingRow":
        """Cast to another type.

        Returns:
            _Cast_LoadedBallBearingRow
        """
        return _Cast_LoadedBallBearingRow(self)
