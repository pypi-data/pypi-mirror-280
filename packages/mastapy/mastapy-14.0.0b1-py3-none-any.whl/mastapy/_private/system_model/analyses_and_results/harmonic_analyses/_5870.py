"""ElectricMachineStatorToothLoadsExcitationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.analyses_and_results.harmonic_analyses import _5863
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_ELECTRIC_MACHINE_STATOR_TOOTH_LOADS_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineStatorToothLoadsExcitationDetail",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5869,
        _5871,
        _5872,
        _5873,
        _5924,
        _5809,
    )

    Self = TypeVar("Self", bound="ElectricMachineStatorToothLoadsExcitationDetail")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorToothLoadsExcitationDetail",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ElectricMachineStatorToothLoadsExcitationDetail:
    """Special nested class for casting ElectricMachineStatorToothLoadsExcitationDetail to subclasses."""

    __parent__: "ElectricMachineStatorToothLoadsExcitationDetail"

    @property
    def electric_machine_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5863.ElectricMachinePeriodicExcitationDetail":
        return self.__parent__._cast(_5863.ElectricMachinePeriodicExcitationDetail)

    @property
    def periodic_excitation_with_reference_shaft(
        self: "CastSelf",
    ) -> "_5924.PeriodicExcitationWithReferenceShaft":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5924,
        )

        return self.__parent__._cast(_5924.PeriodicExcitationWithReferenceShaft)

    @property
    def abstract_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5809.AbstractPeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5809,
        )

        return self.__parent__._cast(_5809.AbstractPeriodicExcitationDetail)

    @property
    def electric_machine_stator_tooth_axial_loads_excitation_detail(
        self: "CastSelf",
    ) -> "_5869.ElectricMachineStatorToothAxialLoadsExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5869,
        )

        return self.__parent__._cast(
            _5869.ElectricMachineStatorToothAxialLoadsExcitationDetail
        )

    @property
    def electric_machine_stator_tooth_moments_excitation_detail(
        self: "CastSelf",
    ) -> "_5871.ElectricMachineStatorToothMomentsExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5871,
        )

        return self.__parent__._cast(
            _5871.ElectricMachineStatorToothMomentsExcitationDetail
        )

    @property
    def electric_machine_stator_tooth_radial_loads_excitation_detail(
        self: "CastSelf",
    ) -> "_5872.ElectricMachineStatorToothRadialLoadsExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5872,
        )

        return self.__parent__._cast(
            _5872.ElectricMachineStatorToothRadialLoadsExcitationDetail
        )

    @property
    def electric_machine_stator_tooth_tangential_loads_excitation_detail(
        self: "CastSelf",
    ) -> "_5873.ElectricMachineStatorToothTangentialLoadsExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5873,
        )

        return self.__parent__._cast(
            _5873.ElectricMachineStatorToothTangentialLoadsExcitationDetail
        )

    @property
    def electric_machine_stator_tooth_loads_excitation_detail(
        self: "CastSelf",
    ) -> "ElectricMachineStatorToothLoadsExcitationDetail":
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
class ElectricMachineStatorToothLoadsExcitationDetail(
    _5863.ElectricMachinePeriodicExcitationDetail
):
    """ElectricMachineStatorToothLoadsExcitationDetail

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ELECTRIC_MACHINE_STATOR_TOOTH_LOADS_EXCITATION_DETAIL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_ElectricMachineStatorToothLoadsExcitationDetail":
        """Cast to another type.

        Returns:
            _Cast_ElectricMachineStatorToothLoadsExcitationDetail
        """
        return _Cast_ElectricMachineStatorToothLoadsExcitationDetail(self)
