"""ConceptGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.part_model.gears import _2588
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CONCEPT_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.concept import _1216
    from mastapy._private.system_model.part_model.gears import _2577
    from mastapy._private.system_model.connections_and_sockets.gears import _2358
    from mastapy._private.system_model.part_model import _2532, _2488, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="ConceptGearSet")
    CastSelf = TypeVar("CastSelf", bound="ConceptGearSet._Cast_ConceptGearSet")


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSet",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConceptGearSet:
    """Special nested class for casting ConceptGearSet to subclasses."""

    __parent__: "ConceptGearSet"

    @property
    def gear_set(self: "CastSelf") -> "_2588.GearSet":
        return self.__parent__._cast(_2588.GearSet)

    @property
    def specialised_assembly(self: "CastSelf") -> "_2532.SpecialisedAssembly":
        from mastapy._private.system_model.part_model import _2532

        return self.__parent__._cast(_2532.SpecialisedAssembly)

    @property
    def abstract_assembly(self: "CastSelf") -> "_2488.AbstractAssembly":
        from mastapy._private.system_model.part_model import _2488

        return self.__parent__._cast(_2488.AbstractAssembly)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def concept_gear_set(self: "CastSelf") -> "ConceptGearSet":
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
class ConceptGearSet(_2588.GearSet):
    """ConceptGearSet

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONCEPT_GEAR_SET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def active_gear_set_design(self: "Self") -> "_1216.ConceptGearSetDesign":
        """mastapy._private.gears.gear_designs.concept.ConceptGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gear_set_design(self: "Self") -> "_1216.ConceptGearSetDesign":
        """mastapy._private.gears.gear_designs.concept.ConceptGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears(self: "Self") -> "List[_2577.ConceptGear]":
        """List[mastapy._private.system_model.part_model.gears.ConceptGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes(self: "Self") -> "List[_2358.ConceptGearMesh]":
        """List[mastapy._private.system_model.connections_and_sockets.gears.ConceptGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ConceptGearSet":
        """Cast to another type.

        Returns:
            _Cast_ConceptGearSet
        """
        return _Cast_ConceptGearSet(self)
