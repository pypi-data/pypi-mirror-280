from itertools import product
from typing import Union

import casadi as cs
import numpy as np
import numpy.typing as npt


def array2cs(x: np.ndarray) -> Union[cs.SX, cs.MX]:
    """Converts numpy array `x` of scalar symbolic variable to a single symbolic
    instance. Opposite to `array2cs`. Note that all entries in `x` must have the same
    type, either SX or MX.

    Parameters
    ----------
    x : np.ndarray
        Array whose entries are either MX or SX. In case `x` is SX, MX or DM, it is
        returned immediately.

    Returns
    -------
    casadi.SX or MX
        A single SX or MX instance whose entries are `x`'s entries.

    Raises
    ------
    ValueError
        Raises if the array is empty (zero dimensions), or if it has more than 2 dims.
    """
    if isinstance(x, (cs.SX, cs.MX, cs.DM)):
        return x
    cls = type(next(x.flat))
    if x.dtype != object or cls is cs.DM:
        return cs.DM(x)  # meaning it is not SX or MX, thus a number
    ndim = x.ndim
    if ndim == 0:
        return x.item()
    elif ndim == 1:
        indices = range(x.shape[0])
        shape = (x.shape[0], 1)
    elif ndim == 2:
        indices = product(  # type: ignore[assignment]
            range(x.shape[0]), range(x.shape[1])
        )
        shape = x.shape  # type: ignore[assignment]
    else:
        raise ValueError("Can only convert 1D and 2D arrays to CasADi SX or MX.")
    m: Union[cs.SX, cs.MX] = cls(*shape)
    for idx in indices:
        m[idx] = x[idx]
    return m


def cs2array(x: Union[cs.MX, cs.SX]) -> npt.NDArray[np.object_]:
    """Converts casadi symbolic variable `x` to a numpy array of scalars. Opposite to
    `array2cs`.

    Inspired by
    https://bitbucket.org/rawlings-group/mpc-tools-casadi/src/master/mpctools/tools.py

    Parameters
    ----------
    x : casadi.SX or MX
        A symbolic variable (with multiple entries).

    Returns
    -------
    np array of cs.SX or MX
        The array containing the symbolic variable scalars.
    """
    if isinstance(x, np.ndarray):
        return x
    if isinstance(x, cs.DM):
        return x.toarray()

    shape = x.shape
    y = np.empty(shape, object)
    indices = product(range(shape[0]), range(shape[1]))
    for idx in indices:
        y[idx] = x[idx]
    return y


def find_index_in_vector(
    V: Union[cs.SX, cs.MX], a: Union[cs.SX, cs.MX]
) -> npt.NDArray[np.int_]:
    """Finds the indices of `a` in `V`.

    Parameters
    ----------
    V : casadi.SX or MX
        The vector in which to search.
    a : casadi.SX or MX
        The vector to search for.

    Returns
    -------
    array of int
        The indices of `a` in `V`.

    Raises
    ------
    ValueError
        Raises if `V` or `a` are not vectors.
    """
    if not V.is_vector() or not a.is_vector():
        raise ValueError("`V` and `a` must be vectors.")

    sp: cs.Sparsity = cs.jacobian_sparsity(a, V)
    idx = np.asarray(sp.get_crs()[1], int)
    if idx.size != a.numel():
        raise RuntimeError("invalid subset: some entries of `a` were not found in `V`")
    return idx
