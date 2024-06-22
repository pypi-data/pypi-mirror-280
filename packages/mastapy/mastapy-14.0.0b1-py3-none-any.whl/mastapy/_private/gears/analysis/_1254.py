"""AbstractGearMeshAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearMeshAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.analysis import _1253, _1260, _1261, _1262, _1263
    from mastapy._private.gears.rating import _363, _371, _376
    from mastapy._private.gears.rating.zerol_bevel import _380
    from mastapy._private.gears.rating.worm import _384, _388
    from mastapy._private.gears.rating.straight_bevel import _406
    from mastapy._private.gears.rating.straight_bevel_diff import _409
    from mastapy._private.gears.rating.spiral_bevel import _413
    from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _416
    from mastapy._private.gears.rating.klingelnberg_hypoid import _419
    from mastapy._private.gears.rating.klingelnberg_conical import _422
    from mastapy._private.gears.rating.hypoid import _449
    from mastapy._private.gears.rating.face import _457, _458
    from mastapy._private.gears.rating.cylindrical import _469, _477
    from mastapy._private.gears.rating.conical import _550, _555
    from mastapy._private.gears.rating.concept import _560, _561
    from mastapy._private.gears.rating.bevel import _565
    from mastapy._private.gears.rating.agma_gleason_conical import _576
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

    Self = TypeVar("Self", bound="AbstractGearMeshAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractGearMeshAnalysis:
    """Special nested class for casting AbstractGearMeshAnalysis to subclasses."""

    __parent__: "AbstractGearMeshAnalysis"

    @property
    def abstract_gear_mesh_rating(self: "CastSelf") -> "_363.AbstractGearMeshRating":
        from mastapy._private.gears.rating import _363

        return self.__parent__._cast(_363.AbstractGearMeshRating)

    @property
    def gear_mesh_rating(self: "CastSelf") -> "_371.GearMeshRating":
        from mastapy._private.gears.rating import _371

        return self.__parent__._cast(_371.GearMeshRating)

    @property
    def mesh_duty_cycle_rating(self: "CastSelf") -> "_376.MeshDutyCycleRating":
        from mastapy._private.gears.rating import _376

        return self.__parent__._cast(_376.MeshDutyCycleRating)

    @property
    def zerol_bevel_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_380.ZerolBevelGearMeshRating":
        from mastapy._private.gears.rating.zerol_bevel import _380

        return self.__parent__._cast(_380.ZerolBevelGearMeshRating)

    @property
    def worm_gear_mesh_rating(self: "CastSelf") -> "_384.WormGearMeshRating":
        from mastapy._private.gears.rating.worm import _384

        return self.__parent__._cast(_384.WormGearMeshRating)

    @property
    def worm_mesh_duty_cycle_rating(self: "CastSelf") -> "_388.WormMeshDutyCycleRating":
        from mastapy._private.gears.rating.worm import _388

        return self.__parent__._cast(_388.WormMeshDutyCycleRating)

    @property
    def straight_bevel_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_406.StraightBevelGearMeshRating":
        from mastapy._private.gears.rating.straight_bevel import _406

        return self.__parent__._cast(_406.StraightBevelGearMeshRating)

    @property
    def straight_bevel_diff_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_409.StraightBevelDiffGearMeshRating":
        from mastapy._private.gears.rating.straight_bevel_diff import _409

        return self.__parent__._cast(_409.StraightBevelDiffGearMeshRating)

    @property
    def spiral_bevel_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_413.SpiralBevelGearMeshRating":
        from mastapy._private.gears.rating.spiral_bevel import _413

        return self.__parent__._cast(_413.SpiralBevelGearMeshRating)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_416.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
        from mastapy._private.gears.rating.klingelnberg_spiral_bevel import _416

        return self.__parent__._cast(
            _416.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_419.KlingelnbergCycloPalloidHypoidGearMeshRating":
        from mastapy._private.gears.rating.klingelnberg_hypoid import _419

        return self.__parent__._cast(_419.KlingelnbergCycloPalloidHypoidGearMeshRating)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_422.KlingelnbergCycloPalloidConicalGearMeshRating":
        from mastapy._private.gears.rating.klingelnberg_conical import _422

        return self.__parent__._cast(_422.KlingelnbergCycloPalloidConicalGearMeshRating)

    @property
    def hypoid_gear_mesh_rating(self: "CastSelf") -> "_449.HypoidGearMeshRating":
        from mastapy._private.gears.rating.hypoid import _449

        return self.__parent__._cast(_449.HypoidGearMeshRating)

    @property
    def face_gear_mesh_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_457.FaceGearMeshDutyCycleRating":
        from mastapy._private.gears.rating.face import _457

        return self.__parent__._cast(_457.FaceGearMeshDutyCycleRating)

    @property
    def face_gear_mesh_rating(self: "CastSelf") -> "_458.FaceGearMeshRating":
        from mastapy._private.gears.rating.face import _458

        return self.__parent__._cast(_458.FaceGearMeshRating)

    @property
    def cylindrical_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_469.CylindricalGearMeshRating":
        from mastapy._private.gears.rating.cylindrical import _469

        return self.__parent__._cast(_469.CylindricalGearMeshRating)

    @property
    def cylindrical_mesh_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_477.CylindricalMeshDutyCycleRating":
        from mastapy._private.gears.rating.cylindrical import _477

        return self.__parent__._cast(_477.CylindricalMeshDutyCycleRating)

    @property
    def conical_gear_mesh_rating(self: "CastSelf") -> "_550.ConicalGearMeshRating":
        from mastapy._private.gears.rating.conical import _550

        return self.__parent__._cast(_550.ConicalGearMeshRating)

    @property
    def conical_mesh_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_555.ConicalMeshDutyCycleRating":
        from mastapy._private.gears.rating.conical import _555

        return self.__parent__._cast(_555.ConicalMeshDutyCycleRating)

    @property
    def concept_gear_mesh_duty_cycle_rating(
        self: "CastSelf",
    ) -> "_560.ConceptGearMeshDutyCycleRating":
        from mastapy._private.gears.rating.concept import _560

        return self.__parent__._cast(_560.ConceptGearMeshDutyCycleRating)

    @property
    def concept_gear_mesh_rating(self: "CastSelf") -> "_561.ConceptGearMeshRating":
        from mastapy._private.gears.rating.concept import _561

        return self.__parent__._cast(_561.ConceptGearMeshRating)

    @property
    def bevel_gear_mesh_rating(self: "CastSelf") -> "_565.BevelGearMeshRating":
        from mastapy._private.gears.rating.bevel import _565

        return self.__parent__._cast(_565.BevelGearMeshRating)

    @property
    def agma_gleason_conical_gear_mesh_rating(
        self: "CastSelf",
    ) -> "_576.AGMAGleasonConicalGearMeshRating":
        from mastapy._private.gears.rating.agma_gleason_conical import _576

        return self.__parent__._cast(_576.AGMAGleasonConicalGearMeshRating)

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
    def gear_mesh_design_analysis(self: "CastSelf") -> "_1260.GearMeshDesignAnalysis":
        from mastapy._private.gears.analysis import _1260

        return self.__parent__._cast(_1260.GearMeshDesignAnalysis)

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
    def abstract_gear_mesh_analysis(self: "CastSelf") -> "AbstractGearMeshAnalysis":
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
class AbstractGearMeshAnalysis(_0.APIBase):
    """AbstractGearMeshAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_GEAR_MESH_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def mesh_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshName

        if temp is None:
            return ""

        return temp

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
    def gear_a(self: "Self") -> "_1253.AbstractGearAnalysis":
        """mastapy._private.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: "Self") -> "_1253.AbstractGearAnalysis":
        """mastapy._private.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

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
    def cast_to(self: "Self") -> "_Cast_AbstractGearMeshAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractGearMeshAnalysis
        """
        return _Cast_AbstractGearMeshAnalysis(self)
