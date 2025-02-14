---
title: Python Quick Start
order: 1
---

## Installing Rerun

The Rerun SDK for Python requires a working installation of [Python-3.8+](https://www.python.org/).

You can install the Rerun SDK using the [rerun-sdk](https://pypi.org/project/rerun-sdk/) pypi package via pip:
```bash
$ pip3 install rerun-sdk
```

You are now ready to start logging and visualizing data.

## Trying out the viewer

The Rerun SDK comes packaged with a simple demo so you can quickly get a feel for the viewer. You can launch it with
```bash
$ python3 -m rerun_demo
```

If everything is installed and working correctly, you should end up with a window like below.
Try looping the recording to see the fun animation.

<picture>
  <source media="(max-width: 480px)" srcset="https://static.rerun.io/6e767ee4d13d9f4ccb887750302ea3934678672f_quickstart0_cube_480w.png">
  <source media="(max-width: 768px)" srcset="https://static.rerun.io/4544950fee5574bbd0fdbd511c2fbbdcf2ca99c9_quickstart0_cube_768w.png">
  <source media="(max-width: 1024px)" srcset="https://static.rerun.io/f1ae7def70ced930795b09a8d84973c3f3859ec4_quickstart0_cube_1024w.png">
  <source media="(max-width: 1200px)" srcset="https://static.rerun.io/14181fab1e3fde320e84727c3804cbc5259b4b93_quickstart0_cube_1200w.png">
  <img src="https://static.rerun.io/770ffcd66ebc020bb0ff00ec123e19f1fcb0a3a4_quickstart0_cube_full.png" alt="colored cube">
</picture>


*Note: If this is your first time launching Rerun you will see a notification in the terminal about the Rerun anonymous
data usage policy. Rerun collects anonymous usage data to help improve the project, though you may choose to opt out if you
would like.*

### If you're having problems
 * Checkout out our [troubleshooting guide](troubleshooting.md).
 * [open an issue](https://github.com/rerun-io/rerun/issues/new/choose).
 * Or [join the Discord server](https://discord.gg/PXtCgFBSmH).

## Using the viewer
Try out the following to interact with the viewer:
 * Click and drag in the main view to rotate the cube.
 * Zoom in and out with the scroll wheel.
 * Mouse over the "?" icons to find out about more controls.
 * Grab the time-slider and move it to see the cube at different time-points.
 * Click the "play" button to animate the cube.
 * Click on the cube to select all of the points.
 * Hover and select individual points to see more information.

This is just a taste of some of what you can do with the viewer. We will cover other functionality in much
more detail later in the [Viewer Walkthrough](viewer-walkthrough.md)

## Logging your own data
Now instead of using a prepackaged demo, let's create some data ourselves. We will start with an
extremely simplified version of this dataset that just logs 1 dimension of points instead of 3.

Create a new python script with the following code:
```python
import rerun as rr  # NOTE: `rerun`, not `rerun-sdk`!
import numpy as np

rr.init("rerun_example_my_data", spawn=True)

positions = np.zeros((10, 3))
positions[:,0] = np.linspace(-10,10,10)

colors = np.zeros((10,3), dtype=np.uint8)
colors[:,0] = np.linspace(0,255,10)

rr.log_points("my_points", positions=positions, colors=colors, radii=0.5)
```

When you run this script you will again be greeted with the [Rerun Viewer](../reference/viewer/overview.md), this time
only showing a simple line of red points.

<picture>
  <source media="(max-width: 480px)" srcset="https://static.rerun.io/a4633eac537a4383a62db88d54c8b9e7260fdd95_quickstart1_line_480w.png">
  <source media="(max-width: 768px)" srcset="https://static.rerun.io/5950b31e3698641b79803cbe61d5160502537bff_quickstart1_line_768w.png">
  <source media="(max-width: 1024px)" srcset="https://static.rerun.io/e274fd2baa46d89365e2e31ee6a2158e00c4ca07_quickstart1_line_1024w.png">
  <source media="(max-width: 1200px)" srcset="https://static.rerun.io/3d0915cfdc86b25ed486693f80f65076e43d57fa_quickstart1_line_1200w.png">
  <img src="https://static.rerun.io/37d42194bc99cbb805e3ca53eba11c2896616893_quickstart1_line_full.png" alt="simple line">
</picture>


The [rr.log_points](https://ref.rerun.io/docs/python/latest/common/spatial_primitives/#rerun.log_points) function can
take any Nx2 or Nx3 numpy array as a collection of positions.

Feel free to modify the code to log a different set of points. If you want to generate the colored cube from the
built-in demo, you can use the following numpy incantation.
```python
import rerun as rr
import numpy as np

rr.init("rerun_example_my_data", spawn=True)

SIZE = 10

pos_grid = np.meshgrid(*[np.linspace(-10, 10, SIZE)]*3)
positions = np.vstack([d.reshape(-1) for d in pos_grid]).T

col_grid = np.meshgrid(*[np.linspace(0, 255, SIZE)]*3)
colors = np.vstack([c.reshape(-1) for c in col_grid]).astype(np.uint8).T

rr.log_points("my_points", positions=positions, colors=colors, radii=0.5)
```

<picture>
  <source media="(max-width: 480px)" srcset="https://static.rerun.io/a624fdd8cd99414f12bb9e05b27d52720a48bd10_quickstart2_simple_cube_480w.png">
  <source media="(max-width: 768px)" srcset="https://static.rerun.io/eee0373668bb90fd6b66c3687012833a136dc969_quickstart2_simple_cube_768w.png">
  <source media="(max-width: 1024px)" srcset="https://static.rerun.io/81da909eb3e44058ac6c67071e2b57490ba6e0ed_quickstart2_simple_cube_1024w.png">
  <source media="(max-width: 1200px)" srcset="https://static.rerun.io/6eb065269db26ff92292c0d4360cd5affc197410_quickstart2_simple_cube_1200w.png">
  <img src="https://static.rerun.io/56b44aef7d6875c222219dcff2bc3a3d470c8891_quickstart2_simple_cube_full.png" alt="">
</picture>

## What's next

If you're ready to move on to more advanced topics, check out the [Viewer Walkthrough](viewer-walkthrough.md) or our
more advanced guide for [Logging Data in Python](logging-python.md) where we will explore the core concepts that make
Rerun tick and log our first non-trivial dataset.

If you'd rather learn from examples, check out the [example gallery](/examples) for some more realistic examples, or browse the [Loggable Data Types](../reference/data_types.md) section for more simple examples of how to use the main  s.
