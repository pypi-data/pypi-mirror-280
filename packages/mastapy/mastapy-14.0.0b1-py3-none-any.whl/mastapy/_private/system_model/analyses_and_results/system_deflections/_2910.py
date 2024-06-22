"""SystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7709
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections", "SystemDeflection"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2912,
        _2860,
        _2917,
    )
    from mastapy._private.system_model.fe import _2461
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7428,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7715,
        _7700,
    )
    from mastapy._private.system_model.analyses_and_results import _2733

    Self = TypeVar("Self", bound="SystemDeflection")
    CastSelf = TypeVar("CastSelf", bound="SystemDeflection._Cast_SystemDeflection")


__docformat__ = "restructuredtext en"
__all__ = ("SystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SystemDeflection:
    """Special nested class for casting SystemDeflection to subclasses."""

    __parent__: "SystemDeflection"

    @property
    def fe_analysis(self: "CastSelf") -> "_7709.FEAnalysis":
        return self.__parent__._cast(_7709.FEAnalysis)

    @property
    def static_load_analysis_case(self: "CastSelf") -> "_7715.StaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7715,
        )

        return self.__parent__._cast(_7715.StaticLoadAnalysisCase)

    @property
    def analysis_case(self: "CastSelf") -> "_7700.AnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7700,
        )

        return self.__parent__._cast(_7700.AnalysisCase)

    @property
    def context(self: "CastSelf") -> "_2733.Context":
        from mastapy._private.system_model.analyses_and_results import _2733

        return self.__parent__._cast(_2733.Context)

    @property
    def torsional_system_deflection(
        self: "CastSelf",
    ) -> "_2917.TorsionalSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2917,
        )

        return self.__parent__._cast(_2917.TorsionalSystemDeflection)

    @property
    def advanced_system_deflection_sub_analysis(
        self: "CastSelf",
    ) -> "_7428.AdvancedSystemDeflectionSubAnalysis":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7428,
        )

        return self.__parent__._cast(_7428.AdvancedSystemDeflectionSubAnalysis)

    @property
    def system_deflection(self: "CastSelf") -> "SystemDeflection":
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
class SystemDeflection(_7709.FEAnalysis):
    """SystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def current_time(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.CurrentTime

        if temp is None:
            return 0.0

        return temp

    @current_time.setter
    @enforce_parameter_types
    def current_time(self: "Self", value: "float") -> None:
        self.wrapped.CurrentTime = float(value) if value is not None else 0.0

    @property
    def include_twist_in_misalignments(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeTwistInMisalignments

        if temp is None:
            return False

        return temp

    @include_twist_in_misalignments.setter
    @enforce_parameter_types
    def include_twist_in_misalignments(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeTwistInMisalignments = (
            bool(value) if value is not None else False
        )

    @property
    def iterations(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Iterations

        if temp is None:
            return 0

        return temp

    @property
    def largest_power_across_a_connection(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LargestPowerAcrossAConnection

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_circulating_power(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumCirculatingPower

        if temp is None:
            return 0.0

        return temp

    @property
    def power_convergence_error(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerConvergenceError

        if temp is None:
            return 0.0

        return temp

    @property
    def power_error(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerError

        if temp is None:
            return 0.0

        return temp

    @property
    def power_lost(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLost

        if temp is None:
            return 0.0

        return temp

    @property
    def total_input_power(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalInputPower

        if temp is None:
            return 0.0

        return temp

    @property
    def total_load_dependent_power_loss(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalLoadDependentPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def total_speed_dependent_power_loss(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalSpeedDependentPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def analysis_options(self: "Self") -> "_2912.SystemDeflectionOptions":
        """mastapy._private.system_model.analyses_and_results.system_deflections.SystemDeflectionOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def overall_efficiency_results(
        self: "Self",
    ) -> "_2860.LoadCaseOverallEfficiencyResult":
        """mastapy._private.system_model.analyses_and_results.system_deflections.LoadCaseOverallEfficiencyResult

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallEfficiencyResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_race_f_es(self: "Self") -> "List[_2461.RaceBearingFESystemDeflection]":
        """List[mastapy._private.system_model.fe.RaceBearingFESystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingRaceFEs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_SystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_SystemDeflection
        """
        return _Cast_SystemDeflection(self)
