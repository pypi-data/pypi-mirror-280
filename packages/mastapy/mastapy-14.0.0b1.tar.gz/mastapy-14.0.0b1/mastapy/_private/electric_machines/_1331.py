"""NonCADElectricMachineDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, utility
from mastapy._private.electric_machines import _1302
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_NON_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "NonCADElectricMachineDetail"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.electric_machines import (
        _1344,
        _1320,
        _1334,
        _1348,
        _1350,
        _1365,
    )

    Self = TypeVar("Self", bound="NonCADElectricMachineDetail")
    CastSelf = TypeVar(
        "CastSelf",
        bound="NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
    )


__docformat__ = "restructuredtext en"
__all__ = ("NonCADElectricMachineDetail",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_NonCADElectricMachineDetail:
    """Special nested class for casting NonCADElectricMachineDetail to subclasses."""

    __parent__: "NonCADElectricMachineDetail"

    @property
    def electric_machine_detail(self: "CastSelf") -> "_1302.ElectricMachineDetail":
        return self.__parent__._cast(_1302.ElectricMachineDetail)

    @property
    def interior_permanent_magnet_machine(
        self: "CastSelf",
    ) -> "_1320.InteriorPermanentMagnetMachine":
        from mastapy._private.electric_machines import _1320

        return self.__parent__._cast(_1320.InteriorPermanentMagnetMachine)

    @property
    def permanent_magnet_assisted_synchronous_reluctance_machine(
        self: "CastSelf",
    ) -> "_1334.PermanentMagnetAssistedSynchronousReluctanceMachine":
        from mastapy._private.electric_machines import _1334

        return self.__parent__._cast(
            _1334.PermanentMagnetAssistedSynchronousReluctanceMachine
        )

    @property
    def surface_permanent_magnet_machine(
        self: "CastSelf",
    ) -> "_1348.SurfacePermanentMagnetMachine":
        from mastapy._private.electric_machines import _1348

        return self.__parent__._cast(_1348.SurfacePermanentMagnetMachine)

    @property
    def synchronous_reluctance_machine(
        self: "CastSelf",
    ) -> "_1350.SynchronousReluctanceMachine":
        from mastapy._private.electric_machines import _1350

        return self.__parent__._cast(_1350.SynchronousReluctanceMachine)

    @property
    def wound_field_synchronous_machine(
        self: "CastSelf",
    ) -> "_1365.WoundFieldSynchronousMachine":
        from mastapy._private.electric_machines import _1365

        return self.__parent__._cast(_1365.WoundFieldSynchronousMachine)

    @property
    def non_cad_electric_machine_detail(
        self: "CastSelf",
    ) -> "NonCADElectricMachineDetail":
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
class NonCADElectricMachineDetail(_1302.ElectricMachineDetail):
    """NonCADElectricMachineDetail

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _NON_CAD_ELECTRIC_MACHINE_DETAIL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def stator(self: "Self") -> "_1344.Stator":
        """mastapy._private.electric_machines.Stator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_NonCADElectricMachineDetail":
        """Cast to another type.

        Returns:
            _Cast_NonCADElectricMachineDetail
        """
        return _Cast_NonCADElectricMachineDetail(self)
