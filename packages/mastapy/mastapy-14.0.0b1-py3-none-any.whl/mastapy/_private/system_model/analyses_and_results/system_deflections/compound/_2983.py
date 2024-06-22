"""CylindricalGearCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _2995,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CylindricalGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2581
    from mastapy._private.gears.rating.cylindrical import _466
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2830,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2986,
        _3016,
        _2961,
        _3018,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CylindricalGearCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearCompoundSystemDeflection:
    """Special nested class for casting CylindricalGearCompoundSystemDeflection to subclasses."""

    __parent__: "CylindricalGearCompoundSystemDeflection"

    @property
    def gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2995.GearCompoundSystemDeflection":
        return self.__parent__._cast(_2995.GearCompoundSystemDeflection)

    @property
    def mountable_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3016.MountableComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3016,
        )

        return self.__parent__._cast(_3016.MountableComponentCompoundSystemDeflection)

    @property
    def component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2961.ComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2961,
        )

        return self.__parent__._cast(_2961.ComponentCompoundSystemDeflection)

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3018.PartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3018,
        )

        return self.__parent__._cast(_3018.PartCompoundSystemDeflection)

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
    def cylindrical_planet_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2986.CylindricalPlanetGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2986,
        )

        return self.__parent__._cast(
            _2986.CylindricalPlanetGearCompoundSystemDeflection
        )

    @property
    def cylindrical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "CylindricalGearCompoundSystemDeflection":
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
class CylindricalGearCompoundSystemDeflection(_2995.GearCompoundSystemDeflection):
    """CylindricalGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2581.CylindricalGear":
        """mastapy._private.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def duty_cycle_rating(self: "Self") -> "_466.CylindricalGearDutyCycleRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_duty_cycle_rating(
        self: "Self",
    ) -> "_466.CylindricalGearDutyCycleRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_2830.CylindricalGearSystemDeflectionWithLTCAResults]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults]

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
    def planetaries(self: "Self") -> "List[CylindricalGearCompoundSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.compound.CylindricalGearCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_2830.CylindricalGearSystemDeflectionWithLTCAResults]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults]

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
    def cast_to(self: "Self") -> "_Cast_CylindricalGearCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearCompoundSystemDeflection
        """
        return _Cast_CylindricalGearCompoundSystemDeflection(self)
