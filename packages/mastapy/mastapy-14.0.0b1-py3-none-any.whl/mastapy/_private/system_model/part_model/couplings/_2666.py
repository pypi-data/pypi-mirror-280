"""SynchroniserHalf"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.system_model.part_model.couplings import _2667
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SYNCHRONISER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.system_model.part_model.couplings import _2665, _2642
    from mastapy._private.system_model.part_model import _2520, _2498, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="SynchroniserHalf")
    CastSelf = TypeVar("CastSelf", bound="SynchroniserHalf._Cast_SynchroniserHalf")


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalf",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SynchroniserHalf:
    """Special nested class for casting SynchroniserHalf to subclasses."""

    __parent__: "SynchroniserHalf"

    @property
    def synchroniser_part(self: "CastSelf") -> "_2667.SynchroniserPart":
        return self.__parent__._cast(_2667.SynchroniserPart)

    @property
    def coupling_half(self: "CastSelf") -> "_2642.CouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2642

        return self.__parent__._cast(_2642.CouplingHalf)

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
        from mastapy._private.system_model.part_model import _2520

        return self.__parent__._cast(_2520.MountableComponent)

    @property
    def component(self: "CastSelf") -> "_2498.Component":
        from mastapy._private.system_model.part_model import _2498

        return self.__parent__._cast(_2498.Component)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def synchroniser_half(self: "CastSelf") -> "SynchroniserHalf":
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
class SynchroniserHalf(_2667.SynchroniserPart):
    """SynchroniserHalf

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SYNCHRONISER_HALF

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def area_of_cone_with_minimum_area(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaOfConeWithMinimumArea

        if temp is None:
            return 0.0

        return temp

    @property
    def blocker_chamfer_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BlockerChamferAngle

        if temp is None:
            return 0.0

        return temp

    @blocker_chamfer_angle.setter
    @enforce_parameter_types
    def blocker_chamfer_angle(self: "Self", value: "float") -> None:
        self.wrapped.BlockerChamferAngle = float(value) if value is not None else 0.0

    @property
    def blocker_chamfer_coefficient_of_friction(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BlockerChamferCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @blocker_chamfer_coefficient_of_friction.setter
    @enforce_parameter_types
    def blocker_chamfer_coefficient_of_friction(self: "Self", value: "float") -> None:
        self.wrapped.BlockerChamferCoefficientOfFriction = (
            float(value) if value is not None else 0.0
        )

    @property
    def blocker_chamfer_pcd(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BlockerChamferPCD

        if temp is None:
            return 0.0

        return temp

    @blocker_chamfer_pcd.setter
    @enforce_parameter_types
    def blocker_chamfer_pcd(self: "Self", value: "float") -> None:
        self.wrapped.BlockerChamferPCD = float(value) if value is not None else 0.0

    @property
    def cone_side(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConeSide

        if temp is None:
            return ""

        return temp

    @property
    def diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Diameter = value

    @property
    def number_of_surfaces(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfSurfaces

        if temp is None:
            return 0

        return temp

    @number_of_surfaces.setter
    @enforce_parameter_types
    def number_of_surfaces(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfSurfaces = int(value) if value is not None else 0

    @property
    def total_area_of_cones(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalAreaOfCones

        if temp is None:
            return 0.0

        return temp

    @property
    def cones(self: "Self") -> "List[_2665.SynchroniserCone]":
        """List[mastapy._private.system_model.part_model.couplings.SynchroniserCone]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_SynchroniserHalf":
        """Cast to another type.

        Returns:
            _Cast_SynchroniserHalf
        """
        return _Cast_SynchroniserHalf(self)
