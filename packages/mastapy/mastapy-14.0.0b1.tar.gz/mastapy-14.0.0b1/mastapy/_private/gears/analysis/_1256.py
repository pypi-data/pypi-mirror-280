"""GearDesignAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.analysis import _1253
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_GEAR_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearDesignAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical import _635, _639, _640
    from mastapy._private.gears.manufacturing.bevel import (
        _798,
        _799,
        _800,
        _801,
        _811,
        _812,
        _817,
    )
    from mastapy._private.gears.ltca import _863
    from mastapy._private.gears.ltca.cylindrical import _879
    from mastapy._private.gears.ltca.conical import _890
    from mastapy._private.gears.load_case import _896
    from mastapy._private.gears.load_case.worm import _899
    from mastapy._private.gears.load_case.face import _902
    from mastapy._private.gears.load_case.cylindrical import _905
    from mastapy._private.gears.load_case.conical import _908
    from mastapy._private.gears.load_case.concept import _911
    from mastapy._private.gears.load_case.bevel import _914
    from mastapy._private.gears.gear_two_d_fe_analysis import _921, _922
    from mastapy._private.gears.gear_designs.face import _1017
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1132,
        _1133,
        _1134,
        _1136,
    )
    from mastapy._private.gears.fe_model import _1235
    from mastapy._private.gears.fe_model.cylindrical import _1239
    from mastapy._private.gears.fe_model.conical import _1242
    from mastapy._private.gears.analysis import _1257, _1258, _1259

    Self = TypeVar("Self", bound="GearDesignAnalysis")
    CastSelf = TypeVar("CastSelf", bound="GearDesignAnalysis._Cast_GearDesignAnalysis")


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearDesignAnalysis:
    """Special nested class for casting GearDesignAnalysis to subclasses."""

    __parent__: "GearDesignAnalysis"

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def cylindrical_gear_manufacturing_config(
        self: "CastSelf",
    ) -> "_635.CylindricalGearManufacturingConfig":
        from mastapy._private.gears.manufacturing.cylindrical import _635

        return self.__parent__._cast(_635.CylindricalGearManufacturingConfig)

    @property
    def cylindrical_manufactured_gear_duty_cycle(
        self: "CastSelf",
    ) -> "_639.CylindricalManufacturedGearDutyCycle":
        from mastapy._private.gears.manufacturing.cylindrical import _639

        return self.__parent__._cast(_639.CylindricalManufacturedGearDutyCycle)

    @property
    def cylindrical_manufactured_gear_load_case(
        self: "CastSelf",
    ) -> "_640.CylindricalManufacturedGearLoadCase":
        from mastapy._private.gears.manufacturing.cylindrical import _640

        return self.__parent__._cast(_640.CylindricalManufacturedGearLoadCase)

    @property
    def conical_gear_manufacturing_analysis(
        self: "CastSelf",
    ) -> "_798.ConicalGearManufacturingAnalysis":
        from mastapy._private.gears.manufacturing.bevel import _798

        return self.__parent__._cast(_798.ConicalGearManufacturingAnalysis)

    @property
    def conical_gear_manufacturing_config(
        self: "CastSelf",
    ) -> "_799.ConicalGearManufacturingConfig":
        from mastapy._private.gears.manufacturing.bevel import _799

        return self.__parent__._cast(_799.ConicalGearManufacturingConfig)

    @property
    def conical_gear_micro_geometry_config(
        self: "CastSelf",
    ) -> "_800.ConicalGearMicroGeometryConfig":
        from mastapy._private.gears.manufacturing.bevel import _800

        return self.__parent__._cast(_800.ConicalGearMicroGeometryConfig)

    @property
    def conical_gear_micro_geometry_config_base(
        self: "CastSelf",
    ) -> "_801.ConicalGearMicroGeometryConfigBase":
        from mastapy._private.gears.manufacturing.bevel import _801

        return self.__parent__._cast(_801.ConicalGearMicroGeometryConfigBase)

    @property
    def conical_pinion_manufacturing_config(
        self: "CastSelf",
    ) -> "_811.ConicalPinionManufacturingConfig":
        from mastapy._private.gears.manufacturing.bevel import _811

        return self.__parent__._cast(_811.ConicalPinionManufacturingConfig)

    @property
    def conical_pinion_micro_geometry_config(
        self: "CastSelf",
    ) -> "_812.ConicalPinionMicroGeometryConfig":
        from mastapy._private.gears.manufacturing.bevel import _812

        return self.__parent__._cast(_812.ConicalPinionMicroGeometryConfig)

    @property
    def conical_wheel_manufacturing_config(
        self: "CastSelf",
    ) -> "_817.ConicalWheelManufacturingConfig":
        from mastapy._private.gears.manufacturing.bevel import _817

        return self.__parent__._cast(_817.ConicalWheelManufacturingConfig)

    @property
    def gear_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_863.GearLoadDistributionAnalysis":
        from mastapy._private.gears.ltca import _863

        return self.__parent__._cast(_863.GearLoadDistributionAnalysis)

    @property
    def cylindrical_gear_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_879.CylindricalGearLoadDistributionAnalysis":
        from mastapy._private.gears.ltca.cylindrical import _879

        return self.__parent__._cast(_879.CylindricalGearLoadDistributionAnalysis)

    @property
    def conical_gear_load_distribution_analysis(
        self: "CastSelf",
    ) -> "_890.ConicalGearLoadDistributionAnalysis":
        from mastapy._private.gears.ltca.conical import _890

        return self.__parent__._cast(_890.ConicalGearLoadDistributionAnalysis)

    @property
    def gear_load_case_base(self: "CastSelf") -> "_896.GearLoadCaseBase":
        from mastapy._private.gears.load_case import _896

        return self.__parent__._cast(_896.GearLoadCaseBase)

    @property
    def worm_gear_load_case(self: "CastSelf") -> "_899.WormGearLoadCase":
        from mastapy._private.gears.load_case.worm import _899

        return self.__parent__._cast(_899.WormGearLoadCase)

    @property
    def face_gear_load_case(self: "CastSelf") -> "_902.FaceGearLoadCase":
        from mastapy._private.gears.load_case.face import _902

        return self.__parent__._cast(_902.FaceGearLoadCase)

    @property
    def cylindrical_gear_load_case(self: "CastSelf") -> "_905.CylindricalGearLoadCase":
        from mastapy._private.gears.load_case.cylindrical import _905

        return self.__parent__._cast(_905.CylindricalGearLoadCase)

    @property
    def conical_gear_load_case(self: "CastSelf") -> "_908.ConicalGearLoadCase":
        from mastapy._private.gears.load_case.conical import _908

        return self.__parent__._cast(_908.ConicalGearLoadCase)

    @property
    def concept_gear_load_case(self: "CastSelf") -> "_911.ConceptGearLoadCase":
        from mastapy._private.gears.load_case.concept import _911

        return self.__parent__._cast(_911.ConceptGearLoadCase)

    @property
    def bevel_load_case(self: "CastSelf") -> "_914.BevelLoadCase":
        from mastapy._private.gears.load_case.bevel import _914

        return self.__parent__._cast(_914.BevelLoadCase)

    @property
    def cylindrical_gear_tiff_analysis(
        self: "CastSelf",
    ) -> "_921.CylindricalGearTIFFAnalysis":
        from mastapy._private.gears.gear_two_d_fe_analysis import _921

        return self.__parent__._cast(_921.CylindricalGearTIFFAnalysis)

    @property
    def cylindrical_gear_tiff_analysis_duty_cycle(
        self: "CastSelf",
    ) -> "_922.CylindricalGearTIFFAnalysisDutyCycle":
        from mastapy._private.gears.gear_two_d_fe_analysis import _922

        return self.__parent__._cast(_922.CylindricalGearTIFFAnalysisDutyCycle)

    @property
    def face_gear_micro_geometry(self: "CastSelf") -> "_1017.FaceGearMicroGeometry":
        from mastapy._private.gears.gear_designs.face import _1017

        return self.__parent__._cast(_1017.FaceGearMicroGeometry)

    @property
    def cylindrical_gear_micro_geometry(
        self: "CastSelf",
    ) -> "_1132.CylindricalGearMicroGeometry":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1132

        return self.__parent__._cast(_1132.CylindricalGearMicroGeometry)

    @property
    def cylindrical_gear_micro_geometry_base(
        self: "CastSelf",
    ) -> "_1133.CylindricalGearMicroGeometryBase":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1133

        return self.__parent__._cast(_1133.CylindricalGearMicroGeometryBase)

    @property
    def cylindrical_gear_micro_geometry_duty_cycle(
        self: "CastSelf",
    ) -> "_1134.CylindricalGearMicroGeometryDutyCycle":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1134

        return self.__parent__._cast(_1134.CylindricalGearMicroGeometryDutyCycle)

    @property
    def cylindrical_gear_micro_geometry_per_tooth(
        self: "CastSelf",
    ) -> "_1136.CylindricalGearMicroGeometryPerTooth":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1136

        return self.__parent__._cast(_1136.CylindricalGearMicroGeometryPerTooth)

    @property
    def gear_fe_model(self: "CastSelf") -> "_1235.GearFEModel":
        from mastapy._private.gears.fe_model import _1235

        return self.__parent__._cast(_1235.GearFEModel)

    @property
    def cylindrical_gear_fe_model(self: "CastSelf") -> "_1239.CylindricalGearFEModel":
        from mastapy._private.gears.fe_model.cylindrical import _1239

        return self.__parent__._cast(_1239.CylindricalGearFEModel)

    @property
    def conical_gear_fe_model(self: "CastSelf") -> "_1242.ConicalGearFEModel":
        from mastapy._private.gears.fe_model.conical import _1242

        return self.__parent__._cast(_1242.ConicalGearFEModel)

    @property
    def gear_implementation_analysis(
        self: "CastSelf",
    ) -> "_1257.GearImplementationAnalysis":
        from mastapy._private.gears.analysis import _1257

        return self.__parent__._cast(_1257.GearImplementationAnalysis)

    @property
    def gear_implementation_analysis_duty_cycle(
        self: "CastSelf",
    ) -> "_1258.GearImplementationAnalysisDutyCycle":
        from mastapy._private.gears.analysis import _1258

        return self.__parent__._cast(_1258.GearImplementationAnalysisDutyCycle)

    @property
    def gear_implementation_detail(
        self: "CastSelf",
    ) -> "_1259.GearImplementationDetail":
        from mastapy._private.gears.analysis import _1259

        return self.__parent__._cast(_1259.GearImplementationDetail)

    @property
    def gear_design_analysis(self: "CastSelf") -> "GearDesignAnalysis":
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
class GearDesignAnalysis(_1253.AbstractGearAnalysis):
    """GearDesignAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_DESIGN_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_GearDesignAnalysis":
        """Cast to another type.

        Returns:
            _Cast_GearDesignAnalysis
        """
        return _Cast_GearDesignAnalysis(self)
