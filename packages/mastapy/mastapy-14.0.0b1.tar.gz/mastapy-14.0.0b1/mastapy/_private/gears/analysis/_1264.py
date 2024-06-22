"""GearSetDesignAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.analysis import _1255
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_GEAR_SET_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetDesignAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical import _643, _644, _648
    from mastapy._private.gears.manufacturing.bevel import _813, _814, _815, _816
    from mastapy._private.gears.ltca import _869
    from mastapy._private.gears.ltca.cylindrical import _883, _885
    from mastapy._private.gears.ltca.conical import _891
    from mastapy._private.gears.load_case import _897
    from mastapy._private.gears.load_case.worm import _900
    from mastapy._private.gears.load_case.face import _903
    from mastapy._private.gears.load_case.cylindrical import _906
    from mastapy._private.gears.load_case.conical import _909
    from mastapy._private.gears.load_case.concept import _912
    from mastapy._private.gears.load_case.bevel import _916
    from mastapy._private.gears.gear_two_d_fe_analysis import _919, _920
    from mastapy._private.gears.gear_designs.face import _1020
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1139,
        _1140,
    )
    from mastapy._private.gears.fe_model import _1238
    from mastapy._private.gears.fe_model.cylindrical import _1241
    from mastapy._private.gears.fe_model.conical import _1244
    from mastapy._private.gears.analysis import _1266, _1267, _1268, _1269

    Self = TypeVar("Self", bound="GearSetDesignAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="GearSetDesignAnalysis._Cast_GearSetDesignAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDesignAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearSetDesignAnalysis:
    """Special nested class for casting GearSetDesignAnalysis to subclasses."""

    __parent__: "GearSetDesignAnalysis"

    @property
    def abstract_gear_set_analysis(self: "CastSelf") -> "_1255.AbstractGearSetAnalysis":
        return self.__parent__._cast(_1255.AbstractGearSetAnalysis)

    @property
    def cylindrical_manufactured_gear_set_duty_cycle(
        self: "CastSelf",
    ) -> "_643.CylindricalManufacturedGearSetDutyCycle":
        from mastapy._private.gears.manufacturing.cylindrical import _643

        return self.__parent__._cast(_643.CylindricalManufacturedGearSetDutyCycle)

    @property
    def cylindrical_manufactured_gear_set_load_case(
        self: "CastSelf",
    ) -> "_644.CylindricalManufacturedGearSetLoadCase":
        from mastapy._private.gears.manufacturing.cylindrical import _644

        return self.__parent__._cast(_644.CylindricalManufacturedGearSetLoadCase)

    @property
    def cylindrical_set_manufacturing_config(
        self: "CastSelf",
    ) -> "_648.CylindricalSetManufacturingConfig":
        from mastapy._private.gears.manufacturing.cylindrical import _648

        return self.__parent__._cast(_648.CylindricalSetManufacturingConfig)

    @property
    def conical_set_manufacturing_analysis(
        self: "CastSelf",
    ) -> "_813.ConicalSetManufacturingAnalysis":
        from mastapy._private.gears.manufacturing.bevel import _813

        return self.__parent__._cast(_813.ConicalSetManufacturingAnalysis)

    @property
    def conical_set_manufacturing_config(
        self: "CastSelf",
    ) -> "_814.ConicalSetManufacturingConfig":
        from mastapy._private.gears.manufacturing.bevel import _814

        return self.__parent__._cast(_814.ConicalSetManufacturingConfig)

    @property
    def conical_set_micro_geometry_config(
        self: "CastSelf",
    ) -> "_815.ConicalSetMicroGeometryConfig":
        from mastapy._private.gears.manufacturing.bevel import _815

        return self.__parent__._cast(_815.ConicalSetMicroGeometryConfig)

    @property
    def conical_set_micro_geometry_config_base(
        self: "CastSelf",
    ) -> "_816.ConicalSetMicroGeometryConfigBase":
        from mastapy._private.gears.manufacturing.bevel import _816

        return self.__parent__._cast(_816.ConicalSetMicroGeometryConfigBase)

    @property
    def gear_set_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_869.GearSetLoadDistributionAnalysis":
        from mastapy._private.gears.ltca import _869

        return self.__parent__._cast(_869.GearSetLoadDistributionAnalysis)

    @property
    def cylindrical_gear_set_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_883.CylindricalGearSetLoadDistributionAnalysis":
        from mastapy._private.gears.ltca.cylindrical import _883

        return self.__parent__._cast(_883.CylindricalGearSetLoadDistributionAnalysis)

    @property
    def face_gear_set_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_885.FaceGearSetLoadDistributionAnalysis":
        from mastapy._private.gears.ltca.cylindrical import _885

        return self.__parent__._cast(_885.FaceGearSetLoadDistributionAnalysis)

    @property
    def conical_gear_set_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_891.ConicalGearSetLoadDistributionAnalysis":
        from mastapy._private.gears.ltca.conical import _891

        return self.__parent__._cast(_891.ConicalGearSetLoadDistributionAnalysis)

    @property
    def gear_set_load_case_base(self: "CastSelf") -> "_897.GearSetLoadCaseBase":
        from mastapy._private.gears.load_case import _897

        return self.__parent__._cast(_897.GearSetLoadCaseBase)

    @property
    def worm_gear_set_load_case(self: "CastSelf") -> "_900.WormGearSetLoadCase":
        from mastapy._private.gears.load_case.worm import _900

        return self.__parent__._cast(_900.WormGearSetLoadCase)

    @property
    def face_gear_set_load_case(self: "CastSelf") -> "_903.FaceGearSetLoadCase":
        from mastapy._private.gears.load_case.face import _903

        return self.__parent__._cast(_903.FaceGearSetLoadCase)

    @property
    def cylindrical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_906.CylindricalGearSetLoadCase":
        from mastapy._private.gears.load_case.cylindrical import _906

        return self.__parent__._cast(_906.CylindricalGearSetLoadCase)

    @property
    def conical_gear_set_load_case(self: "CastSelf") -> "_909.ConicalGearSetLoadCase":
        from mastapy._private.gears.load_case.conical import _909

        return self.__parent__._cast(_909.ConicalGearSetLoadCase)

    @property
    def concept_gear_set_load_case(self: "CastSelf") -> "_912.ConceptGearSetLoadCase":
        from mastapy._private.gears.load_case.concept import _912

        return self.__parent__._cast(_912.ConceptGearSetLoadCase)

    @property
    def bevel_set_load_case(self: "CastSelf") -> "_916.BevelSetLoadCase":
        from mastapy._private.gears.load_case.bevel import _916

        return self.__parent__._cast(_916.BevelSetLoadCase)

    @property
    def cylindrical_gear_set_tiff_analysis(
        self: "CastSelf",
    ) -> "_919.CylindricalGearSetTIFFAnalysis":
        from mastapy._private.gears.gear_two_d_fe_analysis import _919

        return self.__parent__._cast(_919.CylindricalGearSetTIFFAnalysis)

    @property
    def cylindrical_gear_set_tiff_analysis_duty_cycle(
        self: "CastSelf",
    ) -> "_920.CylindricalGearSetTIFFAnalysisDutyCycle":
        from mastapy._private.gears.gear_two_d_fe_analysis import _920

        return self.__parent__._cast(_920.CylindricalGearSetTIFFAnalysisDutyCycle)

    @property
    def face_gear_set_micro_geometry(
        self: "CastSelf",
    ) -> "_1020.FaceGearSetMicroGeometry":
        from mastapy._private.gears.gear_designs.face import _1020

        return self.__parent__._cast(_1020.FaceGearSetMicroGeometry)

    @property
    def cylindrical_gear_set_micro_geometry(
        self: "CastSelf",
    ) -> "_1139.CylindricalGearSetMicroGeometry":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1139

        return self.__parent__._cast(_1139.CylindricalGearSetMicroGeometry)

    @property
    def cylindrical_gear_set_micro_geometry_duty_cycle(
        self: "CastSelf",
    ) -> "_1140.CylindricalGearSetMicroGeometryDutyCycle":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1140

        return self.__parent__._cast(_1140.CylindricalGearSetMicroGeometryDutyCycle)

    @property
    def gear_set_fe_model(self: "CastSelf") -> "_1238.GearSetFEModel":
        from mastapy._private.gears.fe_model import _1238

        return self.__parent__._cast(_1238.GearSetFEModel)

    @property
    def cylindrical_gear_set_fe_model(
        self: "CastSelf",
    ) -> "_1241.CylindricalGearSetFEModel":
        from mastapy._private.gears.fe_model.cylindrical import _1241

        return self.__parent__._cast(_1241.CylindricalGearSetFEModel)

    @property
    def conical_set_fe_model(self: "CastSelf") -> "_1244.ConicalSetFEModel":
        from mastapy._private.gears.fe_model.conical import _1244

        return self.__parent__._cast(_1244.ConicalSetFEModel)

    @property
    def gear_set_implementation_analysis(
        self: "CastSelf",
    ) -> "_1266.GearSetImplementationAnalysis":
        from mastapy._private.gears.analysis import _1266

        return self.__parent__._cast(_1266.GearSetImplementationAnalysis)

    @property
    def gear_set_implementation_analysis_abstract(
        self: "CastSelf",
    ) -> "_1267.GearSetImplementationAnalysisAbstract":
        from mastapy._private.gears.analysis import _1267

        return self.__parent__._cast(_1267.GearSetImplementationAnalysisAbstract)

    @property
    def gear_set_implementation_analysis_duty_cycle(
        self: "CastSelf",
    ) -> "_1268.GearSetImplementationAnalysisDutyCycle":
        from mastapy._private.gears.analysis import _1268

        return self.__parent__._cast(_1268.GearSetImplementationAnalysisDutyCycle)

    @property
    def gear_set_implementation_detail(
        self: "CastSelf",
    ) -> "_1269.GearSetImplementationDetail":
        from mastapy._private.gears.analysis import _1269

        return self.__parent__._cast(_1269.GearSetImplementationDetail)

    @property
    def gear_set_design_analysis(self: "CastSelf") -> "GearSetDesignAnalysis":
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
class GearSetDesignAnalysis(_1255.AbstractGearSetAnalysis):
    """GearSetDesignAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_SET_DESIGN_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_GearSetDesignAnalysis":
        """Cast to another type.

        Returns:
            _Cast_GearSetDesignAnalysis
        """
        return _Cast_GearSetDesignAnalysis(self)
