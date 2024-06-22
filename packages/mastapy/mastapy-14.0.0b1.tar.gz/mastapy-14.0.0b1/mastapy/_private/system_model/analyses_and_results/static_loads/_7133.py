"""WormGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _7042
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_WORM_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearSetLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2608
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7131,
        _7132,
        _7101,
        _6953,
        _7077,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="WormGearSetLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="WormGearSetLoadCase._Cast_WormGearSetLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_WormGearSetLoadCase:
    """Special nested class for casting WormGearSetLoadCase to subclasses."""

    __parent__: "WormGearSetLoadCase"

    @property
    def gear_set_load_case(self: "CastSelf") -> "_7042.GearSetLoadCase":
        return self.__parent__._cast(_7042.GearSetLoadCase)

    @property
    def specialised_assembly_load_case(
        self: "CastSelf",
    ) -> "_7101.SpecialisedAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7101,
        )

        return self.__parent__._cast(_7101.SpecialisedAssemblyLoadCase)

    @property
    def abstract_assembly_load_case(
        self: "CastSelf",
    ) -> "_6953.AbstractAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6953,
        )

        return self.__parent__._cast(_6953.AbstractAssemblyLoadCase)

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
    def worm_gear_set_load_case(self: "CastSelf") -> "WormGearSetLoadCase":
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
class WormGearSetLoadCase(_7042.GearSetLoadCase):
    """WormGearSetLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _WORM_GEAR_SET_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2608.WormGearSet":
        """mastapy._private.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_load_case(self: "Self") -> "List[_7131.WormGearLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.WormGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gears_load_case(self: "Self") -> "List[_7131.WormGearLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.WormGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_load_case(self: "Self") -> "List[_7132.WormGearMeshLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_load_case(self: "Self") -> "List[_7132.WormGearMeshLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_WormGearSetLoadCase":
        """Cast to another type.

        Returns:
            _Cast_WormGearSetLoadCase
        """
        return _Cast_WormGearSetLoadCase(self)
