from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("fixposition")
except PackageNotFoundError:  # pragma: no cover
    # Package is not installed, and therefore, version is unknown.
    __version__ = "0.0.0+unknown"
