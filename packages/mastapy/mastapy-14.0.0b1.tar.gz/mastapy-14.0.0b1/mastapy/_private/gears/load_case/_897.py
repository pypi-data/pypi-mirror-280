"""GearSetLoadCaseBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import utility
from mastapy._private.gears.analysis import _1264
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_GEAR_SET_LOAD_CASE_BASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase", "GearSetLoadCaseBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.load_case.worm import _900
    from mastapy._private.gears.load_case.face import _903
    from mastapy._private.gears.load_case.cylindrical import _906
    from mastapy._private.gears.load_case.conical import _909
    from mastapy._private.gears.load_case.concept import _912
    from mastapy._private.gears.load_case.bevel import _916
    from mastapy._private.gears.analysis import _1255

    Self = TypeVar("Self", bound="GearSetLoadCaseBase")
    CastSelf = TypeVar(
        "CastSelf", bound="GearSetLoadCaseBase._Cast_GearSetLoadCaseBase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearSetLoadCaseBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearSetLoadCaseBase:
    """Special nested class for casting GearSetLoadCaseBase to subclasses."""

    __parent__: "GearSetLoadCaseBase"

    @property
    def gear_set_design_analysis(self: "CastSelf") -> "_1264.GearSetDesignAnalysis":
        return self.__parent__._cast(_1264.GearSetDesignAnalysis)

    @property
    def abstract_gear_set_analysis(self: "CastSelf") -> "_1255.AbstractGearSetAnalysis":
        from mastapy._private.gears.analysis import _1255

        return self.__parent__._cast(_1255.AbstractGearSetAnalysis)

    @property
    def worm_gear_set_load_case(self: "CastSelf") -> "_900.WormGearSetLoadCase":
        from mastapy._private.gears.load_case.worm import _900

        return self.__parent__._cast(_900.WormGearSetLoadCase)

    @property
    def face_gear_set_load_case(self: "CastSelf") -> "_903.FaceGearSetLoadCase":
        from mastapy._private.gears.load_case.face import _903

        return self.__parent__._cast(_903.FaceGearSetLoadCase)

    @property
    def cylindrical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_906.CylindricalGearSetLoadCase":
        from mastapy._private.gears.load_case.cylindrical import _906

        return self.__parent__._cast(_906.CylindricalGearSetLoadCase)

    @property
    def conical_gear_set_load_case(self: "CastSelf") -> "_909.ConicalGearSetLoadCase":
        from mastapy._private.gears.load_case.conical import _909

        return self.__parent__._cast(_909.ConicalGearSetLoadCase)

    @property
    def concept_gear_set_load_case(self: "CastSelf") -> "_912.ConceptGearSetLoadCase":
        from mastapy._private.gears.load_case.concept import _912

        return self.__parent__._cast(_912.ConceptGearSetLoadCase)

    @property
    def bevel_set_load_case(self: "CastSelf") -> "_916.BevelSetLoadCase":
        from mastapy._private.gears.load_case.bevel import _916

        return self.__parent__._cast(_916.BevelSetLoadCase)

    @property
    def gear_set_load_case_base(self: "CastSelf") -> "GearSetLoadCaseBase":
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
class GearSetLoadCaseBase(_1264.GearSetDesignAnalysis):
    """GearSetLoadCaseBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_SET_LOAD_CASE_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def name(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: "Self", value: "str") -> None:
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def unit_duration(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.UnitDuration

        if temp is None:
            return 0.0

        return temp

    @unit_duration.setter
    @enforce_parameter_types
    def unit_duration(self: "Self", value: "float") -> None:
        self.wrapped.UnitDuration = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_GearSetLoadCaseBase":
        """Cast to another type.

        Returns:
            _Cast_GearSetLoadCaseBase
        """
        return _Cast_GearSetLoadCaseBase(self)
