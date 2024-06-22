"""GearMeshDesignAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.analysis import _1254
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_MESH_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshDesignAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.analysis import _1256, _1264, _1261, _1262, _1263
    from mastapy._private.gears.manufacturing.cylindrical import _641, _642, _645
    from mastapy._private.gears.manufacturing.bevel import _807, _808, _809, _810
    from mastapy._private.gears.ltca import _864
    from mastapy._private.gears.ltca.cylindrical import _880
    from mastapy._private.gears.ltca.conical import _893
    from mastapy._private.gears.load_case import _898
    from mastapy._private.gears.load_case.worm import _901
    from mastapy._private.gears.load_case.face import _904
    from mastapy._private.gears.load_case.cylindrical import _907
    from mastapy._private.gears.load_case.conical import _910
    from mastapy._private.gears.load_case.concept import _913
    from mastapy._private.gears.load_case.bevel import _915
    from mastapy._private.gears.gear_two_d_fe_analysis import _917, _918
    from mastapy._private.gears.gear_designs.face import _1016
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1130,
        _1131,
    )
    from mastapy._private.gears.fe_model import _1236
    from mastapy._private.gears.fe_model.cylindrical import _1240
    from mastapy._private.gears.fe_model.conical import _1243

    Self = TypeVar("Self", bound="GearMeshDesignAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshDesignAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearMeshDesignAnalysis:
    """Special nested class for casting GearMeshDesignAnalysis to subclasses."""

    __parent__: "GearMeshDesignAnalysis"

    @property
    def abstract_gear_mesh_analysis(
        self: "CastSelf",
    ) -> "_1254.AbstractGearMeshAnalysis":
        return self.__parent__._cast(_1254.AbstractGearMeshAnalysis)

    @property
    def cylindrical_manufactured_gear_mesh_duty_cycle(
        self: "CastSelf",
    ) -> "_641.CylindricalManufacturedGearMeshDutyCycle":
        from mastapy._private.gears.manufacturing.cylindrical import _641

        return self.__parent__._cast(_641.CylindricalManufacturedGearMeshDutyCycle)

    @property
    def cylindrical_manufactured_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_642.CylindricalManufacturedGearMeshLoadCase":
        from mastapy._private.gears.manufacturing.cylindrical import _642

        return self.__parent__._cast(_642.CylindricalManufacturedGearMeshLoadCase)

    @property
    def cylindrical_mesh_manufacturing_config(
        self: "CastSelf",
    ) -> "_645.CylindricalMeshManufacturingConfig":
        from mastapy._private.gears.manufacturing.cylindrical import _645

        return self.__parent__._cast(_645.CylindricalMeshManufacturingConfig)

    @property
    def conical_mesh_manufacturing_analysis(
        self: "CastSelf",
    ) -> "_807.ConicalMeshManufacturingAnalysis":
        from mastapy._private.gears.manufacturing.bevel import _807

        return self.__parent__._cast(_807.ConicalMeshManufacturingAnalysis)

    @property
    def conical_mesh_manufacturing_config(
        self: "CastSelf",
    ) -> "_808.ConicalMeshManufacturingConfig":
        from mastapy._private.gears.manufacturing.bevel import _808

        return self.__parent__._cast(_808.ConicalMeshManufacturingConfig)

    @property
    def conical_mesh_micro_geometry_config(
        self: "CastSelf",
    ) -> "_809.ConicalMeshMicroGeometryConfig":
        from mastapy._private.gears.manufacturing.bevel import _809

        return self.__parent__._cast(_809.ConicalMeshMicroGeometryConfig)

    @property
    def conical_mesh_micro_geometry_config_base(
        self: "CastSelf",
    ) -> "_810.ConicalMeshMicroGeometryConfigBase":
        from mastapy._private.gears.manufacturing.bevel import _810

        return self.__parent__._cast(_810.ConicalMeshMicroGeometryConfigBase)

    @property
    def gear_mesh_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_864.GearMeshLoadDistributionAnalysis":
        from mastapy._private.gears.ltca import _864

        return self.__parent__._cast(_864.GearMeshLoadDistributionAnalysis)

    @property
    def cylindrical_gear_mesh_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_880.CylindricalGearMeshLoadDistributionAnalysis":
        from mastapy._private.gears.ltca.cylindrical import _880

        return self.__parent__._cast(_880.CylindricalGearMeshLoadDistributionAnalysis)

    @property
    def conical_mesh_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_893.ConicalMeshLoadDistributionAnalysis":
        from mastapy._private.gears.ltca.conical import _893

        return self.__parent__._cast(_893.ConicalMeshLoadDistributionAnalysis)

    @property
    def mesh_load_case(self: "CastSelf") -> "_898.MeshLoadCase":
        from mastapy._private.gears.load_case import _898

        return self.__parent__._cast(_898.MeshLoadCase)

    @property
    def worm_mesh_load_case(self: "CastSelf") -> "_901.WormMeshLoadCase":
        from mastapy._private.gears.load_case.worm import _901

        return self.__parent__._cast(_901.WormMeshLoadCase)

    @property
    def face_mesh_load_case(self: "CastSelf") -> "_904.FaceMeshLoadCase":
        from mastapy._private.gears.load_case.face import _904

        return self.__parent__._cast(_904.FaceMeshLoadCase)

    @property
    def cylindrical_mesh_load_case(self: "CastSelf") -> "_907.CylindricalMeshLoadCase":
        from mastapy._private.gears.load_case.cylindrical import _907

        return self.__parent__._cast(_907.CylindricalMeshLoadCase)

    @property
    def conical_mesh_load_case(self: "CastSelf") -> "_910.ConicalMeshLoadCase":
        from mastapy._private.gears.load_case.conical import _910

        return self.__parent__._cast(_910.ConicalMeshLoadCase)

    @property
    def concept_mesh_load_case(self: "CastSelf") -> "_913.ConceptMeshLoadCase":
        from mastapy._private.gears.load_case.concept import _913

        return self.__parent__._cast(_913.ConceptMeshLoadCase)

    @property
    def bevel_mesh_load_case(self: "CastSelf") -> "_915.BevelMeshLoadCase":
        from mastapy._private.gears.load_case.bevel import _915

        return self.__parent__._cast(_915.BevelMeshLoadCase)

    @property
    def cylindrical_gear_mesh_tiff_analysis(
        self: "CastSelf",
    ) -> "_917.CylindricalGearMeshTIFFAnalysis":
        from mastapy._private.gears.gear_two_d_fe_analysis import _917

        return self.__parent__._cast(_917.CylindricalGearMeshTIFFAnalysis)

    @property
    def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
        self: "CastSelf",
    ) -> "_918.CylindricalGearMeshTIFFAnalysisDutyCycle":
        from mastapy._private.gears.gear_two_d_fe_analysis import _918

        return self.__parent__._cast(_918.CylindricalGearMeshTIFFAnalysisDutyCycle)

    @property
    def face_gear_mesh_micro_geometry(
        self: "CastSelf",
    ) -> "_1016.FaceGearMeshMicroGeometry":
        from mastapy._private.gears.gear_designs.face import _1016

        return self.__parent__._cast(_1016.FaceGearMeshMicroGeometry)

    @property
    def cylindrical_gear_mesh_micro_geometry(
        self: "CastSelf",
    ) -> "_1130.CylindricalGearMeshMicroGeometry":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1130

        return self.__parent__._cast(_1130.CylindricalGearMeshMicroGeometry)

    @property
    def cylindrical_gear_mesh_micro_geometry_duty_cycle(
        self: "CastSelf",
    ) -> "_1131.CylindricalGearMeshMicroGeometryDutyCycle":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1131

        return self.__parent__._cast(_1131.CylindricalGearMeshMicroGeometryDutyCycle)

    @property
    def gear_mesh_fe_model(self: "CastSelf") -> "_1236.GearMeshFEModel":
        from mastapy._private.gears.fe_model import _1236

        return self.__parent__._cast(_1236.GearMeshFEModel)

    @property
    def cylindrical_gear_mesh_fe_model(
        self: "CastSelf",
    ) -> "_1240.CylindricalGearMeshFEModel":
        from mastapy._private.gears.fe_model.cylindrical import _1240

        return self.__parent__._cast(_1240.CylindricalGearMeshFEModel)

    @property
    def conical_mesh_fe_model(self: "CastSelf") -> "_1243.ConicalMeshFEModel":
        from mastapy._private.gears.fe_model.conical import _1243

        return self.__parent__._cast(_1243.ConicalMeshFEModel)

    @property
    def gear_mesh_implementation_analysis(
        self: "CastSelf",
    ) -> "_1261.GearMeshImplementationAnalysis":
        from mastapy._private.gears.analysis import _1261

        return self.__parent__._cast(_1261.GearMeshImplementationAnalysis)

    @property
    def gear_mesh_implementation_analysis_duty_cycle(
        self: "CastSelf",
    ) -> "_1262.GearMeshImplementationAnalysisDutyCycle":
        from mastapy._private.gears.analysis import _1262

        return self.__parent__._cast(_1262.GearMeshImplementationAnalysisDutyCycle)

    @property
    def gear_mesh_implementation_detail(
        self: "CastSelf",
    ) -> "_1263.GearMeshImplementationDetail":
        from mastapy._private.gears.analysis import _1263

        return self.__parent__._cast(_1263.GearMeshImplementationDetail)

    @property
    def gear_mesh_design_analysis(self: "CastSelf") -> "GearMeshDesignAnalysis":
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
class GearMeshDesignAnalysis(_1254.AbstractGearMeshAnalysis):
    """GearMeshDesignAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_MESH_DESIGN_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def gear_a(self: "Self") -> "_1256.GearDesignAnalysis":
        """mastapy._private.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: "Self") -> "_1256.GearDesignAnalysis":
        """mastapy._private.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set(self: "Self") -> "_1264.GearSetDesignAnalysis":
        """mastapy._private.gears.analysis.GearSetDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_GearMeshDesignAnalysis":
        """Cast to another type.

        Returns:
            _Cast_GearMeshDesignAnalysis
        """
        return _Cast_GearMeshDesignAnalysis(self)
