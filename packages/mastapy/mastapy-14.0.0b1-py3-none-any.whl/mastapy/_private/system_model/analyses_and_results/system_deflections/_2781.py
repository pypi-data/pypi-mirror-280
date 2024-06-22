"""BearingSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._math.vector_2d import Vector2D
from mastapy._private._math.vector_3d import Vector3D
from mastapy._private.system_model.analyses_and_results.system_deflections import _2811
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_BEARING_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BearingSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.utility_gui.charts import _1919
    from mastapy._private.system_model.part_model import _2493, _2495
    from mastapy._private.bearings.bearing_results import _2002, _1994
    from mastapy._private.system_model.analyses_and_results.static_loads import _6966
    from mastapy._private.system_model.analyses_and_results.power_flows import _4143
    from mastapy._private.math_utility.measured_vectors import _1607
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

    Self = TypeVar("Self", bound="BearingSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf", bound="BearingSystemDeflection._Cast_BearingSystemDeflection"
    )


__docformat__ = "restructuredtext en"
__all__ = ("BearingSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BearingSystemDeflection:
    """Special nested class for casting BearingSystemDeflection to subclasses."""

    __parent__: "BearingSystemDeflection"

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
    def bearing_system_deflection(self: "CastSelf") -> "BearingSystemDeflection":
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
class BearingSystemDeflection(_2811.ConnectorSystemDeflection):
    """BearingSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEARING_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def axial_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def component_angular_displacements(self: "Self") -> "List[Vector2D]":
        """List[Vector2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAngularDisplacements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector2D)

        if value is None:
            return None

        return value

    @property
    def component_axial_displacements(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAxialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def component_radial_displacements(self: "Self") -> "List[Vector2D]":
        """List[Vector2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentRadialDisplacements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector2D)

        if value is None:
            return None

        return value

    @property
    def element_axial_displacements(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementAxialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def element_radial_displacements(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRadialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def element_tilts(self: "Self") -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementTilts

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elements_in_contact(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementsInContact

        if temp is None:
            return 0

        return temp

    @property
    def have_all_elements_converged(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HaveAllElementsConverged

        if temp is None:
            return False

        return temp

    @property
    def inner_left_mounting_axial_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerLeftMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_left_mounting_displacement(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerLeftMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def inner_left_mounting_maximum_tilt_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerLeftMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_left_mounting_tilt(self: "Self") -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerLeftMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def inner_radial_mounting_linear_displacement(self: "Self") -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRadialMountingLinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def inner_radial_mounting_maximum_tilt_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRadialMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_radial_mounting_tilt(self: "Self") -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRadialMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def inner_right_mounting_axial_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRightMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_right_mounting_displacement(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRightMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def inner_right_mounting_maximum_tilt_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRightMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_right_mounting_tilt(self: "Self") -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRightMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def internal_force(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InternalForce

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def internal_moment(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InternalMoment

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def is_loaded(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def maximum_radial_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRadialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tilt_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_axial_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterLeftMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_displacement(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterLeftMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def outer_left_mounting_maximum_tilt_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterLeftMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_tilt(self: "Self") -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterLeftMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def outer_radial_mounting_linear_displacement(self: "Self") -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRadialMountingLinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def outer_radial_mounting_maximum_tilt_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRadialMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_radial_mounting_tilt(self: "Self") -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRadialMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def outer_right_mounting_axial_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRightMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_right_mounting_displacement(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRightMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def outer_right_mounting_maximum_tilt_stiffness(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRightMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_right_mounting_tilt(self: "Self") -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRightMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def percentage_preload_spring_compression(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentagePreloadSpringCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def preload_spring_compression(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PreloadSpringCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def spring_preload_chart(self: "Self") -> "_1919.TwoDChartDefinition":
        """mastapy._private.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringPreloadChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: "Self") -> "_2493.Bearing":
        """mastapy._private.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: "Self") -> "_2002.LoadedBearingResults":
        """mastapy._private.bearings.bearing_results.LoadedBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: "Self") -> "_6966.BearingLoadCase":
        """mastapy._private.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_left_mounting_stiffness(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerLeftMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_radial_mounting_stiffness(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRadialMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_right_mounting_stiffness(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRightMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_left_mounting_stiffness(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterLeftMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_radial_mounting_stiffness(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRadialMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_right_mounting_stiffness(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRightMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: "Self") -> "_4143.BearingPowerFlow":
        """mastapy._private.system_model.analyses_and_results.power_flows.BearingPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def preload_spring_stiffness(
        self: "Self",
    ) -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PreloadSpringStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_between_rings(self: "Self") -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessBetweenRings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_matrix(self: "Self") -> "_1994.BearingStiffnessMatrixReporter":
        """mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrix

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def forces_at_zero_displacement_for_inner_and_outer_nodes(
        self: "Self",
    ) -> "List[_1607.ForceResults]":
        """List[mastapy._private.math_utility.measured_vectors.ForceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForcesAtZeroDisplacementForInnerAndOuterNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: "Self") -> "List[BearingSystemDeflection]":
        """List[mastapy._private.system_model.analyses_and_results.system_deflections.BearingSystemDeflection]

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
    def race_mounting_options_for_analysis(
        self: "Self",
    ) -> "List[_2495.BearingRaceMountingOptions]":
        """List[mastapy._private.system_model.part_model.BearingRaceMountingOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceMountingOptionsForAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def stiffness_between_each_ring(
        self: "Self",
    ) -> "List[_1994.BearingStiffnessMatrixReporter]":
        """List[mastapy._private.bearings.bearing_results.BearingStiffnessMatrixReporter]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessBetweenEachRing

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def continue_dynamic_analysis(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.ContinueDynamicAnalysis()

    def dynamic_analysis(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.DynamicAnalysis()

    @property
    def cast_to(self: "Self") -> "_Cast_BearingSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_BearingSystemDeflection
        """
        return _Cast_BearingSystemDeflection(self)
