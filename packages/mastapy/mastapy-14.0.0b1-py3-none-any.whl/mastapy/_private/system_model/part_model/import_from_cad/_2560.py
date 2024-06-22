"""MountableComponentFromCAD"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.system_model.part_model.import_from_cad import _2551
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "MountableComponentFromCAD"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model.import_from_cad import (
        _2550,
        _2552,
        _2553,
        _2554,
        _2555,
        _2556,
        _2557,
        _2558,
        _2562,
        _2563,
        _2564,
    )

    Self = TypeVar("Self", bound="MountableComponentFromCAD")
    CastSelf = TypeVar(
        "CastSelf", bound="MountableComponentFromCAD._Cast_MountableComponentFromCAD"
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentFromCAD",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponentFromCAD:
    """Special nested class for casting MountableComponentFromCAD to subclasses."""

    __parent__: "MountableComponentFromCAD"

    @property
    def component_from_cad(self: "CastSelf") -> "_2551.ComponentFromCAD":
        return self.__parent__._cast(_2551.ComponentFromCAD)

    @property
    def clutch_from_cad(self: "CastSelf") -> "_2550.ClutchFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2550

        return self.__parent__._cast(_2550.ClutchFromCAD)

    @property
    def concept_bearing_from_cad(self: "CastSelf") -> "_2552.ConceptBearingFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2552

        return self.__parent__._cast(_2552.ConceptBearingFromCAD)

    @property
    def connector_from_cad(self: "CastSelf") -> "_2553.ConnectorFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2553

        return self.__parent__._cast(_2553.ConnectorFromCAD)

    @property
    def cylindrical_gear_from_cad(self: "CastSelf") -> "_2554.CylindricalGearFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2554

        return self.__parent__._cast(_2554.CylindricalGearFromCAD)

    @property
    def cylindrical_gear_in_planetary_set_from_cad(
        self: "CastSelf",
    ) -> "_2555.CylindricalGearInPlanetarySetFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2555

        return self.__parent__._cast(_2555.CylindricalGearInPlanetarySetFromCAD)

    @property
    def cylindrical_planet_gear_from_cad(
        self: "CastSelf",
    ) -> "_2556.CylindricalPlanetGearFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2556

        return self.__parent__._cast(_2556.CylindricalPlanetGearFromCAD)

    @property
    def cylindrical_ring_gear_from_cad(
        self: "CastSelf",
    ) -> "_2557.CylindricalRingGearFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2557

        return self.__parent__._cast(_2557.CylindricalRingGearFromCAD)

    @property
    def cylindrical_sun_gear_from_cad(
        self: "CastSelf",
    ) -> "_2558.CylindricalSunGearFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2558

        return self.__parent__._cast(_2558.CylindricalSunGearFromCAD)

    @property
    def pulley_from_cad(self: "CastSelf") -> "_2562.PulleyFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2562

        return self.__parent__._cast(_2562.PulleyFromCAD)

    @property
    def rigid_connector_from_cad(self: "CastSelf") -> "_2563.RigidConnectorFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2563

        return self.__parent__._cast(_2563.RigidConnectorFromCAD)

    @property
    def rolling_bearing_from_cad(self: "CastSelf") -> "_2564.RollingBearingFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2564

        return self.__parent__._cast(_2564.RollingBearingFromCAD)

    @property
    def mountable_component_from_cad(self: "CastSelf") -> "MountableComponentFromCAD":
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
class MountableComponentFromCAD(_2551.ComponentFromCAD):
    """MountableComponentFromCAD

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT_FROM_CAD

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def offset(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: "Self", value: "float") -> None:
        self.wrapped.Offset = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_MountableComponentFromCAD":
        """Cast to another type.

        Returns:
            _Cast_MountableComponentFromCAD
        """
        return _Cast_MountableComponentFromCAD(self)
