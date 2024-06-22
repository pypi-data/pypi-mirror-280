"""DIN3990MeshSingleFlankRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.gears.rating.cylindrical.iso6336 import _523
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_DIN3990_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.DIN3990", "DIN3990MeshSingleFlankRating"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.rating.cylindrical import _492, _493, _478
    from mastapy._private.gears.rating.cylindrical.iso6336 import _531, _529
    from mastapy._private.gears.rating import _377

    Self = TypeVar("Self", bound="DIN3990MeshSingleFlankRating")
    CastSelf = TypeVar(
        "CastSelf",
        bound="DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
    )


__docformat__ = "restructuredtext en"
__all__ = ("DIN3990MeshSingleFlankRating",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_DIN3990MeshSingleFlankRating:
    """Special nested class for casting DIN3990MeshSingleFlankRating to subclasses."""

    __parent__: "DIN3990MeshSingleFlankRating"

    @property
    def iso63361996_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "_523.ISO63361996MeshSingleFlankRating":
        return self.__parent__._cast(_523.ISO63361996MeshSingleFlankRating)

    @property
    def iso6336_abstract_metal_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "_531.ISO6336AbstractMetalMeshSingleFlankRating":
        from mastapy._private.gears.rating.cylindrical.iso6336 import _531

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
    def din3990_mesh_single_flank_rating(
        self: "CastSelf",
    ) -> "DIN3990MeshSingleFlankRating":
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
class DIN3990MeshSingleFlankRating(_523.ISO63361996MeshSingleFlankRating):
    """DIN3990MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _DIN3990_MESH_SINGLE_FLANK_RATING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def basic_mean_flash_temperature(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicMeanFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def estimated_bulk_temperature_flash(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedBulkTemperatureFlash

        if temp is None:
            return 0.0

        return temp

    @property
    def estimated_bulk_temperature_integral(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedBulkTemperatureIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def flash_factor_integral(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlashFactorIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_at_maximum_flash_temperature(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def integral_scuffing_temperature(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntegralScuffingTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_at_maximum_flash_temperature(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_coefficient_of_friction_integral_temperature_method(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanCoefficientOfFrictionIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_local_coefficient_of_friction_at_maximum_flash_temperature(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanLocalCoefficientOfFrictionAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def parameter_on_line_of_action_at_maximum_flash_temperature(
        self: "Self",
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterOnLineOfActionAtMaximumFlashTemperature

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
    def resonance_ratio_in_the_main_resonance_range(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResonanceRatioInTheMainResonanceRange

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_rating_method_flash_temperature_method(
        self: "Self",
    ) -> "_492.ScuffingFlashTemperatureRatingMethod":
        """mastapy._private.gears.rating.cylindrical.ScuffingFlashTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingRatingMethodFlashTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.ScuffingFlashTemperatureRatingMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating.cylindrical._492",
            "ScuffingFlashTemperatureRatingMethod",
        )(value)

    @property
    def scuffing_rating_method_integral_temperature_method(
        self: "Self",
    ) -> "_493.ScuffingIntegralTemperatureRatingMethod":
        """mastapy._private.gears.rating.cylindrical.ScuffingIntegralTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingRatingMethodIntegralTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.ScuffingIntegralTemperatureRatingMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating.cylindrical._493",
            "ScuffingIntegralTemperatureRatingMethod",
        )(value)

    @property
    def thermo_elastic_factor_at_maximum_flash_temperature(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermoElasticFactorAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_relief_factor_integral(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipReliefFactorIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_unit_load(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseUnitLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_DIN3990MeshSingleFlankRating":
        """Cast to another type.

        Returns:
            _Cast_DIN3990MeshSingleFlankRating
        """
        return _Cast_DIN3990MeshSingleFlankRating(self)
