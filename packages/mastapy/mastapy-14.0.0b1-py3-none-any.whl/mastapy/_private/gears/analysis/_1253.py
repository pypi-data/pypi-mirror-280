"""AbstractGearAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_GEAR_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.rating import _364, _368, _372
    from mastapy._private.gears.rating.zerol_bevel import _381
    from mastapy._private.gears.rating.worm import _383, _385
    from mastapy._private.gears.rating.straight_bevel import _407
    from mastapy._private.gears.rating.straight_bevel_diff import _410
    from mastapy._private.gears.rating.spiral_bevel import _414
    from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _417
    from mastapy._private.gears.rating.klingelnberg_hypoid import _420
    from mastapy._private.gears.rating.klingelnberg_conical import _423
    from mastapy._private.gears.rating.hypoid import _450
    from mastapy._private.gears.rating.face import _456, _459
    from mastapy._private.gears.rating.cylindrical import _466, _471
    from mastapy._private.gears.rating.conical import _549, _551
    from mastapy._private.gears.rating.concept import _559, _562
    from mastapy._private.gears.rating.bevel import _566
    from mastapy._private.gears.rating.agma_gleason_conical import _577
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
    from mastapy._private.gears.analysis import _1256, _1257, _1258, _1259

    Self = TypeVar("Self", bound="AbstractGearAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="AbstractGearAnalysis._Cast_AbstractGearAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractGearAnalysis:
    """Special nested class for casting AbstractGearAnalysis to subclasses."""

    __parent__: "AbstractGearAnalysis"

    @property
    def abstract_gear_rating(self: "CastSelf") -> "_364.AbstractGearRating":
        from mastapy._private.gears.rating import _364

        return self.__parent__._cast(_364.AbstractGearRating)

    @property
    def gear_duty_cycle_rating(self: "CastSelf") -> "_368.GearDutyCycleRating":
        from mastapy._private.gears.rating import _368

        return self.__parent__._cast(_368.GearDutyCycleRating)

    @property
    def gear_rating(self: "CastSelf") -> "_372.GearRating":
        from mastapy._private.gears.rating import _372

        return self.__parent__._cast(_372.GearRating)

    @property
    def zerol_bevel_gear_rating(self: "CastSelf") -> "_381.ZerolBevelGearRating":
        from mastapy._private.gears.rating.zerol_bevel import _381

        return self.__parent__._cast(_381.ZerolBevelGearRating)

    @property
    def worm_gear_duty_cycle_rating(self: "CastSelf") -> "_383.WormGearDutyCycleRating":
        from mastapy._private.gears.rating.worm import _383

        return self.__parent__._cast(_383.WormGearDutyCycleRating)

    @property
    def worm_gear_rating(self: "CastSelf") -> "_385.WormGearRating":
        from mastapy._private.gears.rating.worm import _385

        return self.__parent__._cast(_385.WormGearRating)

    @property
    def straight_bevel_gear_rating(self: "CastSelf") -> "_407.StraightBevelGearRating":
        from mastapy._private.gears.rating.straight_bevel import _407

        return self.__parent__._cast(_407.StraightBevelGearRating)

    @property
    def straight_bevel_diff_gear_rating(
        self: "CastSelf",
    ) -> "_410.StraightBevelDiffGearRating":
        from mastapy._private.gears.rating.straight_bevel_diff import _410

        return self.__parent__._cast(_410.StraightBevelDiffGearRating)

    @property
    def spiral_bevel_gear_rating(self: "CastSelf") -> "_414.SpiralBevelGearRating":
        from mastapy._private.gears.rating.spiral_bevel import _414

        return self.__parent__._cast(_414.SpiralBevelGearRating)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
        self: "CastSelf",
    ) -> "_417.KlingelnbergCycloPalloidSpiralBevelGearRating":
        from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _417

        return self.__parent__._cast(_417.KlingelnbergCycloPalloidSpiralBevelGearRating)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_rating(
        self: "CastSelf",
    ) -> "_420.KlingelnbergCycloPalloidHypoidGearRating":
        from mastapy._private.gears.rating.klingelnberg_hypoid import _420

        return self.__parent__._cast(_420.KlingelnbergCycloPalloidHypoidGearRating)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_rating(
        self: "CastSelf",
    ) -> "_423.KlingelnbergCycloPalloidConicalGearRating":
        from mastapy._private.gears.rating.klingelnberg_conical import _423

        return self.__parent__._cast(_423.KlingelnbergCycloPalloidConicalGearRating)

    @property
    def hypoid_gear_rating(self: "CastSelf") -> "_450.HypoidGearRating":
        from mastapy._private.gears.rating.hypoid import _450

        return self.__parent__._cast(_450.HypoidGearRating)

    @property
    def face_gear_duty_cycle_rating(self: "CastSelf") -> "_456.FaceGearDutyCycleRating":
        from mastapy._private.gears.rating.face import _456

        return self.__parent__._cast(_456.FaceGearDutyCycleRating)

    @property
    def face_gear_rating(self: "CastSelf") -> "_459.FaceGearRating":
        from mastapy._private.gears.rating.face import _459

        return self.__parent__._cast(_459.FaceGearRating)

    @property
    def cylindrical_gear_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_466.CylindricalGearDutyCycleRating":
        from mastapy._private.gears.rating.cylindrical import _466

        return self.__parent__._cast(_466.CylindricalGearDutyCycleRating)

    @property
    def cylindrical_gear_rating(self: "CastSelf") -> "_471.CylindricalGearRating":
        from mastapy._private.gears.rating.cylindrical import _471

        return self.__parent__._cast(_471.CylindricalGearRating)

    @property
    def conical_gear_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_549.ConicalGearDutyCycleRating":
        from mastapy._private.gears.rating.conical import _549

        return self.__parent__._cast(_549.ConicalGearDutyCycleRating)

    @property
    def conical_gear_rating(self: "CastSelf") -> "_551.ConicalGearRating":
        from mastapy._private.gears.rating.conical import _551

        return self.__parent__._cast(_551.ConicalGearRating)

    @property
    def concept_gear_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_559.ConceptGearDutyCycleRating":
        from mastapy._private.gears.rating.concept import _559

        return self.__parent__._cast(_559.ConceptGearDutyCycleRating)

    @property
    def concept_gear_rating(self: "CastSelf") -> "_562.ConceptGearRating":
        from mastapy._private.gears.rating.concept import _562

        return self.__parent__._cast(_562.ConceptGearRating)

    @property
    def bevel_gear_rating(self: "CastSelf") -> "_566.BevelGearRating":
        from mastapy._private.gears.rating.bevel import _566

        return self.__parent__._cast(_566.BevelGearRating)

    @property
    def agma_gleason_conical_gear_rating(
        self: "CastSelf",
    ) -> "_577.AGMAGleasonConicalGearRating":
        from mastapy._private.gears.rating.agma_gleason_conical import _577

        return self.__parent__._cast(_577.AGMAGleasonConicalGearRating)

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
    def gear_design_analysis(self: "CastSelf") -> "_1256.GearDesignAnalysis":
        from mastapy._private.gears.analysis import _1256

        return self.__parent__._cast(_1256.GearDesignAnalysis)

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
    def abstract_gear_analysis(self: "CastSelf") -> "AbstractGearAnalysis":
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
class AbstractGearAnalysis(_0.APIBase):
    """AbstractGearAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_GEAR_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def name_with_gear_set_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NameWithGearSetName

        if temp is None:
            return ""

        return temp

    @property
    def planet_index(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.PlanetIndex

        if temp is None:
            return 0

        return temp

    @planet_index.setter
    @enforce_parameter_types
    def planet_index(self: "Self", value: "int") -> None:
        self.wrapped.PlanetIndex = int(value) if value is not None else 0

    @property
    def report_names(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: "Self", report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractGearAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractGearAnalysis
        """
        return _Cast_AbstractGearAnalysis(self)
