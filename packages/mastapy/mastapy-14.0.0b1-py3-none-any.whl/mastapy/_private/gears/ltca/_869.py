"""GearSetLoadDistributionAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import utility
from mastapy._private.gears.analysis import _1266
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearSetLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.ltca.cylindrical import _883, _885
    from mastapy._private.gears.ltca.conical import _891
    from mastapy._private.gears.analysis import _1267, _1264, _1255

    Self = TypeVar("Self", bound="GearSetLoadDistributionAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearSetLoadDistributionAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearSetLoadDistributionAnalysis:
    """Special nested class for casting GearSetLoadDistributionAnalysis to subclasses."""

    __parent__: "GearSetLoadDistributionAnalysis"

    @property
    def gear_set_implementation_analysis(
        self: "CastSelf",
    ) -> "_1266.GearSetImplementationAnalysis":
        return self.__parent__._cast(_1266.GearSetImplementationAnalysis)

    @property
    def gear_set_implementation_analysis_abstract(
        self: "CastSelf",
    ) -> "_1267.GearSetImplementationAnalysisAbstract":
        from mastapy._private.gears.analysis import _1267

        return self.__parent__._cast(_1267.GearSetImplementationAnalysisAbstract)

    @property
    def gear_set_design_analysis(self: "CastSelf") -> "_1264.GearSetDesignAnalysis":
        from mastapy._private.gears.analysis import _1264

        return self.__parent__._cast(_1264.GearSetDesignAnalysis)

    @property
    def abstract_gear_set_analysis(self: "CastSelf") -> "_1255.AbstractGearSetAnalysis":
        from mastapy._private.gears.analysis import _1255

        return self.__parent__._cast(_1255.AbstractGearSetAnalysis)

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
    def gear_set_load_distribution_analysis(
        self: "CastSelf",
    ) -> "GearSetLoadDistributionAnalysis":
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
class GearSetLoadDistributionAnalysis(_1266.GearSetImplementationAnalysis):
    """GearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def is_a_system_deflection_analysis(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsASystemDeflectionAnalysis

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_GearSetLoadDistributionAnalysis":
        """Cast to another type.

        Returns:
            _Cast_GearSetLoadDistributionAnalysis
        """
        return _Cast_GearSetLoadDistributionAnalysis(self)
