"""FEStiffnessNode"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private._math.vector_3d import Vector3D
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FE_STIFFNESS_NODE = python_net_import("SMT.MastaAPI.NodalAnalysis", "FEStiffnessNode")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.ltca import _857, _859, _871
    from mastapy._private.gears.ltca.cylindrical import _875, _877
    from mastapy._private.gears.ltca.conical import _887, _889
    from mastapy._private.system_model.fe import _2439

    Self = TypeVar("Self", bound="FEStiffnessNode")
    CastSelf = TypeVar("CastSelf", bound="FEStiffnessNode._Cast_FEStiffnessNode")


__docformat__ = "restructuredtext en"
__all__ = ("FEStiffnessNode",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FEStiffnessNode:
    """Special nested class for casting FEStiffnessNode to subclasses."""

    __parent__: "FEStiffnessNode"

    @property
    def gear_bending_stiffness_node(
        self: "CastSelf",
    ) -> "_857.GearBendingStiffnessNode":
        from mastapy._private.gears.ltca import _857

        return self.__parent__._cast(_857.GearBendingStiffnessNode)

    @property
    def gear_contact_stiffness_node(
        self: "CastSelf",
    ) -> "_859.GearContactStiffnessNode":
        from mastapy._private.gears.ltca import _859

        return self.__parent__._cast(_859.GearContactStiffnessNode)

    @property
    def gear_stiffness_node(self: "CastSelf") -> "_871.GearStiffnessNode":
        from mastapy._private.gears.ltca import _871

        return self.__parent__._cast(_871.GearStiffnessNode)

    @property
    def cylindrical_gear_bending_stiffness_node(
        self: "CastSelf",
    ) -> "_875.CylindricalGearBendingStiffnessNode":
        from mastapy._private.gears.ltca.cylindrical import _875

        return self.__parent__._cast(_875.CylindricalGearBendingStiffnessNode)

    @property
    def cylindrical_gear_contact_stiffness_node(
        self: "CastSelf",
    ) -> "_877.CylindricalGearContactStiffnessNode":
        from mastapy._private.gears.ltca.cylindrical import _877

        return self.__parent__._cast(_877.CylindricalGearContactStiffnessNode)

    @property
    def conical_gear_bending_stiffness_node(
        self: "CastSelf",
    ) -> "_887.ConicalGearBendingStiffnessNode":
        from mastapy._private.gears.ltca.conical import _887

        return self.__parent__._cast(_887.ConicalGearBendingStiffnessNode)

    @property
    def conical_gear_contact_stiffness_node(
        self: "CastSelf",
    ) -> "_889.ConicalGearContactStiffnessNode":
        from mastapy._private.gears.ltca.conical import _889

        return self.__parent__._cast(_889.ConicalGearContactStiffnessNode)

    @property
    def fe_substructure_node(self: "CastSelf") -> "_2439.FESubstructureNode":
        from mastapy._private.system_model.fe import _2439

        return self.__parent__._cast(_2439.FESubstructureNode)

    @property
    def fe_stiffness_node(self: "CastSelf") -> "FEStiffnessNode":
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
class FEStiffnessNode(_0.APIBase):
    """FEStiffnessNode

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_STIFFNESS_NODE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def number_of_degrees_of_freedom(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def position_in_local_coordinate_system(self: "Self") -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.PositionInLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @position_in_local_coordinate_system.setter
    @enforce_parameter_types
    def position_in_local_coordinate_system(self: "Self", value: "Vector3D") -> None:
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.PositionInLocalCoordinateSystem = value

    @property
    def node_index(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeIndex

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_FEStiffnessNode":
        """Cast to another type.

        Returns:
            _Cast_FEStiffnessNode
        """
        return _Cast_FEStiffnessNode(self)
