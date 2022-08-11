"""
pycolormap_2d.colormap_2d.py
~~~~~~~~~~~~~~~~

This exaple module contains classes that model economic supply and
demand curves and compute values such as equilibrium prices. 

It also serves as a demonstration for using type annotations and
abstract base classes in developing libraries intended for use in other
projects.
"""

import abc
from typing import Tuple, TypeVar

import numpy as np
import pkg_resources
from nptyping import NDArray, UInt8, Shape

T = TypeVar("T", int, float)


class ColorMap2D(metaclass=abc.ABCMeta):
    """Abstract class for representing economic shock scenarios.

    TODO
    """

    _cmap_data: NDArray[Shape, UInt8]
    _cmap_width: int
    _cmap_height: int
    width: float
    height: float

    def __init__(self, colormap_npy_loc: str, normalize: bool) -> None:
        stream = pkg_resources.resource_stream(__name__, colormap_npy_loc)
        self._cmap_data = np.load(stream)
        self._cmap_width = self._cmap_data.shape[0]
        self._cmap_height = self._cmap_data.shape[1]
        if normalize:
            self.width = 1.0
            self.height = 1.0
        else:
            self.width = self._cmap_width
            self.height = self._cmap_height

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}'

    def __call__(self, x: T, y: T):
        return self.sample(x, y)

    @staticmethod
    def _clamp(v: T, interval: Tuple[T, T] = (0.0, 1.0)):
        return min(interval[1], max(interval[0], v))

    @staticmethod
    def _linearly_scale_value(value: float, from_range: Tuple[float, float], to_range: Tuple[float, float]) -> float:
        return (value - from_range[0]) * (to_range[1] - to_range[0]) / (from_range[1] - from_range[0]) + to_range[0]

    def get_cmap_data(self) -> NDArray[Shape, UInt8]:
        return self._cmap_data.copy()

    def _scale_x(self, x: T):
        return self._linearly_scale_value(x, (0, self.width), (0, self._cmap_width - 1))

    def _scale_y(self, y: T):
        return self._linearly_scale_value(y, (0, self.height), (0, self._cmap_height - 1))

    def sample(self, x: T, y: T):
        image_x = self._clamp(int(round(self._scale_x(x))), (0, self._cmap_width - 1))
        image_y = self._clamp(int(round(self._scale_y(y))), (0, self._cmap_height - 1))

        return self._cmap_data[image_x, image_y, :]


class ColorMap2DBremm(ColorMap2D):
    def __init__(self, normalize: bool = True) -> None:
        super().__init__("data/bremm.npy", normalize)


class ColorMap2DCubeDiagonal(ColorMap2D):
    def __init__(self, normalize: bool = True) -> None:
        super().__init__("data/cubediagonal.npy", normalize)


class ColorMap2DSchumann(ColorMap2D):
    def __init__(self, normalize: bool = True) -> None:
        super().__init__("data/schumann.npy", normalize)


class ColorMap2DSteiger(ColorMap2D):
    def __init__(self, normalize: bool = True) -> None:
        super().__init__("data/steiger.npy", normalize)


class ColorMap2DTeuling2(ColorMap2D):
    def __init__(self, normalize: bool = True) -> None:
        super().__init__("data/teulingfig2.npy", normalize)


class ColorMap2DZiegler(ColorMap2D):
    def __init__(self, normalize: bool = True) -> None:
        super().__init__("data/ziegler.npy", normalize)
