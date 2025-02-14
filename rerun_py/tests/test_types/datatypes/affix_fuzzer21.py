# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/testing/datatypes/fuzzy.fbs".

# You can extend this class by creating a "AffixFuzzer21Ext" class in "affix_fuzzer21_ext.py".

from __future__ import annotations

from typing import Sequence, Union

import numpy as np
import numpy.typing as npt
import pyarrow as pa
from attrs import define, field
from rerun._baseclasses import (
    BaseExtensionArray,
    BaseExtensionType,
)
from rerun._converters import (
    to_np_float16,
)

__all__ = ["AffixFuzzer21", "AffixFuzzer21Array", "AffixFuzzer21ArrayLike", "AffixFuzzer21Like", "AffixFuzzer21Type"]


@define
class AffixFuzzer21:
    # You can define your own __init__ function as a member of AffixFuzzer21Ext in affix_fuzzer21_ext.py

    single_half: float = field(converter=float)
    many_halves: npt.NDArray[np.float16] = field(converter=to_np_float16)


AffixFuzzer21Like = AffixFuzzer21
AffixFuzzer21ArrayLike = Union[
    AffixFuzzer21,
    Sequence[AffixFuzzer21Like],
]


# --- Arrow support ---


class AffixFuzzer21Type(BaseExtensionType):
    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.struct(
                [
                    pa.field("single_half", pa.float16(), nullable=False, metadata={}),
                    pa.field(
                        "many_halves",
                        pa.list_(pa.field("item", pa.float16(), nullable=False, metadata={})),
                        nullable=False,
                        metadata={},
                    ),
                ]
            ),
            "rerun.testing.datatypes.AffixFuzzer21",
        )


class AffixFuzzer21Array(BaseExtensionArray[AffixFuzzer21ArrayLike]):
    _EXTENSION_NAME = "rerun.testing.datatypes.AffixFuzzer21"
    _EXTENSION_TYPE = AffixFuzzer21Type

    @staticmethod
    def _native_to_pa_array(data: AffixFuzzer21ArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError  # You need to implement native_to_pa_array_override in affix_fuzzer21_ext.py


AffixFuzzer21Type._ARRAY_TYPE = AffixFuzzer21Array

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(AffixFuzzer21Type())
