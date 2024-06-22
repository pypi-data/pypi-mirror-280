"""CylindricalGearMeshFEModel"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.gears.fe_model import _1236
from mastapy._private._internal.cast_exception import CastException

_GEAR_FE_MODEL = python_net_import("SMT.MastaAPI.Gears.FEModel", "GearFEModel")
_GEAR_FLANKS = python_net_import("SMT.MastaAPI.Gears", "GearFlanks")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_CYLINDRICAL_GEAR_MESH_FE_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Cylindrical", "CylindricalGearMeshFEModel"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.fe_model import _1235
    from mastapy._private.gears import _336
    from mastapy._private.gears.ltca import _858
    from mastapy._private import _7724
    from mastapy._private.gears.analysis import _1263, _1260, _1254

    Self = TypeVar("Self", bound="CylindricalGearMeshFEModel")
    CastSelf = TypeVar(
        "CastSelf", bound="CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshFEModel",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearMeshFEModel:
    """Special nested class for casting CylindricalGearMeshFEModel to subclasses."""

    __parent__: "CylindricalGearMeshFEModel"

    @property
    def gear_mesh_fe_model(self: "CastSelf") -> "_1236.GearMeshFEModel":
        return self.__parent__._cast(_1236.GearMeshFEModel)

    @property
    def gear_mesh_implementation_detail(
        self: "CastSelf",
    ) -> "_1263.GearMeshImplementationDetail":
        from mastapy._private.gears.analysis import _1263

        return self.__parent__._cast(_1263.GearMeshImplementationDetail)

    @property
    def gear_mesh_design_analysis(self: "CastSelf") -> "_1260.GearMeshDesignAnalysis":
        from mastapy._private.gears.analysis import _1260

        return self.__parent__._cast(_1260.GearMeshDesignAnalysis)

    @property
    def abstract_gear_mesh_analysis(
        self: "CastSelf",
    ) -> "_1254.AbstractGearMeshAnalysis":
        from mastapy._private.gears.analysis import _1254

        return self.__parent__._cast(_1254.AbstractGearMeshAnalysis)

    @property
    def cylindrical_gear_mesh_fe_model(
        self: "CastSelf",
    ) -> "CylindricalGearMeshFEModel":
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
class CylindricalGearMeshFEModel(_1236.GearMeshFEModel):
    """CylindricalGearMeshFEModel

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_MESH_FE_MODEL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @enforce_parameter_types
    def stiffness_wrt_contacts_for(
        self: "Self", gear: "_1235.GearFEModel", flank: "_336.GearFlanks"
    ) -> "List[_858.GearContactStiffness]":
        """List[mastapy._private.gears.ltca.GearContactStiffness]

        Args:
            gear (mastapy._private.gears.fe_model.GearFEModel)
            flank (mastapy._private.gears.GearFlanks)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.StiffnessWrtContactsFor.Overloads[
                _GEAR_FE_MODEL, _GEAR_FLANKS
            ](gear.wrapped if gear else None, flank)
        )

    @enforce_parameter_types
    def stiffness_wrt_contacts_for_with_progress(
        self: "Self",
        gear: "_1235.GearFEModel",
        flank: "_336.GearFlanks",
        progress: "_7724.TaskProgress",
    ) -> "List[_858.GearContactStiffness]":
        """List[mastapy._private.gears.ltca.GearContactStiffness]

        Args:
            gear (mastapy._private.gears.fe_model.GearFEModel)
            flank (mastapy._private.gears.GearFlanks)
            progress (mastapy._private.TaskProgress)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.StiffnessWrtContactsFor.Overloads[
                _GEAR_FE_MODEL, _GEAR_FLANKS, _TASK_PROGRESS
            ](
                gear.wrapped if gear else None,
                flank,
                progress.wrapped if progress else None,
            )
        )

    @enforce_parameter_types
    def generate_stiffness_wrt_contacts_for(
        self: "Self", progress: "_7724.TaskProgress"
    ) -> None:
        """Method does not return.

        Args:
            progress (mastapy._private.TaskProgress)
        """
        self.wrapped.GenerateStiffnessWrtContactsFor.Overloads[_TASK_PROGRESS](
            progress.wrapped if progress else None
        )

    @enforce_parameter_types
    def generate_stiffness_wrt_contacts_for_flank(
        self: "Self", flank: "_336.GearFlanks", progress: "_7724.TaskProgress"
    ) -> None:
        """Method does not return.

        Args:
            flank (mastapy._private.gears.GearFlanks)
            progress (mastapy._private.TaskProgress)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        self.wrapped.GenerateStiffnessWrtContactsFor.Overloads[
            _GEAR_FLANKS, _TASK_PROGRESS
        ](flank, progress.wrapped if progress else None)

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearMeshFEModel":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearMeshFEModel
        """
        return _Cast_CylindricalGearMeshFEModel(self)
