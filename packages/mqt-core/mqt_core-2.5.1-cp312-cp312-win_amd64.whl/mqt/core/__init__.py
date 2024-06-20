"""MQT Core - The Backbone of the Munich Quantum Toolkit."""

from __future__ import annotations


# start delvewheel patch
def _delvewheel_patch_1_6_0():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'mqt_core.libs'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_6_0()
del _delvewheel_patch_1_6_0
# end delvewheel patch

from ._core import Permutation, QuantumComputation
from ._version import version as __version__
from ._version import version_tuple as version_info

__all__ = [
    "Permutation",
    "QuantumComputation",
    "__version__",
    "version_info",
]

for cls in (Permutation, QuantumComputation):
    cls.__module__ = "mqt.core"
del cls
