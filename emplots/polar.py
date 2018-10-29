import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def plot(axes=None, angles=None, magnitudes=None, csv_file=None, normalize=True, convertToDb=True, **kwargs):
    """Takes in a number of different possible arguments and generates a plot.

    :param axes: The axis on which the plot will be generated. If None is passed, a new axis will be generated
    :type axes: matplotlib.axes.Axes
    :param angles: The angles over which there is data (The independent variable)
    :type angles: array-like
    :param magnitudes: The magnitudes of the radiation pattern
    :type magnitudes: array-like
    :csv_file: The path to a csv_file containing data to plot
    :type csv_file: str or path

    :param kwargs:
        *kwargs* are those expected by matplotlib. In this way, you can specify
        all the line properties you can pass to matplotlib's plot function.
        For example if you pass `color='black'`, this will get passed to the
        underlying matplotlib function and the line color will be black. Consult
        matplotlibs documentation for more information.
    :type kwargs: `matplotlib.axes.Line2D`

    :returns: matplotlib.axes.Axes -- The axes with the newly generated plot.
    :raises: ValueError
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
        fig = _plot_magnitude(axes, angles, magnitudes, normalize, convertToDb, **kwargs)

    return fig

def _plot_from_csv(csv_file):
    """Takes a csv file and generates a radiation pattern

    :param csv_file: path to csv file containing data to be plotted

    :returns: matplotlib.axes.Axes -- The axes with the newly generated plot.
        Returns the axes passed to the function. If no axes was passed, a new axes is created and returned
    """
    # TODO
    pass

def _plot_magnitude(ax, angles, magnitudes, normalize, convertToDb, **kwargs):
    """Takes two array like objects of equal dimension and generates a radiation pattern

    :param ax: The axis on which the plot will be generated
    :type ax: matplotlib.axes.Axes
    :param angles: The angles over which there is data (The independent variable)
    :type angles: array-like
    :param magnitudes: The magnitudes of the radiation pattern
    :type magnitudes: array-like
    :param normalize: This function expects to have to normalize the data passed to it. If the
        data is already normalized, pass False, and the function will leave the
        data as is.
    :type normalize: bool
    :param convertToDb: In addition to expecting to normalize the data passed to it, this
        function also expects to have to convert the magnitudes to dB (after
        normalization). If this is already done, pass False, and the function
        will leave the data as is.
    :type convertToDb: bool

    :param kwargs: kwargs are those expected by matplotlib. In this way, you can specify
        all the line properties you can pass to matplotlib's plot function.
        For example if you pass `color='black'`, this will get passed to the
        underlying matplotlib function and the line color will be black. Consult
        matplotlibs documentation for more information.
    :type kwargs: matplotlib.axes.Line2D

    :returns: matplotlib.axes.Axes -- The axes with the newly generated plot.
    :raises: ValueError
    """

    if len(angles) != len(magnitudes):
        raise ValueError("Array lengths must be equal")

    normalizedMagnitudes = magnitudes
    dbMagnitudes = magnitudes
    if normalize:
        normalizedMagnitudes = magnitudes / np.amax(magnitudes)
    if convertToDb:
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
