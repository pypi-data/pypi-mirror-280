"""CylindricalGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
    _4332,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CylindricalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2582
    from mastapy._private.gears.rating.cylindrical import _474
    from mastapy._private.system_model.analyses_and_results.power_flows import _4185
    from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
        _4319,
        _4320,
        _4358,
        _4372,
        _4272,
        _4353,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CylindricalGearSetCompoundPowerFlow")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearSetCompoundPowerFlow:
    """Special nested class for casting CylindricalGearSetCompoundPowerFlow to subclasses."""

    __parent__: "CylindricalGearSetCompoundPowerFlow"

    @property
    def gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4332.GearSetCompoundPowerFlow":
        return self.__parent__._cast(_4332.GearSetCompoundPowerFlow)

    @property
    def specialised_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4372.SpecialisedAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4372,
        )

        return self.__parent__._cast(_4372.SpecialisedAssemblyCompoundPowerFlow)

    @property
    def abstract_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4272.AbstractAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4272,
        )

        return self.__parent__._cast(_4272.AbstractAssemblyCompoundPowerFlow)

    @property
    def part_compound_power_flow(self: "CastSelf") -> "_4353.PartCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4353,
        )

        return self.__parent__._cast(_4353.PartCompoundPowerFlow)

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
    def planetary_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4358.PlanetaryGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4358,
        )

        return self.__parent__._cast(_4358.PlanetaryGearSetCompoundPowerFlow)

    @property
    def cylindrical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "CylindricalGearSetCompoundPowerFlow":
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
class CylindricalGearSetCompoundPowerFlow(_4332.GearSetCompoundPowerFlow):
    """CylindricalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_SET_COMPOUND_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2582.CylindricalGearSet":
        """mastapy._private.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2582.CylindricalGearSet":
        """mastapy._private.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_duty_cycle_rating(
        self: "Self",
    ) -> "_474.CylindricalGearSetDutyCycleRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_duty_cycle_rating(
        self: "Self",
    ) -> "_474.CylindricalGearSetDutyCycleRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4185.CylindricalGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.CylindricalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gears_compound_power_flow(
        self: "Self",
    ) -> "List[_4319.CylindricalGearCompoundPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.compound.CylindricalGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_power_flow(
        self: "Self",
    ) -> "List[_4320.CylindricalGearMeshCompoundPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.compound.CylindricalGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ratings_for_all_designs(
        self: "Self",
    ) -> "List[_474.CylindricalGearSetDutyCycleRating]":
        """List[mastapy._private.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingsForAllDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_4185.CylindricalGearSetPowerFlow]":
        """List[mastapy._private.system_model.analyses_and_results.power_flows.CylindricalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearSetCompoundPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearSetCompoundPowerFlow
        """
        return _Cast_CylindricalGearSetCompoundPowerFlow(self)
