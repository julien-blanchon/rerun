#!/usr/bin/env python3
"""Shows how to implement custom archetypes and components."""
from __future__ import annotations

import argparse
from typing import Any, Iterable

import numpy as np
import numpy.typing as npt
import pyarrow as pa
import rerun as rr  # pip install rerun-sdk
import rerun.experimental as rr2


class ConfidenceBatch(rr2.ComponentBatchLike):
    """A batch of confidence data."""

    def __init__(self: Any, confidence: npt.ArrayLike) -> None:
        self.confidence = confidence

    def component_name(self) -> str:
        """The name of the custom component."""
        return "user.Confidence"

    def as_arrow_batch(self) -> pa.Array:
        """The arrow batch representing the custom component."""
        return pa.array(self.confidence, type=pa.float32())


class CustomPoints3D(rr2.ArchetypeLike):
    def __init__(self: Any, points3d: npt.ArrayLike, confidences: npt.ArrayLike) -> None:
        self.points3d = points3d
        self.confidences = confidences

    def as_component_batches(self) -> Iterable[rr2.ComponentBatchLike]:
        points3d = np.asarray(self.points3d)
        return (
            list(rr2.Points3D(points3d).as_component_batches())  # The components from Points3D
            + [rr2.IndicatorComponentBatch("user.CustomPoints3D", len(points3d))]  # Our custom indicator
            + [ConfidenceBatch(self.confidences)]  # Custom confidence data
        )


def log_custom_data() -> None:
    lin = np.linspace(-5, 5, 3)
    z, y, x = np.meshgrid(lin, lin, lin, indexing="ij")
    point_grid = np.vstack([x.flatten(), y.flatten(), z.flatten()]).T

    rr2.log(
        "left/my_confident_point_cloud",
        CustomPoints3D(
            points3d=point_grid,
            confidences=[42],  # splat
        ),
    )

    rr2.log(
        "right/my_polarized_point_cloud",
        CustomPoints3D(points3d=point_grid, confidences=np.arange(0, len(point_grid))),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Logs rich data using the Rerun SDK.")
    rr.script_add_args(parser)
    args = parser.parse_args()

    rr.script_setup(args, "rerun_example_car")
    log_custom_data()
    rr.script_teardown(args)


if __name__ == "__main__":
    main()
