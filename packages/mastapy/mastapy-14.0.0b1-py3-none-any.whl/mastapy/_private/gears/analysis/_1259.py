"""GearImplementationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.analysis import _1256
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationDetail"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.scripting import _1789
    from mastapy._private.gears.manufacturing.cylindrical import _635
    from mastapy._private.gears.manufacturing.bevel import (
        _799,
        _800,
        _801,
        _811,
        _812,
        _817,
    )
    from mastapy._private.gears.gear_designs.face import _1017
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1132,
        _1133,
        _1136,
    )
    from mastapy._private.gears.fe_model import _1235
    from mastapy._private.gears.fe_model.cylindrical import _1239
    from mastapy._private.gears.fe_model.conical import _1242
    from mastapy._private.gears.analysis import _1253

    Self = TypeVar("Self", bound="GearImplementationDetail")
    CastSelf = TypeVar(
        "CastSelf", bound="GearImplementationDetail._Cast_GearImplementationDetail"
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationDetail",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearImplementationDetail:
    """Special nested class for casting GearImplementationDetail to subclasses."""

    __parent__: "GearImplementationDetail"

    @property
    def gear_design_analysis(self: "CastSelf") -> "_1256.GearDesignAnalysis":
        return self.__parent__._cast(_1256.GearDesignAnalysis)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def cylindrical_gear_manufacturing_config(
        self: "CastSelf",
    ) -> "_635.CylindricalGearManufacturingConfig":
        from mastapy._private.gears.manufacturing.cylindrical import _635

        return self.__parent__._cast(_635.CylindricalGearManufacturingConfig)

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
    def gear_implementation_detail(self: "CastSelf") -> "GearImplementationDetail":
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
class GearImplementationDetail(_1256.GearDesignAnalysis):
    """GearImplementationDetail

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_IMPLEMENTATION_DETAIL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def user_specified_data(self: "Self") -> "_1789.UserSpecifiedData":
        """mastapy._private.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_GearImplementationDetail":
        """Cast to another type.

        Returns:
            _Cast_GearImplementationDetail
        """
        return _Cast_GearImplementationDetail(self)
