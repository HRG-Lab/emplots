from context import emplots
from emplots import threedee
import numpy as np
from mayavi import mlab

pi = np.pi
eta = 120 * pi
sin = np.sin
cos = np.cos

wavelen = 1
N = 10
C = 0.5
S = 0.13
k = 2*pi/wavelen

phi, theta = np.mgrid[0:pi:201j, 0:2*pi:201j]

def omega(theta):
    return k*S*(cos(theta) - 1) - pi*(2 + 1/N)

def e(theta, phi):
    first = sin(pi / (2*N))
    second = cos(theta)
    num = sin(N*omega(theta) / 2)
    den = sin(omega(theta)/2)
    return first * second * (num/den)

fig = threedee.plot(e(theta, phi), theta, phi)
mlab.title(figure=fig, text="3D plot!!!!")
threedee.show()
