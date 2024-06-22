"""ContourDrawStyle"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.geometry import _318
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONTOUR_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "ContourDrawStyle"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.enums import _1871
    from mastapy._private.utility_gui import _1903
    from mastapy._private.system_model.drawing import _2305
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2911,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3179,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3972,
    )
    from mastapy._private.system_model.analyses_and_results.rotor_dynamics import _4129
    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4769
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5584
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5892,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6468,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6726,
    )

    Self = TypeVar("Self", bound="ContourDrawStyle")
    CastSelf = TypeVar("CastSelf", bound="ContourDrawStyle._Cast_ContourDrawStyle")


__docformat__ = "restructuredtext en"
__all__ = ("ContourDrawStyle",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ContourDrawStyle:
    """Special nested class for casting ContourDrawStyle to subclasses."""

    __parent__: "ContourDrawStyle"

    @property
    def draw_style_base(self: "CastSelf") -> "_318.DrawStyleBase":
        return self.__parent__._cast(_318.DrawStyleBase)

    @property
    def system_deflection_draw_style(
        self: "CastSelf",
    ) -> "_2911.SystemDeflectionDrawStyle":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2911,
        )

        return self.__parent__._cast(_2911.SystemDeflectionDrawStyle)

    @property
    def steady_state_synchronous_response_draw_style(
        self: "CastSelf",
    ) -> "_3179.SteadyStateSynchronousResponseDrawStyle":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3179,
        )

        return self.__parent__._cast(_3179.SteadyStateSynchronousResponseDrawStyle)

    @property
    def stability_analysis_draw_style(
        self: "CastSelf",
    ) -> "_3972.StabilityAnalysisDrawStyle":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3972,
        )

        return self.__parent__._cast(_3972.StabilityAnalysisDrawStyle)

    @property
    def rotor_dynamics_draw_style(self: "CastSelf") -> "_4129.RotorDynamicsDrawStyle":
        from mastapy._private.system_model.analyses_and_results.rotor_dynamics import (
            _4129,
        )

        return self.__parent__._cast(_4129.RotorDynamicsDrawStyle)

    @property
    def modal_analysis_draw_style(self: "CastSelf") -> "_4769.ModalAnalysisDrawStyle":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4769,
        )

        return self.__parent__._cast(_4769.ModalAnalysisDrawStyle)

    @property
    def mbd_analysis_draw_style(self: "CastSelf") -> "_5584.MBDAnalysisDrawStyle":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5584,
        )

        return self.__parent__._cast(_5584.MBDAnalysisDrawStyle)

    @property
    def harmonic_analysis_draw_style(
        self: "CastSelf",
    ) -> "_5892.HarmonicAnalysisDrawStyle":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5892,
        )

        return self.__parent__._cast(_5892.HarmonicAnalysisDrawStyle)

    @property
    def dynamic_analysis_draw_style(
        self: "CastSelf",
    ) -> "_6468.DynamicAnalysisDrawStyle":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
            _6468,
        )

        return self.__parent__._cast(_6468.DynamicAnalysisDrawStyle)

    @property
    def critical_speed_analysis_draw_style(
        self: "CastSelf",
    ) -> "_6726.CriticalSpeedAnalysisDrawStyle":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6726,
        )

        return self.__parent__._cast(_6726.CriticalSpeedAnalysisDrawStyle)

    @property
    def contour_draw_style(self: "CastSelf") -> "ContourDrawStyle":
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
class ContourDrawStyle(_318.DrawStyleBase):
    """ContourDrawStyle

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONTOUR_DRAW_STYLE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def contour(self: "Self") -> "_1871.ThreeDViewContourOption":
        """mastapy._private.utility.enums.ThreeDViewContourOption"""
        temp = self.wrapped.Contour

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Enums.ThreeDViewContourOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.utility.enums._1871", "ThreeDViewContourOption"
        )(value)

    @contour.setter
    @enforce_parameter_types
    def contour(self: "Self", value: "_1871.ThreeDViewContourOption") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Enums.ThreeDViewContourOption"
        )
        self.wrapped.Contour = value

    @property
    def minimum_peak_value_displacement(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumPeakValueDisplacement

        if temp is None:
            return 0.0

        return temp

    @minimum_peak_value_displacement.setter
    @enforce_parameter_types
    def minimum_peak_value_displacement(self: "Self", value: "float") -> None:
        self.wrapped.MinimumPeakValueDisplacement = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_peak_value_stress(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumPeakValueStress

        if temp is None:
            return 0.0

        return temp

    @minimum_peak_value_stress.setter
    @enforce_parameter_types
    def minimum_peak_value_stress(self: "Self", value: "float") -> None:
        self.wrapped.MinimumPeakValueStress = float(value) if value is not None else 0.0

    @property
    def show_local_maxima(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ShowLocalMaxima

        if temp is None:
            return False

        return temp

    @show_local_maxima.setter
    @enforce_parameter_types
    def show_local_maxima(self: "Self", value: "bool") -> None:
        self.wrapped.ShowLocalMaxima = bool(value) if value is not None else False

    @property
    def deflection_scaling(self: "Self") -> "_1903.ScalingDrawStyle":
        """mastapy._private.utility_gui.ScalingDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeflectionScaling

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def model_view_options(self: "Self") -> "_2305.ModelViewOptionsDrawStyle":
        """mastapy._private.system_model.drawing.ModelViewOptionsDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModelViewOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ContourDrawStyle":
        """Cast to another type.

        Returns:
            _Cast_ContourDrawStyle
        """
        return _Cast_ContourDrawStyle(self)
