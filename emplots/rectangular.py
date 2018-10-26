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
        pass # TODO
    else:
        ax = _plot_magnitude(axes, angles, magnitudes)

    return ax

def plot_min_mean_max(ax, angles=None, min=None, mean=None, max=None):
    """
    Plot the minimum, maximum, and average, shading the area between the max and min
    """
    if (min is None) or (mean is None) or (max is None):
        raise ValueError("Must pass all three of min, mean, and max")

    ref_array_len = len(angles)
    if all(len(lst) != ref_array_len for lst in [min, mean, max]):
        raise ValueError("All arrays must be the same length")

    if ax is None:
        ax = plot.gca()

    min_norm_to_mean = min / np.amax(mean)
    max_norm_to_mean = max / np.amax(mean)

    min_dB = 10*np.log10(abs(min_norm_to_mean))
    max_dB = 10*np.log10(abs(max_norm_to_mean))

    _plot_magnitude(ax, angles, min_dB, normalize=False, convertToDb=False, color='blue', label="min")
    _plot_magnitude(ax, angles, mean, color='green', label="mean")
    _plot_magnitude(ax, angles, max_dB, normalize=False, convertToDb=False, color='orange', label="max")

    centered_angles = angles - pi
    # There's some issue in which only having one of these only shades half the graph
    ax.fill_between(centered_angles, min_dB, max_dB, where=min < max, facecolor='green', alpha=0.25)
    ax.fill_between(centered_angles, min_dB, max_dB, where=max <= min, facecolor='green', alpha=0.25)

    return ax

def _plot_from_csv(csv_file):
    """Takes a csv file and generates a radiation pattern
    """
    # TODO
    pass

def _plot_magnitude(ax, angles=None, magnitudes=None, normalize=True, convertToDb=True, **kwargs):
    """Takes two array like objects of equal dimension and generates a radiation pattern

    This function takes raw magnitude values, normalizes them, then converts
    to dB. It then plots them on a new subplot which is then returned from the
    function.
    """

    if len(angles) != len(magnitudes):
        raise ValueError("Array lengths must be equal")

    normalizedMagnitudes = magnitudes
    dbMagnitudes = magnitudes
    if normalize:
        normalizedMagnitudes = magnitudes / np.amax(magnitudes)
    if convertToDb:
        dbMagnitudes = 10 * np.log10(abs(normalizedMagnitudes))

    # rearrange so that 0 is at the center of the graph
    centeredAngles = angles - pi

    if ax is None:
        ax = plt.gca()

    fig = ax.plot(centeredAngles, dbMagnitudes, **kwargs)
    ax.grid(True)

    unit = 0.25
    x_tick = np.arange(-1, 1+unit, unit)
    x_label = [r"$-\pi$", r"$-\frac{3\pi}{4}$", r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$", r"$\pi$"]
    ax.set_xticks(x_tick*pi)
    ax.set_xticklabels(x_label, fontsize=20)
    ax.set_xlim([-pi, pi])
    ax.set_xlabel("Angle [rad]", fontsize=20)

    ax.set_ylim([-40, 0])
    ax.set_ylabel("Directivity [dBi]", fontsize=20)

    return fig
