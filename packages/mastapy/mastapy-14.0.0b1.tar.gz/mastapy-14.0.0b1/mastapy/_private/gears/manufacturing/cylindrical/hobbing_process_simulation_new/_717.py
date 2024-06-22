"""WormGrindingProcessCalculation"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _703,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_WORM_GRINDING_PROCESS_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessCalculation",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _715,
        _716,
        _718,
        _719,
        _720,
        _721,
        _725,
    )

    Self = TypeVar("Self", bound="WormGrindingProcessCalculation")
    CastSelf = TypeVar(
        "CastSelf",
        bound="WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessCalculation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_WormGrindingProcessCalculation:
    """Special nested class for casting WormGrindingProcessCalculation to subclasses."""

    __parent__: "WormGrindingProcessCalculation"

    @property
    def process_calculation(self: "CastSelf") -> "_703.ProcessCalculation":
        return self.__parent__._cast(_703.ProcessCalculation)

    @property
    def worm_grinding_cutter_calculation(
        self: "CastSelf",
    ) -> "_715.WormGrindingCutterCalculation":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _715,
        )

        return self.__parent__._cast(_715.WormGrindingCutterCalculation)

    @property
    def worm_grinding_lead_calculation(
        self: "CastSelf",
    ) -> "_716.WormGrindingLeadCalculation":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _716,
        )

        return self.__parent__._cast(_716.WormGrindingLeadCalculation)

    @property
    def worm_grinding_process_gear_shape(
        self: "CastSelf",
    ) -> "_718.WormGrindingProcessGearShape":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _718,
        )

        return self.__parent__._cast(_718.WormGrindingProcessGearShape)

    @property
    def worm_grinding_process_mark_on_shaft(
        self: "CastSelf",
    ) -> "_719.WormGrindingProcessMarkOnShaft":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _719,
        )

        return self.__parent__._cast(_719.WormGrindingProcessMarkOnShaft)

    @property
    def worm_grinding_process_pitch_calculation(
        self: "CastSelf",
    ) -> "_720.WormGrindingProcessPitchCalculation":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _720,
        )

        return self.__parent__._cast(_720.WormGrindingProcessPitchCalculation)

    @property
    def worm_grinding_process_profile_calculation(
        self: "CastSelf",
    ) -> "_721.WormGrindingProcessProfileCalculation":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _721,
        )

        return self.__parent__._cast(_721.WormGrindingProcessProfileCalculation)

    @property
    def worm_grinding_process_total_modification_calculation(
        self: "CastSelf",
    ) -> "_725.WormGrindingProcessTotalModificationCalculation":
        from mastapy._private.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
            _725,
        )

        return self.__parent__._cast(
            _725.WormGrindingProcessTotalModificationCalculation
        )

    @property
    def worm_grinding_process_calculation(
        self: "CastSelf",
    ) -> "WormGrindingProcessCalculation":
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
class WormGrindingProcessCalculation(_703.ProcessCalculation):
    """WormGrindingProcessCalculation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _WORM_GRINDING_PROCESS_CALCULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_WormGrindingProcessCalculation":
        """Cast to another type.

        Returns:
            _Cast_WormGrindingProcessCalculation
        """
        return _Cast_WormGrindingProcessCalculation(self)
