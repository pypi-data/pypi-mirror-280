"""FESubstructureWithSelection"""
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private.system_model.fe import _2413
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureWithSelection"
)

if TYPE_CHECKING:
    from typing import Any, Type, List, TypeVar

    from mastapy._private.system_model.fe import (
        _2437,
        _2429,
        _2455,
        _2445,
        _2446,
        _2447,
        _2448,
    )

    Self = TypeVar("Self", bound="FESubstructureWithSelection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="FESubstructureWithSelection._Cast_FESubstructureWithSelection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureWithSelection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FESubstructureWithSelection:
    """Special nested class for casting FESubstructureWithSelection to subclasses."""

    __parent__: "FESubstructureWithSelection"

    @property
    def base_fe_with_selection(self: "CastSelf") -> "_2413.BaseFEWithSelection":
        return self.__parent__._cast(_2413.BaseFEWithSelection)

    @property
    def fe_substructure_with_selection_components(
        self: "CastSelf",
    ) -> "_2445.FESubstructureWithSelectionComponents":
        from mastapy._private.system_model.fe import _2445

        return self.__parent__._cast(_2445.FESubstructureWithSelectionComponents)

    @property
    def fe_substructure_with_selection_for_harmonic_analysis(
        self: "CastSelf",
    ) -> "_2446.FESubstructureWithSelectionForHarmonicAnalysis":
        from mastapy._private.system_model.fe import _2446

        return self.__parent__._cast(
            _2446.FESubstructureWithSelectionForHarmonicAnalysis
        )

    @property
    def fe_substructure_with_selection_for_modal_analysis(
        self: "CastSelf",
    ) -> "_2447.FESubstructureWithSelectionForModalAnalysis":
        from mastapy._private.system_model.fe import _2447

        return self.__parent__._cast(_2447.FESubstructureWithSelectionForModalAnalysis)

    @property
    def fe_substructure_with_selection_for_static_analysis(
        self: "CastSelf",
    ) -> "_2448.FESubstructureWithSelectionForStaticAnalysis":
        from mastapy._private.system_model.fe import _2448

        return self.__parent__._cast(_2448.FESubstructureWithSelectionForStaticAnalysis)

    @property
    def fe_substructure_with_selection(
        self: "CastSelf",
    ) -> "FESubstructureWithSelection":
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
class FESubstructureWithSelection(_2413.BaseFEWithSelection):
    """FESubstructureWithSelection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FE_SUBSTRUCTURE_WITH_SELECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def selected_nodes(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedNodes

        if temp is None:
            return ""

        return temp

    @property
    def fe_substructure(self: "Self") -> "_2437.FESubstructure":
        """mastapy._private.system_model.fe.FESubstructure

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FESubstructure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def element_face_groups(
        self: "Self",
    ) -> "List[_2429.ElementFaceGroupWithSelection]":
        """List[mastapy._private.system_model.fe.ElementFaceGroupWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementFaceGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def node_groups(self: "Self") -> "List[_2455.NodeGroupWithSelection]":
        """List[mastapy._private.system_model.fe.NodeGroupWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def create_condensation_node_connected_to_current_selection(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.CreateCondensationNodeConnectedToCurrentSelection()

    def create_element_face_group(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.CreateElementFaceGroup()

    def create_node_group(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.CreateNodeGroup()

    def ground_selected_faces(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.GroundSelectedFaces()

    def remove_grounding_on_selected_faces(self: "Self") -> None:
        """Method does not return."""
        self.wrapped.RemoveGroundingOnSelectedFaces()

    @property
    def cast_to(self: "Self") -> "_Cast_FESubstructureWithSelection":
        """Cast to another type.

        Returns:
            _Cast_FESubstructureWithSelection
        """
        return _Cast_FESubstructureWithSelection(self)
