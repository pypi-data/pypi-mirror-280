"""SpecialisedAssemblyCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6819,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6788,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6825,
        _6829,
        _6832,
        _6837,
        _6839,
        _6840,
        _6845,
        _6850,
        _6853,
        _6856,
        _6860,
        _6862,
        _6868,
        _6874,
        _6876,
        _6879,
        _6883,
        _6887,
        _6890,
        _6893,
        _6896,
        _6901,
        _6905,
        _6912,
        _6922,
        _6923,
        _6928,
        _6931,
        _6934,
        _6938,
        _6946,
        _6949,
        _6900,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis:
    """Special nested class for casting SpecialisedAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

    __parent__: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis"

    @property
    def abstract_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6819.AbstractAssemblyCompoundCriticalSpeedAnalysis":
        return self.__parent__._cast(
            _6819.AbstractAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6900.PartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6900,
        )

        return self.__parent__._cast(_6900.PartCompoundCriticalSpeedAnalysis)

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
    def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6825.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6825,
        )

        return self.__parent__._cast(
            _6825.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def belt_drive_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6829.BeltDriveCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6829,
        )

        return self.__parent__._cast(_6829.BeltDriveCompoundCriticalSpeedAnalysis)

    @property
    def bevel_differential_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6832.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6832,
        )

        return self.__parent__._cast(
            _6832.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6837.BevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6837,
        )

        return self.__parent__._cast(_6837.BevelGearSetCompoundCriticalSpeedAnalysis)

    @property
    def bolted_joint_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6839.BoltedJointCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6839,
        )

        return self.__parent__._cast(_6839.BoltedJointCompoundCriticalSpeedAnalysis)

    @property
    def clutch_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6840.ClutchCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6840,
        )

        return self.__parent__._cast(_6840.ClutchCompoundCriticalSpeedAnalysis)

    @property
    def concept_coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6845.ConceptCouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6845,
        )

        return self.__parent__._cast(_6845.ConceptCouplingCompoundCriticalSpeedAnalysis)

    @property
    def concept_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6850.ConceptGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6850,
        )

        return self.__parent__._cast(_6850.ConceptGearSetCompoundCriticalSpeedAnalysis)

    @property
    def conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6853.ConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6853,
        )

        return self.__parent__._cast(_6853.ConicalGearSetCompoundCriticalSpeedAnalysis)

    @property
    def coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6856.CouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6856,
        )

        return self.__parent__._cast(_6856.CouplingCompoundCriticalSpeedAnalysis)

    @property
    def cvt_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6860.CVTCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6860,
        )

        return self.__parent__._cast(_6860.CVTCompoundCriticalSpeedAnalysis)

    @property
    def cycloidal_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6862.CycloidalAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6862,
        )

        return self.__parent__._cast(
            _6862.CycloidalAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def cylindrical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6868.CylindricalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6868,
        )

        return self.__parent__._cast(
            _6868.CylindricalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def face_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6874.FaceGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6874,
        )

        return self.__parent__._cast(_6874.FaceGearSetCompoundCriticalSpeedAnalysis)

    @property
    def flexible_pin_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6876.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6876,
        )

        return self.__parent__._cast(
            _6876.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6879.GearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6879,
        )

        return self.__parent__._cast(_6879.GearSetCompoundCriticalSpeedAnalysis)

    @property
    def hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6883.HypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6883,
        )

        return self.__parent__._cast(_6883.HypoidGearSetCompoundCriticalSpeedAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6887.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6887,
        )

        return self.__parent__._cast(
            _6887.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6890.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6890,
        )

        return self.__parent__._cast(
            _6890.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> (
        "_6893.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6893,
        )

        return self.__parent__._cast(
            _6893.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def microphone_array_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6896.MicrophoneArrayCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6896,
        )

        return self.__parent__._cast(_6896.MicrophoneArrayCompoundCriticalSpeedAnalysis)

    @property
    def part_to_part_shear_coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6901.PartToPartShearCouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6901,
        )

        return self.__parent__._cast(
            _6901.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
        )

    @property
    def planetary_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6905.PlanetaryGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6905,
        )

        return self.__parent__._cast(
            _6905.PlanetaryGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def rolling_ring_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6912.RollingRingAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6912,
        )

        return self.__parent__._cast(
            _6912.RollingRingAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def spiral_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6922.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6922,
        )

        return self.__parent__._cast(
            _6922.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def spring_damper_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6923.SpringDamperCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6923,
        )

        return self.__parent__._cast(_6923.SpringDamperCompoundCriticalSpeedAnalysis)

    @property
    def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6928.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6928,
        )

        return self.__parent__._cast(
            _6928.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6931.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6931,
        )

        return self.__parent__._cast(
            _6931.StraightBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6934.SynchroniserCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6934,
        )

        return self.__parent__._cast(_6934.SynchroniserCompoundCriticalSpeedAnalysis)

    @property
    def torque_converter_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6938.TorqueConverterCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6938,
        )

        return self.__parent__._cast(_6938.TorqueConverterCompoundCriticalSpeedAnalysis)

    @property
    def worm_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6946.WormGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6946,
        )

        return self.__parent__._cast(_6946.WormGearSetCompoundCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6949.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6949,
        )

        return self.__parent__._cast(
            _6949.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def specialised_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
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
class SpecialisedAssemblyCompoundCriticalSpeedAnalysis(
    _6819.AbstractAssemblyCompoundCriticalSpeedAnalysis
):
    """SpecialisedAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPECIALISED_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_6788.SpecialisedAssemblyCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.SpecialisedAssemblyCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6788.SpecialisedAssemblyCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.SpecialisedAssemblyCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis
        """
        return _Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis(self)
