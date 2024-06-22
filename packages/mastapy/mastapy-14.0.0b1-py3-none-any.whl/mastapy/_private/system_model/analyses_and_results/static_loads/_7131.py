"""WormGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _7037
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_WORM_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model.gears import _2607
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7073,
        _6984,
        _7077,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="WormGearLoadCase")
    CastSelf = TypeVar("CastSelf", bound="WormGearLoadCase._Cast_WormGearLoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("WormGearLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_WormGearLoadCase:
    """Special nested class for casting WormGearLoadCase to subclasses."""

    __parent__: "WormGearLoadCase"

    @property
    def gear_load_case(self: "CastSelf") -> "_7037.GearLoadCase":
        return self.__parent__._cast(_7037.GearLoadCase)

    @property
    def mountable_component_load_case(
        self: "CastSelf",
    ) -> "_7073.MountableComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7073,
        )

        return self.__parent__._cast(_7073.MountableComponentLoadCase)

    @property
    def component_load_case(self: "CastSelf") -> "_6984.ComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6984,
        )

        return self.__parent__._cast(_6984.ComponentLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "_7077.PartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7077,
        )

        return self.__parent__._cast(_7077.PartLoadCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def worm_gear_load_case(self: "CastSelf") -> "WormGearLoadCase":
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
class WormGearLoadCase(_7037.GearLoadCase):
    """WormGearLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _WORM_GEAR_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2607.WormGear":
        """mastapy._private.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_WormGearLoadCase":
        """Cast to another type.

        Returns:
            _Cast_WormGearLoadCase
        """
        return _Cast_WormGearLoadCase(self)
