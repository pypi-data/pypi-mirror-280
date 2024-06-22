"""ShaftHubConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.analyses_and_results.system_deflections import _2811
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ShaftHubConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.part_model.couplings import _2657
    from mastapy._private.detailed_rigid_connectors.rating import _1482
    from mastapy._private.system_model.analyses_and_results.static_loads import _7098
    from mastapy._private.system_model.analyses_and_results.power_flows import _4237
    from mastapy._private.nodal_analysis.nodal_entities import _151
    from mastapy._private.bearings.bearing_results import _1994
    from mastapy._private.system_model.analyses_and_results.system_deflections.reporting import (
        _2935,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2867,
        _2798,
        _2870,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7712,
        _7713,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="ShaftHubConnectionSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShaftHubConnectionSystemDeflection:
    """Special nested class for casting ShaftHubConnectionSystemDeflection to subclasses."""

    __parent__: "ShaftHubConnectionSystemDeflection"

    @property
    def connector_system_deflection(
        self: "CastSelf",
    ) -> "_2811.ConnectorSystemDeflection":
        return self.__parent__._cast(_2811.ConnectorSystemDeflection)

    @property
    def mountable_component_system_deflection(
        self: "CastSelf",
    ) -> "_2867.MountableComponentSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2867,
        )

        return self.__parent__._cast(_2867.MountableComponentSystemDeflection)

    @property
    def component_system_deflection(
        self: "CastSelf",
    ) -> "_2798.ComponentSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2798,
        )

        return self.__parent__._cast(_2798.ComponentSystemDeflection)

    @property
    def part_system_deflection(self: "CastSelf") -> "_2870.PartSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2870,
        )

        return self.__parent__._cast(_2870.PartSystemDeflection)

    @property
    def part_fe_analysis(self: "CastSelf") -> "_7712.PartFEAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7712,
        )

        return self.__parent__._cast(_7712.PartFEAnalysis)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7713.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7713,
        )

        return self.__parent__._cast(_7713.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7710.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2740.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2740

        return self.__parent__._cast(_2740.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2736.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2736

        return self.__parent__._cast(_2736.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2734.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2734

        return self.__parent__._cast(_2734.DesignEntityAnalysis)

    @property
    def shaft_hub_connection_system_deflection(
        self: "CastSelf",
    ) -> "ShaftHubConnectionSystemDeflection":
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
class ShaftHubConnectionSystemDeflection(_2811.ConnectorSystemDeflection):
    """ShaftHubConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SHAFT_HUB_CONNECTION_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def limiting_friction(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitingFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def node_pair_separations(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairSeparations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_radial_forces_on_inner(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeRadialForcesOnInner

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_deflection_left_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflectionLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_deflection_right_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflectionRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_deflection_tooth_centre(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflectionToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_deflection_tooth_root(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflectionToothRoot

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force_left_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForceLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force_right_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForceRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force_tooth_centre(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForceToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force_tooth_root(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForceToothRoot

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_stiffness_left_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_stiffness_right_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_stiffness_tooth_centre(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def number_of_major_diameter_contacts(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfMajorDiameterContacts

        if temp is None:
            return 0

        return temp

    @property
    def number_of_minor_diameter_contacts(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfMinorDiameterContacts

        if temp is None:
            return 0

        return temp

    @property
    def tangential_force_left_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def tangential_force_right_flank(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def tangential_force_tooth_centre(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def tangential_force_on_spline(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceOnSpline

        if temp is None:
            return 0.0

        return temp

    @property
    def will_spline_slip(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WillSplineSlip

        if temp is None:
            return False

        return temp

    @property
    def component_design(self: "Self") -> "_2657.ShaftHubConnection":
        """mastapy._private.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: "Self") -> "_1482.ShaftHubConnectionRating":
        """mastapy._private.detailed_rigid_connectors.rating.ShaftHubConnectionRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: "Self") -> "_7098.ShaftHubConnectionLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: "Self") -> "_4237.ShaftHubConnectionPowerFlow":
        """mastapy._private.system_model.analyses_and_results.power_flows.ShaftHubConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spline_contact(self: "Self") -> "_151.SplineContactNodalComponent":
        """mastapy._private.nodal_analysis.nodal_entities.SplineContactNodalComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SplineContact

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_matrix_in_local_coordinate_system(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrixInLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_matrix_in_unrotated_coordinate_system(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrixInUnrotatedCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank_contacts(self: "Self") -> "List[_2935.SplineFlankContactReporting]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.reporting.SplineFlankContactReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def major_diameter_contacts(
        self: "Self",
    ) -> "List[_2935.SplineFlankContactReporting]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.reporting.SplineFlankContactReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MajorDiameterContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def minor_diameter_contacts(
        self: "Self",
    ) -> "List[_2935.SplineFlankContactReporting]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.reporting.SplineFlankContactReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinorDiameterContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: "Self") -> "List[ShaftHubConnectionSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def right_flank_contacts(self: "Self") -> "List[_2935.SplineFlankContactReporting]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.reporting.SplineFlankContactReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ShaftHubConnectionSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_ShaftHubConnectionSystemDeflection
        """
        return _Cast_ShaftHubConnectionSystemDeflection(self)
