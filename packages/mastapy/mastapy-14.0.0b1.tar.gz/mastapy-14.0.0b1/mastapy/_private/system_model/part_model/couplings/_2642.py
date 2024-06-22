"""CouplingHalf"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.part_model import _2520
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.system_model.part_model.couplings import (
        _2636,
        _2639,
        _2645,
        _2647,
        _2649,
        _2655,
        _2663,
        _2666,
        _2667,
        _2668,
        _2670,
        _2672,
    )
    from mastapy._private.system_model.part_model import _2498, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="CouplingHalf")
    CastSelf = TypeVar("CastSelf", bound="CouplingHalf._Cast_CouplingHalf")


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalf",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalf:
    """Special nested class for casting CouplingHalf to subclasses."""

    __parent__: "CouplingHalf"

    @property
    def mountable_component(self: "CastSelf") -> "_2520.MountableComponent":
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
    def clutch_half(self: "CastSelf") -> "_2636.ClutchHalf":
        from mastapy._private.system_model.part_model.couplings import _2636

        return self.__parent__._cast(_2636.ClutchHalf)

    @property
    def concept_coupling_half(self: "CastSelf") -> "_2639.ConceptCouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2639

        return self.__parent__._cast(_2639.ConceptCouplingHalf)

    @property
    def cvt_pulley(self: "CastSelf") -> "_2645.CVTPulley":
        from mastapy._private.system_model.part_model.couplings import _2645

        return self.__parent__._cast(_2645.CVTPulley)

    @property
    def part_to_part_shear_coupling_half(
        self: "CastSelf",
    ) -> "_2647.PartToPartShearCouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2647

        return self.__parent__._cast(_2647.PartToPartShearCouplingHalf)

    @property
    def pulley(self: "CastSelf") -> "_2649.Pulley":
        from mastapy._private.system_model.part_model.couplings import _2649

        return self.__parent__._cast(_2649.Pulley)

    @property
    def rolling_ring(self: "CastSelf") -> "_2655.RollingRing":
        from mastapy._private.system_model.part_model.couplings import _2655

        return self.__parent__._cast(_2655.RollingRing)

    @property
    def spring_damper_half(self: "CastSelf") -> "_2663.SpringDamperHalf":
        from mastapy._private.system_model.part_model.couplings import _2663

        return self.__parent__._cast(_2663.SpringDamperHalf)

    @property
    def synchroniser_half(self: "CastSelf") -> "_2666.SynchroniserHalf":
        from mastapy._private.system_model.part_model.couplings import _2666

        return self.__parent__._cast(_2666.SynchroniserHalf)

    @property
    def synchroniser_part(self: "CastSelf") -> "_2667.SynchroniserPart":
        from mastapy._private.system_model.part_model.couplings import _2667

        return self.__parent__._cast(_2667.SynchroniserPart)

    @property
    def synchroniser_sleeve(self: "CastSelf") -> "_2668.SynchroniserSleeve":
        from mastapy._private.system_model.part_model.couplings import _2668

        return self.__parent__._cast(_2668.SynchroniserSleeve)

    @property
    def torque_converter_pump(self: "CastSelf") -> "_2670.TorqueConverterPump":
        from mastapy._private.system_model.part_model.couplings import _2670

        return self.__parent__._cast(_2670.TorqueConverterPump)

    @property
    def torque_converter_turbine(self: "CastSelf") -> "_2672.TorqueConverterTurbine":
        from mastapy._private.system_model.part_model.couplings import _2672

        return self.__parent__._cast(_2672.TorqueConverterTurbine)

    @property
    def coupling_half(self: "CastSelf") -> "CouplingHalf":
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
class CouplingHalf(_2520.MountableComponent):
    """CouplingHalf

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bore(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bore.setter
    @enforce_parameter_types
    def bore(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Bore = value

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
    def width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: "Self", value: "float") -> None:
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_CouplingHalf":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalf
        """
        return _Cast_CouplingHalf(self)
