from __future__ import annotations

from typing import TYPE_CHECKING, Iterable, cast

import numpy as np
import pyarrow as pa

from .._unions import build_dense_union, union_discriminant_type

if TYPE_CHECKING:
    from ..log import ComponentBatchLike
    from . import (
        Mat3x3,
        Rotation3D,
        Scale3D,
        Transform3DArrayLike,
        TranslationAndMat3x3,
        TranslationRotationScale3D,
        Vec3D,
    )


class Transform3DExt:
    @staticmethod
    def native_to_pa_array_override(data: Transform3DArrayLike, data_type: pa.DataType) -> pa.Array:
        from . import Transform3D, TranslationAndMat3x3, TranslationRotationScale3D

        if isinstance(data, Transform3D):
            data = data.inner

        if isinstance(data, TranslationAndMat3x3):
            discriminant = "TranslationAndMat3x3"
            repr_type = union_discriminant_type(data_type, discriminant)
            transform_repr = _build_struct_array_from_translation_mat3x3(data, cast(pa.StructType, repr_type))
        elif isinstance(data, TranslationRotationScale3D):
            discriminant = "TranslationRotationScale"
            repr_type = union_discriminant_type(data_type, discriminant)
            transform_repr = _build_struct_array_from_translation_rotation_scale(data, cast(pa.StructType, repr_type))
        else:
            raise ValueError(
                f"unknown transform 3d value: {data} (expected `Transform3D`, `TranslationAndMat3x3`, or "
                "`TranslationRotationScale`"
            )

        storage = build_dense_union(data_type, discriminant, transform_repr)

        # TODO(clement) enable extension type wrapper
        # return cast(Transform3DArray, pa.ExtensionArray.from_storage(Transform3DType(), storage))
        return storage

    # Implement the ArchetypeLike
    def as_component_batches(self) -> Iterable[ComponentBatchLike]:
        from ..archetypes import Transform3D

        return Transform3D(self).as_component_batches()

    def num_instances(self) -> int:
        # Always a mono-component
        return 1


# TODO(#2623): lots of boilerplate here that could be auto-generated
# To address that:
# 1) rewrite everything in the form of `xxx__native_to_pa_array_override()`
# 2) higher level `xxx__native_to_pa_array_override()` should call into lower level `xxx::from_similar()`
# 3) identify regularities and auto-gen them


def _build_union_array_from_scale(scale: Scale3D | None, type_: pa.DenseUnionType) -> pa.Array:
    from . import Vec3D

    if scale is None:
        scale_discriminant = "_null_markers"
        scale_pa_arr = pa.nulls(1, pa.null())
        return build_dense_union(type_, scale_discriminant, scale_pa_arr)

    scale_arm = scale.inner

    if np.isscalar(scale_arm):
        scale_discriminant = "Uniform"
        scale_pa_arr = pa.array([scale_arm], type=pa.float32())
    else:
        scale_discriminant = "ThreeD"
        scale_pa_arr = pa.FixedSizeListArray.from_arrays(
            cast(Vec3D, scale_arm).xyz, type=union_discriminant_type(type_, scale_discriminant)
        )

    return build_dense_union(type_, scale_discriminant, scale_pa_arr)


def _optional_mat3x3_to_arrow(mat: Mat3x3 | None) -> pa.Array:
    from . import Mat3x3Array, Mat3x3Type

    if mat is None:
        return pa.nulls(1, Mat3x3Type().storage_type)
    else:
        return Mat3x3Array._native_to_pa_array(mat, Mat3x3Type().storage_type)


def _optional_translation_to_arrow(translation: Vec3D | None) -> pa.Array:
    from . import Vec3DType

    if translation is None:
        return pa.nulls(1, Vec3DType().storage_type)
    else:
        return pa.FixedSizeListArray.from_arrays(translation.xyz, type=Vec3DType().storage_type)


def _optional_rotation_to_arrow(rotation: Rotation3D | None, storage_type: pa.DataType) -> pa.Array:
    from . import Rotation3DArray

    if rotation is None:
        return pa.nulls(1, storage_type)
    else:
        return Rotation3DArray._native_to_pa_array(rotation, storage_type)


def _build_struct_array_from_translation_mat3x3(
    translation_mat3: TranslationAndMat3x3, type_: pa.StructType
) -> pa.StructArray:
    translation = _optional_translation_to_arrow(translation_mat3.translation)
    matrix = _optional_mat3x3_to_arrow(translation_mat3.matrix)

    return pa.StructArray.from_arrays(
        [
            translation,
            matrix,
            pa.array([translation_mat3.from_parent], type=pa.bool_()),
        ],
        fields=list(type_),
    )


def _build_struct_array_from_translation_rotation_scale(
    transform: TranslationRotationScale3D, type_: pa.StructType
) -> pa.StructArray:
    translation = _optional_translation_to_arrow(transform.translation)
    rotation = _optional_rotation_to_arrow(transform.rotation, type_["rotation"].type)
    scale = _build_union_array_from_scale(transform.scale, type_["scale"].type)

    return pa.StructArray.from_arrays(
        [
            translation,
            rotation,
            scale,
            pa.array([transform.from_parent], type=pa.bool_()),
        ],
        fields=list(type_),
    )
