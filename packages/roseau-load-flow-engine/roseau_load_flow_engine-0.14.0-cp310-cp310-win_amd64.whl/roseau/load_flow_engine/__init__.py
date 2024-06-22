"""""" # start delvewheel patch
def _delvewheel_patch_1_7_0():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'roseau_load_flow_engine.libs'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_7_0()
del _delvewheel_patch_1_7_0
# end delvewheel patch

import importlib.metadata

from roseau.load_flow_engine.__about__ import (
    __authors__,
    __copyright__,
    __credits__,
    __email__,
    __license__,
    __maintainer__,
    __status__,
    __url__,
)

__version__ = importlib.metadata.version("roseau_load_flow_engine")

__all__ = [
    "__authors__",
    "__copyright__",
    "__credits__",
    "__email__",
    "__license__",
    "__maintainer__",
    "__status__",
    "__url__",
    "__version__",
]
