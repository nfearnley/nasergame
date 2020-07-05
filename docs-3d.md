# Coordinate Spaces

## Model Space

Aliases: *Object Space*, *Local Space*, *Model Coordinate System*, *Object Coordinate System*, *Local Coordinate System*

Origin is relative to model

Model files are stored in this space

### Model Matrix (*Model Space → World Space*)

Aliases: *World Matrix*, *Model Transformation Matrix*, *Model to World*, *Modeling Transform*

**Model Space** is transformed into **World Space** via the **Model Matrix**

## World Space

Aliases: *World Coords*

Origin is relative to the world

### View Matrix (*World Space → View Space*)

Aliases: *Camera Transformation Matrix*, *World to View*, *Camera Transformation*

**World Space** is transformed into **View Space** via the **View Matrix**

Inverse of the Camera's transformation matrix

## View Space

Aliases: *Eye Space*, *Camera Space*, *Eye Coords*

Origin is relative to camera

* `-x, +x` = left, right
* `-y, +y` = down, up
* `-z, +z` = far, near

### Perspective Projection Matrix (*View Space → Projection Space*)

Aliases: *Clip Matrix*, *View to Projection Matrix*, *Projection Transformation*

**View Space** is transformed into **Projection Space** via the **View to Projection Matrix**

Matrix depends on type of projection: Orthographic Projection or Perspective Projection

#### Orthographic Projection

view area is a cuboid

##### Parameters

* width
* height
* near (z-distance from camera, positive)
* far (z-distance from camera, positive)

near must be less than far

w-coordinate remains 1

#### Perspective Projection

view area is a frustum

##### Parameters

* fov
* near (z-distance from camera, positive)
* far (z-distance from camera, positive)

near must be less than far

##### Matrix

* translation (assumed zero)
* 


Sets w-coordinate to prepare for **perspective division**

## Projection Space

Aliases: *Clip Space*, *Canonical View Volume Space*, *Canonical View Volume*

Origin is relative to camera

Cuboid

Dimensions for all visible coordinates are between to -1 and +1

* `-x, +x` = left, right (-1 to +1)
* `-y, +y` = down, up (-1 to +1)
* `-z, +z` = far, near (-1 to +1)

### Viewport Transformation

**Projection Space** is transformed into **Screen Space** via the **Viewport Transformation**

### Screen Space

x, y match screen dimensions

z = near

## GPU Stuff

* **Perspective Division** - Divide each coordinate by w-coordinate
* Clipping vertices outside of cuboid area
* Flattening the image by dropping the z-coordinate
* Remapping (-1 to +1) to (0 to +1) and then scaled to viewport width/height

# Matrices

## Column Vector Notation

![matrix](https://render.githubusercontent.com/render/math?math=\begin{pmatrix}x%5C%5Cy%5C%5Cz%5C%5Cw\end{pmatrix})

## Row Vector Notation

![matrix](https://render.githubusercontent.com/render/math?math=\begin{pmatrix}x%26y%26z%26w\end{pmatrix})

# TODO:

* homogenous vector
* view frustum
* column/row vector notation
* generic matrixes
  * translation
  * scale
  * rotate x-axis
  * rotate y-axis
  * rotate z-axis
* Projection Matrix

# References:

* http://www.codinglabs.net/article_world_view_projection_matrix.aspx
* http://learnwebgl.brown37.net/08_projections/projections_perspective.html
* https://en.wikipedia.org/wiki/Viewing_frustum
