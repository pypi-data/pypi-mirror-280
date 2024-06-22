"""FEMeshingOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FE_MESHING_OPTIONS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "FEMeshingOptions"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.nodal_analysis import _58, _95, _62, _77, _88
    from mastapy._private.electric_machines import _1305, _1306, _1307

    Self = TypeVar("Self", bound="FEMeshingOptions")
    CastSelf = TypeVar("CastSelf", bound="FEMeshingOptions._Cast_FEMeshingOptions")


__docformat__ = "restructuredtext en"
__all__ = ("FEMeshingOptions",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FEMeshingOptions:
    """Special nested class for casting FEMeshingOptions to subclasses."""

    __parent__: "FEMeshingOptions"

    @property
    def meshing_options(self: "CastSelf") -> "_77.MeshingOptions":
        from mastapy._private.nodal_analysis import _77

        return self.__parent__._cast(_77.MeshingOptions)

    @property
    def shaft_fe_meshing_options(self: "CastSelf") -> "_88.ShaftFEMeshingOptions":
        from mastapy._private.nodal_analysis import _88

        return self.__parent__._cast(_88.ShaftFEMeshingOptions)

    @property
    def electric_machine_mechanical_analysis_meshing_options(
        self: "CastSelf",
    ) -> "_1305.ElectricMachineMechanicalAnalysisMeshingOptions":
        from mastapy._private.electric_machines import _1305

        return self.__parent__._cast(
            _1305.ElectricMachineMechanicalAnalysisMeshingOptions
        )

    @property
    def electric_machine_meshing_options(
        self: "CastSelf",
    ) -> "_1306.ElectricMachineMeshingOptions":
        from mastapy._private.electric_machines import _1306

        return self.__parent__._cast(_1306.ElectricMachineMeshingOptions)

    @property
    def electric_machine_meshing_options_base(
        self: "CastSelf",
    ) -> "_1307.ElectricMachineMeshingOptionsBase":
        from mastapy._private.electric_machines import _1307

        return self.__parent__._cast(_1307.ElectricMachineMeshingOptionsBase)

    @property
    def fe_meshing_options(self: "CastSelf") -> "FEMeshingOptions":
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
class FEMeshingOptions(_0.APIBase):
    """FEMeshingOptions

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_MESHING_OPTIONS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def element_order(self: "Self") -> "_58.ElementOrder":
        """mastapy._private.nodal_analysis.ElementOrder"""
        temp = self.wrapped.ElementOrder

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.ElementOrder"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.nodal_analysis._58", "ElementOrder"
        )(value)

    @element_order.setter
    @enforce_parameter_types
    def element_order(self: "Self", value: "_58.ElementOrder") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.ElementOrder"
        )
        self.wrapped.ElementOrder = value

    @property
    def element_shape(self: "Self") -> "_95.VolumeElementShape":
        """mastapy._private.nodal_analysis.VolumeElementShape"""
        temp = self.wrapped.ElementShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.VolumeElementShape"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.nodal_analysis._95", "VolumeElementShape"
        )(value)

    @element_shape.setter
    @enforce_parameter_types
    def element_shape(self: "Self", value: "_95.VolumeElementShape") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.VolumeElementShape"
        )
        self.wrapped.ElementShape = value

    @property
    def maximum_chord_height(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumChordHeight

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_chord_height.setter
    @enforce_parameter_types
    def maximum_chord_height(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumChordHeight = value

    @property
    def maximum_edge_altitude_ratio(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumEdgeAltitudeRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_edge_altitude_ratio.setter
    @enforce_parameter_types
    def maximum_edge_altitude_ratio(self: "Self", value: "float") -> None:
        self.wrapped.MaximumEdgeAltitudeRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_growth_rate(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumGrowthRate

        if temp is None:
            return 0.0

        return temp

    @maximum_growth_rate.setter
    @enforce_parameter_types
    def maximum_growth_rate(self: "Self", value: "float") -> None:
        self.wrapped.MaximumGrowthRate = float(value) if value is not None else 0.0

    @property
    def maximum_spanning_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MaximumSpanningAngle

        if temp is None:
            return 0.0

        return temp

    @maximum_spanning_angle.setter
    @enforce_parameter_types
    def maximum_spanning_angle(self: "Self", value: "float") -> None:
        self.wrapped.MaximumSpanningAngle = float(value) if value is not None else 0.0

    @property
    def minimum_element_size(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_element_size.setter
    @enforce_parameter_types
    def minimum_element_size(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumElementSize = value

    @property
    def minimum_triangle_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.MinimumTriangleAngle

        if temp is None:
            return 0.0

        return temp

    @minimum_triangle_angle.setter
    @enforce_parameter_types
    def minimum_triangle_angle(self: "Self", value: "float") -> None:
        self.wrapped.MinimumTriangleAngle = float(value) if value is not None else 0.0

    @property
    def preserve_edge_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PreserveEdgeAngle

        if temp is None:
            return 0.0

        return temp

    @preserve_edge_angle.setter
    @enforce_parameter_types
    def preserve_edge_angle(self: "Self", value: "float") -> None:
        self.wrapped.PreserveEdgeAngle = float(value) if value is not None else 0.0

    @property
    def preserve_node_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.PreserveNodeAngle

        if temp is None:
            return 0.0

        return temp

    @preserve_node_angle.setter
    @enforce_parameter_types
    def preserve_node_angle(self: "Self", value: "float") -> None:
        self.wrapped.PreserveNodeAngle = float(value) if value is not None else 0.0

    @property
    def meshing_problems(self: "Self") -> "List[_62.FEMeshingProblem]":
        """List[mastapy._private.nodal_analysis.FEMeshingProblem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshingProblems

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
    def cast_to(self: "Self") -> "_Cast_FEMeshingOptions":
        """Cast to another type.

        Returns:
            _Cast_FEMeshingOptions
        """
        return _Cast_FEMeshingOptions(self)
