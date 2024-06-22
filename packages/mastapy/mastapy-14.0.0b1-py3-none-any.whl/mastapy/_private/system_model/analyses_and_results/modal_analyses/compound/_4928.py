"""PlanetCarrierCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
    _4920,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "PlanetCarrierCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model import _2525
    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4781
    from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
        _4866,
        _4922,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="PlanetCarrierCompoundModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PlanetCarrierCompoundModalAnalysis._Cast_PlanetCarrierCompoundModalAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCompoundModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PlanetCarrierCompoundModalAnalysis:
    """Special nested class for casting PlanetCarrierCompoundModalAnalysis to subclasses."""

    __parent__: "PlanetCarrierCompoundModalAnalysis"

    @property
    def mountable_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4920.MountableComponentCompoundModalAnalysis":
        return self.__parent__._cast(_4920.MountableComponentCompoundModalAnalysis)

    @property
    def component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4866.ComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4866,
        )

        return self.__parent__._cast(_4866.ComponentCompoundModalAnalysis)

    @property
    def part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4922.PartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4922,
        )

        return self.__parent__._cast(_4922.PartCompoundModalAnalysis)

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
    def planet_carrier_compound_modal_analysis(
        self: "CastSelf",
    ) -> "PlanetCarrierCompoundModalAnalysis":
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
class PlanetCarrierCompoundModalAnalysis(_4920.MountableComponentCompoundModalAnalysis):
    """PlanetCarrierCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PLANET_CARRIER_COMPOUND_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2525.PlanetCarrier":
        """mastapy._private.system_model.part_model.PlanetCarrier

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
    ) -> "List[_4781.PlanetCarrierModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.PlanetCarrierModalAnalysis]

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
    ) -> "List[_4781.PlanetCarrierModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.PlanetCarrierModalAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_PlanetCarrierCompoundModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_PlanetCarrierCompoundModalAnalysis
        """
        return _Cast_PlanetCarrierCompoundModalAnalysis(self)
