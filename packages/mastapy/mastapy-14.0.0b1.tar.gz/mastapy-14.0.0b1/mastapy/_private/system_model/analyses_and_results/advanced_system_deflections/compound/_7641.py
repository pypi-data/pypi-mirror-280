"""PartCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7711
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_PART_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "PartCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7509,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7560,
        _7561,
        _7562,
        _7564,
        _7566,
        _7567,
        _7568,
        _7570,
        _7571,
        _7573,
        _7574,
        _7575,
        _7576,
        _7578,
        _7579,
        _7580,
        _7581,
        _7583,
        _7585,
        _7586,
        _7588,
        _7589,
        _7591,
        _7592,
        _7594,
        _7596,
        _7597,
        _7599,
        _7601,
        _7602,
        _7603,
        _7605,
        _7607,
        _7609,
        _7610,
        _7611,
        _7612,
        _7613,
        _7615,
        _7616,
        _7617,
        _7618,
        _7620,
        _7621,
        _7622,
        _7624,
        _7626,
        _7628,
        _7629,
        _7631,
        _7632,
        _7634,
        _7635,
        _7636,
        _7637,
        _7638,
        _7639,
        _7640,
        _7642,
        _7644,
        _7646,
        _7647,
        _7648,
        _7649,
        _7650,
        _7651,
        _7653,
        _7654,
        _7656,
        _7657,
        _7658,
        _7660,
        _7661,
        _7663,
        _7664,
        _7666,
        _7667,
        _7669,
        _7670,
        _7672,
        _7673,
        _7674,
        _7675,
        _7676,
        _7677,
        _7678,
        _7679,
        _7681,
        _7682,
        _7683,
        _7684,
        _7685,
        _7687,
        _7688,
        _7690,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7708
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="PartCompoundAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundAdvancedSystemDeflection:
    """Special nested class for casting PartCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "PartCompoundAdvancedSystemDeflection"

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
    def abstract_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7560.AbstractAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7560,
        )

        return self.__parent__._cast(
            _7560.AbstractAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def abstract_shaft_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7561.AbstractShaftCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7561,
        )

        return self.__parent__._cast(
            _7561.AbstractShaftCompoundAdvancedSystemDeflection
        )

    @property
    def abstract_shaft_or_housing_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7562.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7562,
        )

        return self.__parent__._cast(
            _7562.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7564.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7564,
        )

        return self.__parent__._cast(
            _7564.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7566.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7566,
        )

        return self.__parent__._cast(
            _7566.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7567.AssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7567,
        )

        return self.__parent__._cast(_7567.AssemblyCompoundAdvancedSystemDeflection)

    @property
    def bearing_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7568.BearingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7568,
        )

        return self.__parent__._cast(_7568.BearingCompoundAdvancedSystemDeflection)

    @property
    def belt_drive_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7570.BeltDriveCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7570,
        )

        return self.__parent__._cast(_7570.BeltDriveCompoundAdvancedSystemDeflection)

    @property
    def bevel_differential_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7571.BevelDifferentialGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7571,
        )

        return self.__parent__._cast(
            _7571.BevelDifferentialGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7573.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7573,
        )

        return self.__parent__._cast(
            _7573.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7574.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7574,
        )

        return self.__parent__._cast(
            _7574.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_sun_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7575.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7575,
        )

        return self.__parent__._cast(
            _7575.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7576.BevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7576,
        )

        return self.__parent__._cast(_7576.BevelGearCompoundAdvancedSystemDeflection)

    @property
    def bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7578.BevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7578,
        )

        return self.__parent__._cast(_7578.BevelGearSetCompoundAdvancedSystemDeflection)

    @property
    def bolt_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7579.BoltCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7579,
        )

        return self.__parent__._cast(_7579.BoltCompoundAdvancedSystemDeflection)

    @property
    def bolted_joint_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7580.BoltedJointCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7580,
        )

        return self.__parent__._cast(_7580.BoltedJointCompoundAdvancedSystemDeflection)

    @property
    def clutch_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7581.ClutchCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7581,
        )

        return self.__parent__._cast(_7581.ClutchCompoundAdvancedSystemDeflection)

    @property
    def clutch_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7583.ClutchHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7583,
        )

        return self.__parent__._cast(_7583.ClutchHalfCompoundAdvancedSystemDeflection)

    @property
    def component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7585.ComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7585,
        )

        return self.__parent__._cast(_7585.ComponentCompoundAdvancedSystemDeflection)

    @property
    def concept_coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7586.ConceptCouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7586,
        )

        return self.__parent__._cast(
            _7586.ConceptCouplingCompoundAdvancedSystemDeflection
        )

    @property
    def concept_coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7588.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7588,
        )

        return self.__parent__._cast(
            _7588.ConceptCouplingHalfCompoundAdvancedSystemDeflection
        )

    @property
    def concept_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7589.ConceptGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7589,
        )

        return self.__parent__._cast(_7589.ConceptGearCompoundAdvancedSystemDeflection)

    @property
    def concept_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7591.ConceptGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7591,
        )

        return self.__parent__._cast(
            _7591.ConceptGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7592.ConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7592,
        )

        return self.__parent__._cast(_7592.ConicalGearCompoundAdvancedSystemDeflection)

    @property
    def conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7594.ConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7594,
        )

        return self.__parent__._cast(
            _7594.ConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def connector_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7596.ConnectorCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7596,
        )

        return self.__parent__._cast(_7596.ConnectorCompoundAdvancedSystemDeflection)

    @property
    def coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7597.CouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7597,
        )

        return self.__parent__._cast(_7597.CouplingCompoundAdvancedSystemDeflection)

    @property
    def coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7599.CouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7599,
        )

        return self.__parent__._cast(_7599.CouplingHalfCompoundAdvancedSystemDeflection)

    @property
    def cvt_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7601.CVTCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7601,
        )

        return self.__parent__._cast(_7601.CVTCompoundAdvancedSystemDeflection)

    @property
    def cvt_pulley_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7602.CVTPulleyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7602,
        )

        return self.__parent__._cast(_7602.CVTPulleyCompoundAdvancedSystemDeflection)

    @property
    def cycloidal_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7603.CycloidalAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7603,
        )

        return self.__parent__._cast(
            _7603.CycloidalAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def cycloidal_disc_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7605.CycloidalDiscCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7605,
        )

        return self.__parent__._cast(
            _7605.CycloidalDiscCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7607.CylindricalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7607,
        )

        return self.__parent__._cast(
            _7607.CylindricalGearCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7609.CylindricalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7609,
        )

        return self.__parent__._cast(
            _7609.CylindricalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7610.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7610,
        )

        return self.__parent__._cast(
            _7610.CylindricalPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def datum_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7611.DatumCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7611,
        )

        return self.__parent__._cast(_7611.DatumCompoundAdvancedSystemDeflection)

    @property
    def external_cad_model_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7612.ExternalCADModelCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7612,
        )

        return self.__parent__._cast(
            _7612.ExternalCADModelCompoundAdvancedSystemDeflection
        )

    @property
    def face_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7613.FaceGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7613,
        )

        return self.__parent__._cast(_7613.FaceGearCompoundAdvancedSystemDeflection)

    @property
    def face_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7615.FaceGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7615,
        )

        return self.__parent__._cast(_7615.FaceGearSetCompoundAdvancedSystemDeflection)

    @property
    def fe_part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7616.FEPartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7616,
        )

        return self.__parent__._cast(_7616.FEPartCompoundAdvancedSystemDeflection)

    @property
    def flexible_pin_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7617.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7617,
        )

        return self.__parent__._cast(
            _7617.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7618.GearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7618,
        )

        return self.__parent__._cast(_7618.GearCompoundAdvancedSystemDeflection)

    @property
    def gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7620.GearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7620,
        )

        return self.__parent__._cast(_7620.GearSetCompoundAdvancedSystemDeflection)

    @property
    def guide_dxf_model_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7621.GuideDxfModelCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7621,
        )

        return self.__parent__._cast(
            _7621.GuideDxfModelCompoundAdvancedSystemDeflection
        )

    @property
    def hypoid_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7622.HypoidGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7622,
        )

        return self.__parent__._cast(_7622.HypoidGearCompoundAdvancedSystemDeflection)

    @property
    def hypoid_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7624.HypoidGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7624,
        )

        return self.__parent__._cast(
            _7624.HypoidGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7626.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7626,
        )

        return self.__parent__._cast(
            _7626.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7628.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7628,
        )

        return self.__parent__._cast(
            _7628.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7629.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7629,
        )

        return self.__parent__._cast(
            _7629.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7631.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7631,
        )

        return self.__parent__._cast(
            _7631.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> (
        "_7632.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7632,
        )

        return self.__parent__._cast(
            _7632.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7634.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7634,
        )

        return self.__parent__._cast(
            _7634.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def mass_disc_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7635.MassDiscCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7635,
        )

        return self.__parent__._cast(_7635.MassDiscCompoundAdvancedSystemDeflection)

    @property
    def measurement_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7636.MeasurementComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7636,
        )

        return self.__parent__._cast(
            _7636.MeasurementComponentCompoundAdvancedSystemDeflection
        )

    @property
    def microphone_array_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7637.MicrophoneArrayCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7637,
        )

        return self.__parent__._cast(
            _7637.MicrophoneArrayCompoundAdvancedSystemDeflection
        )

    @property
    def microphone_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7638.MicrophoneCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7638,
        )

        return self.__parent__._cast(_7638.MicrophoneCompoundAdvancedSystemDeflection)

    @property
    def mountable_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7639.MountableComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7639,
        )

        return self.__parent__._cast(
            _7639.MountableComponentCompoundAdvancedSystemDeflection
        )

    @property
    def oil_seal_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7640.OilSealCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7640,
        )

        return self.__parent__._cast(_7640.OilSealCompoundAdvancedSystemDeflection)

    @property
    def part_to_part_shear_coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7642.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7642,
        )

        return self.__parent__._cast(
            _7642.PartToPartShearCouplingCompoundAdvancedSystemDeflection
        )

    @property
    def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7644.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7644,
        )

        return self.__parent__._cast(
            _7644.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
        )

    @property
    def planetary_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7646.PlanetaryGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7646,
        )

        return self.__parent__._cast(
            _7646.PlanetaryGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def planet_carrier_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7647.PlanetCarrierCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7647,
        )

        return self.__parent__._cast(
            _7647.PlanetCarrierCompoundAdvancedSystemDeflection
        )

    @property
    def point_load_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7648.PointLoadCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7648,
        )

        return self.__parent__._cast(_7648.PointLoadCompoundAdvancedSystemDeflection)

    @property
    def power_load_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7649.PowerLoadCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7649,
        )

        return self.__parent__._cast(_7649.PowerLoadCompoundAdvancedSystemDeflection)

    @property
    def pulley_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7650.PulleyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7650,
        )

        return self.__parent__._cast(_7650.PulleyCompoundAdvancedSystemDeflection)

    @property
    def ring_pins_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7651.RingPinsCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7651,
        )

        return self.__parent__._cast(_7651.RingPinsCompoundAdvancedSystemDeflection)

    @property
    def rolling_ring_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7653.RollingRingAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7653,
        )

        return self.__parent__._cast(
            _7653.RollingRingAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def rolling_ring_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7654.RollingRingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7654,
        )

        return self.__parent__._cast(_7654.RollingRingCompoundAdvancedSystemDeflection)

    @property
    def root_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7656.RootAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7656,
        )

        return self.__parent__._cast(_7656.RootAssemblyCompoundAdvancedSystemDeflection)

    @property
    def shaft_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7657.ShaftCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7657,
        )

        return self.__parent__._cast(_7657.ShaftCompoundAdvancedSystemDeflection)

    @property
    def shaft_hub_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7658.ShaftHubConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7658,
        )

        return self.__parent__._cast(
            _7658.ShaftHubConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def specialised_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7660.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7660,
        )

        return self.__parent__._cast(
            _7660.SpecialisedAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7661.SpiralBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7661,
        )

        return self.__parent__._cast(
            _7661.SpiralBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7663.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7663,
        )

        return self.__parent__._cast(
            _7663.SpiralBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def spring_damper_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7664.SpringDamperCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7664,
        )

        return self.__parent__._cast(_7664.SpringDamperCompoundAdvancedSystemDeflection)

    @property
    def spring_damper_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7666.SpringDamperHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7666,
        )

        return self.__parent__._cast(
            _7666.SpringDamperHalfCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7667.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7667,
        )

        return self.__parent__._cast(
            _7667.StraightBevelDiffGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7669.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7669,
        )

        return self.__parent__._cast(
            _7669.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7670.StraightBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7670,
        )

        return self.__parent__._cast(
            _7670.StraightBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7672.StraightBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7672,
        )

        return self.__parent__._cast(
            _7672.StraightBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7673.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7673,
        )

        return self.__parent__._cast(
            _7673.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_sun_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7674.StraightBevelSunGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7674,
        )

        return self.__parent__._cast(
            _7674.StraightBevelSunGearCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7675.SynchroniserCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7675,
        )

        return self.__parent__._cast(_7675.SynchroniserCompoundAdvancedSystemDeflection)

    @property
    def synchroniser_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7676.SynchroniserHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7676,
        )

        return self.__parent__._cast(
            _7676.SynchroniserHalfCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7677.SynchroniserPartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7677,
        )

        return self.__parent__._cast(
            _7677.SynchroniserPartCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_sleeve_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7678.SynchroniserSleeveCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7678,
        )

        return self.__parent__._cast(
            _7678.SynchroniserSleeveCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7679.TorqueConverterCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7679,
        )

        return self.__parent__._cast(
            _7679.TorqueConverterCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_pump_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7681.TorqueConverterPumpCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7681,
        )

        return self.__parent__._cast(
            _7681.TorqueConverterPumpCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_turbine_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7682.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7682,
        )

        return self.__parent__._cast(
            _7682.TorqueConverterTurbineCompoundAdvancedSystemDeflection
        )

    @property
    def unbalanced_mass_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7683.UnbalancedMassCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7683,
        )

        return self.__parent__._cast(
            _7683.UnbalancedMassCompoundAdvancedSystemDeflection
        )

    @property
    def virtual_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7684.VirtualComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7684,
        )

        return self.__parent__._cast(
            _7684.VirtualComponentCompoundAdvancedSystemDeflection
        )

    @property
    def worm_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7685.WormGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7685,
        )

        return self.__parent__._cast(_7685.WormGearCompoundAdvancedSystemDeflection)

    @property
    def worm_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7687.WormGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7687,
        )

        return self.__parent__._cast(_7687.WormGearSetCompoundAdvancedSystemDeflection)

    @property
    def zerol_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7688.ZerolBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7688,
        )

        return self.__parent__._cast(
            _7688.ZerolBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def zerol_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7690.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7690,
        )

        return self.__parent__._cast(
            _7690.ZerolBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "PartCompoundAdvancedSystemDeflection":
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
class PartCompoundAdvancedSystemDeflection(_7711.PartCompoundAnalysis):
    """PartCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_7509.PartAdvancedSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_system_deflections.PartAdvancedSystemDeflection]

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
    ) -> "List[_7509.PartAdvancedSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_system_deflections.PartAdvancedSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_PartCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundAdvancedSystemDeflection
        """
        return _Cast_PartCompoundAdvancedSystemDeflection(self)
