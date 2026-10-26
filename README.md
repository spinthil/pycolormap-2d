# Colormap 2D Python Package

[![Build](https://github.com/spinthil/pycolormap-2d/actions/workflows/test-lint-publish.yml/badge.svg)](https://github.com/spinthil/pycolormap-2d/actions/workflows/test-lint-publish.yml)
[![PyPI](https://img.shields.io/pypi/v/pycolormap-2d)](https://pypi.org/project/pycolormap-2d/)
[![Docs](https://img.shields.io/badge/docs-pages-blue)](https://tspinner.de/pycolormap-2d/modules.html)
[![Apache 2.0](https://img.shields.io/github/license/spinthil/pycolormap-2d)](https://www.apache.org/licenses/LICENSE-2.0.html)

This package allows to map 2D coordinates to different 2D color maps.

The following color maps are available:

<table>
<tbody>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/15887026/184149936-94cb5f32-d072-4517-8d37-697374ecbcbc.png" alt="Bremm" width="100"></td>
    <td><img src="https://user-images.githubusercontent.com/15887026/184150013-3d2a8dfc-2d83-4ecb-9151-93939b24cbdc.png" alt="Cube Diagonal" width="100"></td>
    <td><img src="https://user-images.githubusercontent.com/15887026/184150040-130322ba-f102-4b3f-8bb9-584c5f594106.png" alt="Schumann" width="100"></td>
  </tr>
  <tr>
    <td>ColorMap2DBremm</td>
    <td>ColorMap2DCubeDiagonal</td>
    <td>ColorMap2DSchumann</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/15887026/184150056-1366e06a-9ea3-4e8f-8248-aee554555370.png" alt="Steiger" width="100"></td>
    <td><img src="https://user-images.githubusercontent.com/15887026/184150078-4fbdd7dc-623b-4add-93a3-805ae21c0239.png" alt="Teuling 2" width="100"></td>
    <td><img src="https://user-images.githubusercontent.com/15887026/184150104-d63a70f9-b02e-4637-ab2d-5d4f02af5050.png" alt="Ziegler" width="100"></td>
  </tr>
  <tr>
    <td>ColorMap2DSteiger</td>
    <td>ColorMap2DTeuling2</td>
    <td>ColorMap2DZiegler</td>
  </tr>
</tbody>
</table>

The package is based on 
> M. Steiger, J. Bernard, S. Thum, S. Mittelstädt, M. Hutter, D. A. Keim, and  J. Kohlhammer, “Explorative Analysis of 2D Color Maps,” in _International Conferences in Central Europe on Computer Graphics, Visualization and Computer Vision_, 2015, vol. 23, pp. 151–160.

For a JavaScript implementation, refer to the [Color2D](https://github.com/dominikjaeckle/Color2D) project by [Dominik Jäckle](http://dominikjaeckle.com/).


## Installation

Install the package from PyPI:

```bash
pip install pycolormap-2d
```

The package needs Python 3.9 or newer. Its only dependency is NumPy.


## Usage

Basic usage with normalized inputs (i.e., x- and y-coordinates ranging from 0 to 1):

```Python
from pycolormap_2d import ColorMap2DBremm

# Create the color map object.
cmap = ColorMap2DBremm()

# Get the color value.
color = cmap(0.2, 0.6)  # array([181, 116,  75], dtype=uint8)
```

The color is a NumPy array with the red, green, and blue values as integers from 0 to 255.

Optionally, ranges for the input x and y input ranges can be passed during object creation:

```Python
from pycolormap_2d import ColorMap2DBremm

# Create the color map object.
cmap = ColorMap2DBremm(range_x=(-10, 30), range_y=(1, 11))

# Get the color value.
color = cmap(10.0, 8.5)
```

Values outside the range are clamped to the nearest edge of the color map. For example, `cmap(-50, 8.5)` returns the same color as `cmap(-10, 8.5)`.

All six color maps share the same interface. Swap `ColorMap2DBremm` for any other class from the table above:

```Python
from pycolormap_2d import ColorMap2DZiegler

cmap = ColorMap2DZiegler()
color = cmap(0.2, 0.6)
```

To get the full color map as an image, use `get_cmap_data()`. It returns a NumPy array of shape `(512, 512, 3)`:

```Python
from pycolormap_2d import ColorMap2DBremm

data = ColorMap2DBremm().get_cmap_data()
```


### Example: coloring a scatter plot

A common use is to color the points of a 2D embedding (e.g., from PCA, t-SNE, or UMAP) by their position. This example uses Matplotlib, which you need to install separately:

```Python
import matplotlib.pyplot as plt
import numpy as np
from pycolormap_2d import ColorMap2DBremm

points = np.random.default_rng(0).normal(size=(500, 2))

# Fit the color map to the extent of the data. The ranges must contain
# Python numbers, so convert the NumPy values with float().
cmap = ColorMap2DBremm(
    range_x=(float(points[:, 0].min()), float(points[:, 0].max())),
    range_y=(float(points[:, 1].min()), float(points[:, 1].max())),
)

# Matplotlib expects RGB values from 0 to 1.
colors = np.array([cmap(x, y) for x, y in points]) / 255

plt.scatter(points[:, 0], points[:, 1], c=colors)
plt.show()
```


## Development

Set up a development environment with [Pipenv](https://pipenv.pypa.io/) and run the checks:

```bash
pipenv sync --dev
pipenv run pip install -e .
pipenv run pytest tests/
pipenv run flake8 pycolormap_2d tests
pipenv run mypy pycolormap_2d
```

The Pipfile pins the development environment to the newest supported Python version, which must be installed.

To run the tests on all supported Python versions, use [tox](https://tox.wiki/). It needs each of these Python versions installed:

```bash
tox
```
