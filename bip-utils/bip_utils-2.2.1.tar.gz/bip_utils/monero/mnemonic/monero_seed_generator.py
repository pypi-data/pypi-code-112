# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Module for Monero mnemonic seed generation."""

# Imports
from typing import Optional, Union
from bip_utils.monero.mnemonic.monero_mnemonic import MoneroLanguages, MoneroMnemonicDecoder
from bip_utils.utils.mnemonic import Mnemonic


class MoneroSeedGenerator:
    """
    Monero seed generator class.
    It generates the seed from a mnemonic.
    """

    m_entropy_bytes: bytes

    def __init__(self,
                 mnemonic: Union[str, Mnemonic],
                 lang: Optional[MoneroLanguages] = None) -> None:
        """
        Construct the class.

        Args:
            mnemonic (str or Mnemonic object): Mnemonic
            lang (MoneroLanguages, optional) : Language, None for automatic detection

        Raises:
            ValueError: If the mnemonic is not valid
        """
        self.m_entropy_bytes = MoneroMnemonicDecoder(lang).Decode(mnemonic)

    def Generate(self) -> bytes:
        """
        Generate seed. The seed is simply the entropy bytes in Monero case.
        There is no really need of this method, since the seed is always the same, but it's
        kept in this way to have the same usage of Bip39/Substrate seed generator
        (i.e. MoneroSeedGenerator(mnemonic).Generate() ).

        Returns:
            bytes: Generated seed
        """
        return self.m_entropy_bytes
