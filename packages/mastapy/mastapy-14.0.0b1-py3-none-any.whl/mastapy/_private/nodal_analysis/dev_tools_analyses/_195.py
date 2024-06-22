"""FEModel"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FE_MODEL = python_net_import("SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModel")

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.nodal_analysis.dev_tools_analyses import _210, _200
    from mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
        _220,
        _214,
        _215,
        _221,
        _222,
        _228,
        _219,
        _223,
        _224,
        _225,
        _226,
        _218,
        _229,
    )

    Self = TypeVar("Self", bound="FEModel")
    CastSelf = TypeVar("CastSelf", bound="FEModel._Cast_FEModel")


__docformat__ = "restructuredtext en"
__all__ = ("FEModel",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FEModel:
    """Special nested class for casting FEModel to subclasses."""

    __parent__: "FEModel"

    @property
    def fe_model(self: "CastSelf") -> "FEModel":
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
class FEModel(_0.APIBase):
    """FEModel

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_MODEL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def degree_of_neighbouring_faces_to_include(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.DegreeOfNeighbouringFacesToInclude

        if temp is None:
            return 0

        return temp

    @degree_of_neighbouring_faces_to_include.setter
    @enforce_parameter_types
    def degree_of_neighbouring_faces_to_include(self: "Self", value: "int") -> None:
        self.wrapped.DegreeOfNeighbouringFacesToInclude = (
            int(value) if value is not None else 0
        )

    @property
    def edge_angle_tolerance(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.EdgeAngleTolerance

        if temp is None:
            return 0.0

        return temp

    @edge_angle_tolerance.setter
    @enforce_parameter_types
    def edge_angle_tolerance(self: "Self", value: "float") -> None:
        self.wrapped.EdgeAngleTolerance = float(value) if value is not None else 0.0

    @property
    def include_adjacent_faces_in_face_selection(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.IncludeAdjacentFacesInFaceSelection

        if temp is None:
            return False

        return temp

    @include_adjacent_faces_in_face_selection.setter
    @enforce_parameter_types
    def include_adjacent_faces_in_face_selection(self: "Self", value: "bool") -> None:
        self.wrapped.IncludeAdjacentFacesInFaceSelection = (
            bool(value) if value is not None else False
        )

    @property
    def model_force_unit(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModelForceUnit

        if temp is None:
            return ""

        return temp

    @property
    def model_length_unit(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModelLengthUnit

        if temp is None:
            return ""

        return temp

    @property
    def model_splitting_method(self: "Self") -> "_210.ModelSplittingMethod":
        """mastapy._private.nodal_analysis.dev_tools_analyses.ModelSplittingMethod"""
        temp = self.wrapped.ModelSplittingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.ModelSplittingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.nodal_analysis.dev_tools_analyses._210",
            "ModelSplittingMethod",
        )(value)

    @model_splitting_method.setter
    @enforce_parameter_types
    def model_splitting_method(
        self: "Self", value: "_210.ModelSplittingMethod"
    ) -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.ModelSplittingMethod"
        )
        self.wrapped.ModelSplittingMethod = value

    @property
    def number_of_elements(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfElements

        if temp is None:
            return 0

        return temp

    @property
    def number_of_elements_with_negative_jacobian(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfElementsWithNegativeJacobian

        if temp is None:
            return 0

        return temp

    @property
    def number_of_elements_with_negative_size(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfElementsWithNegativeSize

        if temp is None:
            return 0

        return temp

    @property
    def number_of_nodes(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNodes

        if temp is None:
            return 0

        return temp

    @property
    def original_file_path(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OriginalFilePath

        if temp is None:
            return ""

        return temp

    @property
    def use_contact_pairs_for_boundary(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseContactPairsForBoundary

        if temp is None:
            return False

        return temp

    @use_contact_pairs_for_boundary.setter
    @enforce_parameter_types
    def use_contact_pairs_for_boundary(self: "Self", value: "bool") -> None:
        self.wrapped.UseContactPairsForBoundary = (
            bool(value) if value is not None else False
        )

    @property
    def use_multipoint_constraints_for_boundary(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseMultipointConstraintsForBoundary

        if temp is None:
            return False

        return temp

    @use_multipoint_constraints_for_boundary.setter
    @enforce_parameter_types
    def use_multipoint_constraints_for_boundary(self: "Self", value: "bool") -> None:
        self.wrapped.UseMultipointConstraintsForBoundary = (
            bool(value) if value is not None else False
        )

    @property
    def use_rigid_elements_for_boundary(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseRigidElementsForBoundary

        if temp is None:
            return False

        return temp

    @use_rigid_elements_for_boundary.setter
    @enforce_parameter_types
    def use_rigid_elements_for_boundary(self: "Self", value: "bool") -> None:
        self.wrapped.UseRigidElementsForBoundary = (
            bool(value) if value is not None else False
        )

    @property
    def use_simplified_normal_calculation_when_deformed(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseSimplifiedNormalCalculationWhenDeformed

        if temp is None:
            return False

        return temp

    @use_simplified_normal_calculation_when_deformed.setter
    @enforce_parameter_types
    def use_simplified_normal_calculation_when_deformed(
        self: "Self", value: "bool"
    ) -> None:
        self.wrapped.UseSimplifiedNormalCalculationWhenDeformed = (
            bool(value) if value is not None else False
        )

    @property
    def beam_element_properties(self: "Self") -> "List[_220.ElementPropertiesBeam]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesBeam]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeamElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def contact_pairs(self: "Self") -> "List[_214.ContactPairReporting]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ContactPairReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPairs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def coordinate_systems(self: "Self") -> "List[_215.CoordinateSystemReporting]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.CoordinateSystemReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoordinateSystems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def interface_element_properties(
        self: "Self",
    ) -> "List[_221.ElementPropertiesInterface]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesInterface]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterfaceElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mass_element_properties(self: "Self") -> "List[_222.ElementPropertiesMass]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesMass]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def materials(self: "Self") -> "List[_228.MaterialPropertiesReporting]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.MaterialPropertiesReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Materials

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def model_parts(self: "Self") -> "List[_200.FEModelPart]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.FEModelPart]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModelParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def other_element_properties(self: "Self") -> "List[_219.ElementPropertiesBase]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesBase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OtherElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigid_element_properties(self: "Self") -> "List[_223.ElementPropertiesRigid]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesRigid]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shell_element_properties(self: "Self") -> "List[_224.ElementPropertiesShell]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesShell]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShellElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def solid_element_properties(self: "Self") -> "List[_225.ElementPropertiesSolid]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesSolid]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SolidElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spring_dashpot_element_properties(
        self: "Self",
    ) -> "List[_226.ElementPropertiesSpringDashpot]":
        """List[mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesSpringDashpot]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringDashpotElementProperties

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

    def add_new_material(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.AddNewMaterial()

    def change_interpolation_constraints_to_distributing(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ChangeInterpolationConstraintsToDistributing()

    def delete_unused_element_properties(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.DeleteUnusedElementProperties()

    def delete_unused_materials(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.DeleteUnusedMaterials()

    def get_all_element_details(self: "Self") -> "_218.ElementDetailsForFEModel":
        """mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementDetailsForFEModel"""
        method_result = self.wrapped.GetAllElementDetails()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def get_all_node_details(self: "Self") -> "_229.NodeDetailsForFEModel":
        """mastapy._private.nodal_analysis.dev_tools_analyses.full_fe_reporting.NodeDetailsForFEModel"""
        method_result = self.wrapped.GetAllNodeDetails()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

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
    def cast_to(self: "Self") -> "_Cast_FEModel":
        """Cast to another type.

        Returns:
            _Cast_FEModel
        """
        return _Cast_FEModel(self)
