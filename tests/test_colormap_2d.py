"""
tests.colormap_2d.py
~~~~~~~~~~~~~~~~~~~~

TODO
Test suite for the pycolormap_2d.py module.
"""
import numpy as np
from nptyping import NDArray, UInt8, Shape

from pycolormap_2d import (ColorMap2DBremm)


class TestColorMap2D:
    """Test suite for ColorMap2D class."""

    def test_colormap_load(self):
        """Test data file load"""
        cmap = ColorMap2DBremm()
        assert isinstance(cmap.get_cmap_data(),
                          NDArray[Shape["512, 512, 3"], UInt8])

    def test_colormap_constructor_type_check(self):
        """Test data file load"""
        try:
            cmap = ColorMap2DBremm(range_x="")
            assert False
        except Exception as e:
            assert type(e) is ValueError

        try:
            cmap = ColorMap2DBremm(range_y="")
            assert False
        except Exception as e:
            assert type(e) is ValueError

        try:
            cmap = ColorMap2DBremm(range_x=(3, ""))
            assert False
        except Exception as e:
            assert type(e) is ValueError

        try:
            cmap = ColorMap2DBremm(range_x=(3, 7, 9))
            assert False
        except Exception as e:
            assert type(e) is ValueError

    def test_colormap_call_result_type(self):
        """Test color map sampling"""
        cmap = ColorMap2DBremm()
        assert isinstance(cmap(0, 0), NDArray[Shape["3"], UInt8])

    def test_colormap_call_result_value(self):
        """Test color map sampling"""
        cmap = ColorMap2DBremm()
        assert np.array_equal(cmap(0, 0), np.array([72, 149, 15]))

    def test_colormap_call_normalized(self):
        """Test color map sampling"""
        cmap = ColorMap2DBremm()
        # Corresponds to pixel coordinates (256, 384)
        assert np.array_equal(cmap(0.5, 0.75), np.array([191, 105, 133]))

    def test_colormap_call_not_normalized(self):
        """Test color map sampling"""
        cmap = ColorMap2DBremm(range_x=(-10, 30), range_y=(1, 11))
        # Corresponds to pixel coordinates (256, 384)
        assert np.array_equal(cmap(10.0, 8.5), np.array([191, 105, 133]))
