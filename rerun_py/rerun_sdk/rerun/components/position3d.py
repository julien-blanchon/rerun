# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/components/position3d.fbs".

# You can extend this class by creating a "Position3DExt" class in "position3d_ext.py".

from __future__ import annotations

from .. import datatypes
from .._baseclasses import (
    BaseDelegatingExtensionArray,
    BaseDelegatingExtensionType,
)

__all__ = ["Position3D", "Position3DArray", "Position3DType"]


class Position3D(datatypes.Vec3D):
    """A position in 3D space."""

    # You can define your own __init__ function as a member of Position3DExt in position3d_ext.py

    # Note: there are no fields here because Position3D delegates to datatypes.Vec3D
    pass


class Position3DType(BaseDelegatingExtensionType):
    _TYPE_NAME = "rerun.components.Position3D"
    _DELEGATED_EXTENSION_TYPE = datatypes.Vec3DType


class Position3DArray(BaseDelegatingExtensionArray[datatypes.Vec3DArrayLike]):
    _EXTENSION_NAME = "rerun.components.Position3D"
    _EXTENSION_TYPE = Position3DType
    _DELEGATED_ARRAY_TYPE = datatypes.Vec3DArray


Position3DType._ARRAY_TYPE = Position3DArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(Position3DType())
