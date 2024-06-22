"""LoadedDetailedBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.bearings.bearing_results import _2010
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_LOADED_DETAILED_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedDetailedBearingResults"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.materials import _278
    from mastapy._private.bearings.bearing_results.rolling import (
        _2036,
        _2039,
        _2042,
        _2047,
        _2050,
        _2055,
        _2058,
        _2062,
        _2065,
        _2070,
        _2074,
        _2077,
        _2082,
        _2086,
        _2089,
        _2093,
        _2096,
        _2101,
        _2104,
        _2107,
        _2110,
    )
    from mastapy._private.bearings.bearing_results.fluid_film import (
        _2172,
        _2173,
        _2174,
        _2175,
        _2177,
        _2180,
        _2181,
    )
    from mastapy._private.bearings.bearing_results import _2002
    from mastapy._private.bearings import _1927

    Self = TypeVar("Self", bound="LoadedDetailedBearingResults")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedDetailedBearingResults",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedDetailedBearingResults:
    """Special nested class for casting LoadedDetailedBearingResults to subclasses."""

    __parent__: "LoadedDetailedBearingResults"

    @property
    def loaded_non_linear_bearing_results(
        self: "CastSelf",
    ) -> "_2010.LoadedNonLinearBearingResults":
        return self.__parent__._cast(_2010.LoadedNonLinearBearingResults)

    @property
    def loaded_bearing_results(self: "CastSelf") -> "_2002.LoadedBearingResults":
        from mastapy._private.bearings.bearing_results import _2002

        return self.__parent__._cast(_2002.LoadedBearingResults)

    @property
    def bearing_load_case_results_lightweight(
        self: "CastSelf",
    ) -> "_1927.BearingLoadCaseResultsLightweight":
        from mastapy._private.bearings import _1927

        return self.__parent__._cast(_1927.BearingLoadCaseResultsLightweight)

    @property
    def loaded_angular_contact_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2036.LoadedAngularContactBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2036

        return self.__parent__._cast(_2036.LoadedAngularContactBallBearingResults)

    @property
    def loaded_angular_contact_thrust_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2039.LoadedAngularContactThrustBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2039

        return self.__parent__._cast(_2039.LoadedAngularContactThrustBallBearingResults)

    @property
    def loaded_asymmetric_spherical_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2042.LoadedAsymmetricSphericalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2042

        return self.__parent__._cast(
            _2042.LoadedAsymmetricSphericalRollerBearingResults
        )

    @property
    def loaded_axial_thrust_cylindrical_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2047.LoadedAxialThrustCylindricalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2047

        return self.__parent__._cast(
            _2047.LoadedAxialThrustCylindricalRollerBearingResults
        )

    @property
    def loaded_axial_thrust_needle_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2050.LoadedAxialThrustNeedleRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2050

        return self.__parent__._cast(_2050.LoadedAxialThrustNeedleRollerBearingResults)

    @property
    def loaded_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2055.LoadedBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2055

        return self.__parent__._cast(_2055.LoadedBallBearingResults)

    @property
    def loaded_crossed_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2058.LoadedCrossedRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2058

        return self.__parent__._cast(_2058.LoadedCrossedRollerBearingResults)

    @property
    def loaded_cylindrical_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2062.LoadedCylindricalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2062

        return self.__parent__._cast(_2062.LoadedCylindricalRollerBearingResults)

    @property
    def loaded_deep_groove_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2065.LoadedDeepGrooveBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2065

        return self.__parent__._cast(_2065.LoadedDeepGrooveBallBearingResults)

    @property
    def loaded_four_point_contact_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2070.LoadedFourPointContactBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2070

        return self.__parent__._cast(_2070.LoadedFourPointContactBallBearingResults)

    @property
    def loaded_needle_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2074.LoadedNeedleRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2074

        return self.__parent__._cast(_2074.LoadedNeedleRollerBearingResults)

    @property
    def loaded_non_barrel_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2077.LoadedNonBarrelRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2077

        return self.__parent__._cast(_2077.LoadedNonBarrelRollerBearingResults)

    @property
    def loaded_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2082.LoadedRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2082

        return self.__parent__._cast(_2082.LoadedRollerBearingResults)

    @property
    def loaded_rolling_bearing_results(
        self: "CastSelf",
    ) -> "_2086.LoadedRollingBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2086

        return self.__parent__._cast(_2086.LoadedRollingBearingResults)

    @property
    def loaded_self_aligning_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2089.LoadedSelfAligningBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2089

        return self.__parent__._cast(_2089.LoadedSelfAligningBallBearingResults)

    @property
    def loaded_spherical_roller_radial_bearing_results(
        self: "CastSelf",
    ) -> "_2093.LoadedSphericalRollerRadialBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2093

        return self.__parent__._cast(_2093.LoadedSphericalRollerRadialBearingResults)

    @property
    def loaded_spherical_roller_thrust_bearing_results(
        self: "CastSelf",
    ) -> "_2096.LoadedSphericalRollerThrustBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2096

        return self.__parent__._cast(_2096.LoadedSphericalRollerThrustBearingResults)

    @property
    def loaded_taper_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2101.LoadedTaperRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2101

        return self.__parent__._cast(_2101.LoadedTaperRollerBearingResults)

    @property
    def loaded_three_point_contact_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2104.LoadedThreePointContactBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2104

        return self.__parent__._cast(_2104.LoadedThreePointContactBallBearingResults)

    @property
    def loaded_thrust_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2107.LoadedThrustBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2107

        return self.__parent__._cast(_2107.LoadedThrustBallBearingResults)

    @property
    def loaded_toroidal_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2110.LoadedToroidalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2110

        return self.__parent__._cast(_2110.LoadedToroidalRollerBearingResults)

    @property
    def loaded_fluid_film_bearing_results(
        self: "CastSelf",
    ) -> "_2172.LoadedFluidFilmBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2172

        return self.__parent__._cast(_2172.LoadedFluidFilmBearingResults)

    @property
    def loaded_grease_filled_journal_bearing_results(
        self: "CastSelf",
    ) -> "_2173.LoadedGreaseFilledJournalBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2173

        return self.__parent__._cast(_2173.LoadedGreaseFilledJournalBearingResults)

    @property
    def loaded_pad_fluid_film_bearing_results(
        self: "CastSelf",
    ) -> "_2174.LoadedPadFluidFilmBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2174

        return self.__parent__._cast(_2174.LoadedPadFluidFilmBearingResults)

    @property
    def loaded_plain_journal_bearing_results(
        self: "CastSelf",
    ) -> "_2175.LoadedPlainJournalBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2175

        return self.__parent__._cast(_2175.LoadedPlainJournalBearingResults)

    @property
    def loaded_plain_oil_fed_journal_bearing(
        self: "CastSelf",
    ) -> "_2177.LoadedPlainOilFedJournalBearing":
        from mastapy._private.bearings.bearing_results.fluid_film import _2177

        return self.__parent__._cast(_2177.LoadedPlainOilFedJournalBearing)

    @property
    def loaded_tilting_pad_journal_bearing_results(
        self: "CastSelf",
    ) -> "_2180.LoadedTiltingPadJournalBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2180

        return self.__parent__._cast(_2180.LoadedTiltingPadJournalBearingResults)

    @property
    def loaded_tilting_pad_thrust_bearing_results(
        self: "CastSelf",
    ) -> "_2181.LoadedTiltingPadThrustBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2181

        return self.__parent__._cast(_2181.LoadedTiltingPadThrustBearingResults)

    @property
    def loaded_detailed_bearing_results(
        self: "CastSelf",
    ) -> "LoadedDetailedBearingResults":
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
class LoadedDetailedBearingResults(_2010.LoadedNonLinearBearingResults):
    """LoadedDetailedBearingResults

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_DETAILED_BEARING_RESULTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def lubricant_flow_rate(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LubricantFlowRate

        if temp is None:
            return 0.0

        return temp

    @lubricant_flow_rate.setter
    @enforce_parameter_types
    def lubricant_flow_rate(self: "Self", value: "float") -> None:
        self.wrapped.LubricantFlowRate = float(value) if value is not None else 0.0

    @property
    def oil_sump_temperature(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OilSumpTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_sump_temperature.setter
    @enforce_parameter_types
    def oil_sump_temperature(self: "Self", value: "float") -> None:
        self.wrapped.OilSumpTemperature = float(value) if value is not None else 0.0

    @property
    def operating_air_temperature(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OperatingAirTemperature

        if temp is None:
            return 0.0

        return temp

    @operating_air_temperature.setter
    @enforce_parameter_types
    def operating_air_temperature(self: "Self", value: "float") -> None:
        self.wrapped.OperatingAirTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def temperature_when_assembled(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TemperatureWhenAssembled

        if temp is None:
            return 0.0

        return temp

    @temperature_when_assembled.setter
    @enforce_parameter_types
    def temperature_when_assembled(self: "Self", value: "float") -> None:
        self.wrapped.TemperatureWhenAssembled = (
            float(value) if value is not None else 0.0
        )

    @property
    def lubrication(self: "Self") -> "_278.LubricationDetail":
        """mastapy._private.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Lubrication

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedDetailedBearingResults":
        """Cast to another type.

        Returns:
            _Cast_LoadedDetailedBearingResults
        """
        return _Cast_LoadedDetailedBearingResults(self)
