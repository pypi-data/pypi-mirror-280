"""AbstractAssemblyCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
    _6092,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AbstractAssemblyCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5808,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
        _6017,
        _6018,
        _6021,
        _6024,
        _6029,
        _6031,
        _6032,
        _6037,
        _6042,
        _6045,
        _6048,
        _6052,
        _6054,
        _6060,
        _6066,
        _6068,
        _6071,
        _6075,
        _6079,
        _6082,
        _6085,
        _6088,
        _6093,
        _6097,
        _6104,
        _6107,
        _6111,
        _6114,
        _6115,
        _6120,
        _6123,
        _6126,
        _6130,
        _6138,
        _6141,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="AbstractAssemblyCompoundHarmonicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundHarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractAssemblyCompoundHarmonicAnalysis:
    """Special nested class for casting AbstractAssemblyCompoundHarmonicAnalysis to subclasses."""

    __parent__: "AbstractAssemblyCompoundHarmonicAnalysis"

    @property
    def part_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6092.PartCompoundHarmonicAnalysis":
        return self.__parent__._cast(_6092.PartCompoundHarmonicAnalysis)

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
    def agma_gleason_conical_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6017.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6017,
        )

        return self.__parent__._cast(
            _6017.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
        )

    @property
    def assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6018.AssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6018,
        )

        return self.__parent__._cast(_6018.AssemblyCompoundHarmonicAnalysis)

    @property
    def belt_drive_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6021.BeltDriveCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6021,
        )

        return self.__parent__._cast(_6021.BeltDriveCompoundHarmonicAnalysis)

    @property
    def bevel_differential_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6024.BevelDifferentialGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6024,
        )

        return self.__parent__._cast(
            _6024.BevelDifferentialGearSetCompoundHarmonicAnalysis
        )

    @property
    def bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6029.BevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6029,
        )

        return self.__parent__._cast(_6029.BevelGearSetCompoundHarmonicAnalysis)

    @property
    def bolted_joint_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6031.BoltedJointCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6031,
        )

        return self.__parent__._cast(_6031.BoltedJointCompoundHarmonicAnalysis)

    @property
    def clutch_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6032.ClutchCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6032,
        )

        return self.__parent__._cast(_6032.ClutchCompoundHarmonicAnalysis)

    @property
    def concept_coupling_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6037.ConceptCouplingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6037,
        )

        return self.__parent__._cast(_6037.ConceptCouplingCompoundHarmonicAnalysis)

    @property
    def concept_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6042.ConceptGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6042,
        )

        return self.__parent__._cast(_6042.ConceptGearSetCompoundHarmonicAnalysis)

    @property
    def conical_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6045.ConicalGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6045,
        )

        return self.__parent__._cast(_6045.ConicalGearSetCompoundHarmonicAnalysis)

    @property
    def coupling_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6048.CouplingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6048,
        )

        return self.__parent__._cast(_6048.CouplingCompoundHarmonicAnalysis)

    @property
    def cvt_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6052.CVTCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6052,
        )

        return self.__parent__._cast(_6052.CVTCompoundHarmonicAnalysis)

    @property
    def cycloidal_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6054.CycloidalAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6054,
        )

        return self.__parent__._cast(_6054.CycloidalAssemblyCompoundHarmonicAnalysis)

    @property
    def cylindrical_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6060.CylindricalGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6060,
        )

        return self.__parent__._cast(_6060.CylindricalGearSetCompoundHarmonicAnalysis)

    @property
    def face_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6066.FaceGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6066,
        )

        return self.__parent__._cast(_6066.FaceGearSetCompoundHarmonicAnalysis)

    @property
    def flexible_pin_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6068.FlexiblePinAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6068,
        )

        return self.__parent__._cast(_6068.FlexiblePinAssemblyCompoundHarmonicAnalysis)

    @property
    def gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6071.GearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6071,
        )

        return self.__parent__._cast(_6071.GearSetCompoundHarmonicAnalysis)

    @property
    def hypoid_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6075.HypoidGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6075,
        )

        return self.__parent__._cast(_6075.HypoidGearSetCompoundHarmonicAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6079.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6079,
        )

        return self.__parent__._cast(
            _6079.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6082.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6082,
        )

        return self.__parent__._cast(
            _6082.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6085.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6085,
        )

        return self.__parent__._cast(
            _6085.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
        )

    @property
    def microphone_array_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6088.MicrophoneArrayCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6088,
        )

        return self.__parent__._cast(_6088.MicrophoneArrayCompoundHarmonicAnalysis)

    @property
    def part_to_part_shear_coupling_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6093.PartToPartShearCouplingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6093,
        )

        return self.__parent__._cast(
            _6093.PartToPartShearCouplingCompoundHarmonicAnalysis
        )

    @property
    def planetary_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6097.PlanetaryGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6097,
        )

        return self.__parent__._cast(_6097.PlanetaryGearSetCompoundHarmonicAnalysis)

    @property
    def rolling_ring_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6104.RollingRingAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6104,
        )

        return self.__parent__._cast(_6104.RollingRingAssemblyCompoundHarmonicAnalysis)

    @property
    def root_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6107.RootAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6107,
        )

        return self.__parent__._cast(_6107.RootAssemblyCompoundHarmonicAnalysis)

    @property
    def specialised_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6111.SpecialisedAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6111,
        )

        return self.__parent__._cast(_6111.SpecialisedAssemblyCompoundHarmonicAnalysis)

    @property
    def spiral_bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6114.SpiralBevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6114,
        )

        return self.__parent__._cast(_6114.SpiralBevelGearSetCompoundHarmonicAnalysis)

    @property
    def spring_damper_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6115.SpringDamperCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6115,
        )

        return self.__parent__._cast(_6115.SpringDamperCompoundHarmonicAnalysis)

    @property
    def straight_bevel_diff_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6120.StraightBevelDiffGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6120,
        )

        return self.__parent__._cast(
            _6120.StraightBevelDiffGearSetCompoundHarmonicAnalysis
        )

    @property
    def straight_bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6123.StraightBevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6123,
        )

        return self.__parent__._cast(_6123.StraightBevelGearSetCompoundHarmonicAnalysis)

    @property
    def synchroniser_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6126.SynchroniserCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6126,
        )

        return self.__parent__._cast(_6126.SynchroniserCompoundHarmonicAnalysis)

    @property
    def torque_converter_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6130.TorqueConverterCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6130,
        )

        return self.__parent__._cast(_6130.TorqueConverterCompoundHarmonicAnalysis)

    @property
    def worm_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6138.WormGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6138,
        )

        return self.__parent__._cast(_6138.WormGearSetCompoundHarmonicAnalysis)

    @property
    def zerol_bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6141.ZerolBevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6141,
        )

        return self.__parent__._cast(_6141.ZerolBevelGearSetCompoundHarmonicAnalysis)

    @property
    def abstract_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "AbstractAssemblyCompoundHarmonicAnalysis":
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
class AbstractAssemblyCompoundHarmonicAnalysis(_6092.PartCompoundHarmonicAnalysis):
    """AbstractAssemblyCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_5808.AbstractAssemblyHarmonicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractAssemblyHarmonicAnalysis]

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
    ) -> "List[_5808.AbstractAssemblyHarmonicAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.harmonic_analyses.AbstractAssemblyHarmonicAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_AbstractAssemblyCompoundHarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractAssemblyCompoundHarmonicAnalysis
        """
        return _Cast_AbstractAssemblyCompoundHarmonicAnalysis(self)
