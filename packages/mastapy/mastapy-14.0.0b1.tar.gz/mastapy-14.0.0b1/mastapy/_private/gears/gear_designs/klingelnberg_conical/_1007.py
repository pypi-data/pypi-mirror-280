"""KlingelnbergConicalGearSetDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.implicit import list_with_selected_item
from mastapy._private.gears.gear_designs.conical import _1194
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergConical",
    "KlingelnbergConicalGearSetDesign",
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.gears.gear_designs.conical import _1206
    from mastapy._private.gears.gear_designs.klingelnberg_conical import _1006
    from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _999
    from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1003
    from mastapy._private.gears.gear_designs import _974, _972

    Self = TypeVar("Self", bound="KlingelnbergConicalGearSetDesign")
    CastSelf = TypeVar(
        "CastSelf",
        bound="KlingelnbergConicalGearSetDesign._Cast_KlingelnbergConicalGearSetDesign",
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalGearSetDesign",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_KlingelnbergConicalGearSetDesign:
    """Special nested class for casting KlingelnbergConicalGearSetDesign to subclasses."""

    __parent__: "KlingelnbergConicalGearSetDesign"

    @property
    def conical_gear_set_design(self: "CastSelf") -> "_1194.ConicalGearSetDesign":
        return self.__parent__._cast(_1194.ConicalGearSetDesign)

    @property
    def gear_set_design(self: "CastSelf") -> "_974.GearSetDesign":
        from mastapy._private.gears.gear_designs import _974

        return self.__parent__._cast(_974.GearSetDesign)

    @property
    def gear_design_component(self: "CastSelf") -> "_972.GearDesignComponent":
        from mastapy._private.gears.gear_designs import _972

        return self.__parent__._cast(_972.GearDesignComponent)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
        self: "CastSelf",
    ) -> "_999.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_spiral_bevel import _999

        return self.__parent__._cast(
            _999.KlingelnbergCycloPalloidSpiralBevelGearSetDesign
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
        self: "CastSelf",
    ) -> "_1003.KlingelnbergCycloPalloidHypoidGearSetDesign":
        from mastapy._private.gears.gear_designs.klingelnberg_hypoid import _1003

        return self.__parent__._cast(_1003.KlingelnbergCycloPalloidHypoidGearSetDesign)

    @property
    def klingelnberg_conical_gear_set_design(
        self: "CastSelf",
    ) -> "KlingelnbergConicalGearSetDesign":
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
class KlingelnbergConicalGearSetDesign(_1194.ConicalGearSetDesign):
    """KlingelnbergConicalGearSetDesign

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _KLINGELNBERG_CONICAL_GEAR_SET_DESIGN

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def addendum_modification_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AddendumModificationFactor

        if temp is None:
            return 0.0

        return temp

    @addendum_modification_factor.setter
    @enforce_parameter_types
    def addendum_modification_factor(self: "Self", value: "float") -> None:
        self.wrapped.AddendumModificationFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def addendum_of_tool(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumOfTool

        if temp is None:
            return 0.0

        return temp

    @property
    def angle_modification(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.AngleModification

        if temp is None:
            return 0.0

        return temp

    @angle_modification.setter
    @enforce_parameter_types
    def angle_modification(self: "Self", value: "float") -> None:
        self.wrapped.AngleModification = float(value) if value is not None else 0.0

    @property
    def auxiliary_value_for_angle_modification(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryValueForAngleModification

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_angle_at_re(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryAngleAtRe

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_angle_at_ri(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryAngleAtRi

        if temp is None:
            return 0.0

        return temp

    @property
    def auxilliary_angle_at_re_2(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxilliaryAngleAtRe2

        if temp is None:
            return 0.0

        return temp

    @property
    def auxilliary_angle_at_ri_2(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxilliaryAngleAtRi2

        if temp is None:
            return 0.0

        return temp

    @property
    def base_circle_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseCircleRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def cone_distance_maximum_tooth_gap(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConeDistanceMaximumToothGap

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_blade_tip_width_causes_cut_off(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterBladeTipWidthCausesCutOff

        if temp is None:
            return False

        return temp

    @property
    def cutter_blade_tip_width_causes_ridge(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterBladeTipWidthCausesRidge

        if temp is None:
            return False

        return temp

    @property
    def cutter_module(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterModule

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_radius(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_face_width(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def face_contact_ratio(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_cutting_machine_options(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.GearCuttingMachineOptions

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @gear_cutting_machine_options.setter
    @enforce_parameter_types
    def gear_cutting_machine_options(self: "Self", value: "str") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.GearCuttingMachineOptions = value

    @property
    def gear_finish(self: "Self") -> "_1206.KlingelnbergFinishingMethods":
        """mastapy._private.gears.gear_designs.conical.KlingelnbergFinishingMethods"""
        temp = self.wrapped.GearFinish

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.KlingelnbergFinishingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.gears.gear_designs.conical._1206",
            "KlingelnbergFinishingMethods",
        )(value)

    @gear_finish.setter
    @enforce_parameter_types
    def gear_finish(self: "Self", value: "_1206.KlingelnbergFinishingMethods") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.KlingelnbergFinishingMethods"
        )
        self.wrapped.GearFinish = value

    @property
    def lead_angle_on_cutter_head(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadAngleOnCutterHead

        if temp is None:
            return 0.0

        return temp

    @property
    def machine_distance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MachineDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def module(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    @enforce_parameter_types
    def module(self: "Self", value: "float") -> None:
        self.wrapped.Module = float(value) if value is not None else 0.0

    @property
    def normal_module_at_inner_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalModuleAtInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_module_at_outer_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalModuleAtOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_at_tooth_tip(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngleAtToothTip

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_starts(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfStarts

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_generating_cone_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionGeneratingConeAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_number_of_teeth(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.PinionNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @pinion_number_of_teeth.setter
    @enforce_parameter_types
    def pinion_number_of_teeth(self: "Self", value: "int") -> None:
        self.wrapped.PinionNumberOfTeeth = int(value) if value is not None else 0

    @property
    def shaft_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def spiral_angle_at_wheel_inner_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralAngleAtWheelInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def spiral_angle_at_wheel_outer_diameter(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralAngleAtWheelOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def stub_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.StubFactor

        if temp is None:
            return 0.0

        return temp

    @stub_factor.setter
    @enforce_parameter_types
    def stub_factor(self: "Self", value: "float") -> None:
        self.wrapped.StubFactor = float(value) if value is not None else 0.0

    @property
    def tip_circle_diameter_of_virtual_gear(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipCircleDiameterOfVirtualGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_cone_angle_from_tooth_tip_chamfering_reduction(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipConeAngleFromToothTipChamferingReduction

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_half_angle_on_pitch_cone(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThicknessHalfAngleOnPitchCone

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_half_angle_on_tooth_tip(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThicknessHalfAngleOnToothTip

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_modification_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ToothThicknessModificationFactor

        if temp is None:
            return 0.0

        return temp

    @tooth_thickness_modification_factor.setter
    @enforce_parameter_types
    def tooth_thickness_modification_factor(self: "Self", value: "float") -> None:
        self.wrapped.ToothThicknessModificationFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def tooth_tip_chamfering_factor(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.ToothTipChamferingFactor

        if temp is None:
            return 0.0

        return temp

    @tooth_tip_chamfering_factor.setter
    @enforce_parameter_types
    def tooth_tip_chamfering_factor(self: "Self", value: "float") -> None:
        self.wrapped.ToothTipChamferingFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def tooth_tip_thickness_at_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothTipThicknessAtInner

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_tip_thickness_at_mean_cone_distance(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothTipThicknessAtMeanConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def use_minimum_addendum_modification_factor(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseMinimumAddendumModificationFactor

        if temp is None:
            return False

        return temp

    @use_minimum_addendum_modification_factor.setter
    @enforce_parameter_types
    def use_minimum_addendum_modification_factor(self: "Self", value: "bool") -> None:
        self.wrapped.UseMinimumAddendumModificationFactor = (
            bool(value) if value is not None else False
        )

    @property
    def use_required_tooth_tip_chamfering_factor(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.UseRequiredToothTipChamferingFactor

        if temp is None:
            return False

        return temp

    @use_required_tooth_tip_chamfering_factor.setter
    @enforce_parameter_types
    def use_required_tooth_tip_chamfering_factor(self: "Self", value: "bool") -> None:
        self.wrapped.UseRequiredToothTipChamferingFactor = (
            bool(value) if value is not None else False
        )

    @property
    def wheel_face_width(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WheelFaceWidth

        if temp is None:
            return 0.0

        return temp

    @wheel_face_width.setter
    @enforce_parameter_types
    def wheel_face_width(self: "Self", value: "float") -> None:
        self.wrapped.WheelFaceWidth = float(value) if value is not None else 0.0

    @property
    def wheel_generating_cone_angle(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelGeneratingConeAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_mean_spiral_angle(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WheelMeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @wheel_mean_spiral_angle.setter
    @enforce_parameter_types
    def wheel_mean_spiral_angle(self: "Self", value: "float") -> None:
        self.wrapped.WheelMeanSpiralAngle = float(value) if value is not None else 0.0

    @property
    def wheel_number_of_teeth(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.WheelNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @wheel_number_of_teeth.setter
    @enforce_parameter_types
    def wheel_number_of_teeth(self: "Self", value: "int") -> None:
        self.wrapped.WheelNumberOfTeeth = int(value) if value is not None else 0

    @property
    def wheel_pitch_diameter(self: "Self") -> "float":
        """float"""
        temp = self.wrapped.WheelPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @wheel_pitch_diameter.setter
    @enforce_parameter_types
    def wheel_pitch_diameter(self: "Self", value: "float") -> None:
        self.wrapped.WheelPitchDiameter = float(value) if value is not None else 0.0

    @property
    def whole_depth(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def conical_meshes(self: "Self") -> "List[_1006.KlingelnbergConicalGearMeshDesign]":
        """List[mastapy._private.gears.gear_designs.klingelnberg_conical.KlingelnbergConicalGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_conical_meshes(
        self: "Self",
    ) -> "List[_1006.KlingelnbergConicalGearMeshDesign]":
        """List[mastapy._private.gears.gear_designs.klingelnberg_conical.KlingelnbergConicalGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergConicalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_KlingelnbergConicalGearSetDesign":
        """Cast to another type.

        Returns:
            _Cast_KlingelnbergConicalGearSetDesign
        """
        return _Cast_KlingelnbergConicalGearSetDesign(self)
