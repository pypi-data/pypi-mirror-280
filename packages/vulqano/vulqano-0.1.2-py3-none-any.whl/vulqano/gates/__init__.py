# This code is part of vulqano.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.


"""
Collections of dictionaries for an abstract description of discrete and
continuous (parametric) gates.
"""
from . import (
    discretegates,
    continuousgates,
)

from .discretegates import *
from .continuousgates import *

__all__ = discretegates.__all__.copy()
__all__ += continuousgates.__all__.copy()
