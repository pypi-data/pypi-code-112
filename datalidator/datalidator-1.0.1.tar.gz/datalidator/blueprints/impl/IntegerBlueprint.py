#!/bin/false

# Copyright (c) 2022 Vít Labuda. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
#     disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#     following disclaimer in the documentation and/or other materials provided with the distribution.
#  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
#     products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from typing import final, Any, Final, Tuple, Type, Optional
from datalidator.blueprints.DefaultBlueprintWithModeSupportImplBase import DefaultBlueprintWithModeSupportImplBase


__all__ = "IntegerBlueprint",


class IntegerBlueprint(DefaultBlueprintWithModeSupportImplBase[int]):
    """
    INPUT in loose mode:
    - any object that can be passed to int()

    INPUT in rational mode:
    - 'int' object
    - 'float' object
    - 'bool' object
    - 'str' object containing a numeric value

    INPUT in strict mode:
    - 'int' object

    OUTPUT:
    - 'int' object
    """

    __slots__ = ()

    # The rationality of 'bool' being converted to 'int' can be controversial
    __RATIONAL_MODE_DATA_TYPE_ALLOWLIST: Final[Tuple[Type, ...]] = (int, float, bool, str)
    __STRICT_MODE_DATA_TYPE_ALLOWLIST: Final[Tuple[Type, ...]] = (int,)

    def _get_allowed_output_data_types(self) -> Optional[Tuple[Type, ...]]:
        return int,

    def _parse_in_loose_mode(self, input_data: Any) -> int:
        return self.__convert_input_data_to_int(input_data)

    def _parse_in_rational_mode(self, input_data: Any) -> int:
        return self._data_conversion_helper.convert_input_with_data_type_allowlist(
            self.__convert_input_data_to_int, self.__class__.__RATIONAL_MODE_DATA_TYPE_ALLOWLIST, input_data
        )

    def _parse_in_strict_mode(self, input_data: Any) -> int:
        return self._data_conversion_helper.convert_input_with_data_type_allowlist(
            self.__convert_input_data_to_int, self.__class__.__STRICT_MODE_DATA_TYPE_ALLOWLIST, input_data
        )

    @final
    def __convert_input_data_to_int(self, input_data: Any) -> int:
        try:
            # If a string is converted to integer, initial and trailing whitespace is automatically stripped from it
            #  (standard behaviour of the int() class)
            return int(input_data)
        except Exception:  # Can be TypeError, ValueError, ...
            raise self._invalid_input_data_exc_factory.generate_input_data_not_convertible_exc((int,), input_data)
