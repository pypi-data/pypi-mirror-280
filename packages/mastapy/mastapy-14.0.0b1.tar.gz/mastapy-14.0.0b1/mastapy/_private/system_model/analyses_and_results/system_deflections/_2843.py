"""GearSetSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.analyses_and_results.system_deflections import _2891
from mastapy._private._internal.cast_exception import CastException

_GEAR_SET_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationDetail"
)
_GEAR_SET_MODES = python_net_import("SMT.MastaAPI.Gears", "GearSetModes")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_BOOLEAN = python_net_import("System", "Boolean")
_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "GearSetSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2588
    from mastapy._private.gears.rating import _374
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2844,
        _2842,
        _2773,
        _2785,
        _2790,
        _2804,
        _2808,
        _2825,
        _2826,
        _2827,
        _2838,
        _2847,
        _2852,
        _2855,
        _2858,
        _2893,
        _2899,
        _2902,
        _2922,
        _2925,
        _2768,
        _2870,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4198
    from mastapy._private.gears.analysis import _1269, _1266
    from mastapy._private.gears import _339
    from mastapy._private import _7724
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7712,
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="GearSetSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf", bound="GearSetSystemDeflection._Cast_GearSetSystemDeflection"
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearSetSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearSetSystemDeflection:
    """Special nested class for casting GearSetSystemDeflection to subclasses."""

    __parent__: "GearSetSystemDeflection"

    @property
    def specialised_assembly_system_deflection(
        self: "CastSelf",
    ) -> "_2891.SpecialisedAssemblySystemDeflection":
        return self.__parent__._cast(_2891.SpecialisedAssemblySystemDeflection)

    @property
    def abstract_assembly_system_deflection(
        self: "CastSelf",
    ) -> "_2768.AbstractAssemblySystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2768,
        )

        return self.__parent__._cast(_2768.AbstractAssemblySystemDeflection)

    @property
    def part_system_deflection(self: "CastSelf") -> "_2870.PartSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2870,
        )

        return self.__parent__._cast(_2870.PartSystemDeflection)

    @property
    def part_fe_analysis(self: "CastSelf") -> "_7712.PartFEAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7712,
        )

        return self.__parent__._cast(_7712.PartFEAnalysis)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7713.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7713,
        )

        return self.__parent__._cast(_7713.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7710.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

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
    def agma_gleason_conical_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2773.AGMAGleasonConicalGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2773,
        )

        return self.__parent__._cast(_2773.AGMAGleasonConicalGearSetSystemDeflection)

    @property
    def bevel_differential_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2785.BevelDifferentialGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2785,
        )

        return self.__parent__._cast(_2785.BevelDifferentialGearSetSystemDeflection)

    @property
    def bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2790.BevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2790,
        )

        return self.__parent__._cast(_2790.BevelGearSetSystemDeflection)

    @property
    def concept_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2804.ConceptGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2804,
        )

        return self.__parent__._cast(_2804.ConceptGearSetSystemDeflection)

    @property
    def conical_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2808.ConicalGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2808,
        )

        return self.__parent__._cast(_2808.ConicalGearSetSystemDeflection)

    @property
    def cylindrical_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2825.CylindricalGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2825,
        )

        return self.__parent__._cast(_2825.CylindricalGearSetSystemDeflection)

    @property
    def cylindrical_gear_set_system_deflection_timestep(
        self: "CastSelf",
    ) -> "_2826.CylindricalGearSetSystemDeflectionTimestep":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2826,
        )

        return self.__parent__._cast(_2826.CylindricalGearSetSystemDeflectionTimestep)

    @property
    def cylindrical_gear_set_system_deflection_with_ltca_results(
        self: "CastSelf",
    ) -> "_2827.CylindricalGearSetSystemDeflectionWithLTCAResults":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2827,
        )

        return self.__parent__._cast(
            _2827.CylindricalGearSetSystemDeflectionWithLTCAResults
        )

    @property
    def face_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2838.FaceGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2838,
        )

        return self.__parent__._cast(_2838.FaceGearSetSystemDeflection)

    @property
    def hypoid_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2847.HypoidGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2847,
        )

        return self.__parent__._cast(_2847.HypoidGearSetSystemDeflection)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2852.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2852,
        )

        return self.__parent__._cast(
            _2852.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2855.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2855,
        )

        return self.__parent__._cast(
            _2855.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2858.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2858,
        )

        return self.__parent__._cast(
            _2858.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
        )

    @property
    def spiral_bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2893.SpiralBevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2893,
        )

        return self.__parent__._cast(_2893.SpiralBevelGearSetSystemDeflection)

    @property
    def straight_bevel_diff_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2899.StraightBevelDiffGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2899,
        )

        return self.__parent__._cast(_2899.StraightBevelDiffGearSetSystemDeflection)

    @property
    def straight_bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2902.StraightBevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2902,
        )

        return self.__parent__._cast(_2902.StraightBevelGearSetSystemDeflection)

    @property
    def worm_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2922.WormGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2922,
        )

        return self.__parent__._cast(_2922.WormGearSetSystemDeflection)

    @property
    def zerol_bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2925.ZerolBevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2925,
        )

        return self.__parent__._cast(_2925.ZerolBevelGearSetSystemDeflection)

    @property
    def gear_set_system_deflection(self: "CastSelf") -> "GearSetSystemDeflection":
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
class GearSetSystemDeflection(_2891.SpecialisedAssemblySystemDeflection):
    """GearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_SET_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2588.GearSet":
        """mastapy._private.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: "Self") -> "_374.GearSetRating":
        """mastapy._private.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_system_deflection(self: "Self") -> "List[_2844.GearSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.GearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_system_deflection(
        self: "Self",
    ) -> "List[_2842.GearMeshSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: "Self") -> "_4198.GearSetPowerFlow":
        """mastapy._private.system_model.analyses_and_results.power_flows.GearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def analysis_for(
        self: "Self",
        gear_set_imp_detail: "_1269.GearSetImplementationDetail",
        gear_set_mode: "_339.GearSetModes",
    ) -> "_1266.GearSetImplementationAnalysis":
        """mastapy._private.gears.analysis.GearSetImplementationAnalysis

        Args:
            gear_set_imp_detail (mastapy._private.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy._private.gears.GearSetModes)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        method_result = self.wrapped.AnalysisFor(
            gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def implementation_detail_results_failed_for(
        self: "Self",
        gear_set_imp_detail: "_1269.GearSetImplementationDetail",
        gear_set_mode: "_339.GearSetModes",
    ) -> "bool":
        """bool

        Args:
            gear_set_imp_detail (mastapy._private.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy._private.gears.GearSetModes)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        method_result = self.wrapped.ImplementationDetailResultsFailedFor(
            gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode
        )
        return method_result

    @enforce_parameter_types
    def perform_implementation_detail_analysis_with_progress(
        self: "Self",
        imp_detail: "_1269.GearSetImplementationDetail",
        gear_set_mode: "_339.GearSetModes",
        progress: "_7724.TaskProgress",
        run_all_planetary_meshes: "bool" = True,
    ) -> None:
        """Method does not return.

        Args:
            imp_detail (mastapy._private.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy._private.gears.GearSetModes)
            progress (mastapy._private.TaskProgress)
            run_all_planetary_meshes (bool, optional)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[
            _GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _TASK_PROGRESS, _BOOLEAN
        ](
            imp_detail.wrapped if imp_detail else None,
            gear_set_mode,
            progress.wrapped if progress else None,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
        )

    @enforce_parameter_types
    def perform_implementation_detail_analysis(
        self: "Self",
        imp_detail: "_1269.GearSetImplementationDetail",
        gear_set_mode: "_339.GearSetModes",
        run_all_planetary_meshes: "bool" = True,
    ) -> None:
        """Method does not return.

        Args:
            imp_detail (mastapy._private.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy._private.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[
            _GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _BOOLEAN
        ](
            imp_detail.wrapped if imp_detail else None,
            gear_set_mode,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
        )

    @property
    def cast_to(self: "Self") -> "_Cast_GearSetSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_GearSetSystemDeflection
        """
        return _Cast_GearSetSystemDeflection(self)
