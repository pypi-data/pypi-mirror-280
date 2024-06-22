"""SynchroniserSleeve"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.part_model.couplings import _2667
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.system_model.part_model.couplings import _2642
    from mastapy._private.system_model.part_model import _2520, _2498, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="SynchroniserSleeve")
    CastSelf = TypeVar("CastSelf", bound="SynchroniserSleeve._Cast_SynchroniserSleeve")


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeve",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SynchroniserSleeve:
    """Special nested class for casting SynchroniserSleeve to subclasses."""

    __parent__: "SynchroniserSleeve"

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
    def synchroniser_sleeve(self: "CastSelf") -> "SynchroniserSleeve":
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
class SynchroniserSleeve(_2667.SynchroniserPart):
    """SynchroniserSleeve

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SYNCHRONISER_SLEEVE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def hub_bore(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.HubBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @hub_bore.setter
    @enforce_parameter_types
    def hub_bore(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.HubBore = value

    @property
    def hub_height(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.HubHeight

        if temp is None:
            return 0.0

        return temp

    @hub_height.setter
    @enforce_parameter_types
    def hub_height(self: "Self", value: "float") -> None:
        self.wrapped.HubHeight = float(value) if value is not None else 0.0

    @property
    def hub_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.HubWidth

        if temp is None:
            return 0.0

        return temp

    @hub_width.setter
    @enforce_parameter_types
    def hub_width(self: "Self", value: "float") -> None:
        self.wrapped.HubWidth = float(value) if value is not None else 0.0

    @property
    def sleeve_outer_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SleeveOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @sleeve_outer_diameter.setter
    @enforce_parameter_types
    def sleeve_outer_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SleeveOuterDiameter = value

    @property
    def sleeve_selection_height(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SleeveSelectionHeight

        if temp is None:
            return 0.0

        return temp

    @sleeve_selection_height.setter
    @enforce_parameter_types
    def sleeve_selection_height(self: "Self", value: "float") -> None:
        self.wrapped.SleeveSelectionHeight = float(value) if value is not None else 0.0

    @property
    def sleeve_selection_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SleeveSelectionWidth

        if temp is None:
            return 0.0

        return temp

    @sleeve_selection_width.setter
    @enforce_parameter_types
    def sleeve_selection_width(self: "Self", value: "float") -> None:
        self.wrapped.SleeveSelectionWidth = float(value) if value is not None else 0.0

    @property
    def sleeve_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.SleeveWidth

        if temp is None:
            return 0.0

        return temp

    @sleeve_width.setter
    @enforce_parameter_types
    def sleeve_width(self: "Self", value: "float") -> None:
        self.wrapped.SleeveWidth = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_SynchroniserSleeve":
        """Cast to another type.

        Returns:
            _Cast_SynchroniserSleeve
        """
        return _Cast_SynchroniserSleeve(self)
