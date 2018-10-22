import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

pi = np.pi

def plot(axes=None, angles=None, magnitudes=None, csv_file=None):
    """Takes in a number of different possible arguments and generates a plot.
    """

    if angles is None and magnitudes is None and csv_file is None:
        raise ValueError("Must pass something to the function")
    if (csv_file is not None) and (angles is not None or magnitudes is not None):
        raise ValueError("Cannont pass both a csv file and angles or magnitudes")
    if (
        (csv_file is None) and
        (angles is not None and magnitudes is None) or
        (angles is None and magnitudes is not None)
       ):
        raise ValueError("Must pass both angles and magnitude")

    if csv_file:
        pass
    else:
        ax = _plot_magnitude(axes, angles, magnitudes)

    return ax

def _plot_from_csv(csv_file):
    """Takes a csv file and generates a radiation pattern
    """

def _plot_magnitude(ax, angles=None, magnitudes=None):
    """Takes two array like objects of equal dimension and generates a radiation pattern

    This function takes raw magnitude values, normalizes them, then converts
    to dB. It then plots them on a new subplot which is then returned from the
    function.
    """

    if len(angles) != len(magnitudes):
        raise ValueError("Array lengths must be equal")

    normalizedMagnitudes = magnitudes / np.amax(magnitudes)
    dbMagnitudes = 10 * np.log10(abs(normalizedMagnitudes))

    # rearrange so that 0 is at the center of the graph
    centeredAngles = angles - pi

    if ax is None:
        ax = plt.gca()

    fig = ax.plot(centeredAngles, dbMagnitudes)
    ax.grid(True)

    unit = 0.25
    x_tick = np.arange(-1, 1+unit, unit)
    x_label = [r"$-\pi$", r"$-\frac{3\pi}{4}$", r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$"]
    ax.set_xticks(x_tick*pi)
    ax.set_xticklabels(x_label, fontsize=20)
    ax.set_xlim([-pi, pi])
    ax.set_xlabel("Angle [rad]", fontsize=20)

    ax.set_ylim([-40, 0])
    ax.set_ylabel("Directivity [dBi]", fontsize=20)

    return fig
