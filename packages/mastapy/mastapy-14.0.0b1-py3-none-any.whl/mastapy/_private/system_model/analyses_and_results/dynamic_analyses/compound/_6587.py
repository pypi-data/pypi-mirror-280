"""CouplingHalfCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
    _6627,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CouplingHalfCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6454,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6571,
        _6576,
        _6590,
        _6632,
        _6638,
        _6642,
        _6654,
        _6664,
        _6665,
        _6666,
        _6669,
        _6670,
        _6573,
        _6629,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CouplingHalfCompoundDynamicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundDynamicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfCompoundDynamicAnalysis:
    """Special nested class for casting CouplingHalfCompoundDynamicAnalysis to subclasses."""

    __parent__: "CouplingHalfCompoundDynamicAnalysis"

    @property
    def mountable_component_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6627.MountableComponentCompoundDynamicAnalysis":
        return self.__parent__._cast(_6627.MountableComponentCompoundDynamicAnalysis)

    @property
    def component_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6573.ComponentCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6573,
        )

        return self.__parent__._cast(_6573.ComponentCompoundDynamicAnalysis)

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
    def clutch_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6571.ClutchHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6571,
        )

        return self.__parent__._cast(_6571.ClutchHalfCompoundDynamicAnalysis)

    @property
    def concept_coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6576.ConceptCouplingHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6576,
        )

        return self.__parent__._cast(_6576.ConceptCouplingHalfCompoundDynamicAnalysis)

    @property
    def cvt_pulley_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6590.CVTPulleyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6590,
        )

        return self.__parent__._cast(_6590.CVTPulleyCompoundDynamicAnalysis)

    @property
    def part_to_part_shear_coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6632.PartToPartShearCouplingHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6632,
        )

        return self.__parent__._cast(
            _6632.PartToPartShearCouplingHalfCompoundDynamicAnalysis
        )

    @property
    def pulley_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6638.PulleyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6638,
        )

        return self.__parent__._cast(_6638.PulleyCompoundDynamicAnalysis)

    @property
    def rolling_ring_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6642.RollingRingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6642,
        )

        return self.__parent__._cast(_6642.RollingRingCompoundDynamicAnalysis)

    @property
    def spring_damper_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6654.SpringDamperHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6654,
        )

        return self.__parent__._cast(_6654.SpringDamperHalfCompoundDynamicAnalysis)

    @property
    def synchroniser_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6664.SynchroniserHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6664,
        )

        return self.__parent__._cast(_6664.SynchroniserHalfCompoundDynamicAnalysis)

    @property
    def synchroniser_part_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6665.SynchroniserPartCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6665,
        )

        return self.__parent__._cast(_6665.SynchroniserPartCompoundDynamicAnalysis)

    @property
    def synchroniser_sleeve_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6666.SynchroniserSleeveCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6666,
        )

        return self.__parent__._cast(_6666.SynchroniserSleeveCompoundDynamicAnalysis)

    @property
    def torque_converter_pump_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6669.TorqueConverterPumpCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6669,
        )

        return self.__parent__._cast(_6669.TorqueConverterPumpCompoundDynamicAnalysis)

    @property
    def torque_converter_turbine_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6670.TorqueConverterTurbineCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6670,
        )

        return self.__parent__._cast(
            _6670.TorqueConverterTurbineCompoundDynamicAnalysis
        )

    @property
    def coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "CouplingHalfCompoundDynamicAnalysis":
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
class CouplingHalfCompoundDynamicAnalysis(
    _6627.MountableComponentCompoundDynamicAnalysis
):
    """CouplingHalfCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_6454.CouplingHalfDynamicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis]

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
    ) -> "List[_6454.CouplingHalfDynamicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_CouplingHalfCompoundDynamicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfCompoundDynamicAnalysis
        """
        return _Cast_CouplingHalfCompoundDynamicAnalysis(self)
