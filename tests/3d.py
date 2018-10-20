from context import emplots
from emplots import threedee
import numpy as np
from mayavi import mlab

pi = np.pi
eta = 120 * pi
sin = np.sin
cos = np.cos

phi, theta = np.mgrid[0:pi:201j, 0:2*pi:201j]

r = eta/(8*pi**2) * (sin(theta) ** 3)

fig = threedee.plot(r, theta, phi)
mlab.title(figure=fig, text="This is a title")
threedee.show()
