from typing import Any, Union

import casadi as cs
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from cycler import cycler
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D

from ..core.data import array2cs

MATLAB_COLORS = [
    "#0072BD",
    "#D95319",
    "#EDB120",
    "#7E2F8E",
    "#77AC30",
    "#4DBEEE",
    "#A2142F",
]


def save2tikz(*figs: Figure) -> None:
    """Saves the figure to a tikz file (`.tex` extension). See
    https://pypi.org/project/tikzplotlib/ for more details.

    Parameters
    ----------
    figs : matplotlib Figures
        One or more matplotlib figures to be converted to tikz files. These
        files will be named based on the number of the corresponding figure.
    """
    import tikzplotlib

    # monkey patching to fix some issues with tikzplotlib
    mpl.lines.Line2D._us_dashSeq = property(lambda self: self._dash_pattern[1])
    mpl.lines.Line2D._us_dashOffset = property(lambda self: self._dash_pattern[0])
    mpl.legend.Legend._ncol = property(lambda self: self._ncols)
    for fig in figs:
        tikzplotlib.save(
            f"figure_{fig.number}.tex",
            figure=fig,
            extra_axis_parameters={r"tick scale binop=\times"},
        )


def spy(
    H: Union[cs.SX, cs.MX, cs.DM, npt.ArrayLike], ax: Axes = None, **spy_kwargs: Any
) -> Union[AxesImage, Line2D]:
    """Equivalent of `matplotlib.pyplot.spy` that works also with casadi
    matrices.

    Parameters
    ----------
    H : casadi SX, MX, DM or array_like
        The matrix to spy.
    ax : Axes, optional
        The axis to draw the result on. If `None`, creates a new axis.
    spy_kwargs
        Other arguments passed directly to `matplotlib.pyplot.spy`.

    Returns
    -------
    AxesImage or Line2D
        Same return types of `matplotlib.pyplot.spy`.
    """
    H = array2cs(H)  # type: ignore[arg-type]
    try:
        # try convert to numerical; if it fails, use symbolic method from cs
        H = np.asarray(H, dtype=float)
    except Exception:
        from contextlib import redirect_stdout
        from io import StringIO

        f = StringIO()
        with redirect_stdout(f):
            H.sparsity().spy()
        out = f.getvalue()
        H = np.asarray(
            [
                list(line)
                for line in out.replace(".", "0").replace("*", "1").splitlines()
            ],
            dtype=int,
        )
    if ax is None:
        _, ax = plt.subplots(1, 1)
    o = ax.spy(H, **spy_kwargs)
    nz = np.count_nonzero(H)
    ax.set_xlabel(f"nz = {nz} ({nz / H.size * 100:.2f}%)")
    return o


def set_mpl_defaults(
    mpl_style: str = "bmh",
    linewidth: float = 1.5,
    markersize: float = 2,
    savefig_dpi: int = 600,
    np_print_precision: int = 4,
    matlab_colors: bool = False,
) -> None:
    """Sets some default parameters for `numpy` and `matplotlib` for printing
    and plotting.

    Parameters
    ----------
    mpl_style : str, optional
        `matplotlib` plotting style, by default 'bmh'.
    linewidth : float, optional
        `matplotlib` default linewidth, by default 1.5.
    markersize : float, optional
        `matplotlib` default markersize, by default 2.
    savefig_dpi : int, optional
        `matplotlib` savefig dpi, by default 600.
    np_print_precision : int, optional
        `numpy` printing precision, by default 4.
    matlab_colors : bool, optional
        Whether `matplotlib` should use Matlab colors for plotting, by default
        `False`.
    """
    np.set_printoptions(precision=np_print_precision)
    mpl.style.use(mpl_style)  # 'seaborn-darkgrid'
    mpl.rcParams["lines.solid_capstyle"] = "round"
    mpl.rcParams["lines.linewidth"] = linewidth
    mpl.rcParams["lines.markersize"] = markersize
    mpl.rcParams["savefig.dpi"] = savefig_dpi
    if matlab_colors:
        mpl.rcParams["axes.prop_cycle"] = cycler("color", MATLAB_COLORS)
