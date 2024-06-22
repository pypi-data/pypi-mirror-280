"""FEPartSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections import _2769
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FE_PART_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "FEPartSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2507
    from mastapy._private.system_model.analyses_and_results.static_loads import _7034
    from mastapy._private.nodal_analysis.component_mode_synthesis import _246
    from mastapy._private.nodal_analysis import _79
    from mastapy._private.system_model.analyses_and_results.power_flows import _4194
    from mastapy._private.math_utility.measured_vectors import _1610, _1606
    from mastapy._private.system_model.fe import _2464
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2798,
        _2870,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7712,
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="FEPartSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf", bound="FEPartSystemDeflection._Cast_FEPartSystemDeflection"
    )


__docformat__ = "restructuredtext en"
__all__ = ("FEPartSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FEPartSystemDeflection:
    """Special nested class for casting FEPartSystemDeflection to subclasses."""

    __parent__: "FEPartSystemDeflection"

    @property
    def abstract_shaft_or_housing_system_deflection(
        self: "CastSelf",
    ) -> "_2769.AbstractShaftOrHousingSystemDeflection":
        return self.__parent__._cast(_2769.AbstractShaftOrHousingSystemDeflection)

    @property
    def component_system_deflection(
        self: "CastSelf",
    ) -> "_2798.ComponentSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2798,
        )

        return self.__parent__._cast(_2798.ComponentSystemDeflection)

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
    def fe_part_system_deflection(self: "CastSelf") -> "FEPartSystemDeflection":
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
class FEPartSystemDeflection(_2769.AbstractShaftOrHousingSystemDeflection):
    """FEPartSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_PART_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2507.FEPart":
        """mastapy._private.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: "Self") -> "_7034.FEPartLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def full_fe_results(self: "Self") -> "_246.StaticCMSResults":
        """mastapy._private.nodal_analysis.component_mode_synthesis.StaticCMSResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullFEResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_in_world_coordinate_system_mn_rad_s_kg(self: "Self") -> "_79.NodalMatrix":
        """mastapy._private.nodal_analysis.NodalMatrix

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassInWorldCoordinateSystemMNRadSKg

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: "Self") -> "_4194.FEPartPowerFlow":
        """mastapy._private.system_model.analyses_and_results.power_flows.FEPartPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_in_world_coordinate_system_mn_rad(self: "Self") -> "_79.NodalMatrix":
        """mastapy._private.nodal_analysis.NodalMatrix

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessInWorldCoordinateSystemMNRad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def applied_internal_forces_in_world_coordinate_system(
        self: "Self",
    ) -> "List[_1610.VectorWithLinearAndAngularComponents]":
        """List[mastapy._private.math_utility.measured_vectors.VectorWithLinearAndAngularComponents]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AppliedInternalForcesInWorldCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def node_results_in_shaft_coordinate_system(
        self: "Self",
    ) -> "List[_1606.ForceAndDisplacementResults]":
        """List[mastapy._private.math_utility.measured_vectors.ForceAndDisplacementResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeResultsInShaftCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: "Self") -> "List[FEPartSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection]

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
    def export(self: "Self") -> "_2464.SystemDeflectionFEExportOptions":
        """mastapy._private.system_model.fe.SystemDeflectionFEExportOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def export_displacements(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ExportDisplacements()

    def export_forces(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ExportForces()

    @property
    def cast_to(self: "Self") -> "_Cast_FEPartSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_FEPartSystemDeflection
        """
        return _Cast_FEPartSystemDeflection(self)
