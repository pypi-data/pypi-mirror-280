"""GearSetImplementationAnalysisAbstract"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.analysis import _1264
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationAnalysisAbstract"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical import _643, _644
    from mastapy._private.gears.manufacturing.bevel import _813
    from mastapy._private.gears.ltca import _869
    from mastapy._private.gears.ltca.cylindrical import _883, _885
    from mastapy._private.gears.ltca.conical import _891
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1140
    from mastapy._private.gears.analysis import _1266, _1268, _1255

    Self = TypeVar("Self", bound="GearSetImplementationAnalysisAbstract")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearSetImplementationAnalysisAbstract",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearSetImplementationAnalysisAbstract:
    """Special nested class for casting GearSetImplementationAnalysisAbstract to subclasses."""

    __parent__: "GearSetImplementationAnalysisAbstract"

    @property
    def gear_set_design_analysis(self: "CastSelf") -> "_1264.GearSetDesignAnalysis":
        return self.__parent__._cast(_1264.GearSetDesignAnalysis)

    @property
    def abstract_gear_set_analysis(self: "CastSelf") -> "_1255.AbstractGearSetAnalysis":
        from mastapy._private.gears.analysis import _1255

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
    def conical_set_manufacturing_analysis(
        self: "CastSelf",
    ) -> "_813.ConicalSetManufacturingAnalysis":
        from mastapy._private.gears.manufacturing.bevel import _813

        return self.__parent__._cast(_813.ConicalSetManufacturingAnalysis)

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
    def cylindrical_gear_set_micro_geometry_duty_cycle(
        self: "CastSelf",
    ) -> "_1140.CylindricalGearSetMicroGeometryDutyCycle":
        from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1140

        return self.__parent__._cast(_1140.CylindricalGearSetMicroGeometryDutyCycle)

    @property
    def gear_set_implementation_analysis(
        self: "CastSelf",
    ) -> "_1266.GearSetImplementationAnalysis":
        from mastapy._private.gears.analysis import _1266

        return self.__parent__._cast(_1266.GearSetImplementationAnalysis)

    @property
    def gear_set_implementation_analysis_duty_cycle(
        self: "CastSelf",
    ) -> "_1268.GearSetImplementationAnalysisDutyCycle":
        from mastapy._private.gears.analysis import _1268

        return self.__parent__._cast(_1268.GearSetImplementationAnalysisDutyCycle)

    @property
    def gear_set_implementation_analysis_abstract(
        self: "CastSelf",
    ) -> "GearSetImplementationAnalysisAbstract":
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
class GearSetImplementationAnalysisAbstract(_1264.GearSetDesignAnalysis):
    """GearSetImplementationAnalysisAbstract

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_GearSetImplementationAnalysisAbstract":
        """Cast to another type.

        Returns:
            _Cast_GearSetImplementationAnalysisAbstract
        """
        return _Cast_GearSetImplementationAnalysisAbstract(self)
