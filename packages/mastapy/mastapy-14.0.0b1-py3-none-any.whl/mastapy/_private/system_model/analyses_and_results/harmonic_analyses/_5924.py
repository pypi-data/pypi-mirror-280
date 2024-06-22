"""PeriodicExcitationWithReferenceShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.analyses_and_results.harmonic_analyses import _5809
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PeriodicExcitationWithReferenceShaft",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5863,
        _5864,
        _5865,
        _5866,
        _5867,
        _5868,
        _5869,
        _5870,
        _5871,
        _5872,
        _5873,
        _5874,
        _5889,
        _5941,
        _5967,
    )

    Self = TypeVar("Self", bound="PeriodicExcitationWithReferenceShaft")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PeriodicExcitationWithReferenceShaft",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PeriodicExcitationWithReferenceShaft:
    """Special nested class for casting PeriodicExcitationWithReferenceShaft to subclasses."""

    __parent__: "PeriodicExcitationWithReferenceShaft"

    @property
    def abstract_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5809.AbstractPeriodicExcitationDetail":
        return self.__parent__._cast(_5809.AbstractPeriodicExcitationDetail)

    @property
    def electric_machine_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5863.ElectricMachinePeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5863,
        )

        return self.__parent__._cast(_5863.ElectricMachinePeriodicExcitationDetail)

    @property
    def electric_machine_rotor_x_force_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5864.ElectricMachineRotorXForcePeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5864,
        )

        return self.__parent__._cast(
            _5864.ElectricMachineRotorXForcePeriodicExcitationDetail
        )

    @property
    def electric_machine_rotor_x_moment_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5865.ElectricMachineRotorXMomentPeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5865,
        )

        return self.__parent__._cast(
            _5865.ElectricMachineRotorXMomentPeriodicExcitationDetail
        )

    @property
    def electric_machine_rotor_y_force_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5866.ElectricMachineRotorYForcePeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5866,
        )

        return self.__parent__._cast(
            _5866.ElectricMachineRotorYForcePeriodicExcitationDetail
        )

    @property
    def electric_machine_rotor_y_moment_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5867.ElectricMachineRotorYMomentPeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5867,
        )

        return self.__parent__._cast(
            _5867.ElectricMachineRotorYMomentPeriodicExcitationDetail
        )

    @property
    def electric_machine_rotor_z_force_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5868.ElectricMachineRotorZForcePeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5868,
        )

        return self.__parent__._cast(
            _5868.ElectricMachineRotorZForcePeriodicExcitationDetail
        )

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
    def electric_machine_stator_tooth_loads_excitation_detail(
        self: "CastSelf",
    ) -> "_5870.ElectricMachineStatorToothLoadsExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5870,
        )

        return self.__parent__._cast(
            _5870.ElectricMachineStatorToothLoadsExcitationDetail
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
    def electric_machine_torque_ripple_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5874.ElectricMachineTorqueRipplePeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5874,
        )

        return self.__parent__._cast(
            _5874.ElectricMachineTorqueRipplePeriodicExcitationDetail
        )

    @property
    def general_periodic_excitation_detail(
        self: "CastSelf",
    ) -> "_5889.GeneralPeriodicExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5889,
        )

        return self.__parent__._cast(_5889.GeneralPeriodicExcitationDetail)

    @property
    def single_node_periodic_excitation_with_reference_shaft(
        self: "CastSelf",
    ) -> "_5941.SingleNodePeriodicExcitationWithReferenceShaft":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5941,
        )

        return self.__parent__._cast(
            _5941.SingleNodePeriodicExcitationWithReferenceShaft
        )

    @property
    def unbalanced_mass_excitation_detail(
        self: "CastSelf",
    ) -> "_5967.UnbalancedMassExcitationDetail":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5967,
        )

        return self.__parent__._cast(_5967.UnbalancedMassExcitationDetail)

    @property
    def periodic_excitation_with_reference_shaft(
        self: "CastSelf",
    ) -> "PeriodicExcitationWithReferenceShaft":
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
class PeriodicExcitationWithReferenceShaft(_5809.AbstractPeriodicExcitationDetail):
    """PeriodicExcitationWithReferenceShaft

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_PeriodicExcitationWithReferenceShaft":
        """Cast to another type.

        Returns:
            _Cast_PeriodicExcitationWithReferenceShaft
        """
        return _Cast_PeriodicExcitationWithReferenceShaft(self)
