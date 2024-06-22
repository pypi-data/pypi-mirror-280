"""GearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5573
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "GearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.nodal_analysis import _69
    from mastapy._private.system_model.connections_and_sockets.gears import _2366
    from mastapy._private.nodal_analysis.nodal_entities.external_force import _157
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
        _5503,
        _5513,
        _5518,
        _5532,
        _5535,
        _5550,
        _5556,
        _5566,
        _5574,
        _5577,
        _5580,
        _5616,
        _5623,
        _5626,
        _5644,
        _5647,
        _5538,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7707,
        _7703,
    )
    from mastapy._private.system_model.analyses_and_results import _2732, _2736, _2734

    Self = TypeVar("Self", bound="GearMeshMultibodyDynamicsAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearMeshMultibodyDynamicsAnalysis:
    """Special nested class for casting GearMeshMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "GearMeshMultibodyDynamicsAnalysis"

    @property
    def inter_mountable_component_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5573.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
        return self.__parent__._cast(
            _5573.InterMountableComponentConnectionMultibodyDynamicsAnalysis
        )

    @property
    def connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5538.ConnectionMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5538,
        )

        return self.__parent__._cast(_5538.ConnectionMultibodyDynamicsAnalysis)

    @property
    def connection_time_series_load_analysis_case(
        self: "CastSelf",
    ) -> "_7707.ConnectionTimeSeriesLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7707,
        )

        return self.__parent__._cast(_7707.ConnectionTimeSeriesLoadAnalysisCase)

    @property
    def connection_analysis_case(self: "CastSelf") -> "_7703.ConnectionAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7703,
        )

        return self.__parent__._cast(_7703.ConnectionAnalysisCase)

    @property
    def connection_analysis(self: "CastSelf") -> "_2732.ConnectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2732

        return self.__parent__._cast(_2732.ConnectionAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5503.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5503,
        )

        return self.__parent__._cast(
            _5503.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
        )

    @property
    def bevel_differential_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5513.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5513,
        )

        return self.__parent__._cast(
            _5513.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
        )

    @property
    def bevel_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5518.BevelGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5518,
        )

        return self.__parent__._cast(_5518.BevelGearMeshMultibodyDynamicsAnalysis)

    @property
    def concept_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5532.ConceptGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5532,
        )

        return self.__parent__._cast(_5532.ConceptGearMeshMultibodyDynamicsAnalysis)

    @property
    def conical_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5535.ConicalGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5535,
        )

        return self.__parent__._cast(_5535.ConicalGearMeshMultibodyDynamicsAnalysis)

    @property
    def cylindrical_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5550.CylindricalGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5550,
        )

        return self.__parent__._cast(_5550.CylindricalGearMeshMultibodyDynamicsAnalysis)

    @property
    def face_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5556.FaceGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5556,
        )

        return self.__parent__._cast(_5556.FaceGearMeshMultibodyDynamicsAnalysis)

    @property
    def hypoid_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5566.HypoidGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5566,
        )

        return self.__parent__._cast(_5566.HypoidGearMeshMultibodyDynamicsAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5574.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5574,
        )

        return self.__parent__._cast(
            _5574.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5577.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5577,
        )

        return self.__parent__._cast(
            _5577.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5580.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5580,
        )

        return self.__parent__._cast(
            _5580.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
        )

    @property
    def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5616.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5616,
        )

        return self.__parent__._cast(_5616.SpiralBevelGearMeshMultibodyDynamicsAnalysis)

    @property
    def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5623.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5623,
        )

        return self.__parent__._cast(
            _5623.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5626.StraightBevelGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5626,
        )

        return self.__parent__._cast(
            _5626.StraightBevelGearMeshMultibodyDynamicsAnalysis
        )

    @property
    def worm_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5644.WormGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5644,
        )

        return self.__parent__._cast(_5644.WormGearMeshMultibodyDynamicsAnalysis)

    @property
    def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5647.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5647,
        )

        return self.__parent__._cast(_5647.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

    @property
    def gear_mesh_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "GearMeshMultibodyDynamicsAnalysis":
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
class GearMeshMultibodyDynamicsAnalysis(
    _5573.InterMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """GearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def average_sliding_velocity_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageSlidingVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def average_sliding_velocity_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageSlidingVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_status(self: "Self") -> "_69.GearMeshContactStatus":
        """mastapy._private.nodal_analysis.GearMeshContactStatus

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.GearMeshContactStatus"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.nodal_analysis._69", "GearMeshContactStatus"
        )(value)

    @property
    def equivalent_misalignment_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentMisalignmentLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_misalignment_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentMisalignmentRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def force_normal_to_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceNormalToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def force_normal_to_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceNormalToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImpactPowerLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImpactPowerRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_total(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImpactPowerTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_time_step(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTimeStep

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_loss(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_tilt_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentDueToTiltLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_tilt_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentDueToTiltRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_separations_left_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalSeparationsLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_separations_right_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalSeparationsRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_velocity_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_velocity_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLineVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLineVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Separation

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_normal_to_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationNormalToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_normal_to_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationNormalToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_transverse_to_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationTransverseToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_transverse_to_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationTransverseToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrainEnergyLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrainEnergyRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_total(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrainEnergyTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed_gear_a(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingSpeedGearA

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed_gear_b(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingSpeedGearB

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stiffness_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseStiffnessLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stiffness_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseStiffnessRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: "Self") -> "_2366.GearMesh":
        """mastapy._private.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank(self: "Self") -> "_157.ExternalForceLineContactEntity":
        """mastapy._private.nodal_analysis.nodal_entities.external_force.ExternalForceLineContactEntity

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: "Self") -> "_157.ExternalForceLineContactEntity":
        """mastapy._private.nodal_analysis.nodal_entities.external_force.ExternalForceLineContactEntity

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_GearMeshMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_GearMeshMultibodyDynamicsAnalysis
        """
        return _Cast_GearMeshMultibodyDynamicsAnalysis(self)
