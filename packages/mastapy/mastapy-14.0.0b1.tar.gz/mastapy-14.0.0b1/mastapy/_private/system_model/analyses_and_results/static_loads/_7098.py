"""ShaftHubConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar


from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.analyses_and_results.static_loads import _6997
from mastapy._private._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_SHAFT_HUB_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftHubConnectionLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar

    from mastapy._private.system_model.part_model.couplings import (
        _2657,
        _2659,
        _2658,
        _2661,
        _2652,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5619
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7073,
        _6984,
        _7077,
    )
    from mastapy._private.system_model.analyses_and_results import _2740, _2736, _2734

    Self = TypeVar("Self", bound="ShaftHubConnectionLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="ShaftHubConnectionLoadCase._Cast_ShaftHubConnectionLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShaftHubConnectionLoadCase:
    """Special nested class for casting ShaftHubConnectionLoadCase to subclasses."""

    __parent__: "ShaftHubConnectionLoadCase"

    @property
    def connector_load_case(self: "CastSelf") -> "_6997.ConnectorLoadCase":
        return self.__parent__._cast(_6997.ConnectorLoadCase)

    @property
    def mountable_component_load_case(
        self: "CastSelf",
    ) -> "_7073.MountableComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7073,
        )

        return self.__parent__._cast(_7073.MountableComponentLoadCase)

    @property
    def component_load_case(self: "CastSelf") -> "_6984.ComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _6984,
        )

        return self.__parent__._cast(_6984.ComponentLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "_7077.PartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7077,
        )

        return self.__parent__._cast(_7077.PartLoadCase)

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
    def shaft_hub_connection_load_case(
        self: "CastSelf",
    ) -> "ShaftHubConnectionLoadCase":
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
class ShaftHubConnectionLoadCase(_6997.ConnectorLoadCase):
    """ShaftHubConnectionLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SHAFT_HUB_CONNECTION_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def additional_tilt_stiffness(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalTiltStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_tilt_stiffness.setter
    @enforce_parameter_types
    def additional_tilt_stiffness(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalTiltStiffness = value

    @property
    def angular_backlash(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def application_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return temp

    @application_factor.setter
    @enforce_parameter_types
    def application_factor(self: "Self", value: "float") -> None:
        self.wrapped.ApplicationFactor = float(value) if value is not None else 0.0

    @property
    def axial_preload(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialPreload

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_preload.setter
    @enforce_parameter_types
    def axial_preload(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialPreload = value

    @property
    def axial_stiffness(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_stiffness.setter
    @enforce_parameter_types
    def axial_stiffness(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialStiffness = value

    @property
    def is_torsionally_rigid(self: "Self") -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.IsTorsionallyRigid

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @is_torsionally_rigid.setter
    @enforce_parameter_types
    def is_torsionally_rigid(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.IsTorsionallyRigid = value

    @property
    def load_distribution_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @load_distribution_factor.setter
    @enforce_parameter_types
    def load_distribution_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LoadDistributionFactor = value

    @property
    def load_distribution_factor_single_key(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.LoadDistributionFactorSingleKey

        if temp is None:
            return 0.0

        return temp

    @load_distribution_factor_single_key.setter
    @enforce_parameter_types
    def load_distribution_factor_single_key(self: "Self", value: "float") -> None:
        self.wrapped.LoadDistributionFactorSingleKey = (
            float(value) if value is not None else 0.0
        )

    @property
    def normal_clearance(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NormalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @normal_clearance.setter
    @enforce_parameter_types
    def normal_clearance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NormalClearance = value

    @property
    def number_of_torque_peaks(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NumberOfTorquePeaks

        if temp is None:
            return 0.0

        return temp

    @number_of_torque_peaks.setter
    @enforce_parameter_types
    def number_of_torque_peaks(self: "Self", value: "float") -> None:
        self.wrapped.NumberOfTorquePeaks = float(value) if value is not None else 0.0

    @property
    def number_of_torque_reversals(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.NumberOfTorqueReversals

        if temp is None:
            return 0.0

        return temp

    @number_of_torque_reversals.setter
    @enforce_parameter_types
    def number_of_torque_reversals(self: "Self", value: "float") -> None:
        self.wrapped.NumberOfTorqueReversals = (
            float(value) if value is not None else 0.0
        )

    @property
    def override_design_specified_stiffness_matrix(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignSpecifiedStiffnessMatrix

        if temp is None:
            return False

        return temp

    @override_design_specified_stiffness_matrix.setter
    @enforce_parameter_types
    def override_design_specified_stiffness_matrix(self: "Self", value: "bool") -> None:
        self.wrapped.OverrideDesignSpecifiedStiffnessMatrix = (
            bool(value) if value is not None else False
        )

    @property
    def radial_clearance(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadialClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radial_clearance.setter
    @enforce_parameter_types
    def radial_clearance(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadialClearance = value

    @property
    def radial_stiffness(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadialStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radial_stiffness.setter
    @enforce_parameter_types
    def radial_stiffness(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadialStiffness = value

    @property
    def specified_application_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpecifiedApplicationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @specified_application_factor.setter
    @enforce_parameter_types
    def specified_application_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpecifiedApplicationFactor = value

    @property
    def specified_backlash_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpecifiedBacklashFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @specified_backlash_factor.setter
    @enforce_parameter_types
    def specified_backlash_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpecifiedBacklashFactor = value

    @property
    def specified_load_distribution_factor(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpecifiedLoadDistributionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @specified_load_distribution_factor.setter
    @enforce_parameter_types
    def specified_load_distribution_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpecifiedLoadDistributionFactor = value

    @property
    def specified_load_sharing_factor(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpecifiedLoadSharingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @specified_load_sharing_factor.setter
    @enforce_parameter_types
    def specified_load_sharing_factor(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpecifiedLoadSharingFactor = value

    @property
    def tilt_clearance(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TiltClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tilt_clearance.setter
    @enforce_parameter_types
    def tilt_clearance(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TiltClearance = value

    @property
    def tilt_stiffness(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tilt_stiffness.setter
    @enforce_parameter_types
    def tilt_stiffness(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TiltStiffness = value

    @property
    def torsional_stiffness(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @torsional_stiffness.setter
    @enforce_parameter_types
    def torsional_stiffness(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TorsionalStiffness = value

    @property
    def torsional_twist_preload(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TorsionalTwistPreload

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @torsional_twist_preload.setter
    @enforce_parameter_types
    def torsional_twist_preload(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TorsionalTwistPreload = value

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
    def damping_options(self: "Self") -> "_5619.SplineDampingOptions":
        """mastapy._private.system_model.analyses_and_results.mbd_analyses.SplineDampingOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DampingOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank_lead_relief(self: "Self") -> "_2659.SplineLeadRelief":
        """mastapy._private.system_model.part_model.couplings.SplineLeadRelief

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankLeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def major_fit_options(self: "Self") -> "_2658.SplineFitOptions":
        """mastapy._private.system_model.part_model.couplings.SplineFitOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MajorFitOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minor_fit_options(self: "Self") -> "_2658.SplineFitOptions":
        """mastapy._private.system_model.part_model.couplings.SplineFitOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinorFitOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_lead_relief(self: "Self") -> "_2659.SplineLeadRelief":
        """mastapy._private.system_model.part_model.couplings.SplineLeadRelief

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankLeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spline_pitch_error_options(self: "Self") -> "_2661.SplinePitchErrorOptions":
        """mastapy._private.system_model.part_model.couplings.SplinePitchErrorOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SplinePitchErrorOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fit_options(self: "Self") -> "List[_2658.SplineFitOptions]":
        """List[mastapy._private.system_model.part_model.couplings.SplineFitOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FitOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def lead_reliefs(self: "Self") -> "List[_2659.SplineLeadRelief]":
        """List[mastapy._private.system_model.part_model.couplings.SplineLeadRelief]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadReliefs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: "Self") -> "List[ShaftHubConnectionLoadCase]":
        """List[mastapy._private.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase]

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
    def tooth_locations_external_spline_half(
        self: "Self",
    ) -> "List[_2652.RigidConnectorToothLocation]":
        """List[mastapy._private.system_model.part_model.couplings.RigidConnectorToothLocation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothLocationsExternalSplineHalf

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def specified_stiffness_for_shaft_hub_connection_in_local_coordinate_system(
        self: "Self",
    ) -> "List[List[float]]":
        """List[List[float]]"""
        temp = (
            self.wrapped.SpecifiedStiffnessForShaftHubConnectionInLocalCoordinateSystem
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_list_float_2d(temp)

        if value is None:
            return None

        return value

    @specified_stiffness_for_shaft_hub_connection_in_local_coordinate_system.setter
    @enforce_parameter_types
    def specified_stiffness_for_shaft_hub_connection_in_local_coordinate_system(
        self: "Self", value: "List[List[float]]"
    ) -> None:
        value = conversion.mp_to_pn_list_float_2d(value)
        self.wrapped.SpecifiedStiffnessForShaftHubConnectionInLocalCoordinateSystem = (
            value
        )

    @property
    def cast_to(self: "Self") -> "_Cast_ShaftHubConnectionLoadCase":
        """Cast to another type.

        Returns:
            _Cast_ShaftHubConnectionLoadCase
        """
        return _Cast_ShaftHubConnectionLoadCase(self)
