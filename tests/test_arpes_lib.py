from types import SimpleNamespace

from numpy.testing import assert_allclose

from chinook.ARPES_lib import experiment


def test_missing_orbital_scaling_preserves_global_scaling():
    tb = SimpleNamespace(basis=[SimpleNamespace(spin=1)])
    arpes = experiment(tb, {
        'cube': {'X': [-1, 1], 'Y': [-1, 1], 'E': [-1, 1]},
        'hv': 21.2,
        'resolution': {'E': 0.01, 'k': 0.01},
        'SE': None,
        'scaling': [1.5],
    })

    assert_allclose(arpes.scaling, [1.5])
    assert_allclose(arpes.scaling_orb, [1.0])
