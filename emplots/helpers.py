import numpy as np

sin = np.sin
cos = np.cos

pi = np.pi

def x_from_spherical(r, theta, phi):
    return r * sin(theta) * cos(phi)

def y_from_spherical(r, theta, phi):
    return r * sin(theta) * sin(phi)

def z_from_spherical(r,theta):
    return r * cos(theta)

def rad_to_deg(radians):
    return radians * 180 / pi

def deg_to_rad(degrees):
    return degrees * pi / 180
