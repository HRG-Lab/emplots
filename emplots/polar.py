import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

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

    fig = None

    if csv_file:
        pass
    else:
        fig = _plot_magnitude(axes, angles, magnitudes)

    return fig

def _plot_from_csv(csv_file):
    """Takes a csv file and generates a radiation pattern
    """

def _plot_magnitude(ax, angles=None, magnitudes=None):
    """Takes two array like objects of equal dimension and generates a radiation pattern

    This function takes raw magnitude values, normalizes them, then converts
    to dB. It then plots them on the given axes, or a new one if None is passed
    function.
    """

    if len(angles) != len(magnitudes):
        raise ValueError("Array lengths must be equal")

    normalizedMagnitudes = magnitudes / np.amax(magnitudes)
    dbMagnitudes = 10 * np.log10(abs(normalizedMagnitudes))

    if ax is None:
        ax = plt.gca(projection='polar')

    fig = ax.plot(angles, dbMagnitudes)
    ax.set_rmax(0)
    ax.set_rmin(-40)
    ax.set_rticks([-40, -30, -20, -10, 0])
    ax.set_rlabel_position(-22.5)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.grid(True)

    return fig
