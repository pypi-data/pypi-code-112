# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2022 fetchai
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""
This module contains the support resources for the acn protocol.

It was created with protocol buffer compiler version `libprotoc 3.19.4` and aea version `1.5.0`.
"""

from packages.fetchai.protocols.acn.message import AcnMessage
from packages.fetchai.protocols.acn.serialization import AcnSerializer


AcnMessage.serializer = AcnSerializer
