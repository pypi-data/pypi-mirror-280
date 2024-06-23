from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import numpy as np


def add_ruler(
    fig: Figure,
    disable: bool = False,
    increments: float = 0.1,
    bar_height: float = 0.1,
    color="gray",
    lw: float = 1.0,
    zorder: float = 9,
) -> None:
    """add ruler on figure

    fig : matplotlib.figure.Figure
        draw ruler on the figure
    disable : bool (default: False)
        do nothing if true
    increments: float (default: 0.1 inches)
        increments of ruler in inches
    bar_height: float (default: 0.1 inches)
        bar height in inches
    color: (default: "gray")
        color
    lw: float (default: 1.0)
        line weight
    zorder: float (default: 9.0)
        zorder of ruler

    """

    if disable:
        return

    width_inches, height_inches = fig.get_size_inches()
    for f in np.arange(0.0, width_inches + increments, increments):
        fraction = f / width_inches
        if f.is_integer():
            bar = bar_height / height_inches
        else:
            bar = 0.5 * bar_height / height_inches
        fig.add_artist(Line2D([fraction, fraction], [0, bar], color=color, lw=lw, zorder=zorder))
        fig.add_artist(
            Line2D([fraction, fraction], [1, 1 - bar], color=color, lw=lw, zorder=zorder)
        )

    for f in np.arange(0.0, height_inches + increments, increments):
        fraction = f / height_inches
        if f.is_integer():
            bar = bar_height / width_inches
        else:
            bar = 0.5 * bar_height / width_inches
        fig.add_artist(Line2D([0, bar], [fraction, fraction], color="gray", lw=lw, zorder=zorder))
        fig.add_artist(
            Line2D([1, 1 - bar], [fraction, fraction], color="gray", lw=lw, zorder=zorder)
        )


def add_grid(
    fig: Figure,
    disable: bool = False,
    num_grid: int = 10,
    color="gray",
    lw: float = 1.0,
    ls="dotted",
    zorder: float = 9,
) -> None:
    """add grid on figure

    fig : matplotlib.figure.Figure
        draw grid on the figure
    disable : bool (default: False)
        do nothing if true
    num_grid: int (default: 10)
    color: (default: "gray")
        color
    lw: float (default: 1.0)
        line weight
    ls: (default: dotted)
        line style
    zorder: float (default: 9.0)
        zorder of ruler

    """

    if disable:
        return

    for f in range(1, num_grid):
        fraction = f / num_grid
        fig.add_artist(
            Line2D([fraction, fraction], [0, 1], ls="dotted", color=color, lw=lw, zorder=zorder)
        )
        fig.add_artist(
            Line2D([0, 1], [fraction, fraction], ls="dotted", color=color, lw=lw, zorder=zorder)
        )
