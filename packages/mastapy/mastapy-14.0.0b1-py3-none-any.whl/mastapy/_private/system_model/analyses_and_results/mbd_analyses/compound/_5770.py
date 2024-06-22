"""StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
    _5764,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5629
    from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
        _5673,
        _5661,
        _5689,
        _5715,
        _5736,
        _5682,
        _5738,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar(
        "Self", bound="StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis:
    """Special nested class for casting StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis"

    @property
    def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5764.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
        return self.__parent__._cast(
            _5764.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5673.BevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5673,
        )

        return self.__parent__._cast(_5673.BevelGearCompoundMultibodyDynamicsAnalysis)

    @property
    def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5661.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5661,
        )

        return self.__parent__._cast(
            _5661.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5689.ConicalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5689,
        )

        return self.__parent__._cast(_5689.ConicalGearCompoundMultibodyDynamicsAnalysis)

    @property
    def gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5715.GearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5715,
        )

        return self.__parent__._cast(_5715.GearCompoundMultibodyDynamicsAnalysis)

    @property
    def mountable_component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5736.MountableComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5736,
        )

        return self.__parent__._cast(
            _5736.MountableComponentCompoundMultibodyDynamicsAnalysis
        )

    @property
    def component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5682.ComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5682,
        )

        return self.__parent__._cast(_5682.ComponentCompoundMultibodyDynamicsAnalysis)

    @property
    def part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5738.PartCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5738,
        )

        return self.__parent__._cast(_5738.PartCompoundMultibodyDynamicsAnalysis)

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
    def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
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
class StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis(
    _5764.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
):
    """StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar[
        "Type"
    ] = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_5629.StraightBevelPlanetGearMultibodyDynamicsAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelPlanetGearMultibodyDynamicsAnalysis]

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
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_5629.StraightBevelPlanetGearMultibodyDynamicsAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.mbd_analyses.StraightBevelPlanetGearMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
        """
        return _Cast_StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis(self)
