"""ConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import conversion, utility
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7460,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7563,
        _7565,
        _7569,
        _7572,
        _7577,
        _7582,
        _7584,
        _7587,
        _7590,
        _7593,
        _7598,
        _7600,
        _7604,
        _7606,
        _7608,
        _7614,
        _7619,
        _7623,
        _7625,
        _7627,
        _7630,
        _7633,
        _7643,
        _7645,
        _7652,
        _7655,
        _7659,
        _7662,
        _7665,
        _7668,
        _7671,
        _7680,
        _7686,
        _7689,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7708
    from mastapy._private.system_model.analyses_and_results import _2734

    Self = TypeVar("Self", bound="ConnectionCompoundAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionCompoundAdvancedSystemDeflection:
    """Special nested class for casting ConnectionCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "ConnectionCompoundAdvancedSystemDeflection"

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
    def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7563.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7563,
        )

        return self.__parent__._cast(
            _7563.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7565.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7565,
        )

        return self.__parent__._cast(
            _7565.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def belt_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7569.BeltConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7569,
        )

        return self.__parent__._cast(
            _7569.BeltConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7572.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7572,
        )

        return self.__parent__._cast(
            _7572.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7577.BevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7577,
        )

        return self.__parent__._cast(
            _7577.BevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def clutch_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7582.ClutchConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7582,
        )

        return self.__parent__._cast(
            _7582.ClutchConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def coaxial_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7584.CoaxialConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7584,
        )

        return self.__parent__._cast(
            _7584.CoaxialConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def concept_coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7587.ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7587,
        )

        return self.__parent__._cast(
            _7587.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def concept_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7590.ConceptGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7590,
        )

        return self.__parent__._cast(
            _7590.ConceptGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def conical_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7593.ConicalGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7593,
        )

        return self.__parent__._cast(
            _7593.ConicalGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7598.CouplingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7598,
        )

        return self.__parent__._cast(
            _7598.CouplingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def cvt_belt_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7600.CVTBeltConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7600,
        )

        return self.__parent__._cast(
            _7600.CVTBeltConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7604.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7604,
        )

        return self.__parent__._cast(
            _7604.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> (
        "_7606.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7606,
        )

        return self.__parent__._cast(
            _7606.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7608.CylindricalGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7608,
        )

        return self.__parent__._cast(
            _7608.CylindricalGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def face_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7614.FaceGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7614,
        )

        return self.__parent__._cast(_7614.FaceGearMeshCompoundAdvancedSystemDeflection)

    @property
    def gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7619.GearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7619,
        )

        return self.__parent__._cast(_7619.GearMeshCompoundAdvancedSystemDeflection)

    @property
    def hypoid_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7623.HypoidGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7623,
        )

        return self.__parent__._cast(
            _7623.HypoidGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def inter_mountable_component_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7625.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7625,
        )

        return self.__parent__._cast(
            _7625.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> (
        "_7627.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7627,
        )

        return self.__parent__._cast(
            _7627.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7630.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7630,
        )

        return self.__parent__._cast(
            _7630.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7633.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7633,
        )

        return self.__parent__._cast(
            _7633.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7643.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7643,
        )

        return self.__parent__._cast(
            _7643.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def planetary_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7645.PlanetaryConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7645,
        )

        return self.__parent__._cast(
            _7645.PlanetaryConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def ring_pins_to_disc_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7652.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7652,
        )

        return self.__parent__._cast(
            _7652.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def rolling_ring_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7655.RollingRingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7655,
        )

        return self.__parent__._cast(
            _7655.RollingRingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7659.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7659,
        )

        return self.__parent__._cast(
            _7659.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7662.SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7662,
        )

        return self.__parent__._cast(
            _7662.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def spring_damper_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7665.SpringDamperConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7665,
        )

        return self.__parent__._cast(
            _7665.SpringDamperConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7668.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7668,
        )

        return self.__parent__._cast(
            _7668.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7671.StraightBevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7671,
        )

        return self.__parent__._cast(
            _7671.StraightBevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7680.TorqueConverterConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7680,
        )

        return self.__parent__._cast(
            _7680.TorqueConverterConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def worm_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7686.WormGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7686,
        )

        return self.__parent__._cast(_7686.WormGearMeshCompoundAdvancedSystemDeflection)

    @property
    def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7689.ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7689,
        )

        return self.__parent__._cast(
            _7689.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "ConnectionCompoundAdvancedSystemDeflection":
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
class ConnectionCompoundAdvancedSystemDeflection(_7704.ConnectionCompoundAnalysis):
    """ConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_7460.ConnectionAdvancedSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_system_deflections.ConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7460.ConnectionAdvancedSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.advanced_system_deflections.ConnectionAdvancedSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_ConnectionCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_ConnectionCompoundAdvancedSystemDeflection
        """
        return _Cast_ConnectionCompoundAdvancedSystemDeflection(self)
