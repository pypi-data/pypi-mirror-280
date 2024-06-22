"""GearFEModel"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.gears.analysis import _1259
from mastapy._private._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_GEAR_FLANKS = python_net_import("SMT.MastaAPI.Gears", "GearFlanks")
_GEAR_FE_MODEL = python_net_import("SMT.MastaAPI.Gears.FEModel", "GearFEModel")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, TypeVar

    from mastapy._private.gears.fe_model import _1237
    from mastapy._private import _7724
    from mastapy._private.gears import _336
    from mastapy._private.gears.fe_model.cylindrical import _1239
    from mastapy._private.gears.fe_model.conical import _1242
    from mastapy._private.gears.analysis import _1256, _1253

    Self = TypeVar("Self", bound="GearFEModel")
    CastSelf = TypeVar("CastSelf", bound="GearFEModel._Cast_GearFEModel")


__docformat__ = "restructuredtext en"
__all__ = ("GearFEModel",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearFEModel:
    """Special nested class for casting GearFEModel to subclasses."""

    __parent__: "GearFEModel"

    @property
    def gear_implementation_detail(
        self: "CastSelf",
    ) -> "_1259.GearImplementationDetail":
        return self.__parent__._cast(_1259.GearImplementationDetail)

    @property
    def gear_design_analysis(self: "CastSelf") -> "_1256.GearDesignAnalysis":
        from mastapy._private.gears.analysis import _1256

        return self.__parent__._cast(_1256.GearDesignAnalysis)

    @property
    def abstract_gear_analysis(self: "CastSelf") -> "_1253.AbstractGearAnalysis":
        from mastapy._private.gears.analysis import _1253

        return self.__parent__._cast(_1253.AbstractGearAnalysis)

    @property
    def cylindrical_gear_fe_model(self: "CastSelf") -> "_1239.CylindricalGearFEModel":
        from mastapy._private.gears.fe_model.cylindrical import _1239

        return self.__parent__._cast(_1239.CylindricalGearFEModel)

    @property
    def conical_gear_fe_model(self: "CastSelf") -> "_1242.ConicalGearFEModel":
        from mastapy._private.gears.fe_model.conical import _1242

        return self.__parent__._cast(_1242.ConicalGearFEModel)

    @property
    def gear_fe_model(self: "CastSelf") -> "GearFEModel":
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
class GearFEModel(_1259.GearImplementationDetail):
    """GearFEModel

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_FE_MODEL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def fe_bore(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FEBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @fe_bore.setter
    @enforce_parameter_types
    def fe_bore(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FEBore = value

    @property
    def include_all_teeth_in_the_fe_mesh(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeAllTeethInTheFEMesh

        if temp is None:
            return False

        return temp

    @include_all_teeth_in_the_fe_mesh.setter
    @enforce_parameter_types
    def include_all_teeth_in_the_fe_mesh(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeAllTeethInTheFEMesh = (
            bool(value) if value is not None else False
        )

    @property
    def element_settings(self: "Self") -> "_1237.GearMeshingElementOptions":
        """mastapy._private.gears.fe_model.GearMeshingElementOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def calculate_stiffness_from_fe(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.CalculateStiffnessFromFE()

    @enforce_parameter_types
    def calculate_stiffness_from_fe_with_progress(
        self: "Self", progress: "_7724.TaskProgress"
    ) -> None:
        """Method does not return.

        Args:
            progress (mastapy._private.TaskProgress)
        """
        self.wrapped.CalculateStiffnessFromFE.Overloads[_TASK_PROGRESS](
            progress.wrapped if progress else None
        )

    @enforce_parameter_types
    def get_stress_influence_coefficients_from_fe(
        self: "Self", flank: "_336.GearFlanks"
    ) -> None:
        """Method does not return.

        Args:
            flank (mastapy._private.gears.GearFlanks)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        self.wrapped.GetStressInfluenceCoefficientsFromFE.Overloads[_GEAR_FLANKS](flank)

    @enforce_parameter_types
    def get_stress_influence_coefficients_from_fe_with_progress(
        self: "Self", flank: "_336.GearFlanks", progress: "_7724.TaskProgress"
    ) -> None:
        """Method does not return.

        Args:
            flank (mastapy._private.gears.GearFlanks)
            progress (mastapy._private.TaskProgress)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        self.wrapped.GetStressInfluenceCoefficientsFromFE.Overloads[
            _GEAR_FLANKS, _TASK_PROGRESS
        ](flank, progress.wrapped if progress else None)

    @property
    def cast_to(self: "Self") -> "_Cast_GearFEModel":
        """Cast to another type.

        Returns:
            _Cast_GearFEModel
        """
        return _Cast_GearFEModel(self)
