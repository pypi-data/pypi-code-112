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


from typing import Sequence, Generic, TypeVar
from datalidator.validators.DefaultValidatorImplBase import DefaultValidatorImplBase


__all__ = "SequenceHasAllItemsUniqueValidator", "SequenceHasAllItemsUniqueValidator_T"
SequenceHasAllItemsUniqueValidator_T = TypeVar("SequenceHasAllItemsUniqueValidator_T", Sequence, str)


class SequenceHasAllItemsUniqueValidator(DefaultValidatorImplBase[SequenceHasAllItemsUniqueValidator_T], Generic[SequenceHasAllItemsUniqueValidator_T]):
    """
    The input sequence is valid if all of its items are unique.
    """

    __slots__ = ()

    def _validate(self, data: SequenceHasAllItemsUniqueValidator_T) -> None:
        # len(data) != len(set(data)) --> This would not work in all cases, because it would require all the sequence's
        #  items to be Hashable!

        for item in data:
            if data.count(item) != 1:
                raise self._generate_data_validation_failed_exc("The input sequence contains a duplicate item: {}".format(repr(item)))
