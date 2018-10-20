import numpy as np

sin = np.sin
cos = np.cos

def x_from_spherical(r, theta, phi):
    return r * sin(theta) * cos(phi)

def y_from_spherical(r, theta, phi):
    return r * sin(theta) * sin(phi)

def z_from_spherical(r,theta):
    return r * cos(theta)
