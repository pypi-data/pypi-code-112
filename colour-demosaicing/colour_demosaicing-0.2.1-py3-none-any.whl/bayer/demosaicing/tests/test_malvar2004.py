# !/usr/bin/env python
"""
Defines the unit tests for the
:mod:`colour_demosaicing.bayer.demosaicing.malvar2004` module.
"""

from __future__ import annotations

import numpy as np
import os
import unittest

from colour import read_image

from colour_demosaicing import TESTS_RESOURCES_DIRECTORY
from colour_demosaicing.bayer import demosaicing_CFA_Bayer_Malvar2004

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "BAYER_DIRECTORY",
    "TestDemosaicing_CFA_Bayer_Malvar2004",
]

BAYER_DIRECTORY: str = os.path.join(
    TESTS_RESOURCES_DIRECTORY, "colour_demosaicing", "bayer"
)


class TestDemosaicing_CFA_Bayer_Malvar2004(unittest.TestCase):
    """
    Define :func:`colour_demosaicing.bayer.demosaicing.malvar2004.\
demosaicing_CFA_Bayer_Malvar2004` definition unit tests methods.
    """

    def test_demosaicing_CFA_Bayer_Malvar2004(self):
        """
        Test :func:`colour_demosaicing.bayer.demosaicing.malvar2004.\
demosaicing_CFA_Bayer_Malvar2004` definition.
        """

        for pattern in ("RGGB", "BGGR", "GRBG", "GBRG"):
            CFA = os.path.join(
                BAYER_DIRECTORY, f"Lighthouse_CFA_{pattern}.exr"
            )
            RGB = os.path.join(
                BAYER_DIRECTORY, f"Lighthouse_Malvar2004_{pattern}.exr"
            )

            np.testing.assert_almost_equal(
                demosaicing_CFA_Bayer_Malvar2004(
                    read_image(str(CFA))[..., 0], pattern
                ),
                read_image(str(RGB)),
                decimal=7,
            )


if __name__ == "__main__":
    unittest.main()
