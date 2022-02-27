#!/usr/bin/env python
# cardinal_pythonlib/pyramid/constants.py

"""
===============================================================================

    Original code copyright (C) 2009-2021 Rudolf Cardinal (rudolf@pobox.com).

    This file is part of cardinal_pythonlib.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

===============================================================================

Constants for Pyramid.

"""

from typing import Callable

# noinspection PyUnresolvedReferences
from pyramid.request import Request
# noinspection PyUnresolvedReferences
from pyramid.response import Response


# =============================================================================
# Type constants
# =============================================================================

PyramidHandlerType = Callable[[Request], Response]
