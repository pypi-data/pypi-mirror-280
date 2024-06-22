"""CycloidalAssembly"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.part_model import _2532
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.cycloidal import _1499
    from mastapy._private.system_model.part_model.cycloidal import _2626, _2625
    from mastapy._private.system_model.part_model import _2488, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="CycloidalAssembly")
    CastSelf = TypeVar("CastSelf", bound="CycloidalAssembly._Cast_CycloidalAssembly")


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssembly",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CycloidalAssembly:
    """Special nested class for casting CycloidalAssembly to subclasses."""

    __parent__: "CycloidalAssembly"

    @property
    def specialised_assembly(self: "CastSelf") -> "_2532.SpecialisedAssembly":
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
    def cycloidal_assembly(self: "CastSelf") -> "CycloidalAssembly":
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
class CycloidalAssembly(_2532.SpecialisedAssembly):
    """CycloidalAssembly

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYCLOIDAL_ASSEMBLY

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cycloidal_assembly_design(self: "Self") -> "_1499.CycloidalAssemblyDesign":
        """mastapy._private.cycloidal.CycloidalAssemblyDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalAssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_pins(self: "Self") -> "_2626.RingPins":
        """mastapy._private.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPins

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def known_designs(self: "Self") -> "List[_1499.CycloidalAssemblyDesign]":
        """List[mastapy._private.cycloidal.CycloidalAssemblyDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KnownDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_disc(self: "Self") -> "_2625.CycloidalDisc":
        """mastapy._private.system_model.part_model.cycloidal.CycloidalDisc"""
        method_result = self.wrapped.AddDisc()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def design_named(self: "Self", name: "str") -> "_1499.CycloidalAssemblyDesign":
        """mastapy._private.cycloidal.CycloidalAssemblyDesign

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.DesignNamed(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def remove_disc_from_designs(self: "Self", disc_id: "int") -> None:
        """Method does not return.

        Args:
            disc_id (int)
        """
        disc_id = int(disc_id)
        self.wrapped.RemoveDiscFromDesigns(disc_id if disc_id else 0)

    @enforce_parameter_types
    def set_active_cycloidal_assembly_design(
        self: "Self", cycloidal_assembly_design: "_1499.CycloidalAssemblyDesign"
    ) -> None:
        """Method does not return.

        Args:
            cycloidal_assembly_design (mastapy._private.cycloidal.CycloidalAssemblyDesign)
        """
        self.wrapped.SetActiveCycloidalAssemblyDesign(
            cycloidal_assembly_design.wrapped if cycloidal_assembly_design else None
        )

    @enforce_parameter_types
    def try_remove_design(
        self: "Self", design: "_1499.CycloidalAssemblyDesign"
    ) -> "bool":
        """bool

        Args:
            design (mastapy._private.cycloidal.CycloidalAssemblyDesign)
        """
        method_result = self.wrapped.TryRemoveDesign(design.wrapped if design else None)
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_CycloidalAssembly":
        """Cast to another type.

        Returns:
            _Cast_CycloidalAssembly
        """
        return _Cast_CycloidalAssembly(self)
