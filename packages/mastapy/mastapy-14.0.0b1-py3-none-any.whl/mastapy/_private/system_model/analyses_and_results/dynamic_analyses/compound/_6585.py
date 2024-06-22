"""CouplingCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
    _6648,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CouplingCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6453,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6569,
        _6574,
        _6630,
        _6652,
        _6667,
        _6548,
        _6629,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CouplingCompoundDynamicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingCompoundDynamicAnalysis._Cast_CouplingCompoundDynamicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundDynamicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingCompoundDynamicAnalysis:
    """Special nested class for casting CouplingCompoundDynamicAnalysis to subclasses."""

    __parent__: "CouplingCompoundDynamicAnalysis"

    @property
    def specialised_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6648.SpecialisedAssemblyCompoundDynamicAnalysis":
        return self.__parent__._cast(_6648.SpecialisedAssemblyCompoundDynamicAnalysis)

    @property
    def abstract_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6548.AbstractAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6548,
        )

        return self.__parent__._cast(_6548.AbstractAssemblyCompoundDynamicAnalysis)

    @property
    def part_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6629.PartCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6629,
        )

        return self.__parent__._cast(_6629.PartCompoundDynamicAnalysis)

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
    def clutch_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6569.ClutchCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6569,
        )

        return self.__parent__._cast(_6569.ClutchCompoundDynamicAnalysis)

    @property
    def concept_coupling_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6574.ConceptCouplingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6574,
        )

        return self.__parent__._cast(_6574.ConceptCouplingCompoundDynamicAnalysis)

    @property
    def part_to_part_shear_coupling_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6630.PartToPartShearCouplingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6630,
        )

        return self.__parent__._cast(
            _6630.PartToPartShearCouplingCompoundDynamicAnalysis
        )

    @property
    def spring_damper_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6652.SpringDamperCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6652,
        )

        return self.__parent__._cast(_6652.SpringDamperCompoundDynamicAnalysis)

    @property
    def torque_converter_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6667.TorqueConverterCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6667,
        )

        return self.__parent__._cast(_6667.TorqueConverterCompoundDynamicAnalysis)

    @property
    def coupling_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "CouplingCompoundDynamicAnalysis":
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
class CouplingCompoundDynamicAnalysis(_6648.SpecialisedAssemblyCompoundDynamicAnalysis):
    """CouplingCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_COMPOUND_DYNAMIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(self: "Self") -> "List[_6453.CouplingDynamicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.dynamic_analyses.CouplingDynamicAnalysis]

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
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6453.CouplingDynamicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.dynamic_analyses.CouplingDynamicAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_CouplingCompoundDynamicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CouplingCompoundDynamicAnalysis
        """
        return _Cast_CouplingCompoundDynamicAnalysis(self)
