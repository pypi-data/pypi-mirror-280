"""StraightBevelDiffGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.static_loads import _6976
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearSetLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.gears import _2602
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7108,
        _7109,
        _6962,
        _6995,
        _7042,
        _7101,
        _6953,
        _7077,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="StraightBevelDiffGearSetLoadCase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelDiffGearSetLoadCase:
    """Special nested class for casting StraightBevelDiffGearSetLoadCase to subclasses."""

    __parent__: "StraightBevelDiffGearSetLoadCase"

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
    def straight_bevel_diff_gear_set_load_case(
        self: "CastSelf",
    ) -> "StraightBevelDiffGearSetLoadCase":
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
class StraightBevelDiffGearSetLoadCase(_6976.BevelGearSetLoadCase):
    """StraightBevelDiffGearSetLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def sun_speeds_are_equal(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.SunSpeedsAreEqual

        if temp is None:
            return False

        return temp

    @sun_speeds_are_equal.setter
    @enforce_parameter_types
    def sun_speeds_are_equal(self: "Self", value: "bool") -> None:
        self.wrapped.SunSpeedsAreEqual = bool(value) if value is not None else False

    @property
    def assembly_design(self: "Self") -> "_2602.StraightBevelDiffGearSet":
        """mastapy._private.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears_load_case(
        self: "Self",
    ) -> "List[_7108.StraightBevelDiffGearLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase]

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
    def straight_bevel_diff_gears_load_case(
        self: "Self",
    ) -> "List[_7108.StraightBevelDiffGearLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_load_case(
        self: "Self",
    ) -> "List[_7109.StraightBevelDiffGearMeshLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase]

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
    def straight_bevel_diff_meshes_load_case(
        self: "Self",
    ) -> "List[_7109.StraightBevelDiffGearMeshLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelDiffGearSetLoadCase":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelDiffGearSetLoadCase
        """
        return _Cast_StraightBevelDiffGearSetLoadCase(self)
