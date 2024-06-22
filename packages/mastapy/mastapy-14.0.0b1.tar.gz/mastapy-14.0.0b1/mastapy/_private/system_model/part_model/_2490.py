"""AbstractShaftOrHousing"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private.system_model.part_model import _2498
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import
from mastapy._private._internal import utility

_ABSTRACT_SHAFT_OR_HOUSING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model import _2489, _2507, _2524
    from mastapy._private.system_model.part_model.shaft_model import _2538
    from mastapy._private.system_model.part_model.cycloidal import _2625
    from mastapy._private.system_model import _2256

    Self = TypeVar("Self", bound="AbstractShaftOrHousing")
    CastSelf = TypeVar(
        "CastSelf", bound="AbstractShaftOrHousing._Cast_AbstractShaftOrHousing"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftOrHousing:
    """Special nested class for casting AbstractShaftOrHousing to subclasses."""

    __parent__: "AbstractShaftOrHousing"

    @property
    def component(self: "CastSelf") -> "_2498.Component":
        return self.__parent__._cast(_2498.Component)

    @property
    def part(self: "CastSelf") -> "_2524.Part":
        from mastapy._private.system_model.part_model import _2524

        return self.__parent__._cast(_2524.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2256.DesignEntity":
        from mastapy._private.system_model import _2256

        return self.__parent__._cast(_2256.DesignEntity)

    @property
    def abstract_shaft(self: "CastSelf") -> "_2489.AbstractShaft":
        from mastapy._private.system_model.part_model import _2489

        return self.__parent__._cast(_2489.AbstractShaft)

    @property
    def fe_part(self: "CastSelf") -> "_2507.FEPart":
        from mastapy._private.system_model.part_model import _2507

        return self.__parent__._cast(_2507.FEPart)

    @property
    def shaft(self: "CastSelf") -> "_2538.Shaft":
        from mastapy._private.system_model.part_model.shaft_model import _2538

        return self.__parent__._cast(_2538.Shaft)

    @property
    def cycloidal_disc(self: "CastSelf") -> "_2625.CycloidalDisc":
        from mastapy._private.system_model.part_model.cycloidal import _2625

        return self.__parent__._cast(_2625.CycloidalDisc)

    @property
    def abstract_shaft_or_housing(self: "CastSelf") -> "AbstractShaftOrHousing":
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
class AbstractShaftOrHousing(_2498.Component):
    """AbstractShaftOrHousing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_SHAFT_OR_HOUSING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractShaftOrHousing":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftOrHousing
        """
        return _Cast_AbstractShaftOrHousing(self)
