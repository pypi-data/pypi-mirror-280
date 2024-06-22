"""CylindricalGearMeshMicroGeometry"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private.gears.analysis import _1263
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearMeshMicroGeometry",
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.utility_gui.charts import _1919
    from mastapy._private.gears.gear_designs.cylindrical import _1056, _1048
    from mastapy._private.gears.gear_designs.cylindrical.micro_geometry import (
        _1139,
        _1133,
        _1136,
    )
    from mastapy._private.gears.analysis import _1260, _1254

    Self = TypeVar("Self", bound="CylindricalGearMeshMicroGeometry")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalGearMeshMicroGeometry._Cast_CylindricalGearMeshMicroGeometry",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshMicroGeometry",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalGearMeshMicroGeometry:
    """Special nested class for casting CylindricalGearMeshMicroGeometry to subclasses."""

    __parent__: "CylindricalGearMeshMicroGeometry"

    @property
    def gear_mesh_implementation_detail(
        self: "CastSelf",
    ) -> "_1263.GearMeshImplementationDetail":
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
    def cylindrical_gear_mesh_micro_geometry(
        self: "CastSelf",
    ) -> "CylindricalGearMeshMicroGeometry":
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
class CylindricalGearMeshMicroGeometry(_1263.GearMeshImplementationDetail):
    """CylindricalGearMeshMicroGeometry

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def has_gears_specifying_micro_geometry_per_tooth(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasGearsSpecifyingMicroGeometryPerTooth

        if temp is None:
            return False

        return temp

    @property
    def left_flank_lead_modification_chart(self: "Self") -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankLeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank_profile_modification_chart(
        self: "Self",
    ) -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_tooth_passes_for_ltca(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfToothPassesForLTCA

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_tooth_passes_for_ltca.setter
    @enforce_parameter_types
    def number_of_tooth_passes_for_ltca(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfToothPassesForLTCA = value

    @property
    def profile_measured_as(
        self: "Self",
    ) -> "_1056.CylindricalGearProfileMeasurementType":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurementType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileMeasuredAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.cylindrical._1056",
            "CylindricalGearProfileMeasurementType",
        )(value)

    @property
    def right_flank_lead_modification_chart(
        self: "Self",
    ) -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankLeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_profile_modification_chart(
        self: "Self",
    ) -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_micro_geometry(
        self: "Self",
    ) -> "_1139.CylindricalGearSetMicroGeometry":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_mesh(self: "Self") -> "_1048.CylindricalGearMeshDesign":
        """mastapy._private.gears.gear_designs.cylindrical.CylindricalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_micro_geometries(
        self: "Self",
    ) -> "List[_1133.CylindricalGearMicroGeometryBase]":
        """List[mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryBase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_micro_geometries_specified_per_tooth(
        self: "Self",
    ) -> "List[_1136.CylindricalGearMicroGeometryPerTooth]":
        """List[mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryPerTooth]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMicroGeometriesSpecifiedPerTooth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_a(self: "Self") -> "_1133.CylindricalGearMicroGeometryBase":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: "Self") -> "_1133.CylindricalGearMicroGeometryBase":
        """mastapy._private.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalGearMeshMicroGeometry":
        """Cast to another type.

        Returns:
            _Cast_CylindricalGearMeshMicroGeometry
        """
        return _Cast_CylindricalGearMeshMicroGeometry(self)
