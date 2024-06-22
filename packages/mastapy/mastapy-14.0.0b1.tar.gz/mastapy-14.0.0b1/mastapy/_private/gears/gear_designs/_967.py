"""BevelHypoidGearRatingSettingsItem"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility.databases import _1879
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "BevelHypoidGearRatingSettingsItem"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.materials import _627
    from mastapy._private.gears.rating.iso_10300 import _431, _446, _439
    from mastapy._private.gears.rating.hypoid import _452

    Self = TypeVar("Self", bound="BevelHypoidGearRatingSettingsItem")
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelHypoidGearRatingSettingsItem._Cast_BevelHypoidGearRatingSettingsItem",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelHypoidGearRatingSettingsItem",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelHypoidGearRatingSettingsItem:
    """Special nested class for casting BevelHypoidGearRatingSettingsItem to subclasses."""

    __parent__: "BevelHypoidGearRatingSettingsItem"

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def bevel_hypoid_gear_rating_settings_item(
        self: "CastSelf",
    ) -> "BevelHypoidGearRatingSettingsItem":
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
class BevelHypoidGearRatingSettingsItem(_1879.NamedDatabaseItem):
    """BevelHypoidGearRatingSettingsItem

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_HYPOID_GEAR_RATING_SETTINGS_ITEM

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bevel_gear_rating_method(self: "Self") -> "_627.RatingMethods":
        """mastapy._private.gears.materials.RatingMethods"""
        temp = self.wrapped.BevelGearRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.RatingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.materials._627", "RatingMethods"
        )(value)

    @bevel_gear_rating_method.setter
    @enforce_parameter_types
    def bevel_gear_rating_method(self: "Self", value: "_627.RatingMethods") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.RatingMethods"
        )
        self.wrapped.BevelGearRatingMethod = value

    @property
    def bevel_general_load_factors_k_method(
        self: "Self",
    ) -> "_431.GeneralLoadFactorCalculationMethod":
        """mastapy._private.gears.rating.isoGeneralLoadFactorCalculationMethod"""
        temp = self.wrapped.BevelGeneralLoadFactorsKMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating._431", "GeneralLoadFactorCalculationMethod"
        )(value)

    @bevel_general_load_factors_k_method.setter
    @enforce_parameter_types
    def bevel_general_load_factors_k_method(
        self: "Self", value: "_431.GeneralLoadFactorCalculationMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod",
        )
        self.wrapped.BevelGeneralLoadFactorsKMethod = value

    @property
    def bevel_pitting_factor_calculation_method(
        self: "Self",
    ) -> "_446.PittingFactorCalculationMethod":
        """mastapy._private.gears.rating.isoPittingFactorCalculationMethod"""
        temp = self.wrapped.BevelPittingFactorCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating._446", "PittingFactorCalculationMethod"
        )(value)

    @bevel_pitting_factor_calculation_method.setter
    @enforce_parameter_types
    def bevel_pitting_factor_calculation_method(
        self: "Self", value: "_446.PittingFactorCalculationMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod"
        )
        self.wrapped.BevelPittingFactorCalculationMethod = value

    @property
    def hypoid_gear_rating_method(self: "Self") -> "_452.HypoidRatingMethod":
        """mastapy._private.gears.rating.hypoid.HypoidRatingMethod"""
        temp = self.wrapped.HypoidGearRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Hypoid.HypoidRatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating.hypoid._452", "HypoidRatingMethod"
        )(value)

    @hypoid_gear_rating_method.setter
    @enforce_parameter_types
    def hypoid_gear_rating_method(
        self: "Self", value: "_452.HypoidRatingMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Hypoid.HypoidRatingMethod"
        )
        self.wrapped.HypoidGearRatingMethod = value

    @property
    def hypoid_general_load_factors_k_method(
        self: "Self",
    ) -> "_431.GeneralLoadFactorCalculationMethod":
        """mastapy._private.gears.rating.isoGeneralLoadFactorCalculationMethod"""
        temp = self.wrapped.HypoidGeneralLoadFactorsKMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating._431", "GeneralLoadFactorCalculationMethod"
        )(value)

    @hypoid_general_load_factors_k_method.setter
    @enforce_parameter_types
    def hypoid_general_load_factors_k_method(
        self: "Self", value: "_431.GeneralLoadFactorCalculationMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod",
        )
        self.wrapped.HypoidGeneralLoadFactorsKMethod = value

    @property
    def hypoid_pitting_factor_calculation_method(
        self: "Self",
    ) -> "_446.PittingFactorCalculationMethod":
        """mastapy._private.gears.rating.isoPittingFactorCalculationMethod"""
        temp = self.wrapped.HypoidPittingFactorCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating._446", "PittingFactorCalculationMethod"
        )(value)

    @hypoid_pitting_factor_calculation_method.setter
    @enforce_parameter_types
    def hypoid_pitting_factor_calculation_method(
        self: "Self", value: "_446.PittingFactorCalculationMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod"
        )
        self.wrapped.HypoidPittingFactorCalculationMethod = value

    @property
    def iso_rating_method_for_bevel_gears(self: "Self") -> "_439.ISO10300RatingMethod":
        """mastapy._private.gears.rating.isoISO10300RatingMethod"""
        temp = self.wrapped.ISORatingMethodForBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating._439", "ISO10300RatingMethod"
        )(value)

    @iso_rating_method_for_bevel_gears.setter
    @enforce_parameter_types
    def iso_rating_method_for_bevel_gears(
        self: "Self", value: "_439.ISO10300RatingMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod"
        )
        self.wrapped.ISORatingMethodForBevelGears = value

    @property
    def iso_rating_method_for_hypoid_gears(self: "Self") -> "_439.ISO10300RatingMethod":
        """mastapy._private.gears.rating.isoISO10300RatingMethod"""
        temp = self.wrapped.ISORatingMethodForHypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.rating._439", "ISO10300RatingMethod"
        )(value)

    @iso_rating_method_for_hypoid_gears.setter
    @enforce_parameter_types
    def iso_rating_method_for_hypoid_gears(
        self: "Self", value: "_439.ISO10300RatingMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod"
        )
        self.wrapped.ISORatingMethodForHypoidGears = value

    @property
    def include_mesh_node_misalignments_in_default_report(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport

        if temp is None:
            return False

        return temp

    @include_mesh_node_misalignments_in_default_report.setter
    @enforce_parameter_types
    def include_mesh_node_misalignments_in_default_report(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: "Self") -> "_Cast_BevelHypoidGearRatingSettingsItem":
        """Cast to another type.

        Returns:
            _Cast_BevelHypoidGearRatingSettingsItem
        """
        return _Cast_BevelHypoidGearRatingSettingsItem(self)
