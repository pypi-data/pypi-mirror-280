"""AbstractGearSetAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearSetAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility.model_validation import _1842, _1841
    from mastapy._private.gears.rating import _365, _373, _374
    from mastapy._private.gears.rating.zerol_bevel import _382
    from mastapy._private.gears.rating.worm import _386, _387
    from mastapy._private.gears.rating.straight_bevel import _408
    from mastapy._private.gears.rating.straight_bevel_diff import _411
    from mastapy._private.gears.rating.spiral_bevel import _415
    from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _418
    from mastapy._private.gears.rating.klingelnberg_hypoid import _421
    from mastapy._private.gears.rating.klingelnberg_conical import _424
    from mastapy._private.gears.rating.hypoid import _451
    from mastapy._private.gears.rating.face import _460, _461
    from mastapy._private.gears.rating.cylindrical import _474, _475, _491
    from mastapy._private.gears.rating.conical import _552, _553
    from mastapy._private.gears.rating.concept import _563, _564
    from mastapy._private.gears.rating.bevel import _567
    from mastapy._private.gears.rating.agma_gleason_conical import _578
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
    from mastapy._private.gears.analysis import _1264, _1266, _1267, _1268, _1269

    Self = TypeVar("Self", bound="AbstractGearSetAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractGearSetAnalysis:
    """Special nested class for casting AbstractGearSetAnalysis to subclasses."""

    __parent__: "AbstractGearSetAnalysis"

    @property
    def abstract_gear_set_rating(self: "CastSelf") -> "_365.AbstractGearSetRating":
        from mastapy._private.gears.rating import _365

        return self.__parent__._cast(_365.AbstractGearSetRating)

    @property
    def gear_set_duty_cycle_rating(self: "CastSelf") -> "_373.GearSetDutyCycleRating":
        from mastapy._private.gears.rating import _373

        return self.__parent__._cast(_373.GearSetDutyCycleRating)

    @property
    def gear_set_rating(self: "CastSelf") -> "_374.GearSetRating":
        from mastapy._private.gears.rating import _374

        return self.__parent__._cast(_374.GearSetRating)

    @property
    def zerol_bevel_gear_set_rating(self: "CastSelf") -> "_382.ZerolBevelGearSetRating":
        from mastapy._private.gears.rating.zerol_bevel import _382

        return self.__parent__._cast(_382.ZerolBevelGearSetRating)

    @property
    def worm_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_386.WormGearSetDutyCycleRating":
        from mastapy._private.gears.rating.worm import _386

        return self.__parent__._cast(_386.WormGearSetDutyCycleRating)

    @property
    def worm_gear_set_rating(self: "CastSelf") -> "_387.WormGearSetRating":
        from mastapy._private.gears.rating.worm import _387

        return self.__parent__._cast(_387.WormGearSetRating)

    @property
    def straight_bevel_gear_set_rating(
        self: "CastSelf",
    ) -> "_408.StraightBevelGearSetRating":
        from mastapy._private.gears.rating.straight_bevel import _408

        return self.__parent__._cast(_408.StraightBevelGearSetRating)

    @property
    def straight_bevel_diff_gear_set_rating(
        self: "CastSelf",
    ) -> "_411.StraightBevelDiffGearSetRating":
        from mastapy._private.gears.rating.straight_bevel_diff import _411

        return self.__parent__._cast(_411.StraightBevelDiffGearSetRating)

    @property
    def spiral_bevel_gear_set_rating(
        self: "CastSelf",
    ) -> "_415.SpiralBevelGearSetRating":
        from mastapy._private.gears.rating.spiral_bevel import _415

        return self.__parent__._cast(_415.SpiralBevelGearSetRating)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
        self: "CastSelf",
    ) -> "_418.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
        from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _418

        return self.__parent__._cast(
            _418.KlingelnbergCycloPalloidSpiralBevelGearSetRating
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
        self: "CastSelf",
    ) -> "_421.KlingelnbergCycloPalloidHypoidGearSetRating":
        from mastapy._private.gears.rating.klingelnberg_hypoid import _421

        return self.__parent__._cast(_421.KlingelnbergCycloPalloidHypoidGearSetRating)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_rating(
        self: "CastSelf",
    ) -> "_424.KlingelnbergCycloPalloidConicalGearSetRating":
        from mastapy._private.gears.rating.klingelnberg_conical import _424

        return self.__parent__._cast(_424.KlingelnbergCycloPalloidConicalGearSetRating)

    @property
    def hypoid_gear_set_rating(self: "CastSelf") -> "_451.HypoidGearSetRating":
        from mastapy._private.gears.rating.hypoid import _451

        return self.__parent__._cast(_451.HypoidGearSetRating)

    @property
    def face_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_460.FaceGearSetDutyCycleRating":
        from mastapy._private.gears.rating.face import _460

        return self.__parent__._cast(_460.FaceGearSetDutyCycleRating)

    @property
    def face_gear_set_rating(self: "CastSelf") -> "_461.FaceGearSetRating":
        from mastapy._private.gears.rating.face import _461

        return self.__parent__._cast(_461.FaceGearSetRating)

    @property
    def cylindrical_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_474.CylindricalGearSetDutyCycleRating":
        from mastapy._private.gears.rating.cylindrical import _474

        return self.__parent__._cast(_474.CylindricalGearSetDutyCycleRating)

    @property
    def cylindrical_gear_set_rating(
        self: "CastSelf",
    ) -> "_475.CylindricalGearSetRating":
        from mastapy._private.gears.rating.cylindrical import _475

        return self.__parent__._cast(_475.CylindricalGearSetRating)

    @property
    def reduced_cylindrical_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_491.ReducedCylindricalGearSetDutyCycleRating":
        from mastapy._private.gears.rating.cylindrical import _491

        return self.__parent__._cast(_491.ReducedCylindricalGearSetDutyCycleRating)

    @property
    def conical_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_552.ConicalGearSetDutyCycleRating":
        from mastapy._private.gears.rating.conical import _552

        return self.__parent__._cast(_552.ConicalGearSetDutyCycleRating)

    @property
    def conical_gear_set_rating(self: "CastSelf") -> "_553.ConicalGearSetRating":
        from mastapy._private.gears.rating.conical import _553

        return self.__parent__._cast(_553.ConicalGearSetRating)

    @property
    def concept_gear_set_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_563.ConceptGearSetDutyCycleRating":
        from mastapy._private.gears.rating.concept import _563

        return self.__parent__._cast(_563.ConceptGearSetDutyCycleRating)

    @property
    def concept_gear_set_rating(self: "CastSelf") -> "_564.ConceptGearSetRating":
        from mastapy._private.gears.rating.concept import _564

        return self.__parent__._cast(_564.ConceptGearSetRating)

    @property
    def bevel_gear_set_rating(self: "CastSelf") -> "_567.BevelGearSetRating":
        from mastapy._private.gears.rating.bevel import _567

        return self.__parent__._cast(_567.BevelGearSetRating)

    @property
    def agma_gleason_conical_gear_set_rating(
        self: "CastSelf",
    ) -> "_578.AGMAGleasonConicalGearSetRating":
        from mastapy._private.gears.rating.agma_gleason_conical import _578

        return self.__parent__._cast(_578.AGMAGleasonConicalGearSetRating)

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
    def gear_set_design_analysis(self: "CastSelf") -> "_1264.GearSetDesignAnalysis":
        from mastapy._private.gears.analysis import _1264

        return self.__parent__._cast(_1264.GearSetDesignAnalysis)

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
    def abstract_gear_set_analysis(self: "CastSelf") -> "AbstractGearSetAnalysis":
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
class AbstractGearSetAnalysis(_0.APIBase):
    """AbstractGearSetAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_GEAR_SET_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def name(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: "Self", value: "str") -> None:
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def all_status_errors(self: "Self") -> "List[_1842.StatusItem]":
        """List[mastapy._private.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: "Self") -> "_1841.Status":
        """mastapy._private.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: "Self") -> "_Cast_AbstractGearSetAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractGearSetAnalysis
        """
        return _Cast_AbstractGearSetAnalysis(self)
