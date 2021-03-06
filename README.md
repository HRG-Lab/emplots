EM Plots
========

This is a python module meant to help with generating common plots used
in electromagnetics. These plots include:

* Radiation patterns (polar, rectangular, and 3D)
* Others as they come up

For radiation patterns, the idea is you only have to generate your input array
(thetas for example) and your magnitudes. These values can then be passed to
an appropriate plot function. For polar plots, that function is  
`emplots.polar.plot()`, for 3D plots, that function is `emplots.threedee.plot()`.
Each of these (in particular, the 3D plotting function) has its own requirements
in terms of dependencies. These are all imported by the module, however it is
your responsibility to ensure each of these is installed.

Module Requirements
-------------------

For rectangular and polar plots, you must have the following packages installed:

* numpy
* scipy
* matplotlib

For 3D plots, you must have the following packages installed:

* numpy
* scipy
* mayavi

Note: mayavi is particularly annoying to get right. It is recommended you use
anaconda, set up a new environment, and install mayavi in the following way:

```
conda create -n <name of environment> python=3.5 qt=4
conda activate <name of environment>
conda install -c menpo mayavi
```

Setup
-----
The simplest way to use this package is to clone this repository, ensure
the dependencies are met, and run

```
python setup.py install
```

then you can use emplots just like you would any other python package

```python
import emplots
#OR
import emplots.rectangular
#OR
from emplots import threedee
```

Examples
--------

### Rectangular Plot
This example plots the radiation pattern of a have wavelength dipole

```python
from emplots import rectangular
import numpy as np

pi = np.pi
eta = 120 * pi

thetas = np.arange(0, 2*pi, pi/180)

def U(thetas):
    const = eta / (8 * pi ** 2)
    return const * (np.sin(thetas) ** 3)

fig = rectangular.plot(angles, U(thetas))

plt.tight_layout()
plt.show()
```
TODO: add output image

Note: the function polar.plot returns a matplotlib figure. This allows you to
manipulate the figure by adding titles, scaling axes, etc. For example, to
add a title, you would call

```python
fig.set_title("Half-wavelength Dipole")
```

### Polar Plot
This example plots one cutplane of the radiation pattern of a have wavelength dipole

```python
from emplots import polar
import numpy as np

pi = np.pi
eta = 120 * pi

thetas = np.arange(0, 2*pi, pi/180)

def U(thetas):
    const = eta / (8 * pi ** 2)
    return const * (np.sin(thetas) ** 3)

fig = polar.plot(angles = thetas, magnitudes = U(thetas))
plt.show()
```
TODO: add output image

Note: the function polar.plot returns a matplotlib figure. This allows you to
manipulate the figure by adding titles, scaling axes, etc. For example, to
add a title, you would call

```python
fig.set_title("Half-wavelength Dipole")
```

### 3D Plot
This example plots the 3D radiation pattern of a have wavelength dipole

```python
from emplots import threedee
import numpy as np

pi = np.pi
eta = 120 * pi
sin = np.sin
cos = np.cos

phi, theta = np.mgrid[0:pi:201j, 0:2*pi:201j]

r = eta/(8*pi**2) * (sin(theta) ** 3)

fig = threedee.plot(r, theta, phi)
mlab.title(figure=fig, text="This is a title")
threedee.show()

```
TODO: add output image

Note: The function threedee.plot does not return a figure in the same way
polar.plot and rectangular.plot do. This is because threedee.plot uses mayavi
instead of matplotlib. Instead, it returns an mlab.scene object. This can be
manipulated by passing the scene object in functions that do things like add a
title. Also note however that this does require to import mlab. For example:

```python
from mayavi import mlab

...

mlab.title(figure=scene, text="Half-wavelength Dipole")
```
