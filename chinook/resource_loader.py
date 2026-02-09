import functools
import importlib
import importlib.resources
import pkgutil
import os


@functools.lru_cache(maxsize=8)
def load_text_lines(package: str, resource: str):
    """Load a text resource from a package and return its lines.

    Tries multiple strategies to be compatible with different install types:
    - importlib.resources.read_text
    - importlib.resources.files(...).read_text()
    - pkgutil.get_data
    - filesystem fallback relative to the package __file__

    Caches results to avoid repeated IO.
    """
    # 1) importlib.resources.read_text
    try:
        txt = importlib.resources.read_text(package, resource, encoding="utf-8")
        return txt.splitlines()
    except Exception:
        pass

    # 2) importlib.resources.files (Traversable)
    try:
        trav = importlib.resources.files(package).joinpath(resource)
        return trav.read_text(encoding="utf-8").splitlines()
    except Exception:
        pass

    # 3) pkgutil.get_data (bytes)
    try:
        data = pkgutil.get_data(package, resource)
        if data is not None:
            return data.decode("utf-8").splitlines()
    except Exception:
        pass

    # 4) filesystem fallback relative to package __file__
    try:
        pkg = importlib.import_module(package)
        pkgdir = os.path.dirname(getattr(pkg, "__file__", "") or "")
        path = os.path.join(pkgdir, resource)
        with open(path, encoding="utf-8") as f:
            return f.read().splitlines()
    except Exception as exc:
        raise FileNotFoundError(f"Resource '{resource}' not found in package '{package}': {exc}")
