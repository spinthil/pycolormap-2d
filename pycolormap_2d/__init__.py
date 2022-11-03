"""
pycolormap_2d
~~~~~~~~~~~~~

The PyColorMap 2D package, mapping 2D coordinates to colors sampled from
different 2D color maps.
"""

from .colormap_2d import (BaseColorMap2D, ColorMap2DBremm,
                          ColorMap2DCubeDiagonal, ColorMap2DSchumann,
                          ColorMap2DTeuling2, ColorMap2DSteiger,
                          ColorMap2DZiegler)

__all__ = ['BaseColorMap2D', 'ColorMap2DBremm', 'ColorMap2DCubeDiagonal',
           'ColorMap2DSchumann', 'ColorMap2DTeuling2', 'ColorMap2DSteiger',
           'ColorMap2DZiegler']
