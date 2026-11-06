import numpy as np
from numpy.testing import assert_allclose

from docs.source.downloads import graphene_backend, input_square


def test_graphene_pz_bands_at_gamma_and_k():
    model, path = graphene_backend.construct_tightbinding(pzonly=True)
    model.solve_H()

    gamma, k = [
        np.argmin(np.linalg.norm(path.kpts - point, axis=1))
        for point in path.pts[:2]
    ]
    # Three nearest-neighbor hoppings add at Gamma and cancel at K.
    assert_allclose(
        model.Eband[[gamma, k]],
        [[-9.65, 8.77], [-0.44, -0.44]],
        rtol=0,
        atol=1e-8,
    )


def test_square_lattice_arpes_intensity():
    # Keep the tutorial's momentum cut and reduce the grid for CI.
    cut = input_square.xmomentum_cut_args
    cube = {**cut["cube"]}
    cube["X"] = [*cube["X"][:2], 9]
    cube["E"] = [*cube["E"][:2], 231]
    _, experiment = input_square.build_ARPES(
        input_square.build_model(), {**cut, "cube": cube}
    )
    _, broadened = experiment.spectral()

    assert broadened.shape == (1, 9, 231)
    # Sample both sides of the cut at -3.5, -2.5, -1.5, and -0.5 eV.
    assert_allclose(
        broadened[0, [1, 3, 5, 7], [50, 100, 150, 200]],
        [3.10270721e-9, 1.30340145e-8, 1.39378201e-8, 1.03072595e-7],
        rtol=1e-5,
        atol=0,
    )
