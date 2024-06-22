"""BoltGeometry"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.utility.databases import _1879
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BOLT_GEOMETRY = python_net_import("SMT.MastaAPI.Bolts", "BoltGeometry")

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.bolts import _1518, _1519, _1530, _1520, _1525, _1532

    Self = TypeVar("Self", bound="BoltGeometry")
    CastSelf = TypeVar("CastSelf", bound="BoltGeometry._Cast_BoltGeometry")


__docformat__ = "restructuredtext en"
__all__ = ("BoltGeometry",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BoltGeometry:
    """Special nested class for casting BoltGeometry to subclasses."""

    __parent__: "BoltGeometry"

    @property
    def named_database_item(self: "CastSelf") -> "_1879.NamedDatabaseItem":
        return self.__parent__._cast(_1879.NamedDatabaseItem)

    @property
    def bolt_geometry(self: "CastSelf") -> "BoltGeometry":
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
class BoltGeometry(_1879.NamedDatabaseItem):
    """BoltGeometry

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BOLT_GEOMETRY

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bolt_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BoltDiameter

        if temp is None:
            return 0.0

        return temp

    @bolt_diameter.setter
    @enforce_parameter_types
    def bolt_diameter(self: "Self", value: "float") -> None:
        self.wrapped.BoltDiameter = float(value) if value is not None else 0.0

    @property
    def bolt_inner_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BoltInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @bolt_inner_diameter.setter
    @enforce_parameter_types
    def bolt_inner_diameter(self: "Self", value: "float") -> None:
        self.wrapped.BoltInnerDiameter = float(value) if value is not None else 0.0

    @property
    def bolt_length(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BoltLength

        if temp is None:
            return 0.0

        return temp

    @bolt_length.setter
    @enforce_parameter_types
    def bolt_length(self: "Self", value: "float") -> None:
        self.wrapped.BoltLength = float(value) if value is not None else 0.0

    @property
    def bolt_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltName

        if temp is None:
            return ""

        return temp

    @property
    def bolt_sections(self: "Self") -> "List[_1518.BoltSection]":
        """List[mastapy._private.bolts.BoltSection]"""
        temp = self.wrapped.BoltSections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @bolt_sections.setter
    @enforce_parameter_types
    def bolt_sections(self: "Self", value: "List[_1518.BoltSection]") -> None:
        value = conversion.mp_to_pn_objects_in_list(value)
        self.wrapped.BoltSections = value

    @property
    def bolt_shank_type(self: "Self") -> "_1519.BoltShankType":
        """mastapy._private.bolts.BoltShankType"""
        temp = self.wrapped.BoltShankType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bolts.BoltShankType")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bolts._1519", "BoltShankType"
        )(value)

    @bolt_shank_type.setter
    @enforce_parameter_types
    def bolt_shank_type(self: "Self", value: "_1519.BoltShankType") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bolts.BoltShankType")
        self.wrapped.BoltShankType = value

    @property
    def bolt_thread_pitch_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.BoltThreadPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @bolt_thread_pitch_diameter.setter
    @enforce_parameter_types
    def bolt_thread_pitch_diameter(self: "Self", value: "float") -> None:
        self.wrapped.BoltThreadPitchDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def has_cross_sections_of_different_diameters(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.HasCrossSectionsOfDifferentDiameters

        if temp is None:
            return False

        return temp

    @has_cross_sections_of_different_diameters.setter
    @enforce_parameter_types
    def has_cross_sections_of_different_diameters(self: "Self", value: "bool") -> None:
        self.wrapped.HasCrossSectionsOfDifferentDiameters = (
            bool(value) if value is not None else False
        )

    @property
    def hole_chamfer_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.HoleChamferWidth

        if temp is None:
            return 0.0

        return temp

    @hole_chamfer_width.setter
    @enforce_parameter_types
    def hole_chamfer_width(self: "Self", value: "float") -> None:
        self.wrapped.HoleChamferWidth = float(value) if value is not None else 0.0

    @property
    def hole_diameter_of_clamped_parts(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.HoleDiameterOfClampedParts

        if temp is None:
            return 0.0

        return temp

    @hole_diameter_of_clamped_parts.setter
    @enforce_parameter_types
    def hole_diameter_of_clamped_parts(self: "Self", value: "float") -> None:
        self.wrapped.HoleDiameterOfClampedParts = (
            float(value) if value is not None else 0.0
        )

    @property
    def is_threaded_to_head(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsThreadedToHead

        if temp is None:
            return False

        return temp

    @property
    def minor_diameter_of_bolt_thread(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinorDiameterOfBoltThread

        if temp is None:
            return 0.0

        return temp

    @minor_diameter_of_bolt_thread.setter
    @enforce_parameter_types
    def minor_diameter_of_bolt_thread(self: "Self", value: "float") -> None:
        self.wrapped.MinorDiameterOfBoltThread = (
            float(value) if value is not None else 0.0
        )

    @property
    def nut_thread_minor_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NutThreadMinorDiameter

        if temp is None:
            return 0.0

        return temp

    @nut_thread_minor_diameter.setter
    @enforce_parameter_types
    def nut_thread_minor_diameter(self: "Self", value: "float") -> None:
        self.wrapped.NutThreadMinorDiameter = float(value) if value is not None else 0.0

    @property
    def nut_thread_pitch_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NutThreadPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @nut_thread_pitch_diameter.setter
    @enforce_parameter_types
    def nut_thread_pitch_diameter(self: "Self", value: "float") -> None:
        self.wrapped.NutThreadPitchDiameter = float(value) if value is not None else 0.0

    @property
    def outside_diameter_of_clamped_parts(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.OutsideDiameterOfClampedParts

        if temp is None:
            return 0.0

        return temp

    @outside_diameter_of_clamped_parts.setter
    @enforce_parameter_types
    def outside_diameter_of_clamped_parts(self: "Self", value: "float") -> None:
        self.wrapped.OutsideDiameterOfClampedParts = (
            float(value) if value is not None else 0.0
        )

    @property
    def pitch_of_thread(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PitchOfThread

        if temp is None:
            return 0.0

        return temp

    @pitch_of_thread.setter
    @enforce_parameter_types
    def pitch_of_thread(self: "Self", value: "float") -> None:
        self.wrapped.PitchOfThread = float(value) if value is not None else 0.0

    @property
    def shank_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ShankDiameter

        if temp is None:
            return 0.0

        return temp

    @shank_diameter.setter
    @enforce_parameter_types
    def shank_diameter(self: "Self", value: "float") -> None:
        self.wrapped.ShankDiameter = float(value) if value is not None else 0.0

    @property
    def shank_inner_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ShankInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @shank_inner_diameter.setter
    @enforce_parameter_types
    def shank_inner_diameter(self: "Self", value: "float") -> None:
        self.wrapped.ShankInnerDiameter = float(value) if value is not None else 0.0

    @property
    def shank_length(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ShankLength

        if temp is None:
            return 0.0

        return temp

    @shank_length.setter
    @enforce_parameter_types
    def shank_length(self: "Self", value: "float") -> None:
        self.wrapped.ShankLength = float(value) if value is not None else 0.0

    @property
    def standard_size(self: "Self") -> "_1530.StandardSizes":
        """mastapy._private.bolts.StandardSizes"""
        temp = self.wrapped.StandardSize

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bolts.StandardSizes")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bolts._1530", "StandardSizes"
        )(value)

    @standard_size.setter
    @enforce_parameter_types
    def standard_size(self: "Self", value: "_1530.StandardSizes") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bolts.StandardSizes")
        self.wrapped.StandardSize = value

    @property
    def tapped_thread_minor_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TappedThreadMinorDiameter

        if temp is None:
            return 0.0

        return temp

    @tapped_thread_minor_diameter.setter
    @enforce_parameter_types
    def tapped_thread_minor_diameter(self: "Self", value: "float") -> None:
        self.wrapped.TappedThreadMinorDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def tapped_thread_pitch_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.TappedThreadPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @tapped_thread_pitch_diameter.setter
    @enforce_parameter_types
    def tapped_thread_pitch_diameter(self: "Self", value: "float") -> None:
        self.wrapped.TappedThreadPitchDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def type_of_bolted_joint(self: "Self") -> "_1520.BoltTypes":
        """mastapy._private.bolts.BoltTypes"""
        temp = self.wrapped.TypeOfBoltedJoint

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bolts.BoltTypes")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bolts._1520", "BoltTypes"
        )(value)

    @type_of_bolted_joint.setter
    @enforce_parameter_types
    def type_of_bolted_joint(self: "Self", value: "_1520.BoltTypes") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bolts.BoltTypes")
        self.wrapped.TypeOfBoltedJoint = value

    @property
    def type_of_head_cap(self: "Self") -> "_1525.HeadCapTypes":
        """mastapy._private.bolts.HeadCapTypes"""
        temp = self.wrapped.TypeOfHeadCap

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bolts.HeadCapTypes")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bolts._1525", "HeadCapTypes"
        )(value)

    @type_of_head_cap.setter
    @enforce_parameter_types
    def type_of_head_cap(self: "Self", value: "_1525.HeadCapTypes") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bolts.HeadCapTypes")
        self.wrapped.TypeOfHeadCap = value

    @property
    def type_of_thread(self: "Self") -> "_1532.ThreadTypes":
        """mastapy._private.bolts.ThreadTypes"""
        temp = self.wrapped.TypeOfThread

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bolts.ThreadTypes")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bolts._1532", "ThreadTypes"
        )(value)

    @type_of_thread.setter
    @enforce_parameter_types
    def type_of_thread(self: "Self", value: "_1532.ThreadTypes") -> None:
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bolts.ThreadTypes")
        self.wrapped.TypeOfThread = value

    @property
    def width_across_flats(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WidthAcrossFlats

        if temp is None:
            return 0.0

        return temp

    @width_across_flats.setter
    @enforce_parameter_types
    def width_across_flats(self: "Self", value: "float") -> None:
        self.wrapped.WidthAcrossFlats = float(value) if value is not None else 0.0

    @property
    def cast_to(self: "Self") -> "_Cast_BoltGeometry":
        """Cast to another type.

        Returns:
            _Cast_BoltGeometry
        """
        return _Cast_BoltGeometry(self)
