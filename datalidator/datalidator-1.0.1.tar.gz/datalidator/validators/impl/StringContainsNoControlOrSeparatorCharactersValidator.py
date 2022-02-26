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


from typing import final, Final
import unicodedata
from datalidator.validators.DefaultValidatorImplBase import DefaultValidatorImplBase


__all__ = "StringContainsNoControlOrSeparatorCharactersValidator",


class StringContainsNoControlOrSeparatorCharactersValidator(DefaultValidatorImplBase[str]):
    """
    The input string is valid if it does not contain any control or separator characters, i.e. characters that belong
     to one of the "C" or "Z" Unicode character categories. This includes characters such as space, '\0', '\r', '\n',
     '\b', '\v' and '\f'.

    To make some specific control or separator characters valid, use the 'allowed_characters' initializer argument. By
     default, the following characters are considered valid: space, '\r', '\n', '\t'.
    """

    __slots__ = "__allowed_characters",

    def __init__(self, allowed_characters: str = " \r\n\t", tag: str = ""):
        DefaultValidatorImplBase.__init__(self, tag)

        self.__allowed_characters: Final[str] = allowed_characters

    @final
    def get_allowed_characters(self) -> str:
        return self.__allowed_characters

    def _validate(self, data: str) -> None:
        for char in data:
            if char in self.__allowed_characters:
                continue

            if unicodedata.category(char)[0].upper() in ("C", "Z"):
                raise self._generate_data_validation_failed_exc(
                    "The input string contains an Unicode control or separator character: {}".format(repr(char))
                )
