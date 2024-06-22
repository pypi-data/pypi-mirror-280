"""FEEntityGroupInteger"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.nodal_analysis.dev_tools_analyses import _193
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_FE_ENTITY_GROUP_INTEGER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEEntityGroupInteger"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.nodal_analysis.dev_tools_analyses import _192, _211
    from mastapy._private.nodal_analysis.component_mode_synthesis import _238

    Self = TypeVar("Self", bound="FEEntityGroupInteger")
    CastSelf = TypeVar(
        "CastSelf", bound="FEEntityGroupInteger._Cast_FEEntityGroupInteger"
    )


__docformat__ = "restructuredtext en"
__all__ = ("FEEntityGroupInteger",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FEEntityGroupInteger:
    """Special nested class for casting FEEntityGroupInteger to subclasses."""

    __parent__: "FEEntityGroupInteger"

    @property
    def fe_entity_group(self: "CastSelf") -> "_193.FEEntityGroup":
        return self.__parent__._cast(_193.FEEntityGroup)

    @property
    def element_group(self: "CastSelf") -> "_192.ElementGroup":
        from mastapy._private.nodal_analysis.dev_tools_analyses import _192

        return self.__parent__._cast(_192.ElementGroup)

    @property
    def node_group(self: "CastSelf") -> "_211.NodeGroup":
        from mastapy._private.nodal_analysis.dev_tools_analyses import _211

        return self.__parent__._cast(_211.NodeGroup)

    @property
    def cms_node_group(self: "CastSelf") -> "_238.CMSNodeGroup":
        from mastapy._private.nodal_analysis.component_mode_synthesis import _238

        return self.__parent__._cast(_238.CMSNodeGroup)

    @property
    def fe_entity_group_integer(self: "CastSelf") -> "FEEntityGroupInteger":
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
class FEEntityGroupInteger(_193.FEEntityGroup[int]):
    """FEEntityGroupInteger

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_ENTITY_GROUP_INTEGER

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_FEEntityGroupInteger":
        """Cast to another type.

        Returns:
            _Cast_FEEntityGroupInteger
        """
        return _Cast_FEEntityGroupInteger(self)
