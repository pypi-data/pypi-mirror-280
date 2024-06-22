"""BevelLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.load_case.conical import _908
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_BEVEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Bevel", "BevelLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.load_case import _896
    from mastapy._private.gears.analysis import _1256, _1253

    Self = TypeVar("Self", bound="BevelLoadCase")
    CastSelf = TypeVar("CastSelf", bound="BevelLoadCase._Cast_BevelLoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("BevelLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelLoadCase:
    """Special nested class for casting BevelLoadCase to subclasses."""

    __parent__: "BevelLoadCase"

    @property
    def conical_gear_load_case(self: "CastSelf") -> "_908.ConicalGearLoadCase":
        return self.__parent__._cast(_908.ConicalGearLoadCase)

    @property
    def gear_load_case_base(self: "CastSelf") -> "_896.GearLoadCaseBase":
        from mastapy._private.gears.load_case import _896

        return self.__parent__._cast(_896.GearLoadCaseBase)

    @property
    def gear_design_analysis(self: "CastSelf") -> "_1256.GearDesignAnalysis":
        from mastapy._private.gears.analysis import _1256

        return self.__parent__._cast(_1256.GearDesignAnalysis)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def bevel_load_case(self: "CastSelf") -> "BevelLoadCase":
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
class BevelLoadCase(_908.ConicalGearLoadCase):
    """BevelLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_BevelLoadCase":
        """Cast to another type.

        Returns:
            _Cast_BevelLoadCase
        """
        return _Cast_BevelLoadCase(self)
