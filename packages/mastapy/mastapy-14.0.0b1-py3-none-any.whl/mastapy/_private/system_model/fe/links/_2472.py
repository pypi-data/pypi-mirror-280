"""FELink"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal.implicit import (
    overridable,
    enum_with_selected_value,
    list_with_selected_item,
)
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal import (
    constructor,
    enum_with_selected_value_runtime,
    overridable_enum_runtime,
    conversion,
    utility,
)
from mastapy._private.system_model.fe import _2416, _2452, _2456, _2439
from mastapy._private.nodal_analysis.dev_tools_analyses import _213
from mastapy._private import _0
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FE_LINK = python_net_import("SMT.MastaAPI.SystemModel.FE.Links", "FELink")

if TYPE_CHECKING:
    from typing import Any, Type, Union, Tuple, List, TypeVar
    from collections import OrderedDict

    from mastapy._private.system_model.fe import _2451
    from mastapy._private.system_model.part_model import _2520
    from mastapy._private.system_model.connections_and_sockets import _2349
    from mastapy._private.materials import _280
    from mastapy._private.system_model.fe.links import (
        _2473,
        _2475,
        _2476,
        _2477,
        _2478,
        _2479,
        _2480,
        _2481,
        _2482,
        _2483,
        _2484,
        _2485,
        _2486,
    )

    Self = TypeVar("Self", bound="FELink")
    CastSelf = TypeVar("CastSelf", bound="FELink._Cast_FELink")


__docformat__ = "restructuredtext en"
__all__ = ("FELink",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FELink:
    """Special nested class for casting FELink to subclasses."""

    __parent__: "FELink"

    @property
    def electric_machine_stator_fe_link(
        self: "CastSelf",
    ) -> "_2473.ElectricMachineStatorFELink":
        from mastapy._private.system_model.fe.links import _2473

        return self.__parent__._cast(_2473.ElectricMachineStatorFELink)

    @property
    def gear_mesh_fe_link(self: "CastSelf") -> "_2475.GearMeshFELink":
        from mastapy._private.system_model.fe.links import _2475

        return self.__parent__._cast(_2475.GearMeshFELink)

    @property
    def gear_with_duplicated_meshes_fe_link(
        self: "CastSelf",
    ) -> "_2476.GearWithDuplicatedMeshesFELink":
        from mastapy._private.system_model.fe.links import _2476

        return self.__parent__._cast(_2476.GearWithDuplicatedMeshesFELink)

    @property
    def multi_angle_connection_fe_link(
        self: "CastSelf",
    ) -> "_2477.MultiAngleConnectionFELink":
        from mastapy._private.system_model.fe.links import _2477

        return self.__parent__._cast(_2477.MultiAngleConnectionFELink)

    @property
    def multi_node_connector_fe_link(
        self: "CastSelf",
    ) -> "_2478.MultiNodeConnectorFELink":
        from mastapy._private.system_model.fe.links import _2478

        return self.__parent__._cast(_2478.MultiNodeConnectorFELink)

    @property
    def multi_node_fe_link(self: "CastSelf") -> "_2479.MultiNodeFELink":
        from mastapy._private.system_model.fe.links import _2479

        return self.__parent__._cast(_2479.MultiNodeFELink)

    @property
    def planetary_connector_multi_node_fe_link(
        self: "CastSelf",
    ) -> "_2480.PlanetaryConnectorMultiNodeFELink":
        from mastapy._private.system_model.fe.links import _2480

        return self.__parent__._cast(_2480.PlanetaryConnectorMultiNodeFELink)

    @property
    def planet_based_fe_link(self: "CastSelf") -> "_2481.PlanetBasedFELink":
        from mastapy._private.system_model.fe.links import _2481

        return self.__parent__._cast(_2481.PlanetBasedFELink)

    @property
    def planet_carrier_fe_link(self: "CastSelf") -> "_2482.PlanetCarrierFELink":
        from mastapy._private.system_model.fe.links import _2482

        return self.__parent__._cast(_2482.PlanetCarrierFELink)

    @property
    def point_load_fe_link(self: "CastSelf") -> "_2483.PointLoadFELink":
        from mastapy._private.system_model.fe.links import _2483

        return self.__parent__._cast(_2483.PointLoadFELink)

    @property
    def rolling_ring_connection_fe_link(
        self: "CastSelf",
    ) -> "_2484.RollingRingConnectionFELink":
        from mastapy._private.system_model.fe.links import _2484

        return self.__parent__._cast(_2484.RollingRingConnectionFELink)

    @property
    def shaft_hub_connection_fe_link(
        self: "CastSelf",
    ) -> "_2485.ShaftHubConnectionFELink":
        from mastapy._private.system_model.fe.links import _2485

        return self.__parent__._cast(_2485.ShaftHubConnectionFELink)

    @property
    def single_node_fe_link(self: "CastSelf") -> "_2486.SingleNodeFELink":
        from mastapy._private.system_model.fe.links import _2486

        return self.__parent__._cast(_2486.SingleNodeFELink)

    @property
    def fe_link(self: "CastSelf") -> "FELink":
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
class FELink(_0.APIBase):
    """FELink

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_LINK

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def angle_of_centre_of_connection_patch(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AngleOfCentreOfConnectionPatch

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle_of_centre_of_connection_patch.setter
    @enforce_parameter_types
    def angle_of_centre_of_connection_patch(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AngleOfCentreOfConnectionPatch = value

    @property
    def bearing_node_link_option(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption":
        """EnumWithSelectedValue[mastapy._private.system_model.fe.BearingNodeOption]"""
        temp = self.wrapped.BearingNodeLinkOption

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @bearing_node_link_option.setter
    @enforce_parameter_types
    def bearing_node_link_option(
        self: "Self", value: "_2416.BearingNodeOption"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BearingNodeLinkOption = value

    @property
    def bearing_race_in_fe(self: "Self") -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.BearingRaceInFE

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @bearing_race_in_fe.setter
    @enforce_parameter_types
    def bearing_race_in_fe(
        self: "Self", value: "Union[bool, Tuple[bool, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.BearingRaceInFE = value

    @property
    def component_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentName

        if temp is None:
            return ""

        return temp

    @property
    def connect_to_midside_nodes(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.ConnectToMidsideNodes

        if temp is None:
            return False

        return temp

    @connect_to_midside_nodes.setter
    @enforce_parameter_types
    def connect_to_midside_nodes(self: "Self", value: "bool") -> None:
        self.wrapped.ConnectToMidsideNodes = bool(value) if value is not None else False

    @property
    def connection(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connection

        if temp is None:
            return ""

        return temp

    @property
    def coupling_type(self: "Self") -> "overridable.Overridable_RigidCouplingType":
        """Overridable[mastapy._private.nodal_analysis.dev_tools_analyses.RigidCouplingType]"""
        temp = self.wrapped.CouplingType

        if temp is None:
            return None

        value = overridable.Overridable_RigidCouplingType.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @coupling_type.setter
    @enforce_parameter_types
    def coupling_type(
        self: "Self",
        value: "Union[_213.RigidCouplingType, Tuple[_213.RigidCouplingType, bool]]",
    ) -> None:
        wrapper_type = overridable.Overridable_RigidCouplingType.wrapper_type()
        enclosed_type = overridable.Overridable_RigidCouplingType.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.CouplingType = value

    @property
    def external_node_ids(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalNodeIDs

        if temp is None:
            return ""

        return temp

    @property
    def has_teeth(self: "Self") -> "bool":
        """bool"""
        temp = self.wrapped.HasTeeth

        if temp is None:
            return False

        return temp

    @has_teeth.setter
    @enforce_parameter_types
    def has_teeth(self: "Self", value: "bool") -> None:
        self.wrapped.HasTeeth = bool(value) if value is not None else False

    @property
    def link_node_source(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource":
        """EnumWithSelectedValue[mastapy._private.system_model.fe.LinkNodeSource]"""
        temp = self.wrapped.LinkNodeSource

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @link_node_source.setter
    @enforce_parameter_types
    def link_node_source(self: "Self", value: "_2452.LinkNodeSource") -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LinkNodeSource = value

    @property
    def link_to_get_nodes_from(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_FELink":
        """ListWithSelectedItem[mastapy._private.system_model.fe.links.FELink]"""
        temp = self.wrapped.LinkToGetNodesFrom

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_FELink",
        )(temp)

    @link_to_get_nodes_from.setter
    @enforce_parameter_types
    def link_to_get_nodes_from(self: "Self", value: "FELink") -> None:
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_FELink.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_FELink.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LinkToGetNodesFrom = value

    @property
    def node_cone_search_angle(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NodeConeSearchAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @node_cone_search_angle.setter
    @enforce_parameter_types
    def node_cone_search_angle(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NodeConeSearchAngle = value

    @property
    def node_cylinder_search_axial_offset(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NodeCylinderSearchAxialOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @node_cylinder_search_axial_offset.setter
    @enforce_parameter_types
    def node_cylinder_search_axial_offset(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NodeCylinderSearchAxialOffset = value

    @property
    def node_cylinder_search_diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NodeCylinderSearchDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @node_cylinder_search_diameter.setter
    @enforce_parameter_types
    def node_cylinder_search_diameter(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NodeCylinderSearchDiameter = value

    @property
    def node_cylinder_search_length(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NodeCylinderSearchLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @node_cylinder_search_length.setter
    @enforce_parameter_types
    def node_cylinder_search_length(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NodeCylinderSearchLength = value

    @property
    def node_search_cylinder_thickness(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NodeSearchCylinderThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @node_search_cylinder_thickness.setter
    @enforce_parameter_types
    def node_search_cylinder_thickness(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NodeSearchCylinderThickness = value

    @property
    def node_selection_depth(
        self: "Self",
    ) -> "overridable.Overridable_NodeSelectionDepthOption":
        """Overridable[mastapy._private.system_model.fe.NodeSelectionDepthOption]"""
        temp = self.wrapped.NodeSelectionDepth

        if temp is None:
            return None

        value = overridable.Overridable_NodeSelectionDepthOption.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @node_selection_depth.setter
    @enforce_parameter_types
    def node_selection_depth(
        self: "Self",
        value: "Union[_2456.NodeSelectionDepthOption, Tuple[_2456.NodeSelectionDepthOption, bool]]",
    ) -> None:
        wrapper_type = overridable.Overridable_NodeSelectionDepthOption.wrapper_type()
        enclosed_type = overridable.Overridable_NodeSelectionDepthOption.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.NodeSelectionDepth = value

    @property
    def number_of_axial_nodes(self: "Self") -> "int":
        """int"""
        temp = self.wrapped.NumberOfAxialNodes

        if temp is None:
            return 0

        return temp

    @number_of_axial_nodes.setter
    @enforce_parameter_types
    def number_of_axial_nodes(self: "Self", value: "int") -> None:
        self.wrapped.NumberOfAxialNodes = int(value) if value is not None else 0

    @property
    def number_of_nodes_in_full_fe_mesh(self: "Self") -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNodesInFullFEMesh

        if temp is None:
            return 0

        return temp

    @property
    def number_of_nodes_in_ring(self: "Self") -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfNodesInRing

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_nodes_in_ring.setter
    @enforce_parameter_types
    def number_of_nodes_in_ring(
        self: "Self", value: "Union[int, Tuple[int, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfNodesInRing = value

    @property
    def span_of_patch(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpanOfPatch

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @span_of_patch.setter
    @enforce_parameter_types
    def span_of_patch(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpanOfPatch = value

    @property
    def support_material_id(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.SupportMaterialID

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @support_material_id.setter
    @enforce_parameter_types
    def support_material_id(self: "Self", value: "int") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.SupportMaterialID = value

    @property
    def width_of_axial_patch(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WidthOfAxialPatch

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @width_of_axial_patch.setter
    @enforce_parameter_types
    def width_of_axial_patch(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WidthOfAxialPatch = value

    @property
    def alignment_in_component_coordinate_system(
        self: "Self",
    ) -> "_2451.LinkComponentAxialPositionErrorReporter":
        """mastapy._private.system_model.fe.LinkComponentAxialPositionErrorReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlignmentInComponentCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def alignment_in_fe_coordinate_system(
        self: "Self",
    ) -> "_2451.LinkComponentAxialPositionErrorReporter":
        """mastapy._private.system_model.fe.LinkComponentAxialPositionErrorReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlignmentInFECoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def alignment_in_world_coordinate_system(
        self: "Self",
    ) -> "_2451.LinkComponentAxialPositionErrorReporter":
        """mastapy._private.system_model.fe.LinkComponentAxialPositionErrorReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlignmentInWorldCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component(self: "Self") -> "_2520.MountableComponent":
        """mastapy._private.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Component

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket(self: "Self") -> "_2349.Socket":
        """mastapy._private.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Socket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def support_material(self: "Self") -> "_280.Material":
        """mastapy._private.materials.Material

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SupportMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def nodes(self: "Self") -> "List[_2439.FESubstructureNode]":
        """List[mastapy._private.system_model.fe.FESubstructureNode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Nodes

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

    def nodes_grouped_by_angle(
        self: "Self",
    ) -> "OrderedDict[float, List[_2439.FESubstructureNode]]":
        """OrderedDict[float, List[mastapy._private.system_model.fe.FESubstructureNode]]"""
        return conversion.pn_to_mp_objects_in_list_in_ordered_dict(
            self.wrapped.NodesGroupedByAngle(), float
        )

    @enforce_parameter_types
    def add_or_replace_node(self: "Self", node: "_2439.FESubstructureNode") -> None:
        """Method does not return.

        Args:
            node (mastapy._private.system_model.fe.FESubstructureNode)
        """
        self.wrapped.AddOrReplaceNode(node.wrapped if node else None)

    def remove_all_nodes(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.RemoveAllNodes()

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
    def cast_to(self: "Self") -> "_Cast_FELink":
        """Cast to another type.

        Returns:
            _Cast_FELink
        """
        return _Cast_FELink(self)
