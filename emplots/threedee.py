from mayavi import mlab
import numpy as np

from .helpers import x_from_spherical, y_from_spherical, z_from_spherical

pi  = np.pi
cos = np.cos
sin = np.sin

def plot(r, theta, phi):
    """ Generates a 3D plot of a radiation pattern.

    :param r: r components of magnitude vector
    :type r: numpy.ndarray
    :param theta: theta components of magnitude vector
    :type theta: numpy.ndarray
    :param phi: phi components of magnitude vector
    :type phi: numpy.ndarray

    :returns: mayavi figure
    """
    # normalize and convert to dB
    r0 = r / np.amax(r)
    r_dB = 10*np.log10(abs(r0))
    r_dB[r_dB<-40] = -40
    r_dB = r_dB + 40

    x = x_from_spherical(r_dB, theta, phi)
    y = y_from_spherical(r_dB, theta, phi)
    z = z_from_spherical(r_dB, theta)

    scene = mlab.figure(1, bgcolor=(1,1,1), fgcolor=(0,0,0))
    mlab.clf()

    obj = mlab.mesh(x, y, z, scalars=r_dB, colormap='jet')

    obj.enable_contours = True
    obj.contour.filled_contours = True
    obj.contour.number_of_contours = 20

    return scene

def show():
    mlab.show()
