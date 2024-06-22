"""GearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7639,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "GearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.rating import _368
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7485,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7564,
        _7571,
        _7574,
        _7575,
        _7576,
        _7589,
        _7592,
        _7607,
        _7610,
        _7613,
        _7622,
        _7626,
        _7629,
        _7632,
        _7661,
        _7667,
        _7670,
        _7673,
        _7674,
        _7685,
        _7688,
        _7585,
        _7641,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="GearCompoundAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearCompoundAdvancedSystemDeflection._Cast_GearCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearCompoundAdvancedSystemDeflection:
    """Special nested class for casting GearCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "GearCompoundAdvancedSystemDeflection"

    @property
    def mountable_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7639.MountableComponentCompoundAdvancedSystemDeflection":
        return self.__parent__._cast(
            _7639.MountableComponentCompoundAdvancedSystemDeflection
        )

    @property
    def component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7585.ComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7585,
        )

        return self.__parent__._cast(_7585.ComponentCompoundAdvancedSystemDeflection)

    @property
    def part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7641.PartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7641,
        )

        return self.__parent__._cast(_7641.PartCompoundAdvancedSystemDeflection)

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7711.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7711,
        )

        return self.__parent__._cast(_7711.PartCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7708.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7708,
        )

        return self.__parent__._cast(_7708.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def agma_gleason_conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7564.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7564,
        )

        return self.__parent__._cast(
            _7564.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7571.BevelDifferentialGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7571,
        )

        return self.__parent__._cast(
            _7571.BevelDifferentialGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7574.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7574,
        )

        return self.__parent__._cast(
            _7574.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_sun_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7575.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7575,
        )

        return self.__parent__._cast(
            _7575.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7576.BevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7576,
        )

        return self.__parent__._cast(_7576.BevelGearCompoundAdvancedSystemDeflection)

    @property
    def concept_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7589.ConceptGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7589,
        )

        return self.__parent__._cast(_7589.ConceptGearCompoundAdvancedSystemDeflection)

    @property
    def conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7592.ConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7592,
        )

        return self.__parent__._cast(_7592.ConicalGearCompoundAdvancedSystemDeflection)

    @property
    def cylindrical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7607.CylindricalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7607,
        )

        return self.__parent__._cast(
            _7607.CylindricalGearCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7610.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7610,
        )

        return self.__parent__._cast(
            _7610.CylindricalPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def face_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7613.FaceGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7613,
        )

        return self.__parent__._cast(_7613.FaceGearCompoundAdvancedSystemDeflection)

    @property
    def hypoid_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7622.HypoidGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7622,
        )

        return self.__parent__._cast(_7622.HypoidGearCompoundAdvancedSystemDeflection)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7626.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7626,
        )

        return self.__parent__._cast(
            _7626.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7629.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7629,
        )

        return self.__parent__._cast(
            _7629.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> (
        "_7632.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7632,
        )

        return self.__parent__._cast(
            _7632.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7661.SpiralBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7661,
        )

        return self.__parent__._cast(
            _7661.SpiralBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7667.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7667,
        )

        return self.__parent__._cast(
            _7667.StraightBevelDiffGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7670.StraightBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7670,
        )

        return self.__parent__._cast(
            _7670.StraightBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7673.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7673,
        )

        return self.__parent__._cast(
            _7673.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_sun_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7674.StraightBevelSunGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7674,
        )

        return self.__parent__._cast(
            _7674.StraightBevelSunGearCompoundAdvancedSystemDeflection
        )

    @property
    def worm_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7685.WormGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7685,
        )

        return self.__parent__._cast(_7685.WormGearCompoundAdvancedSystemDeflection)

    @property
    def zerol_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7688.ZerolBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7688,
        )

        return self.__parent__._cast(
            _7688.ZerolBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "GearCompoundAdvancedSystemDeflection":
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
class GearCompoundAdvancedSystemDeflection(
    _7639.MountableComponentCompoundAdvancedSystemDeflection
):
    """GearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def gear_duty_cycle_rating(self: "Self") -> "_368.GearDutyCycleRating":
        """mastapy._private.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_7485.GearAdvancedSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_system_deflections.GearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_7485.GearAdvancedSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_system_deflections.GearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_GearCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_GearCompoundAdvancedSystemDeflection
        """
        return _Cast_GearCompoundAdvancedSystemDeflection(self)
