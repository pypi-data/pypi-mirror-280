"""GearMeshImplementationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.analysis import _1260
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_GEAR_MESH_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshImplementationDetail"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical import _645
    from mastapy._private.gears.manufacturing.bevel import _808, _809, _810
    from mastapy._private.gears.gear_designs.face import _1016
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import _1130
    from mastapy._private.gears.fe_model import _1236
    from mastapy._private.gears.fe_model.cylindrical import _1240
    from mastapy._private.gears.fe_model.conical import _1243
    from mastapy._private.gears.analysis import _1254

    Self = TypeVar("Self", bound="GearMeshImplementationDetail")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshImplementationDetail",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearMeshImplementationDetail:
    """Special nested class for casting GearMeshImplementationDetail to subclasses."""

    __parent__: "GearMeshImplementationDetail"

    @property
    def gear_mesh_design_analysis(self: "CastSelf") -> "_1260.GearMeshDesignAnalysis":
        return self.__parent__._cast(_1260.GearMeshDesignAnalysis)

    @property
    def abstract_gear_mesh_analysis(
        self: "CastSelf",
    ) -> "_1254.AbstractGearMeshAnalysis":
        from mastapy._private.gears.analysis import _1254

        return self.__parent__._cast(_1254.AbstractGearMeshAnalysis)

    @property
    def cylindrical_mesh_manufacturing_config(
        self: "CastSelf",
    ) -> "_645.CylindricalMeshManufacturingConfig":
        from mastapy._private.gears.manufacturing.cylindrical import _645

        return self.__parent__._cast(_645.CylindricalMeshManufacturingConfig)

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
    def gear_mesh_implementation_detail(
        self: "CastSelf",
    ) -> "GearMeshImplementationDetail":
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
class GearMeshImplementationDetail(_1260.GearMeshDesignAnalysis):
    """GearMeshImplementationDetail

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_MESH_IMPLEMENTATION_DETAIL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_GearMeshImplementationDetail":
        """Cast to another type.

        Returns:
            _Cast_GearMeshImplementationDetail
        """
        return _Cast_GearMeshImplementationDetail(self)
