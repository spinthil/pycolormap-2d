# Colormap 2D Python Package

This package allows to map 2D coordinates to different 2D color maps.

The following color maps are available:

<table>
<tbody>
  <tr>
<td><img src="https://user-images.githubusercontent.com/15887026/184149936-94cb5f32-d072-4517-8d37-697374ecbcbc.png" alt="Bremm" width="100"></td>
<td><img src="https://user-images.githubusercontent.com/15887026/184150013-3d2a8dfc-2d83-4ecb-9151-93939b24cbdc.png" alt="Cube Diagonal" width="100"></td>
<td><img src="https://user-images.githubusercontent.com/15887026/184150040-130322ba-f102-4b3f-8bb9-584c5f594106.png" alt="Schumann" width="100"></td>
<td><img src="https://user-images.githubusercontent.com/15887026/184150056-1366e06a-9ea3-4e8f-8248-aee554555370.png" alt="Steiger" width="100"></td>
<td><img src="https://user-images.githubusercontent.com/15887026/184150078-4fbdd7dc-623b-4add-93a3-805ae21c0239.png" alt="Teuling 2" width="100"></td>
<td><img src="https://user-images.githubusercontent.com/15887026/184150104-d63a70f9-b02e-4637-ab2d-5d4f02af5050.png" alt="Ziegler" width="100"></td>
  </tr>
  <tr>
    <td>ColorMap2DBremm</td>
    <td>ColorMap2DCubeDiagonal</td>
    <td>ColorMap2DSchumann</td>
    <td>ColorMap2DSteiger</td>
    <td>ColorMap2DTeuling2</td>
    <td>ColorMap2DZiegler</td>
  </tr>
</tbody>
</table>

The package is based on 
> M. Steiger, J. Bernard, S. Thum, S. Mittelstädt, M. Hutter, D. A. Keim, and  J. Kohlhammer, “Explorative Analysis of 2D Color Maps,” in _International Conferences in Central Europe on Computer Graphics, Visualization and Computer Vision_, 2015, vol. 23, pp. 151–160.**

For a JavaScript implementation, refer to the [Color2D](https://github.com/dominikjaeckle/Color2D) project by [Dominik Jäckle](http://dominikjaeckle.com/).


## Example

The following example demonstrates how this library is used to map 2D coordinates to colors.

```Python
# Import the Bremm et al. color map class.
from colormap_2d import ColorMap2DBremm

# Create the color map object.
cmap = ColorMap2DBremm()

# Get the color value at relative position [0.2, 0.6].
color = cmap(0.2, 0.6)
```