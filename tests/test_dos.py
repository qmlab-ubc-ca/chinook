import numpy as np
import pytest
from numpy.testing import assert_allclose

from chinook.dos import proj_mat


def test_proj_mat_2d_float_weights():
    # Issue #24: Nx2 array with float weights promoted the whole array to float,
    # causing IndexError when used as indices.
    proj = np.array([[0, 0.3], [1, 0.7]])
    lenbasis = 2
    mat = proj_mat(proj, lenbasis)

    norm = np.sqrt(0.3**2 + 0.7**2)
    expected = np.diag([0.3 / norm, 0.7 / norm])
    assert_allclose(mat, expected)


def test_proj_mat_1d_indices():
    proj = np.array([0, 2])
    lenbasis = 4
    mat = proj_mat(proj, lenbasis)

    expected = np.zeros((4, 4), dtype=complex)
    val = 1.0 / np.sqrt(2)
    expected[0, 0] = val
    expected[2, 2] = val
    assert_allclose(mat, expected)


def test_proj_mat_invalid_non_integer_indices():
    with pytest.raises(ValueError, match="Orbital indices must be integers"):
        proj_mat(np.array([[0.5, 0.3]]), 2)

    with pytest.raises(ValueError, match="Orbital indices must be integers"):
        proj_mat(np.array([0.5, 1.0]), 2)


def test_proj_mat_out_of_bounds_index():
    with pytest.raises(IndexError):
        proj_mat(np.array([[5, 0.3]]), 2)
