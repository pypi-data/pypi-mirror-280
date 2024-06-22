"""Coupling"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.part_model import _2532
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.couplings import (
        _2642,
        _2635,
        _2638,
        _2646,
        _2662,
        _2669,
    )
    from mastapy._private.system_model.part_model import _2488, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="Coupling")
    CastSelf = TypeVar("CastSelf", bound="Coupling._Cast_Coupling")


__docformat__ = "restructuredtext en"
__all__ = ("Coupling",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Coupling:
    """Special nested class for casting Coupling to subclasses."""

    __parent__: "Coupling"

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
    def clutch(self: "CastSelf") -> "_2635.Clutch":
        from mastapy._private.system_model.part_model.couplings import _2635

        return self.__parent__._cast(_2635.Clutch)

    @property
    def concept_coupling(self: "CastSelf") -> "_2638.ConceptCoupling":
        from mastapy._private.system_model.part_model.couplings import _2638

        return self.__parent__._cast(_2638.ConceptCoupling)

    @property
    def part_to_part_shear_coupling(
        self: "CastSelf",
    ) -> "_2646.PartToPartShearCoupling":
        from mastapy._private.system_model.part_model.couplings import _2646

        return self.__parent__._cast(_2646.PartToPartShearCoupling)

    @property
    def spring_damper(self: "CastSelf") -> "_2662.SpringDamper":
        from mastapy._private.system_model.part_model.couplings import _2662

        return self.__parent__._cast(_2662.SpringDamper)

    @property
    def torque_converter(self: "CastSelf") -> "_2669.TorqueConverter":
        from mastapy._private.system_model.part_model.couplings import _2669

        return self.__parent__._cast(_2669.TorqueConverter)

    @property
    def coupling(self: "CastSelf") -> "Coupling":
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
class Coupling(_2532.SpecialisedAssembly):
    """Coupling

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def axial_stiffness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness.setter
    @enforce_parameter_types
    def axial_stiffness(self: "Self", value: "float") -> None:
        self.wrapped.AxialStiffness = float(value) if value is not None else 0.0

    @property
    def radial_stiffness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.RadialStiffness

        if temp is None:
            return 0.0

        return temp

    @radial_stiffness.setter
    @enforce_parameter_types
    def radial_stiffness(self: "Self", value: "float") -> None:
        self.wrapped.RadialStiffness = float(value) if value is not None else 0.0

    @property
    def tilt_stiffness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness.setter
    @enforce_parameter_types
    def tilt_stiffness(self: "Self", value: "float") -> None:
        self.wrapped.TiltStiffness = float(value) if value is not None else 0.0

    @property
    def torsional_stiffness(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @torsional_stiffness.setter
    @enforce_parameter_types
    def torsional_stiffness(self: "Self", value: "float") -> None:
        self.wrapped.TorsionalStiffness = float(value) if value is not None else 0.0

    @property
    def halves(self: "Self") -> "List[_2642.CouplingHalf]":
        """List[mastapy._private.system_model.part_model.couplings.CouplingHalf]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Halves

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def half_a(self: "Self") -> "_2642.CouplingHalf":
        """mastapy._private.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HalfA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def half_b(self: "Self") -> "_2642.CouplingHalf":
        """mastapy._private.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HalfB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_Coupling":
        """Cast to another type.

        Returns:
            _Cast_Coupling
        """
        return _Cast_Coupling(self)
