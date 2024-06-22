"""VirtualComponentCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _3016,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "VirtualComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2920,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _3012,
        _3013,
        _3025,
        _3026,
        _3061,
        _2961,
        _3018,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="VirtualComponentCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_VirtualComponentCompoundSystemDeflection:
    """Special nested class for casting VirtualComponentCompoundSystemDeflection to subclasses."""

    __parent__: "VirtualComponentCompoundSystemDeflection"

    @property
    def mountable_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3016.MountableComponentCompoundSystemDeflection":
        return self.__parent__._cast(_3016.MountableComponentCompoundSystemDeflection)

    @property
    def component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2961.ComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2961,
        )

        return self.__parent__._cast(_2961.ComponentCompoundSystemDeflection)

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3018.PartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3018,
        )

        return self.__parent__._cast(_3018.PartCompoundSystemDeflection)

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
    def mass_disc_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3012.MassDiscCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3012,
        )

        return self.__parent__._cast(_3012.MassDiscCompoundSystemDeflection)

    @property
    def measurement_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3013.MeasurementComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3013,
        )

        return self.__parent__._cast(_3013.MeasurementComponentCompoundSystemDeflection)

    @property
    def point_load_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3025.PointLoadCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3025,
        )

        return self.__parent__._cast(_3025.PointLoadCompoundSystemDeflection)

    @property
    def power_load_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3026.PowerLoadCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3026,
        )

        return self.__parent__._cast(_3026.PowerLoadCompoundSystemDeflection)

    @property
    def unbalanced_mass_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3061.UnbalancedMassCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3061,
        )

        return self.__parent__._cast(_3061.UnbalancedMassCompoundSystemDeflection)

    @property
    def virtual_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "VirtualComponentCompoundSystemDeflection":
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
class VirtualComponentCompoundSystemDeflection(
    _3016.MountableComponentCompoundSystemDeflection
):
    """VirtualComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _VIRTUAL_COMPONENT_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_2920.VirtualComponentSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection]

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
    ) -> "List[_2920.VirtualComponentSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_VirtualComponentCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_VirtualComponentCompoundSystemDeflection
        """
        return _Cast_VirtualComponentCompoundSystemDeflection(self)
