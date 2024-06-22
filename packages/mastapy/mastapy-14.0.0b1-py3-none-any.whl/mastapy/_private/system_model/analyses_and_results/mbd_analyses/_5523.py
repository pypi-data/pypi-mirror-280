"""ClutchConnectionMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5540
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CLUTCH_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ClutchConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets.couplings import _2395
    from mastapy._private.system_model.analyses_and_results.static_loads import _6979
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
        _5573,
        _5538,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7707,
        _7703,
    )
    from mastapy._private.system_model.analyses_and_results import _2732, _2736, _2734

    Self = TypeVar("Self", bound="ClutchConnectionMultibodyDynamicsAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ClutchConnectionMultibodyDynamicsAnalysis:
    """Special nested class for casting ClutchConnectionMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "ClutchConnectionMultibodyDynamicsAnalysis"

    @property
    def coupling_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5540.CouplingConnectionMultibodyDynamicsAnalysis":
        return self.__parent__._cast(_5540.CouplingConnectionMultibodyDynamicsAnalysis)

    @property
    def inter_mountable_component_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5573.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5573,
        )

        return self.__parent__._cast(
            _5573.InterMountableComponentConnectionMultibodyDynamicsAnalysis
        )

    @property
    def connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5538.ConnectionMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5538,
        )

        return self.__parent__._cast(_5538.ConnectionMultibodyDynamicsAnalysis)

    @property
    def connection_time_series_load_analysis_case(
        self: "CastSelf",
    ) -> "_7707.ConnectionTimeSeriesLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7707,
        )

        return self.__parent__._cast(_7707.ConnectionTimeSeriesLoadAnalysisCase)

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
    def clutch_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "ClutchConnectionMultibodyDynamicsAnalysis":
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
class ClutchConnectionMultibodyDynamicsAnalysis(
    _5540.CouplingConnectionMultibodyDynamicsAnalysis
):
    """ClutchConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CLUTCH_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def applied_clutch_pressure_at_clutch_plate(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AppliedClutchPressureAtClutchPlate

        if temp is None:
            return 0.0

        return temp

    @applied_clutch_pressure_at_clutch_plate.setter
    @enforce_parameter_types
    def applied_clutch_pressure_at_clutch_plate(self: "Self", value: "float") -> None:
        self.wrapped.AppliedClutchPressureAtClutchPlate = (
            float(value) if value is not None else 0.0
        )

    @property
    def applied_clutch_pressure_at_piston(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AppliedClutchPressureAtPiston

        if temp is None:
            return 0.0

        return temp

    @applied_clutch_pressure_at_piston.setter
    @enforce_parameter_types
    def applied_clutch_pressure_at_piston(self: "Self", value: "float") -> None:
        self.wrapped.AppliedClutchPressureAtPiston = (
            float(value) if value is not None else 0.0
        )

    @property
    def clutch_connection_elastic_torque(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnectionElasticTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_connection_viscous_torque(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnectionViscousTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_plate_dynamic_temperature(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchPlateDynamicTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_torque_capacity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchTorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_clutch_torque_capacity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcessClutchTorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @property
    def is_locked(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLocked

        if temp is None:
            return False

        return temp

    @property
    def percentage_applied_pressure(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PercentageAppliedPressure

        if temp is None:
            return 0.0

        return temp

    @percentage_applied_pressure.setter
    @enforce_parameter_types
    def percentage_applied_pressure(self: "Self", value: "float") -> None:
        self.wrapped.PercentageAppliedPressure = (
            float(value) if value is not None else 0.0
        )

    @property
    def power_loss(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_shaft_displacement(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeShaftDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_shaft_speed(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeShaftSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: "Self") -> "_2395.ClutchConnection":
        """mastapy._private.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: "Self") -> "_6979.ClutchConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ClutchConnectionMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ClutchConnectionMultibodyDynamicsAnalysis
        """
        return _Cast_ClutchConnectionMultibodyDynamicsAnalysis(self)
