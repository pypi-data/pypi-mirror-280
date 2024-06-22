"""CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7225,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets.couplings import _2399
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2812,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7181,
        _7186,
        _7243,
        _7265,
        _7280,
        _7194,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7703,
    )
    from mastapy._private.system_model.analyses_and_results import _2732, _2736, _2734

    Self = TypeVar(
        "Self", bound="CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation:
    """Special nested class for casting CouplingConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

    __parent__: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"

    @property
    def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7225.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self.__parent__._cast(
            _7225.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7194.ConnectionAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7194,
        )

        return self.__parent__._cast(
            _7194.ConnectionAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def connection_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7706.ConnectionStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7706,
        )

        return self.__parent__._cast(_7706.ConnectionStaticLoadAnalysisCase)

    @property
    def connection_analysis_case(self: "CastSelf") -> "_7703.ConnectionAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7703,
        )

        return self.__parent__._cast(_7703.ConnectionAnalysisCase)

    @property
    def connection_analysis(self: "CastSelf") -> "_2732.ConnectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2732

        return self.__parent__._cast(_2732.ConnectionAnalysis)

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
    def clutch_connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7181.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7181,
        )

        return self.__parent__._cast(
            _7181.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7186.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7186,
        )

        return self.__parent__._cast(
            _7186.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7243.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7243,
        )

        return self.__parent__._cast(
            _7243.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7265.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7265,
        )

        return self.__parent__._cast(
            _7265.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7280.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7280,
        )

        return self.__parent__._cast(
            _7280.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def coupling_connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
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
class CouplingConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7225.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """CouplingConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _COUPLING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2399.CouplingConnection":
        """mastapy._private.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: "Self",
    ) -> "_2812.CouplingConnectionSystemDeflection":
        """mastapy._private.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
        """Cast to another type.

        Returns:
            _Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
        """
        return _Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation(self)
