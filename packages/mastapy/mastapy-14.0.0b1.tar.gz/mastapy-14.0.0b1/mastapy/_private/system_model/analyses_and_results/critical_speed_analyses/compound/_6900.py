"""PartCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7711
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "PartCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6769,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6819,
        _6820,
        _6821,
        _6823,
        _6825,
        _6826,
        _6827,
        _6829,
        _6830,
        _6832,
        _6833,
        _6834,
        _6835,
        _6837,
        _6838,
        _6839,
        _6840,
        _6842,
        _6844,
        _6845,
        _6847,
        _6848,
        _6850,
        _6851,
        _6853,
        _6855,
        _6856,
        _6858,
        _6860,
        _6861,
        _6862,
        _6864,
        _6866,
        _6868,
        _6869,
        _6870,
        _6871,
        _6872,
        _6874,
        _6875,
        _6876,
        _6877,
        _6879,
        _6880,
        _6881,
        _6883,
        _6885,
        _6887,
        _6888,
        _6890,
        _6891,
        _6893,
        _6894,
        _6895,
        _6896,
        _6897,
        _6898,
        _6899,
        _6901,
        _6903,
        _6905,
        _6906,
        _6907,
        _6908,
        _6909,
        _6910,
        _6912,
        _6913,
        _6915,
        _6916,
        _6917,
        _6919,
        _6920,
        _6922,
        _6923,
        _6925,
        _6926,
        _6928,
        _6929,
        _6931,
        _6932,
        _6933,
        _6934,
        _6935,
        _6936,
        _6937,
        _6938,
        _6940,
        _6941,
        _6942,
        _6943,
        _6944,
        _6946,
        _6947,
        _6949,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7708
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="PartCompoundCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartCompoundCriticalSpeedAnalysis._Cast_PartCompoundCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundCriticalSpeedAnalysis:
    """Special nested class for casting PartCompoundCriticalSpeedAnalysis to subclasses."""

    __parent__: "PartCompoundCriticalSpeedAnalysis"

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7711.PartCompoundAnalysis":
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
    def abstract_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6819.AbstractAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6819,
        )

        return self.__parent__._cast(
            _6819.AbstractAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def abstract_shaft_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6820.AbstractShaftCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6820,
        )

        return self.__parent__._cast(_6820.AbstractShaftCompoundCriticalSpeedAnalysis)

    @property
    def abstract_shaft_or_housing_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6821.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6821,
        )

        return self.__parent__._cast(
            _6821.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
        )

    @property
    def agma_gleason_conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6823.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6823,
        )

        return self.__parent__._cast(
            _6823.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
        )

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
    def assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6826.AssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6826,
        )

        return self.__parent__._cast(_6826.AssemblyCompoundCriticalSpeedAnalysis)

    @property
    def bearing_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6827.BearingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6827,
        )

        return self.__parent__._cast(_6827.BearingCompoundCriticalSpeedAnalysis)

    @property
    def belt_drive_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6829.BeltDriveCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6829,
        )

        return self.__parent__._cast(_6829.BeltDriveCompoundCriticalSpeedAnalysis)

    @property
    def bevel_differential_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6830.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6830,
        )

        return self.__parent__._cast(
            _6830.BevelDifferentialGearCompoundCriticalSpeedAnalysis
        )

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
    def bevel_differential_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6833.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6833,
        )

        return self.__parent__._cast(
            _6833.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6834.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6834,
        )

        return self.__parent__._cast(
            _6834.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6835.BevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6835,
        )

        return self.__parent__._cast(_6835.BevelGearCompoundCriticalSpeedAnalysis)

    @property
    def bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6837.BevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6837,
        )

        return self.__parent__._cast(_6837.BevelGearSetCompoundCriticalSpeedAnalysis)

    @property
    def bolt_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6838.BoltCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6838,
        )

        return self.__parent__._cast(_6838.BoltCompoundCriticalSpeedAnalysis)

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
    def clutch_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6842.ClutchHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6842,
        )

        return self.__parent__._cast(_6842.ClutchHalfCompoundCriticalSpeedAnalysis)

    @property
    def component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6844.ComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6844,
        )

        return self.__parent__._cast(_6844.ComponentCompoundCriticalSpeedAnalysis)

    @property
    def concept_coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6845.ConceptCouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6845,
        )

        return self.__parent__._cast(_6845.ConceptCouplingCompoundCriticalSpeedAnalysis)

    @property
    def concept_coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6847.ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6847,
        )

        return self.__parent__._cast(
            _6847.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def concept_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6848.ConceptGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6848,
        )

        return self.__parent__._cast(_6848.ConceptGearCompoundCriticalSpeedAnalysis)

    @property
    def concept_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6850.ConceptGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6850,
        )

        return self.__parent__._cast(_6850.ConceptGearSetCompoundCriticalSpeedAnalysis)

    @property
    def conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6851.ConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6851,
        )

        return self.__parent__._cast(_6851.ConicalGearCompoundCriticalSpeedAnalysis)

    @property
    def conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6853.ConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6853,
        )

        return self.__parent__._cast(_6853.ConicalGearSetCompoundCriticalSpeedAnalysis)

    @property
    def connector_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6855.ConnectorCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6855,
        )

        return self.__parent__._cast(_6855.ConnectorCompoundCriticalSpeedAnalysis)

    @property
    def coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6856.CouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6856,
        )

        return self.__parent__._cast(_6856.CouplingCompoundCriticalSpeedAnalysis)

    @property
    def coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6858.CouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6858,
        )

        return self.__parent__._cast(_6858.CouplingHalfCompoundCriticalSpeedAnalysis)

    @property
    def cvt_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6860.CVTCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6860,
        )

        return self.__parent__._cast(_6860.CVTCompoundCriticalSpeedAnalysis)

    @property
    def cvt_pulley_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6861.CVTPulleyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6861,
        )

        return self.__parent__._cast(_6861.CVTPulleyCompoundCriticalSpeedAnalysis)

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
    def cycloidal_disc_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6864.CycloidalDiscCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6864,
        )

        return self.__parent__._cast(_6864.CycloidalDiscCompoundCriticalSpeedAnalysis)

    @property
    def cylindrical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6866.CylindricalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6866,
        )

        return self.__parent__._cast(_6866.CylindricalGearCompoundCriticalSpeedAnalysis)

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
    def cylindrical_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6869.CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6869,
        )

        return self.__parent__._cast(
            _6869.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def datum_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6870.DatumCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6870,
        )

        return self.__parent__._cast(_6870.DatumCompoundCriticalSpeedAnalysis)

    @property
    def external_cad_model_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6871.ExternalCADModelCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6871,
        )

        return self.__parent__._cast(
            _6871.ExternalCADModelCompoundCriticalSpeedAnalysis
        )

    @property
    def face_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6872.FaceGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6872,
        )

        return self.__parent__._cast(_6872.FaceGearCompoundCriticalSpeedAnalysis)

    @property
    def face_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6874.FaceGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6874,
        )

        return self.__parent__._cast(_6874.FaceGearSetCompoundCriticalSpeedAnalysis)

    @property
    def fe_part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6875.FEPartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6875,
        )

        return self.__parent__._cast(_6875.FEPartCompoundCriticalSpeedAnalysis)

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
    def gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6877.GearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6877,
        )

        return self.__parent__._cast(_6877.GearCompoundCriticalSpeedAnalysis)

    @property
    def gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6879.GearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6879,
        )

        return self.__parent__._cast(_6879.GearSetCompoundCriticalSpeedAnalysis)

    @property
    def guide_dxf_model_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6880.GuideDxfModelCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6880,
        )

        return self.__parent__._cast(_6880.GuideDxfModelCompoundCriticalSpeedAnalysis)

    @property
    def hypoid_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6881.HypoidGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6881,
        )

        return self.__parent__._cast(_6881.HypoidGearCompoundCriticalSpeedAnalysis)

    @property
    def hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6883.HypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6883,
        )

        return self.__parent__._cast(_6883.HypoidGearSetCompoundCriticalSpeedAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6885.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6885,
        )

        return self.__parent__._cast(
            _6885.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
        )

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
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6888.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6888,
        )

        return self.__parent__._cast(
            _6888.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
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
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6891.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6891,
        )

        return self.__parent__._cast(
            _6891.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
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
    def mass_disc_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6894.MassDiscCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6894,
        )

        return self.__parent__._cast(_6894.MassDiscCompoundCriticalSpeedAnalysis)

    @property
    def measurement_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6895.MeasurementComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6895,
        )

        return self.__parent__._cast(
            _6895.MeasurementComponentCompoundCriticalSpeedAnalysis
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
    def microphone_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6897.MicrophoneCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6897,
        )

        return self.__parent__._cast(_6897.MicrophoneCompoundCriticalSpeedAnalysis)

    @property
    def mountable_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6898.MountableComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6898,
        )

        return self.__parent__._cast(
            _6898.MountableComponentCompoundCriticalSpeedAnalysis
        )

    @property
    def oil_seal_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6899.OilSealCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6899,
        )

        return self.__parent__._cast(_6899.OilSealCompoundCriticalSpeedAnalysis)

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
    def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6903.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6903,
        )

        return self.__parent__._cast(
            _6903.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
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
    def planet_carrier_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6906.PlanetCarrierCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6906,
        )

        return self.__parent__._cast(_6906.PlanetCarrierCompoundCriticalSpeedAnalysis)

    @property
    def point_load_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6907.PointLoadCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6907,
        )

        return self.__parent__._cast(_6907.PointLoadCompoundCriticalSpeedAnalysis)

    @property
    def power_load_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6908.PowerLoadCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6908,
        )

        return self.__parent__._cast(_6908.PowerLoadCompoundCriticalSpeedAnalysis)

    @property
    def pulley_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6909.PulleyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6909,
        )

        return self.__parent__._cast(_6909.PulleyCompoundCriticalSpeedAnalysis)

    @property
    def ring_pins_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6910.RingPinsCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6910,
        )

        return self.__parent__._cast(_6910.RingPinsCompoundCriticalSpeedAnalysis)

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
    def rolling_ring_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6913.RollingRingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6913,
        )

        return self.__parent__._cast(_6913.RollingRingCompoundCriticalSpeedAnalysis)

    @property
    def root_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6915.RootAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6915,
        )

        return self.__parent__._cast(_6915.RootAssemblyCompoundCriticalSpeedAnalysis)

    @property
    def shaft_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6916.ShaftCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6916,
        )

        return self.__parent__._cast(_6916.ShaftCompoundCriticalSpeedAnalysis)

    @property
    def shaft_hub_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6917.ShaftHubConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6917,
        )

        return self.__parent__._cast(
            _6917.ShaftHubConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def specialised_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6919.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6919,
        )

        return self.__parent__._cast(
            _6919.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def spiral_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6920.SpiralBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6920,
        )

        return self.__parent__._cast(_6920.SpiralBevelGearCompoundCriticalSpeedAnalysis)

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
    def spring_damper_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6925.SpringDamperHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6925,
        )

        return self.__parent__._cast(
            _6925.SpringDamperHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_diff_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6926.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6926,
        )

        return self.__parent__._cast(
            _6926.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
        )

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
    def straight_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6929.StraightBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6929,
        )

        return self.__parent__._cast(
            _6929.StraightBevelGearCompoundCriticalSpeedAnalysis
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
    def straight_bevel_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6932.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6932,
        )

        return self.__parent__._cast(
            _6932.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6933.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6933,
        )

        return self.__parent__._cast(
            _6933.StraightBevelSunGearCompoundCriticalSpeedAnalysis
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
    def synchroniser_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6935.SynchroniserHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6935,
        )

        return self.__parent__._cast(
            _6935.SynchroniserHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6936.SynchroniserPartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6936,
        )

        return self.__parent__._cast(
            _6936.SynchroniserPartCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_sleeve_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6937.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6937,
        )

        return self.__parent__._cast(
            _6937.SynchroniserSleeveCompoundCriticalSpeedAnalysis
        )

    @property
    def torque_converter_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6938.TorqueConverterCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6938,
        )

        return self.__parent__._cast(_6938.TorqueConverterCompoundCriticalSpeedAnalysis)

    @property
    def torque_converter_pump_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6940.TorqueConverterPumpCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6940,
        )

        return self.__parent__._cast(
            _6940.TorqueConverterPumpCompoundCriticalSpeedAnalysis
        )

    @property
    def torque_converter_turbine_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6941.TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6941,
        )

        return self.__parent__._cast(
            _6941.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
        )

    @property
    def unbalanced_mass_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6942.UnbalancedMassCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6942,
        )

        return self.__parent__._cast(_6942.UnbalancedMassCompoundCriticalSpeedAnalysis)

    @property
    def virtual_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6943.VirtualComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6943,
        )

        return self.__parent__._cast(
            _6943.VirtualComponentCompoundCriticalSpeedAnalysis
        )

    @property
    def worm_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6944.WormGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6944,
        )

        return self.__parent__._cast(_6944.WormGearCompoundCriticalSpeedAnalysis)

    @property
    def worm_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6946.WormGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6946,
        )

        return self.__parent__._cast(_6946.WormGearSetCompoundCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6947.ZerolBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6947,
        )

        return self.__parent__._cast(_6947.ZerolBevelGearCompoundCriticalSpeedAnalysis)

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
    def part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "PartCompoundCriticalSpeedAnalysis":
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
class PartCompoundCriticalSpeedAnalysis(_7711.PartCompoundAnalysis):
    """PartCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_6769.PartCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.PartCriticalSpeedAnalysis]

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
    ) -> "List[_6769.PartCriticalSpeedAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.critical_speed_analyses.PartCriticalSpeedAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_PartCompoundCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundCriticalSpeedAnalysis
        """
        return _Cast_PartCompoundCriticalSpeedAnalysis(self)
