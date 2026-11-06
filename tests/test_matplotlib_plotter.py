from types import SimpleNamespace

import numpy as np
from matplotlib import pyplot as plt

from chinook.matplotlib_plotter import interface


def test_viewer_initializes_with_current_matplotlib(monkeypatch):
    experiment = SimpleNamespace(
        cube=[(-1, 1, 3)] * 3,
        pks=np.array([[0, 1, 1, 0]]),
        spectral=lambda: (None, np.zeros((3, 3, 3))),
    )
    monkeypatch.setattr(plt, "show", lambda: None)

    viewer = interface(experiment)
    try:
        viewer.fig.canvas.draw()
        assert len(viewer.fig.axes) == 5
    finally:
        plt.close(viewer.fig)
