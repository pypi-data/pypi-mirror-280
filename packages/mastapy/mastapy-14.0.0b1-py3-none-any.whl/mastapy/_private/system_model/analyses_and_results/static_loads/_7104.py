"""SpiralBevelGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _6976
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearSetLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2600
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7102,
        _7103,
        _6962,
        _6995,
        _7042,
        _7101,
        _6953,
        _7077,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="SpiralBevelGearSetLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpiralBevelGearSetLoadCase:
    """Special nested class for casting SpiralBevelGearSetLoadCase to subclasses."""

    __parent__: "SpiralBevelGearSetLoadCase"

    @property
    def bevel_gear_set_load_case(self: "CastSelf") -> "_6976.BevelGearSetLoadCase":
        return self.__parent__._cast(_6976.BevelGearSetLoadCase)

    @property
    def agma_gleason_conical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_6962.AGMAGleasonConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6962,
        )

        return self.__parent__._cast(_6962.AGMAGleasonConicalGearSetLoadCase)

    @property
    def conical_gear_set_load_case(self: "CastSelf") -> "_6995.ConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6995,
        )

        return self.__parent__._cast(_6995.ConicalGearSetLoadCase)

    @property
    def gear_set_load_case(self: "CastSelf") -> "_7042.GearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7042,
        )

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
    def spiral_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "SpiralBevelGearSetLoadCase":
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
class SpiralBevelGearSetLoadCase(_6976.BevelGearSetLoadCase):
    """SpiralBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2600.SpiralBevelGearSet":
        """mastapy._private.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears_load_case(self: "Self") -> "List[_7102.SpiralBevelGearLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears_load_case(
        self: "Self",
    ) -> "List[_7102.SpiralBevelGearLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_load_case(
        self: "Self",
    ) -> "List[_7103.SpiralBevelGearMeshLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_load_case(
        self: "Self",
    ) -> "List[_7103.SpiralBevelGearMeshLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_SpiralBevelGearSetLoadCase":
        """Cast to another type.

        Returns:
            _Cast_SpiralBevelGearSetLoadCase
        """
        return _Cast_SpiralBevelGearSetLoadCase(self)
