# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/components/annotation_context.fbs".

# You can extend this class by creating a "AnnotationContextExt" class in "annotation_context_ext.py".

from __future__ import annotations

from typing import Sequence, Union

import pyarrow as pa
from attrs import define, field

from .. import datatypes
from .._baseclasses import (
    BaseExtensionArray,
    BaseExtensionType,
)
from .annotation_context_ext import AnnotationContextExt

__all__ = [
    "AnnotationContext",
    "AnnotationContextArray",
    "AnnotationContextArrayLike",
    "AnnotationContextLike",
    "AnnotationContextType",
]


@define
class AnnotationContext(AnnotationContextExt):
    """
    The `AnnotationContext` provides additional information on how to display entities.

    Entities can use `ClassId`s and `KeypointId`s to provide annotations, and
    the labels and colors will be looked up in the appropriate
    `AnnotationContext`. We use the *first* annotation context we find in the
    path-hierarchy when searching up through the ancestors of a given entity
    path.
    """

    # You can define your own __init__ function as a member of AnnotationContextExt in annotation_context_ext.py

    class_map: list[datatypes.ClassDescriptionMapElem] = field(
        converter=AnnotationContextExt.class_map__field_converter_override,  # type: ignore[misc]
    )


AnnotationContextLike = AnnotationContext
AnnotationContextArrayLike = Union[
    AnnotationContext,
    Sequence[AnnotationContextLike],
    datatypes.ClassDescription,
    Sequence[datatypes.ClassDescriptionMapElemLike],
]


# --- Arrow support ---


class AnnotationContextType(BaseExtensionType):
    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.list_(
                pa.field(
                    "item",
                    pa.struct(
                        [
                            pa.field("class_id", pa.uint16(), nullable=False, metadata={}),
                            pa.field(
                                "class_description",
                                pa.struct(
                                    [
                                        pa.field(
                                            "info",
                                            pa.struct(
                                                [
                                                    pa.field("id", pa.uint16(), nullable=False, metadata={}),
                                                    pa.field("label", pa.utf8(), nullable=True, metadata={}),
                                                    pa.field("color", pa.uint32(), nullable=True, metadata={}),
                                                ]
                                            ),
                                            nullable=False,
                                            metadata={},
                                        ),
                                        pa.field(
                                            "keypoint_annotations",
                                            pa.list_(
                                                pa.field(
                                                    "item",
                                                    pa.struct(
                                                        [
                                                            pa.field("id", pa.uint16(), nullable=False, metadata={}),
                                                            pa.field("label", pa.utf8(), nullable=True, metadata={}),
                                                            pa.field("color", pa.uint32(), nullable=True, metadata={}),
                                                        ]
                                                    ),
                                                    nullable=False,
                                                    metadata={},
                                                )
                                            ),
                                            nullable=False,
                                            metadata={},
                                        ),
                                        pa.field(
                                            "keypoint_connections",
                                            pa.list_(
                                                pa.field(
                                                    "item",
                                                    pa.struct(
                                                        [
                                                            pa.field(
                                                                "keypoint0", pa.uint16(), nullable=False, metadata={}
                                                            ),
                                                            pa.field(
                                                                "keypoint1", pa.uint16(), nullable=False, metadata={}
                                                            ),
                                                        ]
                                                    ),
                                                    nullable=False,
                                                    metadata={},
                                                )
                                            ),
                                            nullable=False,
                                            metadata={},
                                        ),
                                    ]
                                ),
                                nullable=False,
                                metadata={},
                            ),
                        ]
                    ),
                    nullable=False,
                    metadata={},
                )
            ),
            "rerun.components.AnnotationContext",
        )


class AnnotationContextArray(BaseExtensionArray[AnnotationContextArrayLike]):
    _EXTENSION_NAME = "rerun.components.AnnotationContext"
    _EXTENSION_TYPE = AnnotationContextType

    @staticmethod
    def _native_to_pa_array(data: AnnotationContextArrayLike, data_type: pa.DataType) -> pa.Array:
        return AnnotationContextExt.native_to_pa_array_override(data, data_type)


AnnotationContextType._ARRAY_TYPE = AnnotationContextArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(AnnotationContextType())
