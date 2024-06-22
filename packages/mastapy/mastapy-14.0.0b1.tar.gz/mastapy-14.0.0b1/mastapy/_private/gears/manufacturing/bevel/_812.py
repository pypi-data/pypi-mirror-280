"""ConicalPinionMicroGeometryConfig"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.manufacturing.bevel import _800
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_PINION_MICRO_GEOMETRY_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalPinionMicroGeometryConfig"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.bevel import _806, _801
    from mastapy._private.gears.analysis import _1259, _1256, _1253

    Self = TypeVar("Self", bound="ConicalPinionMicroGeometryConfig")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalPinionMicroGeometryConfig",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalPinionMicroGeometryConfig:
    """Special nested class for casting ConicalPinionMicroGeometryConfig to subclasses."""

    __parent__: "ConicalPinionMicroGeometryConfig"

    @property
    def conical_gear_micro_geometry_config(
        self: "CastSelf",
    ) -> "_800.ConicalGearMicroGeometryConfig":
        return self.__parent__._cast(_800.ConicalGearMicroGeometryConfig)

    @property
    def conical_gear_micro_geometry_config_base(
        self: "CastSelf",
    ) -> "_801.ConicalGearMicroGeometryConfigBase":
        from mastapy._private.gears.manufacturing.bevel import _801

        return self.__parent__._cast(_801.ConicalGearMicroGeometryConfigBase)

    @property
    def gear_implementation_detail(
        self: "CastSelf",
    ) -> "_1259.GearImplementationDetail":
        from mastapy._private.gears.analysis import _1259

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
    def conical_pinion_micro_geometry_config(
        self: "CastSelf",
    ) -> "ConicalPinionMicroGeometryConfig":
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
class ConicalPinionMicroGeometryConfig(_800.ConicalGearMicroGeometryConfig):
    """ConicalPinionMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_PINION_MICRO_GEOMETRY_CONFIG

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def pinion_concave_ob_configuration(
        self: "Self",
    ) -> "_806.ConicalMeshFlankNURBSMicroGeometryConfig":
        """mastapy._private.gears.manufacturing.bevel.ConicalMeshFlankNURBSMicroGeometryConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConcaveOBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_convex_ib_configuration(
        self: "Self",
    ) -> "_806.ConicalMeshFlankNURBSMicroGeometryConfig":
        """mastapy._private.gears.manufacturing.bevel.ConicalMeshFlankNURBSMicroGeometryConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConvexIBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalPinionMicroGeometryConfig":
        """Cast to another type.

        Returns:
            _Cast_ConicalPinionMicroGeometryConfig
        """
        return _Cast_ConicalPinionMicroGeometryConfig(self)
