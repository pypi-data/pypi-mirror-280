"""ConicalGearMicroGeometryConfigBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.analysis import _1259
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalGearMicroGeometryConfigBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.bevel import (
        _819,
        _799,
        _800,
        _811,
        _812,
        _817,
    )
    from mastapy._private.gears.analysis import _1256, _1253

    Self = TypeVar("Self", bound="ConicalGearMicroGeometryConfigBase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMicroGeometryConfigBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearMicroGeometryConfigBase:
    """Special nested class for casting ConicalGearMicroGeometryConfigBase to subclasses."""

    __parent__: "ConicalGearMicroGeometryConfigBase"

    @property
    def gear_implementation_detail(
        self: "CastSelf",
    ) -> "_1259.GearImplementationDetail":
        return self.__parent__._cast(_1259.GearImplementationDetail)

    @property
    def gear_design_analysis(self: "CastSelf") -> "_1256.GearDesignAnalysis":
        from mastapy._private.gears.analysis import _1256

        return self.__parent__._cast(_1256.GearDesignAnalysis)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

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
    def conical_gear_micro_geometry_config_base(
        self: "CastSelf",
    ) -> "ConicalGearMicroGeometryConfigBase":
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
class ConicalGearMicroGeometryConfigBase(_1259.GearImplementationDetail):
    """ConicalGearMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def flank_measurement_border(self: "Self") -> "_819.FlankMeasurementBorder":
        """mastapy._private.gears.manufacturing.bevel.FlankMeasurementBorder

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankMeasurementBorder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearMicroGeometryConfigBase":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearMicroGeometryConfigBase
        """
        return _Cast_ConicalGearMicroGeometryConfigBase(self)
