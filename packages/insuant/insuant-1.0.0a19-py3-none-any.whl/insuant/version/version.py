from importlib import metadata

try:
    __version__ = metadata.version("langflow")
    # Check if the version is a pre-release version
    is_pre_release = any(label in __version__ for label in ["a", "b", "rc", "dev", "post"])
except metadata.PackageNotFoundError:
    __version__ = "1.0.0a19"
    is_pre_release = False
del metadata