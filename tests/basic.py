from context import emplots
from emplots import polar
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
eta = 120 * pi

thetas = np.arange(0, 2*pi, pi/180)

def U(thetas):
    const = eta / (8 * pi ** 2)
    return const * (np.sin(thetas) ** 3)

polar.plot(angles = thetas, magnitudes = U(thetas))
plt.show()
