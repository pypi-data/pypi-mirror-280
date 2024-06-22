"""SpecialisedAssemblyCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _2936,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "SpecialisedAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2891,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2942,
        _2946,
        _2949,
        _2954,
        _2956,
        _2957,
        _2962,
        _2967,
        _2970,
        _2973,
        _2977,
        _2979,
        _2985,
        _2992,
        _2994,
        _2997,
        _3001,
        _3005,
        _3008,
        _3011,
        _3014,
        _3019,
        _3023,
        _3030,
        _3041,
        _3042,
        _3047,
        _3050,
        _3053,
        _3057,
        _3065,
        _3068,
        _3018,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssemblyCompoundSystemDeflection:
    """Special nested class for casting SpecialisedAssemblyCompoundSystemDeflection to subclasses."""

    __parent__: "SpecialisedAssemblyCompoundSystemDeflection"

    @property
    def abstract_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2936.AbstractAssemblyCompoundSystemDeflection":
        return self.__parent__._cast(_2936.AbstractAssemblyCompoundSystemDeflection)

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
    def agma_gleason_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2942.AGMAGleasonConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2942,
        )

        return self.__parent__._cast(
            _2942.AGMAGleasonConicalGearSetCompoundSystemDeflection
        )

    @property
    def belt_drive_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2946.BeltDriveCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2946,
        )

        return self.__parent__._cast(_2946.BeltDriveCompoundSystemDeflection)

    @property
    def bevel_differential_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2949.BevelDifferentialGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2949,
        )

        return self.__parent__._cast(
            _2949.BevelDifferentialGearSetCompoundSystemDeflection
        )

    @property
    def bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2954.BevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2954,
        )

        return self.__parent__._cast(_2954.BevelGearSetCompoundSystemDeflection)

    @property
    def bolted_joint_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2956.BoltedJointCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2956,
        )

        return self.__parent__._cast(_2956.BoltedJointCompoundSystemDeflection)

    @property
    def clutch_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2957.ClutchCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2957,
        )

        return self.__parent__._cast(_2957.ClutchCompoundSystemDeflection)

    @property
    def concept_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2962.ConceptCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2962,
        )

        return self.__parent__._cast(_2962.ConceptCouplingCompoundSystemDeflection)

    @property
    def concept_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2967.ConceptGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2967,
        )

        return self.__parent__._cast(_2967.ConceptGearSetCompoundSystemDeflection)

    @property
    def conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2970.ConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2970,
        )

        return self.__parent__._cast(_2970.ConicalGearSetCompoundSystemDeflection)

    @property
    def coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2973.CouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2973,
        )

        return self.__parent__._cast(_2973.CouplingCompoundSystemDeflection)

    @property
    def cvt_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2977.CVTCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2977,
        )

        return self.__parent__._cast(_2977.CVTCompoundSystemDeflection)

    @property
    def cycloidal_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2979.CycloidalAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2979,
        )

        return self.__parent__._cast(_2979.CycloidalAssemblyCompoundSystemDeflection)

    @property
    def cylindrical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2985.CylindricalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2985,
        )

        return self.__parent__._cast(_2985.CylindricalGearSetCompoundSystemDeflection)

    @property
    def face_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2992.FaceGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2992,
        )

        return self.__parent__._cast(_2992.FaceGearSetCompoundSystemDeflection)

    @property
    def flexible_pin_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2994.FlexiblePinAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2994,
        )

        return self.__parent__._cast(_2994.FlexiblePinAssemblyCompoundSystemDeflection)

    @property
    def gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2997.GearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2997,
        )

        return self.__parent__._cast(_2997.GearSetCompoundSystemDeflection)

    @property
    def hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3001.HypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3001,
        )

        return self.__parent__._cast(_3001.HypoidGearSetCompoundSystemDeflection)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3005.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3005,
        )

        return self.__parent__._cast(
            _3005.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3008.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3008,
        )

        return self.__parent__._cast(
            _3008.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3011.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3011,
        )

        return self.__parent__._cast(
            _3011.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
        )

    @property
    def microphone_array_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3014.MicrophoneArrayCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3014,
        )

        return self.__parent__._cast(_3014.MicrophoneArrayCompoundSystemDeflection)

    @property
    def part_to_part_shear_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3019.PartToPartShearCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3019,
        )

        return self.__parent__._cast(
            _3019.PartToPartShearCouplingCompoundSystemDeflection
        )

    @property
    def planetary_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3023.PlanetaryGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3023,
        )

        return self.__parent__._cast(_3023.PlanetaryGearSetCompoundSystemDeflection)

    @property
    def rolling_ring_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3030.RollingRingAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3030,
        )

        return self.__parent__._cast(_3030.RollingRingAssemblyCompoundSystemDeflection)

    @property
    def spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3041.SpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3041,
        )

        return self.__parent__._cast(_3041.SpiralBevelGearSetCompoundSystemDeflection)

    @property
    def spring_damper_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3042.SpringDamperCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3042,
        )

        return self.__parent__._cast(_3042.SpringDamperCompoundSystemDeflection)

    @property
    def straight_bevel_diff_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3047.StraightBevelDiffGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3047,
        )

        return self.__parent__._cast(
            _3047.StraightBevelDiffGearSetCompoundSystemDeflection
        )

    @property
    def straight_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3050.StraightBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3050,
        )

        return self.__parent__._cast(_3050.StraightBevelGearSetCompoundSystemDeflection)

    @property
    def synchroniser_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3053.SynchroniserCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3053,
        )

        return self.__parent__._cast(_3053.SynchroniserCompoundSystemDeflection)

    @property
    def torque_converter_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3057.TorqueConverterCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3057,
        )

        return self.__parent__._cast(_3057.TorqueConverterCompoundSystemDeflection)

    @property
    def worm_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3065.WormGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3065,
        )

        return self.__parent__._cast(_3065.WormGearSetCompoundSystemDeflection)

    @property
    def zerol_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3068.ZerolBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3068,
        )

        return self.__parent__._cast(_3068.ZerolBevelGearSetCompoundSystemDeflection)

    @property
    def specialised_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "SpecialisedAssemblyCompoundSystemDeflection":
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
class SpecialisedAssemblyCompoundSystemDeflection(
    _2936.AbstractAssemblyCompoundSystemDeflection
):
    """SpecialisedAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_2891.SpecialisedAssemblySystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection]

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
    ) -> "List[_2891.SpecialisedAssemblySystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_SpecialisedAssemblyCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssemblyCompoundSystemDeflection
        """
        return _Cast_SpecialisedAssemblyCompoundSystemDeflection(self)
