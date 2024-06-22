"""UnbalancedMassCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
    _4122,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "UnbalancedMassCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2533
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3990,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
        _4077,
        _4023,
        _4079,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="UnbalancedMassCompoundStabilityAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="UnbalancedMassCompoundStabilityAnalysis._Cast_UnbalancedMassCompoundStabilityAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundStabilityAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_UnbalancedMassCompoundStabilityAnalysis:
    """Special nested class for casting UnbalancedMassCompoundStabilityAnalysis to subclasses."""

    __parent__: "UnbalancedMassCompoundStabilityAnalysis"

    @property
    def virtual_component_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4122.VirtualComponentCompoundStabilityAnalysis":
        return self.__parent__._cast(_4122.VirtualComponentCompoundStabilityAnalysis)

    @property
    def mountable_component_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4077.MountableComponentCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4077,
        )

        return self.__parent__._cast(_4077.MountableComponentCompoundStabilityAnalysis)

    @property
    def component_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4023.ComponentCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4023,
        )

        return self.__parent__._cast(_4023.ComponentCompoundStabilityAnalysis)

    @property
    def part_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4079.PartCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4079,
        )

        return self.__parent__._cast(_4079.PartCompoundStabilityAnalysis)

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
    def unbalanced_mass_compound_stability_analysis(
        self: "CastSelf",
    ) -> "UnbalancedMassCompoundStabilityAnalysis":
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
class UnbalancedMassCompoundStabilityAnalysis(
    _4122.VirtualComponentCompoundStabilityAnalysis
):
    """UnbalancedMassCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _UNBALANCED_MASS_COMPOUND_STABILITY_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2533.UnbalancedMass":
        """mastapy._private.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3990.UnbalancedMassStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.UnbalancedMassStabilityAnalysis]

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
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3990.UnbalancedMassStabilityAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.stability_analyses.UnbalancedMassStabilityAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_UnbalancedMassCompoundStabilityAnalysis":
        """Cast to another type.

        Returns:
            _Cast_UnbalancedMassCompoundStabilityAnalysis
        """
        return _Cast_UnbalancedMassCompoundStabilityAnalysis(self)
