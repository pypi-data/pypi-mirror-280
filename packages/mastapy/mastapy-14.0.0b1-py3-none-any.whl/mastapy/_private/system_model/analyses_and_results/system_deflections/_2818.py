"""CycloidalAssemblySystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections import _2891
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CycloidalAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.cycloidal import _2624
    from mastapy._private.system_model.analyses_and_results.static_loads import _7004
    from mastapy._private.system_model.analyses_and_results.power_flows import _4178
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2880,
        _2768,
        _2870,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7712,
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="CycloidalAssemblySystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblySystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CycloidalAssemblySystemDeflection:
    """Special nested class for casting CycloidalAssemblySystemDeflection to subclasses."""

    __parent__: "CycloidalAssemblySystemDeflection"

    @property
    def specialised_assembly_system_deflection(
        self: "CastSelf",
    ) -> "_2891.SpecialisedAssemblySystemDeflection":
        return self.__parent__._cast(_2891.SpecialisedAssemblySystemDeflection)

    @property
    def abstract_assembly_system_deflection(
        self: "CastSelf",
    ) -> "_2768.AbstractAssemblySystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2768,
        )

        return self.__parent__._cast(_2768.AbstractAssemblySystemDeflection)

    @property
    def part_system_deflection(self: "CastSelf") -> "_2870.PartSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2870,
        )

        return self.__parent__._cast(_2870.PartSystemDeflection)

    @property
    def part_fe_analysis(self: "CastSelf") -> "_7712.PartFEAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7712,
        )

        return self.__parent__._cast(_7712.PartFEAnalysis)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7713.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7713,
        )

        return self.__parent__._cast(_7713.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7710.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def cycloidal_assembly_system_deflection(
        self: "CastSelf",
    ) -> "CycloidalAssemblySystemDeflection":
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
class CycloidalAssemblySystemDeflection(_2891.SpecialisedAssemblySystemDeflection):
    """CycloidalAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYCLOIDAL_ASSEMBLY_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2624.CycloidalAssembly":
        """mastapy._private.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_7004.CycloidalAssemblyLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: "Self") -> "_4178.CycloidalAssemblyPowerFlow":
        """mastapy._private.system_model.analyses_and_results.power_flows.CycloidalAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_pins_to_disc_connections(
        self: "Self",
    ) -> "List[_2880.RingPinsToDiscConnectionSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.RingPinsToDiscConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPinsToDiscConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CycloidalAssemblySystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_CycloidalAssemblySystemDeflection
        """
        return _Cast_CycloidalAssemblySystemDeflection(self)
