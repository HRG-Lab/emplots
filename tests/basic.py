from context import emplots
from emplots import polar, rectangular
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
eta = 120 * pi

thetas = np.arange(0, 2*pi, pi/180)

def U(thetas):
    const = eta / (8 * pi ** 2)
    return const * (np.sin(thetas) ** 3)

fig = plt.figure()

ax1 = fig.add_subplot(121, projection='polar')
polar.plot(ax1, angles=thetas, magnitudes=U(thetas))
ax1.set_title("This is a title")

ax2 = fig.add_subplot(122)
rectangular.plot(ax2, angles=thetas, magnitudes=U(thetas))

plt.tight_layout()
plt.show()
