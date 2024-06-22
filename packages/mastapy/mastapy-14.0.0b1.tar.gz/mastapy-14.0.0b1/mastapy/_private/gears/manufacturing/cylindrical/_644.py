"""CylindricalManufacturedGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.analysis import _1266
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "CylindricalManufacturedGearSetLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical import _648
    from mastapy._private.gears.rating.cylindrical import _475
    from mastapy._private.gears.analysis import _1267, _1264, _1255

    Self = TypeVar("Self", bound="CylindricalManufacturedGearSetLoadCase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalManufacturedGearSetLoadCase._Cast_CylindricalManufacturedGearSetLoadCase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalManufacturedGearSetLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalManufacturedGearSetLoadCase:
    """Special nested class for casting CylindricalManufacturedGearSetLoadCase to subclasses."""

    __parent__: "CylindricalManufacturedGearSetLoadCase"

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
    def cylindrical_manufactured_gear_set_load_case(
        self: "CastSelf",
    ) -> "CylindricalManufacturedGearSetLoadCase":
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
class CylindricalManufacturedGearSetLoadCase(_1266.GearSetImplementationAnalysis):
    """CylindricalManufacturedGearSetLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_MANUFACTURED_GEAR_SET_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def manufacturing_configuration(
        self: "Self",
    ) -> "_648.CylindricalSetManufacturingConfig":
        """mastapy._private.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: "Self") -> "_475.CylindricalGearSetRating":
        """mastapy._private.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalManufacturedGearSetLoadCase":
        """Cast to another type.

        Returns:
            _Cast_CylindricalManufacturedGearSetLoadCase
        """
        return _Cast_CylindricalManufacturedGearSetLoadCase(self)
