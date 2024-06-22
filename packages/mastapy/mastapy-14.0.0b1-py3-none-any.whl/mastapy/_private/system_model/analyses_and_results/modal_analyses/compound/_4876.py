"""ConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4718
    from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
        _4844,
        _4846,
        _4850,
        _4853,
        _4858,
        _4863,
        _4865,
        _4868,
        _4871,
        _4874,
        _4879,
        _4881,
        _4885,
        _4887,
        _4889,
        _4895,
        _4900,
        _4904,
        _4906,
        _4908,
        _4911,
        _4914,
        _4924,
        _4926,
        _4933,
        _4936,
        _4940,
        _4943,
        _4946,
        _4949,
        _4952,
        _4961,
        _4967,
        _4970,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7708
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="ConnectionCompoundModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConnectionCompoundModalAnalysis._Cast_ConnectionCompoundModalAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionCompoundModalAnalysis:
    """Special nested class for casting ConnectionCompoundModalAnalysis to subclasses."""

    __parent__: "ConnectionCompoundModalAnalysis"

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.ConnectionCompoundAnalysis":
        return self.__parent__._cast(_7704.ConnectionCompoundAnalysis)

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
    def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4844.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4844,
        )

        return self.__parent__._cast(
            _4844.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
        )

    @property
    def agma_gleason_conical_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4846.AGMAGleasonConicalGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4846,
        )

        return self.__parent__._cast(
            _4846.AGMAGleasonConicalGearMeshCompoundModalAnalysis
        )

    @property
    def belt_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4850.BeltConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4850,
        )

        return self.__parent__._cast(_4850.BeltConnectionCompoundModalAnalysis)

    @property
    def bevel_differential_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4853.BevelDifferentialGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4853,
        )

        return self.__parent__._cast(
            _4853.BevelDifferentialGearMeshCompoundModalAnalysis
        )

    @property
    def bevel_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4858.BevelGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4858,
        )

        return self.__parent__._cast(_4858.BevelGearMeshCompoundModalAnalysis)

    @property
    def clutch_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4863.ClutchConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4863,
        )

        return self.__parent__._cast(_4863.ClutchConnectionCompoundModalAnalysis)

    @property
    def coaxial_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4865.CoaxialConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4865,
        )

        return self.__parent__._cast(_4865.CoaxialConnectionCompoundModalAnalysis)

    @property
    def concept_coupling_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4868.ConceptCouplingConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4868,
        )

        return self.__parent__._cast(
            _4868.ConceptCouplingConnectionCompoundModalAnalysis
        )

    @property
    def concept_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4871.ConceptGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4871,
        )

        return self.__parent__._cast(_4871.ConceptGearMeshCompoundModalAnalysis)

    @property
    def conical_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4874.ConicalGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4874,
        )

        return self.__parent__._cast(_4874.ConicalGearMeshCompoundModalAnalysis)

    @property
    def coupling_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4879.CouplingConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4879,
        )

        return self.__parent__._cast(_4879.CouplingConnectionCompoundModalAnalysis)

    @property
    def cvt_belt_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4881.CVTBeltConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4881,
        )

        return self.__parent__._cast(_4881.CVTBeltConnectionCompoundModalAnalysis)

    @property
    def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4885.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4885,
        )

        return self.__parent__._cast(
            _4885.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4887.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4887,
        )

        return self.__parent__._cast(
            _4887.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
        )

    @property
    def cylindrical_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4889.CylindricalGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4889,
        )

        return self.__parent__._cast(_4889.CylindricalGearMeshCompoundModalAnalysis)

    @property
    def face_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4895.FaceGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4895,
        )

        return self.__parent__._cast(_4895.FaceGearMeshCompoundModalAnalysis)

    @property
    def gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4900.GearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4900,
        )

        return self.__parent__._cast(_4900.GearMeshCompoundModalAnalysis)

    @property
    def hypoid_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4904.HypoidGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4904,
        )

        return self.__parent__._cast(_4904.HypoidGearMeshCompoundModalAnalysis)

    @property
    def inter_mountable_component_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4906.InterMountableComponentConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4906,
        )

        return self.__parent__._cast(
            _4906.InterMountableComponentConnectionCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4908.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4908,
        )

        return self.__parent__._cast(
            _4908.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4911.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4911,
        )

        return self.__parent__._cast(
            _4911.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4914.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4914,
        )

        return self.__parent__._cast(
            _4914.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
        )

    @property
    def part_to_part_shear_coupling_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4924.PartToPartShearCouplingConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4924,
        )

        return self.__parent__._cast(
            _4924.PartToPartShearCouplingConnectionCompoundModalAnalysis
        )

    @property
    def planetary_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4926.PlanetaryConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4926,
        )

        return self.__parent__._cast(_4926.PlanetaryConnectionCompoundModalAnalysis)

    @property
    def ring_pins_to_disc_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4933.RingPinsToDiscConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4933,
        )

        return self.__parent__._cast(
            _4933.RingPinsToDiscConnectionCompoundModalAnalysis
        )

    @property
    def rolling_ring_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4936.RollingRingConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4936,
        )

        return self.__parent__._cast(_4936.RollingRingConnectionCompoundModalAnalysis)

    @property
    def shaft_to_mountable_component_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4940.ShaftToMountableComponentConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4940,
        )

        return self.__parent__._cast(
            _4940.ShaftToMountableComponentConnectionCompoundModalAnalysis
        )

    @property
    def spiral_bevel_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4943.SpiralBevelGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4943,
        )

        return self.__parent__._cast(_4943.SpiralBevelGearMeshCompoundModalAnalysis)

    @property
    def spring_damper_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4946.SpringDamperConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4946,
        )

        return self.__parent__._cast(_4946.SpringDamperConnectionCompoundModalAnalysis)

    @property
    def straight_bevel_diff_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4949.StraightBevelDiffGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4949,
        )

        return self.__parent__._cast(
            _4949.StraightBevelDiffGearMeshCompoundModalAnalysis
        )

    @property
    def straight_bevel_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4952.StraightBevelGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4952,
        )

        return self.__parent__._cast(_4952.StraightBevelGearMeshCompoundModalAnalysis)

    @property
    def torque_converter_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4961.TorqueConverterConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4961,
        )

        return self.__parent__._cast(
            _4961.TorqueConverterConnectionCompoundModalAnalysis
        )

    @property
    def worm_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4967.WormGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4967,
        )

        return self.__parent__._cast(_4967.WormGearMeshCompoundModalAnalysis)

    @property
    def zerol_bevel_gear_mesh_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4970.ZerolBevelGearMeshCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4970,
        )

        return self.__parent__._cast(_4970.ZerolBevelGearMeshCompoundModalAnalysis)

    @property
    def connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "ConnectionCompoundModalAnalysis":
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
class ConnectionCompoundModalAnalysis(_7704.ConnectionCompoundAnalysis):
    """ConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_COMPOUND_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_4718.ConnectionModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.ConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4718.ConnectionModalAnalysis]":
        """List[mastapy._private.system_model.analyses_and_results.modal_analyses.ConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ConnectionCompoundModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ConnectionCompoundModalAnalysis
        """
        return _Cast_ConnectionCompoundModalAnalysis(self)
