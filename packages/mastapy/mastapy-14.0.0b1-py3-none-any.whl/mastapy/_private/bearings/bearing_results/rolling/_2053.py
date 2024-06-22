"""LoadedBallBearingElement"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.bearings.bearing_results.rolling import _2067
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_BALL_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedBallBearingElement"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility.vectors import _1885, _1884
    from mastapy._private.bearings.bearing_results.rolling import (
        _2021,
        _2035,
        _2038,
        _2064,
        _2068,
        _2072,
        _2088,
        _2103,
        _2106,
    )

    Self = TypeVar("Self", bound="LoadedBallBearingElement")
    CastSelf = TypeVar(
        "CastSelf", bound="LoadedBallBearingElement._Cast_LoadedBallBearingElement"
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBallBearingElement",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedBallBearingElement:
    """Special nested class for casting LoadedBallBearingElement to subclasses."""

    __parent__: "LoadedBallBearingElement"

    @property
    def loaded_element(self: "CastSelf") -> "_2067.LoadedElement":
        return self.__parent__._cast(_2067.LoadedElement)

    @property
    def loaded_angular_contact_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2035.LoadedAngularContactBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2035

        return self.__parent__._cast(_2035.LoadedAngularContactBallBearingElement)

    @property
    def loaded_angular_contact_thrust_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2038.LoadedAngularContactThrustBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2038

        return self.__parent__._cast(_2038.LoadedAngularContactThrustBallBearingElement)

    @property
    def loaded_deep_groove_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2064.LoadedDeepGrooveBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2064

        return self.__parent__._cast(_2064.LoadedDeepGrooveBallBearingElement)

    @property
    def loaded_four_point_contact_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2068.LoadedFourPointContactBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2068

        return self.__parent__._cast(_2068.LoadedFourPointContactBallBearingElement)

    @property
    def loaded_multi_point_contact_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2072.LoadedMultiPointContactBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2072

        return self.__parent__._cast(_2072.LoadedMultiPointContactBallBearingElement)

    @property
    def loaded_self_aligning_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2088.LoadedSelfAligningBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2088

        return self.__parent__._cast(_2088.LoadedSelfAligningBallBearingElement)

    @property
    def loaded_three_point_contact_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2103.LoadedThreePointContactBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2103

        return self.__parent__._cast(_2103.LoadedThreePointContactBallBearingElement)

    @property
    def loaded_thrust_ball_bearing_element(
        self: "CastSelf",
    ) -> "_2106.LoadedThrustBallBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2106

        return self.__parent__._cast(_2106.LoadedThrustBallBearingElement)

    @property
    def loaded_ball_bearing_element(self: "CastSelf") -> "LoadedBallBearingElement":
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
class LoadedBallBearingElement(_2067.LoadedElement):
    """LoadedBallBearingElement

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_BALL_BEARING_ELEMENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def angular_velocity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def approximate_percentage_of_friction_used_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproximatePercentageOfFrictionUsedInner

        if temp is None:
            return 0.0

        return temp

    @property
    def approximate_percentage_of_friction_used_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproximatePercentageOfFrictionUsedOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_inner_left_raceway_inside_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfInnerLeftRacewayInsideEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_inner_raceway_inner_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfInnerRacewayInnerEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_inner_raceway_left_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfInnerRacewayLeftEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_inner_raceway_outer_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfInnerRacewayOuterEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_inner_raceway_right_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfInnerRacewayRightEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_inner_right_raceway_inside_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfInnerRightRacewayInsideEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_outer_left_raceway_inside_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfOuterLeftRacewayInsideEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_outer_raceway_inner_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfOuterRacewayInnerEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_outer_raceway_left_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfOuterRacewayLeftEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_outer_raceway_outer_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfOuterRacewayOuterEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_outer_raceway_right_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfOuterRacewayRightEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def arc_distance_of_outer_right_raceway_inside_edge_to_hertzian_contact(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArcDistanceOfOuterRightRacewayInsideEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def centrifugal_force(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentrifugalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_patch_pressure_velocity_inner(
        self: "Self",
    ) -> "_1885.PlaneScalarFieldData":
        """mastapy._private.utility.vectors.PlaneScalarFieldData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchPressureVelocityInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_patch_pressure_velocity_outer(
        self: "Self",
    ) -> "_1885.PlaneScalarFieldData":
        """mastapy._private.utility.vectors.PlaneScalarFieldData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchPressureVelocityOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_patch_sliding_speed_inner(self: "Self") -> "_1885.PlaneScalarFieldData":
        """mastapy._private.utility.vectors.PlaneScalarFieldData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchSlidingSpeedInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_patch_sliding_speed_outer(self: "Self") -> "_1885.PlaneScalarFieldData":
        """mastapy._private.utility.vectors.PlaneScalarFieldData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchSlidingSpeedOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_patch_sliding_velocity_inner(
        self: "Self",
    ) -> "_1884.PlaneVectorFieldData":
        """mastapy._private.utility.vectors.PlaneVectorFieldData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchSlidingVelocityInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_patch_sliding_velocity_outer(
        self: "Self",
    ) -> "_1884.PlaneVectorFieldData":
        """mastapy._private.utility.vectors.PlaneVectorFieldData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchSlidingVelocityOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def curvature_moment_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureMomentInner

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureMomentOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def depth_of_maximum_shear_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def depth_of_maximum_shear_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthOfMaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def difference_between_cage_speed_and_orbit_speed(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DifferenceBetweenCageSpeedAndOrbitSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def drag_power_loss(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DragPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def gyroscopic_moment(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GyroscopicMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def gyroscopic_moment_about_radial_direction(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GyroscopicMomentAboutRadialDirection

        if temp is None:
            return 0.0

        return temp

    @property
    def gyroscopic_speed(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GyroscopicSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_left_race_inside_edge(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerLeftRaceInsideEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_left(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_race_inner_edge(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerRaceInnerEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_race_outer_edge(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerRaceOuterEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_right_race_inside_edge(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerRightRaceInsideEdge
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_right(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_left_race_inside_edge(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterLeftRaceInsideEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_left(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_race_inner_edge(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterRaceInnerEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_race_outer_edge(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterRaceOuterEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_right_race_inside_edge(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterRightRaceInsideEdge
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_right(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_pressure_force_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicPressureForceInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_pressure_force_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicPressureForceOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicRollingResistanceForceInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicRollingResistanceForceOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_smearing_intensity_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumSmearingIntensityInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_smearing_intensity_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumSmearingIntensityOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_contact_points(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfContactPoints

        if temp is None:
            return 0

        return temp

    @property
    def orbit_speed_ignoring_cage(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OrbitSpeedIgnoringCage

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PivotingMomentInner

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PivotingMomentOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossInner

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_total(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToElasticRollingResistanceInner

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToElasticRollingResistanceOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_inner(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceInner

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_outer(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMajorAxisInner

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMajorAxisOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMinorAxisInner

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMinorAxisOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMajorAxisInner

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMajorAxisOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMinorAxisInner

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMinorAxisOuter

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
    def smearing_safety_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmearingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def spinto_roll_ratio_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpintoRollRatioInner

        if temp is None:
            return 0.0

        return temp

    @property
    def spinto_roll_ratio_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpintoRollRatioOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_velocity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceVelocity

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
    def yaw_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YawAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_race_contact_geometries(
        self: "Self",
    ) -> "List[_2021.BallBearingRaceContactGeometry]":
        """List[mastapy._private.bearings.bearing_results.rolling.BallBearingRaceContactGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRaceContactGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def outer_race_contact_geometries(
        self: "Self",
    ) -> "List[_2021.BallBearingRaceContactGeometry]":
        """List[mastapy._private.bearings.bearing_results.rolling.BallBearingRaceContactGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRaceContactGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedBallBearingElement":
        """Cast to another type.

        Returns:
            _Cast_LoadedBallBearingElement
        """
        return _Cast_LoadedBallBearingElement(self)
