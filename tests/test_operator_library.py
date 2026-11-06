import os
import subprocess
import sys


def test_import_registers_colormaps_without_deprecation():
    subprocess.run(
        [
            sys.executable,
            "-c",
            """
import warnings

from matplotlib import MatplotlibDeprecationWarning
from matplotlib import pyplot as plt

warnings.filterwarnings("error", message=".*register_cmap", category=MatplotlibDeprecationWarning)
import chinook.operator_library

for name in ("Blues", "Greens", "Reds", "Purples", "Greys", "RdBu"):
    assert plt.get_cmap(f"{name}_alpha").name == f"{name}_alpha"
""",
        ],
        env={**os.environ, "MPLBACKEND": "Agg"},
        check=True,
    )
