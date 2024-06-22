"""DetailedRigidConnectorHalfDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_DETAILED_RIGID_CONNECTOR_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors", "DetailedRigidConnectorHalfDesign"
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.detailed_rigid_connectors.splines import (
        _1435,
        _1438,
        _1442,
        _1445,
        _1453,
        _1460,
        _1465,
    )
    from mastapy._private.detailed_rigid_connectors.keyed_joints import _1485
    from mastapy._private.detailed_rigid_connectors.interference_fits import _1492

    Self = TypeVar("Self", bound="DetailedRigidConnectorHalfDesign")
    CastSelf = TypeVar(
        "CastSelf",
        bound="DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
    )


__docformat__ = "restructuredtext en"
__all__ = ("DetailedRigidConnectorHalfDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_DetailedRigidConnectorHalfDesign:
    """Special nested class for casting DetailedRigidConnectorHalfDesign to subclasses."""

    __parent__: "DetailedRigidConnectorHalfDesign"

    @property
    def custom_spline_half_design(self: "CastSelf") -> "_1435.CustomSplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1435

        return self.__parent__._cast(_1435.CustomSplineHalfDesign)

    @property
    def din5480_spline_half_design(self: "CastSelf") -> "_1438.DIN5480SplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1438

        return self.__parent__._cast(_1438.DIN5480SplineHalfDesign)

    @property
    def gbt3478_spline_half_design(self: "CastSelf") -> "_1442.GBT3478SplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1442

        return self.__parent__._cast(_1442.GBT3478SplineHalfDesign)

    @property
    def iso4156_spline_half_design(self: "CastSelf") -> "_1445.ISO4156SplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1445

        return self.__parent__._cast(_1445.ISO4156SplineHalfDesign)

    @property
    def sae_spline_half_design(self: "CastSelf") -> "_1453.SAESplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1453

        return self.__parent__._cast(_1453.SAESplineHalfDesign)

    @property
    def spline_half_design(self: "CastSelf") -> "_1460.SplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1460

        return self.__parent__._cast(_1460.SplineHalfDesign)

    @property
    def standard_spline_half_design(
        self: "CastSelf",
    ) -> "_1465.StandardSplineHalfDesign":
        from mastapy._private.detailed_rigid_connectors.splines import _1465

        return self.__parent__._cast(_1465.StandardSplineHalfDesign)

    @property
    def keyway_joint_half_design(self: "CastSelf") -> "_1485.KeywayJointHalfDesign":
        from mastapy._private.detailed_rigid_connectors.keyed_joints import _1485

        return self.__parent__._cast(_1485.KeywayJointHalfDesign)

    @property
    def interference_fit_half_design(
        self: "CastSelf",
    ) -> "_1492.InterferenceFitHalfDesign":
        from mastapy._private.detailed_rigid_connectors.interference_fits import _1492

        return self.__parent__._cast(_1492.InterferenceFitHalfDesign)

    @property
    def detailed_rigid_connector_half_design(
        self: "CastSelf",
    ) -> "DetailedRigidConnectorHalfDesign":
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
class DetailedRigidConnectorHalfDesign(_0.APIBase):
    """DetailedRigidConnectorHalfDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _DETAILED_RIGID_CONNECTOR_HALF_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def non_contacting_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonContactingDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_contacting_diameter.setter
    @enforce_parameter_types
    def non_contacting_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonContactingDiameter = value

    @property
    def tensile_yield_strength(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TensileYieldStrength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tensile_yield_strength.setter
    @enforce_parameter_types
    def tensile_yield_strength(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TensileYieldStrength = value

    @property
    def ultimate_tensile_strength(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UltimateTensileStrength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ultimate_tensile_strength.setter
    @enforce_parameter_types
    def ultimate_tensile_strength(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UltimateTensileStrength = value

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
    def cast_to(self: "Self") -> "_Cast_DetailedRigidConnectorHalfDesign":
        """Cast to another type.

        Returns:
            _Cast_DetailedRigidConnectorHalfDesign
        """
        return _Cast_DetailedRigidConnectorHalfDesign(self)
