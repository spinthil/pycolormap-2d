"""
tests.colormap_2d.py
~~~~~~~~~~~~~~~~~~~~

TODO
Test suite for the pycolormap_2d.py module.
"""
import numpy as np
import pytest

from pycolormap_2d import (ColorMap2DBremm, ColorMap2DCubeDiagonal,
                           ColorMap2DSchumann, ColorMap2DSteiger,
                           ColorMap2DTeuling2, ColorMap2DZiegler)

# Colors at the (0, 0) and (1, 1) corners of each color map. They pin the
# content of the bundled data files, so a missing or changed file fails.
CMAP_CORNERS = [
    (ColorMap2DBremm, [72, 149, 15], [192, 82, 228]),
    (ColorMap2DCubeDiagonal, [255, 0, 0], [0, 255, 255]),
    (ColorMap2DSchumann, [0, 252, 128], [248, 0, 128]),
    (ColorMap2DSteiger, [230, 218, 0], [0, 44, 255]),
    (ColorMap2DTeuling2, [0, 128, 255], [255, 128, 0]),
    (ColorMap2DZiegler, [255, 255, 0], [0, 0, 255]),
]
CMAP_CLASSES = [corners[0] for corners in CMAP_CORNERS]


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


@pytest.mark.parametrize("cmap_class", CMAP_CLASSES)
class TestAllColorMaps:
    """Tests that run against every color map."""

    def test_colormap_load(self, cmap_class):
        """Test data file load"""
        data = cmap_class().get_cmap_data()
        assert isinstance(data, np.ndarray)
        assert data.shape == (512, 512, 3)
        assert data.dtype == np.uint8

    def test_colormap_call_result_type(self, cmap_class):
        """Test color map sampling"""
        result = cmap_class()(0.3, 0.7)
        assert isinstance(result, np.ndarray)
        assert result.shape == (3,)
        assert result.dtype == np.uint8

    def test_colormap_corners(self, cmap_class):
        """Test that the range corners map to the data corners"""
        cmap = cmap_class()
        data = cmap.get_cmap_data()
        assert np.array_equal(cmap(0, 0), data[0, 0])
        assert np.array_equal(cmap(1, 0), data[-1, 0])
        assert np.array_equal(cmap(0, 1), data[0, -1])
        assert np.array_equal(cmap(1, 1), data[-1, -1])

    def test_colormap_clamps_out_of_range(self, cmap_class):
        """Test that inputs outside the range clamp to the edge"""
        cmap = cmap_class()
        assert np.array_equal(cmap(-5, -5), cmap(0, 0))
        assert np.array_equal(cmap(5, 5), cmap(1, 1))
        assert np.array_equal(cmap(-5, 5), cmap(0, 1))
        assert np.array_equal(cmap(0.5, 5), cmap(0.5, 1))


@pytest.mark.parametrize("cmap_class, color_min, color_max", CMAP_CORNERS)
def test_colormap_corner_values(cmap_class, color_min, color_max):
    """Test the exact colors at the corners of each color map"""
    cmap = cmap_class()
    assert np.array_equal(cmap(0, 0), np.array(color_min))
    assert np.array_equal(cmap(1, 1), np.array(color_max))


class TestColorMap2DSampling:
    """Tests for the mapping from input values to pixels."""

    def test_colormap_reversed_range(self):
        """Test that a reversed range flips the color map"""
        cmap = ColorMap2DBremm(range_x=(1.0, 0.0), range_y=(1.0, 0.0))
        data = cmap.get_cmap_data()
        assert np.array_equal(cmap(0, 0), data[-1, -1])
        assert np.array_equal(cmap(1, 1), data[0, 0])

    def test_colormap_rounds_to_nearest_pixel(self):
        """Test that values between pixels snap to the nearest one"""
        # This range maps input values 1:1 to pixel indices.
        cmap = ColorMap2DBremm(range_x=(0, 511), range_y=(0, 511))
        data = cmap.get_cmap_data()
        assert np.array_equal(cmap(0.4, 0), data[0, 0])
        assert np.array_equal(cmap(0.6, 0), data[1, 0])
        assert np.array_equal(cmap(0, 0.4), data[0, 0])
        assert np.array_equal(cmap(0, 0.6), data[0, 1])

    def test_colormap_sample_matches_call(self):
        """Test that sample() and __call__() return the same color"""
        cmap = ColorMap2DBremm()
        assert np.array_equal(cmap.sample(0.2, 0.6), cmap(0.2, 0.6))


class TestColorMap2DIsolation:
    """Tests that callers can't change the color map data."""

    def test_get_cmap_data_returns_copy(self):
        """Test that changing the returned data leaves the color map as is"""
        cmap = ColorMap2DBremm()
        data = cmap.get_cmap_data()
        data[:] = 0
        assert np.array_equal(cmap(0, 0), np.array([72, 149, 15]))

    def test_sample_returns_copy(self):
        """Test that changing a sampled color leaves the color map as is"""
        cmap = ColorMap2DBremm()
        color = cmap(0, 0)
        color[:] = 0
        assert np.array_equal(cmap(0, 0), np.array([72, 149, 15]))


def test_range_type_error_names_value_type():
    """Test that the error message names the type of the passed value"""
    with pytest.raises(ValueError, match="Instead was list"):
        ColorMap2DBremm(range_x=[0, 1])
