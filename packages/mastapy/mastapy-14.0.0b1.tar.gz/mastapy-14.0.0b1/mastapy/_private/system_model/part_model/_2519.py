"""MicrophoneArray"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.part_model import _2532
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_MICROPHONE_ARRAY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MicrophoneArray"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model.acoustics import _2694
    from mastapy._private.system_model.part_model import _2488, _2524
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="MicrophoneArray")
    CastSelf = TypeVar("CastSelf", bound="MicrophoneArray._Cast_MicrophoneArray")


__docformat__ = "restructuredtext en"
__all__ = ("MicrophoneArray",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MicrophoneArray:
    """Special nested class for casting MicrophoneArray to subclasses."""

    __parent__: "MicrophoneArray"

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
    def microphone_array(self: "CastSelf") -> "MicrophoneArray":
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
class MicrophoneArray(_2532.SpecialisedAssembly):
    """MicrophoneArray

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MICROPHONE_ARRAY

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def drawing_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.DrawingDiameter

        if temp is None:
            return 0.0

        return temp

    @drawing_diameter.setter
    @enforce_parameter_types
    def drawing_diameter(self: "Self", value: "float") -> None:
        self.wrapped.DrawingDiameter = float(value) if value is not None else 0.0

    @property
    def array_design(self: "Self") -> "_2694.MicrophoneArrayDesign":
        """mastapy._private.system_model.part_model.acoustics.MicrophoneArrayDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ArrayDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_MicrophoneArray":
        """Cast to another type.

        Returns:
            _Cast_MicrophoneArray
        """
        return _Cast_MicrophoneArray(self)
