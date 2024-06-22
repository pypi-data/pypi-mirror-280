"""CouplingConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6884,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6722,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6841,
        _6846,
        _6902,
        _6924,
        _6939,
        _6854,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="CouplingConnectionCompoundCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingConnectionCompoundCriticalSpeedAnalysis:
    """Special nested class for casting CouplingConnectionCompoundCriticalSpeedAnalysis to subclasses."""

    __parent__: "CouplingConnectionCompoundCriticalSpeedAnalysis"

    @property
    def inter_mountable_component_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6884.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
        return self.__parent__._cast(
            _6884.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6854.ConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6854,
        )

        return self.__parent__._cast(_6854.ConnectionCompoundCriticalSpeedAnalysis)

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.ConnectionCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7704,
        )

        return self.__parent__._cast(_7704.ConnectionCompoundAnalysis)

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
    def clutch_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6841.ClutchConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6841,
        )

        return self.__parent__._cast(
            _6841.ClutchConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def concept_coupling_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6846.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6846,
        )

        return self.__parent__._cast(
            _6846.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6902.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6902,
        )

        return self.__parent__._cast(
            _6902.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def spring_damper_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6924.SpringDamperConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6924,
        )

        return self.__parent__._cast(
            _6924.SpringDamperConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def torque_converter_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6939.TorqueConverterConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6939,
        )

        return self.__parent__._cast(
            _6939.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def coupling_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "CouplingConnectionCompoundCriticalSpeedAnalysis":
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
class CouplingConnectionCompoundCriticalSpeedAnalysis(
    _6884.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """CouplingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_6722.CouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.CouplingConnectionCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6722.CouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.CouplingConnectionCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_CouplingConnectionCompoundCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CouplingConnectionCompoundCriticalSpeedAnalysis
        """
        return _Cast_CouplingConnectionCompoundCriticalSpeedAnalysis(self)
