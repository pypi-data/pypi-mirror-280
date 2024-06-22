"""ClutchConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _6998
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CLUTCH_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ClutchConnectionLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.math_utility import _1581
    from mastapy._private.system_model.connections_and_sockets.couplings import _2395
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7058,
        _6996,
    )
    from mastapy._private.system_model.analyses_and_results import _2732, _2736, _2734

    Self = TypeVar("Self", bound="ClutchConnectionLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ClutchConnectionLoadCase:
    """Special nested class for casting ClutchConnectionLoadCase to subclasses."""

    __parent__: "ClutchConnectionLoadCase"

    @property
    def coupling_connection_load_case(
        self: "CastSelf",
    ) -> "_6998.CouplingConnectionLoadCase":
        return self.__parent__._cast(_6998.CouplingConnectionLoadCase)

    @property
    def inter_mountable_component_connection_load_case(
        self: "CastSelf",
    ) -> "_7058.InterMountableComponentConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7058,
        )

        return self.__parent__._cast(_7058.InterMountableComponentConnectionLoadCase)

    @property
    def connection_load_case(self: "CastSelf") -> "_6996.ConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6996,
        )

        return self.__parent__._cast(_6996.ConnectionLoadCase)

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
    def clutch_connection_load_case(self: "CastSelf") -> "ClutchConnectionLoadCase":
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
class ClutchConnectionLoadCase(_6998.CouplingConnectionLoadCase):
    """ClutchConnectionLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CLUTCH_CONNECTION_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def clutch_initial_temperature(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ClutchInitialTemperature

        if temp is None:
            return 0.0

        return temp

    @clutch_initial_temperature.setter
    @enforce_parameter_types
    def clutch_initial_temperature(self: "Self", value: "float") -> None:
        self.wrapped.ClutchInitialTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def clutch_pressures(self: "Self") -> "_1581.Vector2DListAccessor":
        """mastapy._private.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ClutchPressures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @clutch_pressures.setter
    @enforce_parameter_types
    def clutch_pressures(self: "Self", value: "_1581.Vector2DListAccessor") -> None:
        self.wrapped.ClutchPressures = value.wrapped

    @property
    def is_initially_locked(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IsInitiallyLocked

        if temp is None:
            return False

        return temp

    @is_initially_locked.setter
    @enforce_parameter_types
    def is_initially_locked(self: "Self", value: "bool") -> None:
        self.wrapped.IsInitiallyLocked = bool(value) if value is not None else False

    @property
    def unlocked_clutch_linear_resistance_coefficient(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.UnlockedClutchLinearResistanceCoefficient

        if temp is None:
            return 0.0

        return temp

    @unlocked_clutch_linear_resistance_coefficient.setter
    @enforce_parameter_types
    def unlocked_clutch_linear_resistance_coefficient(
        self: "Self", value: "float"
    ) -> None:
        self.wrapped.UnlockedClutchLinearResistanceCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_fixed_update_time(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseFixedUpdateTime

        if temp is None:
            return False

        return temp

    @use_fixed_update_time.setter
    @enforce_parameter_types
    def use_fixed_update_time(self: "Self", value: "bool") -> None:
        self.wrapped.UseFixedUpdateTime = bool(value) if value is not None else False

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
    def cast_to(self: "Self") -> "_Cast_ClutchConnectionLoadCase":
        """Cast to another type.

        Returns:
            _Cast_ClutchConnectionLoadCase
        """
        return _Cast_ClutchConnectionLoadCase(self)
