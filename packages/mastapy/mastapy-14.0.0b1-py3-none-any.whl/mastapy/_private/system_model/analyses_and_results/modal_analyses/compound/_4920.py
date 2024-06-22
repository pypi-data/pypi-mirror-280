"""MountableComponentCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
    _4866,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "MountableComponentCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4771
    from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
        _4845,
        _4849,
        _4852,
        _4855,
        _4856,
        _4857,
        _4864,
        _4869,
        _4870,
        _4873,
        _4877,
        _4880,
        _4883,
        _4888,
        _4891,
        _4894,
        _4899,
        _4903,
        _4907,
        _4910,
        _4913,
        _4916,
        _4917,
        _4921,
        _4925,
        _4928,
        _4929,
        _4930,
        _4931,
        _4932,
        _4935,
        _4939,
        _4942,
        _4947,
        _4948,
        _4951,
        _4954,
        _4955,
        _4957,
        _4958,
        _4959,
        _4962,
        _4963,
        _4964,
        _4965,
        _4966,
        _4969,
        _4922,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7711,
        _7708,
    )
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="MountableComponentCompoundModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponentCompoundModalAnalysis:
    """Special nested class for casting MountableComponentCompoundModalAnalysis to subclasses."""

    __parent__: "MountableComponentCompoundModalAnalysis"

    @property
    def component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4866.ComponentCompoundModalAnalysis":
        return self.__parent__._cast(_4866.ComponentCompoundModalAnalysis)

    @property
    def part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4922.PartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4922,
        )

        return self.__parent__._cast(_4922.PartCompoundModalAnalysis)

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
    def agma_gleason_conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4845.AGMAGleasonConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4845,
        )

        return self.__parent__._cast(_4845.AGMAGleasonConicalGearCompoundModalAnalysis)

    @property
    def bearing_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4849.BearingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4849,
        )

        return self.__parent__._cast(_4849.BearingCompoundModalAnalysis)

    @property
    def bevel_differential_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4852.BevelDifferentialGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4852,
        )

        return self.__parent__._cast(_4852.BevelDifferentialGearCompoundModalAnalysis)

    @property
    def bevel_differential_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4855.BevelDifferentialPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4855,
        )

        return self.__parent__._cast(
            _4855.BevelDifferentialPlanetGearCompoundModalAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4856.BevelDifferentialSunGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4856,
        )

        return self.__parent__._cast(
            _4856.BevelDifferentialSunGearCompoundModalAnalysis
        )

    @property
    def bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4857.BevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4857,
        )

        return self.__parent__._cast(_4857.BevelGearCompoundModalAnalysis)

    @property
    def clutch_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4864.ClutchHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4864,
        )

        return self.__parent__._cast(_4864.ClutchHalfCompoundModalAnalysis)

    @property
    def concept_coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4869.ConceptCouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4869,
        )

        return self.__parent__._cast(_4869.ConceptCouplingHalfCompoundModalAnalysis)

    @property
    def concept_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4870.ConceptGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4870,
        )

        return self.__parent__._cast(_4870.ConceptGearCompoundModalAnalysis)

    @property
    def conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4873.ConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4873,
        )

        return self.__parent__._cast(_4873.ConicalGearCompoundModalAnalysis)

    @property
    def connector_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4877.ConnectorCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4877,
        )

        return self.__parent__._cast(_4877.ConnectorCompoundModalAnalysis)

    @property
    def coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4880.CouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4880,
        )

        return self.__parent__._cast(_4880.CouplingHalfCompoundModalAnalysis)

    @property
    def cvt_pulley_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4883.CVTPulleyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4883,
        )

        return self.__parent__._cast(_4883.CVTPulleyCompoundModalAnalysis)

    @property
    def cylindrical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4888.CylindricalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4888,
        )

        return self.__parent__._cast(_4888.CylindricalGearCompoundModalAnalysis)

    @property
    def cylindrical_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4891.CylindricalPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4891,
        )

        return self.__parent__._cast(_4891.CylindricalPlanetGearCompoundModalAnalysis)

    @property
    def face_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4894.FaceGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4894,
        )

        return self.__parent__._cast(_4894.FaceGearCompoundModalAnalysis)

    @property
    def gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4899.GearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4899,
        )

        return self.__parent__._cast(_4899.GearCompoundModalAnalysis)

    @property
    def hypoid_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4903.HypoidGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4903,
        )

        return self.__parent__._cast(_4903.HypoidGearCompoundModalAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4907.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4907,
        )

        return self.__parent__._cast(
            _4907.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4910.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4910,
        )

        return self.__parent__._cast(
            _4910.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4913.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4913,
        )

        return self.__parent__._cast(
            _4913.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
        )

    @property
    def mass_disc_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4916.MassDiscCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4916,
        )

        return self.__parent__._cast(_4916.MassDiscCompoundModalAnalysis)

    @property
    def measurement_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4917.MeasurementComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4917,
        )

        return self.__parent__._cast(_4917.MeasurementComponentCompoundModalAnalysis)

    @property
    def oil_seal_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4921.OilSealCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4921,
        )

        return self.__parent__._cast(_4921.OilSealCompoundModalAnalysis)

    @property
    def part_to_part_shear_coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4925.PartToPartShearCouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4925,
        )

        return self.__parent__._cast(
            _4925.PartToPartShearCouplingHalfCompoundModalAnalysis
        )

    @property
    def planet_carrier_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4928.PlanetCarrierCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4928,
        )

        return self.__parent__._cast(_4928.PlanetCarrierCompoundModalAnalysis)

    @property
    def point_load_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4929.PointLoadCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4929,
        )

        return self.__parent__._cast(_4929.PointLoadCompoundModalAnalysis)

    @property
    def power_load_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4930.PowerLoadCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4930,
        )

        return self.__parent__._cast(_4930.PowerLoadCompoundModalAnalysis)

    @property
    def pulley_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4931.PulleyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4931,
        )

        return self.__parent__._cast(_4931.PulleyCompoundModalAnalysis)

    @property
    def ring_pins_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4932.RingPinsCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4932,
        )

        return self.__parent__._cast(_4932.RingPinsCompoundModalAnalysis)

    @property
    def rolling_ring_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4935.RollingRingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4935,
        )

        return self.__parent__._cast(_4935.RollingRingCompoundModalAnalysis)

    @property
    def shaft_hub_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4939.ShaftHubConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4939,
        )

        return self.__parent__._cast(_4939.ShaftHubConnectionCompoundModalAnalysis)

    @property
    def spiral_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4942.SpiralBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4942,
        )

        return self.__parent__._cast(_4942.SpiralBevelGearCompoundModalAnalysis)

    @property
    def spring_damper_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4947.SpringDamperHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4947,
        )

        return self.__parent__._cast(_4947.SpringDamperHalfCompoundModalAnalysis)

    @property
    def straight_bevel_diff_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4948.StraightBevelDiffGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4948,
        )

        return self.__parent__._cast(_4948.StraightBevelDiffGearCompoundModalAnalysis)

    @property
    def straight_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4951.StraightBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4951,
        )

        return self.__parent__._cast(_4951.StraightBevelGearCompoundModalAnalysis)

    @property
    def straight_bevel_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4954.StraightBevelPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4954,
        )

        return self.__parent__._cast(_4954.StraightBevelPlanetGearCompoundModalAnalysis)

    @property
    def straight_bevel_sun_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4955.StraightBevelSunGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4955,
        )

        return self.__parent__._cast(_4955.StraightBevelSunGearCompoundModalAnalysis)

    @property
    def synchroniser_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4957.SynchroniserHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4957,
        )

        return self.__parent__._cast(_4957.SynchroniserHalfCompoundModalAnalysis)

    @property
    def synchroniser_part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4958.SynchroniserPartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4958,
        )

        return self.__parent__._cast(_4958.SynchroniserPartCompoundModalAnalysis)

    @property
    def synchroniser_sleeve_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4959.SynchroniserSleeveCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4959,
        )

        return self.__parent__._cast(_4959.SynchroniserSleeveCompoundModalAnalysis)

    @property
    def torque_converter_pump_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4962.TorqueConverterPumpCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4962,
        )

        return self.__parent__._cast(_4962.TorqueConverterPumpCompoundModalAnalysis)

    @property
    def torque_converter_turbine_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4963.TorqueConverterTurbineCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4963,
        )

        return self.__parent__._cast(_4963.TorqueConverterTurbineCompoundModalAnalysis)

    @property
    def unbalanced_mass_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4964.UnbalancedMassCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4964,
        )

        return self.__parent__._cast(_4964.UnbalancedMassCompoundModalAnalysis)

    @property
    def virtual_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4965.VirtualComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4965,
        )

        return self.__parent__._cast(_4965.VirtualComponentCompoundModalAnalysis)

    @property
    def worm_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4966.WormGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4966,
        )

        return self.__parent__._cast(_4966.WormGearCompoundModalAnalysis)

    @property
    def zerol_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4969.ZerolBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4969,
        )

        return self.__parent__._cast(_4969.ZerolBevelGearCompoundModalAnalysis)

    @property
    def mountable_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "MountableComponentCompoundModalAnalysis":
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
class MountableComponentCompoundModalAnalysis(_4866.ComponentCompoundModalAnalysis):
    """MountableComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_4771.MountableComponentModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis]

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
    ) -> "List[_4771.MountableComponentModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_MountableComponentCompoundModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_MountableComponentCompoundModalAnalysis
        """
        return _Cast_MountableComponentCompoundModalAnalysis(self)
