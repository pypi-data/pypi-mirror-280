"""ConicalMeshMicroGeometryConfigBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.gears.analysis import _1263
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshMicroGeometryConfigBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.conical import _1193
    from mastapy._private.gears.manufacturing.bevel import _801, _808, _809
    from mastapy._private.gears.analysis import _1260, _1254

    Self = TypeVar("Self", bound="ConicalMeshMicroGeometryConfigBase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshMicroGeometryConfigBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalMeshMicroGeometryConfigBase:
    """Special nested class for casting ConicalMeshMicroGeometryConfigBase to subclasses."""

    __parent__: "ConicalMeshMicroGeometryConfigBase"

    @property
    def gear_mesh_implementation_detail(
        self: "CastSelf",
    ) -> "_1263.GearMeshImplementationDetail":
        return self.__parent__._cast(_1263.GearMeshImplementationDetail)

    @property
    def gear_mesh_design_analysis(self: "CastSelf") -> "_1260.GearMeshDesignAnalysis":
        from mastapy._private.gears.analysis import _1260

        return self.__parent__._cast(_1260.GearMeshDesignAnalysis)

    @property
    def abstract_gear_mesh_analysis(
        self: "CastSelf",
    ) -> "_1254.AbstractGearMeshAnalysis":
        from mastapy._private.gears.analysis import _1254

        return self.__parent__._cast(_1254.AbstractGearMeshAnalysis)

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
    ) -> "ConicalMeshMicroGeometryConfigBase":
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
class ConicalMeshMicroGeometryConfigBase(_1263.GearMeshImplementationDetail):
    """ConicalMeshMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def mesh(self: "Self") -> "_1193.ConicalGearMeshDesign":
        """mastapy._private.gears.gear_designs.conical.ConicalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_config(self: "Self") -> "_801.ConicalGearMicroGeometryConfigBase":
        """mastapy._private.gears.manufacturing.bevel.ConicalGearMicroGeometryConfigBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalMeshMicroGeometryConfigBase":
        """Cast to another type.

        Returns:
            _Cast_ConicalMeshMicroGeometryConfigBase
        """
        return _Cast_ConicalMeshMicroGeometryConfigBase(self)
