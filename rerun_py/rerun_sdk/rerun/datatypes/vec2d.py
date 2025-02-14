# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/datatypes/vec2d.fbs".

# You can extend this class by creating a "Vec2DExt" class in "vec2d_ext.py".

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Sequence, Union

import numpy as np
import numpy.typing as npt
import pyarrow as pa
from attrs import define, field

from .._baseclasses import (
    BaseExtensionArray,
    BaseExtensionType,
)
from .._converters import (
    to_np_float32,
)
from .vec2d_ext import Vec2DExt

__all__ = ["Vec2D", "Vec2DArray", "Vec2DArrayLike", "Vec2DLike", "Vec2DType"]


@define
class Vec2D(Vec2DExt):
    """A vector in 2D space."""

    # You can define your own __init__ function as a member of Vec2DExt in vec2d_ext.py

    xy: npt.NDArray[np.float32] = field(converter=to_np_float32)

    def __array__(self, dtype: npt.DTypeLike = None) -> npt.NDArray[Any]:
        # You can define your own __array__ function as a member of Vec2DExt in vec2d_ext.py
        return np.asarray(self.xy, dtype=dtype)


if TYPE_CHECKING:
    Vec2DLike = Union[Vec2D, npt.NDArray[Any], npt.ArrayLike, Sequence[float]]
else:
    Vec2DLike = Any

Vec2DArrayLike = Union[
    Vec2D, Sequence[Vec2DLike], npt.NDArray[Any], npt.ArrayLike, Sequence[Sequence[float]], Sequence[float]
]


# --- Arrow support ---


class Vec2DType(BaseExtensionType):
    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self, pa.list_(pa.field("item", pa.float32(), nullable=False, metadata={}), 2), "rerun.datatypes.Vec2D"
        )


class Vec2DArray(BaseExtensionArray[Vec2DArrayLike]):
    _EXTENSION_NAME = "rerun.datatypes.Vec2D"
    _EXTENSION_TYPE = Vec2DType

    @staticmethod
    def _native_to_pa_array(data: Vec2DArrayLike, data_type: pa.DataType) -> pa.Array:
        return Vec2DExt.native_to_pa_array_override(data, data_type)


Vec2DType._ARRAY_TYPE = Vec2DArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(Vec2DType())
