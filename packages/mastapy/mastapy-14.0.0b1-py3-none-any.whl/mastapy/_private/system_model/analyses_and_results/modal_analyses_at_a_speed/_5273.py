"""CouplingConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
    _5301,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets.couplings import _2399
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5257,
        _5262,
        _5319,
        _5341,
        _5356,
        _5271,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7703,
    )
    from mastapy._private.system_model.analyses_and_results import _2732, _2736, _2734

    Self = TypeVar("Self", bound="CouplingConnectionModalAnalysisAtASpeed")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionModalAnalysisAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingConnectionModalAnalysisAtASpeed:
    """Special nested class for casting CouplingConnectionModalAnalysisAtASpeed to subclasses."""

    __parent__: "CouplingConnectionModalAnalysisAtASpeed"

    @property
    def inter_mountable_component_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5301.InterMountableComponentConnectionModalAnalysisAtASpeed":
        return self.__parent__._cast(
            _5301.InterMountableComponentConnectionModalAnalysisAtASpeed
        )

    @property
    def connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5271.ConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5271,
        )

        return self.__parent__._cast(_5271.ConnectionModalAnalysisAtASpeed)

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
    def clutch_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5257.ClutchConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5257,
        )

        return self.__parent__._cast(_5257.ClutchConnectionModalAnalysisAtASpeed)

    @property
    def concept_coupling_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5262.ConceptCouplingConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5262,
        )

        return self.__parent__._cast(
            _5262.ConceptCouplingConnectionModalAnalysisAtASpeed
        )

    @property
    def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5319.PartToPartShearCouplingConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5319,
        )

        return self.__parent__._cast(
            _5319.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
        )

    @property
    def spring_damper_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5341.SpringDamperConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5341,
        )

        return self.__parent__._cast(_5341.SpringDamperConnectionModalAnalysisAtASpeed)

    @property
    def torque_converter_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5356.TorqueConverterConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5356,
        )

        return self.__parent__._cast(
            _5356.TorqueConverterConnectionModalAnalysisAtASpeed
        )

    @property
    def coupling_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "CouplingConnectionModalAnalysisAtASpeed":
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
class CouplingConnectionModalAnalysisAtASpeed(
    _5301.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """CouplingConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED

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
    def cast_to(self: "Self") -> "_Cast_CouplingConnectionModalAnalysisAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_CouplingConnectionModalAnalysisAtASpeed
        """
        return _Cast_CouplingConnectionModalAnalysisAtASpeed(self)
