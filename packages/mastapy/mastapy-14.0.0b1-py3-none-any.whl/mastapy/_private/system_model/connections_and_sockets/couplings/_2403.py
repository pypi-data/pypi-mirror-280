"""SpringDamperConnection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.connections_and_sockets.couplings import _2399
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2254, _2256
    from mastapy._private.nodal_analysis import _72
    from mastapy._private.system_model.connections_and_sockets import _2334, _2325

    Self = TypeVar("Self", bound="SpringDamperConnection")
    CastSelf = TypeVar(
        "CastSelf", bound="SpringDamperConnection._Cast_SpringDamperConnection"
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpringDamperConnection:
    """Special nested class for casting SpringDamperConnection to subclasses."""

    __parent__: "SpringDamperConnection"

    @property
    def coupling_connection(self: "CastSelf") -> "_2399.CouplingConnection":
        return self.__parent__._cast(_2399.CouplingConnection)

    @property
    def inter_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2334.InterMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2334

        return self.__parent__._cast(_2334.InterMountableComponentConnection)

    @property
    def connection(self: "CastSelf") -> "_2325.Connection":
        from mastapy._private.system_model.connections_and_sockets import _2325

        return self.__parent__._cast(_2325.Connection)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def spring_damper_connection(self: "CastSelf") -> "SpringDamperConnection":
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
class SpringDamperConnection(_2399.CouplingConnection):
    """SpringDamperConnection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPRING_DAMPER_CONNECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def damping_option(self: "Self") -> "_2254.ComponentDampingOption":
        """mastapy._private.system_model.ComponentDampingOption"""
        temp = self.wrapped.DampingOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.ComponentDampingOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.system_model._2254", "ComponentDampingOption"
        )(value)

    @damping_option.setter
    @enforce_parameter_types
    def damping_option(self: "Self", value: "_2254.ComponentDampingOption") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.ComponentDampingOption"
        )
        self.wrapped.DampingOption = value

    @property
    def damping(self: "Self") -> "_72.LinearDampingConnectionProperties":
        """mastapy._private.nodal_analysis.LinearDampingConnectionProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Damping

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_SpringDamperConnection":
        """Cast to another type.

        Returns:
            _Cast_SpringDamperConnection
        """
        return _Cast_SpringDamperConnection(self)
