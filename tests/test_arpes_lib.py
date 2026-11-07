from types import SimpleNamespace

import numpy as np
from numpy.testing import assert_allclose
import pytest

from chinook.ARPES_lib import experiment
from chinook.tilt import k_parallel


class MeshModel:
    basis = [SimpleNamespace(spin=1)]

    def solve_H(self):
        return np.zeros((len(self.Kobj.kpts), 1)), None


@pytest.mark.parametrize("angle", [0.0, 0.8])
@pytest.mark.parametrize("vo", [12.0, -1.0])
def test_angle_mesh_matches_momentum_mesh_at_same_emission_directions(vo, angle):
    hv, work_function, fixed_kz = 100.0, 4.5, 0.25

    def mesh(**grid):
        scan = experiment(MeshModel(), {
            "cube": {**grid, "E": [-0.3, 0.1, 5], "kz": fixed_kz},
            "hv": hv, "W": work_function, "Vo": vo, "angle": angle,
            "resolution": {"E": 0.04, "k": 0.02}, "SE": None,
        })
        scan.diagonalize(True)
        return scan.TB.Kobj.kpts

    x = np.linspace(-0.2, 0.2, 5)
    y = np.linspace(-0.2, 0.2, 3)
    cartesian = mesh(X=[x[0], x[-1], x.size], Y=[y[0], y[-1], y.size])
    vacuum_k = k_parallel(hv - work_function)
    tx = -np.arcsin(x / vacuum_k)
    ty = -np.arcsin(y[:, None] / (vacuum_k * np.cos(tx)))
    columns = [
        mesh(Tx=[theta, theta, 1], Ty=[phi[0], phi[-1], y.size])
        for theta, phi in zip(tx, ty.T)
    ]
    angular = np.stack(columns, axis=1).reshape(-1, 3)

    assert_allclose(angular, cartesian, rtol=0, atol=1e-12)
    if vo > 0:
        assert np.ptp(angular[:, 2]) > 0
    else:
        assert_allclose(angular[:, 2], fixed_kz, rtol=0, atol=1e-12)
