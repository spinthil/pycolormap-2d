"""
tests.colormap_2d.py
~~~~~~~~~~~~~~~~~~~~

TODO
Test suite for the pycolormap_2d.py module.
"""
import numpy as np

from pycolormap_2d import (ColorMap2DBremm)


class TestColorMap2D:
    """Test suite for ColorMap2D class."""

    def test_colormap_load(self):
        """Test data file load"""
        cmap = ColorMap2DBremm()
        data = cmap.get_cmap_data()
        assert isinstance(data, np.ndarray)
        assert data.shape == (512, 512, 3)
        assert data.dtype == np.uint8

    def test_colormap_constructor_type_check(self):
        """Test data file load"""
        try:
            ColorMap2DBremm(range_x="")
            assert False
        except Exception as e:
            assert type(e) is ValueError

        try:
            ColorMap2DBremm(range_y="")
            assert False
        except Exception as e:
            assert type(e) is ValueError

        try:
            ColorMap2DBremm(range_x=(3, ""))
            assert False
        except Exception as e:
            assert type(e) is ValueError

        try:
            ColorMap2DBremm(range_x=(3, 7, 9))
            assert False
        except Exception as e:
            assert type(e) is ValueError

    def test_colormap_call_result_type(self):
        """Test color map sampling"""
        cmap = ColorMap2DBremm()
        result = cmap(0, 0)
        assert isinstance(result, np.ndarray)
        assert result.shape == (3,)
        assert result.dtype == np.uint8

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
