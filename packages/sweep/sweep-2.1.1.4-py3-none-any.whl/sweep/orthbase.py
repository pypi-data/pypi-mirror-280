#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .sweep_support.orth import orth
import numpy as np

def orthbase(lin, col, seed=None):
    """
    Generate an orthogonal basis matrix.

    Args:
        lin (int): Number of rows in the matrix.
        col (int): Number of columns in the matrix.
        seed (int, optional): Seed for the random number generator.

    Returns:
        ndarray: Orthogonal basis matrix.
    """
    if seed is not None:
        np.random.seed(seed)

    if lin != col:
        Ro = orth(np.random.rand(lin, col+1))
        mret = Ro[:, 1:]
    else:
        mret = orth(np.random.rand(lin, col))

    return np.array(mret)