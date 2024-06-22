"""Rotor"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import (
    constructor,
    overridable_enum_runtime,
    conversion,
    utility,
)
from mastapy._private._internal.implicit import overridable
from mastapy._private.electric_machines import _1300
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal.python_net import python_net_import
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ROTOR = python_net_import("SMT.MastaAPI.ElectricMachines", "Rotor")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.electric_machines import (
        _1340,
        _1289,
        _1292,
        _1319,
        _1335,
        _1349,
        _1366,
    )

    Self = TypeVar("Self", bound="Rotor")
    CastSelf = TypeVar("CastSelf", bound="Rotor._Cast_Rotor")


__docformat__ = "restructuredtext en"
__all__ = ("Rotor",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Rotor:
    """Special nested class for casting Rotor to subclasses."""

    __parent__: "Rotor"

    @property
    def cad_rotor(self: "CastSelf") -> "_1289.CADRotor":
        from mastapy._private.electric_machines import _1289

        return self.__parent__._cast(_1289.CADRotor)

    @property
    def cad_wound_field_synchronous_rotor(
        self: "CastSelf",
    ) -> "_1292.CADWoundFieldSynchronousRotor":
        from mastapy._private.electric_machines import _1292

        return self.__parent__._cast(_1292.CADWoundFieldSynchronousRotor)

    @property
    def interior_permanent_magnet_and_synchronous_reluctance_rotor(
        self: "CastSelf",
    ) -> "_1319.InteriorPermanentMagnetAndSynchronousReluctanceRotor":
        from mastapy._private.electric_machines import _1319

        return self.__parent__._cast(
            _1319.InteriorPermanentMagnetAndSynchronousReluctanceRotor
        )

    @property
    def permanent_magnet_rotor(self: "CastSelf") -> "_1335.PermanentMagnetRotor":
        from mastapy._private.electric_machines import _1335

        return self.__parent__._cast(_1335.PermanentMagnetRotor)

    @property
    def surface_permanent_magnet_rotor(
        self: "CastSelf",
    ) -> "_1349.SurfacePermanentMagnetRotor":
        from mastapy._private.electric_machines import _1349

        return self.__parent__._cast(_1349.SurfacePermanentMagnetRotor)

    @property
    def wound_field_synchronous_rotor(
        self: "CastSelf",
    ) -> "_1366.WoundFieldSynchronousRotor":
        from mastapy._private.electric_machines import _1366

        return self.__parent__._cast(_1366.WoundFieldSynchronousRotor)

    @property
    def rotor(self: "CastSelf") -> "Rotor":
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
class Rotor(_0.APIBase):
    """Rotor

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ROTOR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bore(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: "Self", value: "float") -> None:
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def d_axis_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_and_q_axis_convention(
        self: "Self",
    ) -> "overridable.Overridable_DQAxisConvention":
        """Overridable[mastapy._private.electric_machines.DQAxisConvention]"""
        temp = self.wrapped.DAxisAndQAxisConvention

        if temp is None:
            return None

        value = overridable.Overridable_DQAxisConvention.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @d_axis_and_q_axis_convention.setter
    @enforce_parameter_types
    def d_axis_and_q_axis_convention(
        self: "Self",
        value: "Union[_1300.DQAxisConvention, Tuple[_1300.DQAxisConvention, bool]]",
    ) -> None:
        wrapper_type = overridable.Overridable_DQAxisConvention.wrapper_type()
        enclosed_type = overridable.Overridable_DQAxisConvention.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.DAxisAndQAxisConvention = value

    @property
    def initial_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.InitialAngle

        if temp is None:
            return 0.0

        return temp

    @initial_angle.setter
    @enforce_parameter_types
    def initial_angle(self: "Self", value: "float") -> None:
        self.wrapped.InitialAngle = float(value) if value is not None else 0.0

    @property
    def is_skewed(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IsSkewed

        if temp is None:
            return False

        return temp

    @is_skewed.setter
    @enforce_parameter_types
    def is_skewed(self: "Self", value: "bool") -> None:
        self.wrapped.IsSkewed = bool(value) if value is not None else False

    @property
    def kair(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Kair

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_flux_barrier_length(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MagnetFluxBarrierLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @magnet_flux_barrier_length.setter
    @enforce_parameter_types
    def magnet_flux_barrier_length(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MagnetFluxBarrierLength = value

    @property
    def number_of_magnet_segments_in_axial_direction(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfMagnetSegmentsInAxialDirection

        if temp is None:
            return 0

        return temp

    @number_of_magnet_segments_in_axial_direction.setter
    @enforce_parameter_types
    def number_of_magnet_segments_in_axial_direction(
        self: "Self", value: "int"
    ) -> None:
        self.wrapped.NumberOfMagnetSegmentsInAxialDirection = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_poles(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfPoles

        if temp is None:
            return 0

        return temp

    @number_of_poles.setter
    @enforce_parameter_types
    def number_of_poles(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfPoles = int(value) if value is not None else 0

    @property
    def number_of_slices(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfSlices

        if temp is None:
            return 0

        return temp

    @number_of_slices.setter
    @enforce_parameter_types
    def number_of_slices(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfSlices = int(value) if value is not None else 0

    @property
    def outer_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_inertia(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PolarInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_length(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RotorLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rotor_length.setter
    @enforce_parameter_types
    def rotor_length(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RotorLength = value

    @property
    def rotor_material_database(self: "Self") -> "str":
        """str"""
        temp = self.wrapped.RotorMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @rotor_material_database.setter
    @enforce_parameter_types
    def rotor_material_database(self: "Self", value: "str") -> None:
        self.wrapped.RotorMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def use_same_material_as_stator(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseSameMaterialAsStator

        if temp is None:
            return False

        return temp

    @use_same_material_as_stator.setter
    @enforce_parameter_types
    def use_same_material_as_stator(self: "Self", value: "bool") -> None:
        self.wrapped.UseSameMaterialAsStator = (
            bool(value) if value is not None else False
        )

    @property
    def skew_slices(self: "Self") -> "List[_1340.RotorSkewSlice]":
        """List[mastapy._private.electric_machines.RotorSkewSlice]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SkewSlices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: "Self", report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_Rotor":
        """Cast to another type.

        Returns:
            _Cast_Rotor
        """
        return _Cast_Rotor(self)
