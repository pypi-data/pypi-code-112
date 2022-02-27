#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  This file is part of the `pypath` python module
#
#  Copyright
#  2014-2022
#  EMBL, EMBL-EBI, Uniklinik RWTH Aachen, Heidelberg University
#
#  Authors: Dénes Türei (turei.denes@gmail.com)
#           Nicolàs Palacio
#           Olga Ivanova
#           Sebastian Lobentanzer
#           Ahmet Rifaioglu
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: http://pypath.omnipathdb.org/
#

import collections

import pypath.resources.urls as urls
import pypath.share.curl as curl


def laudanna_directions():
    """
    Downloads and processes the SignalingFlow edge attributes
    from Laudanna Lab.
    Returns list of directions.
    """

    LaudannaDirection = collections.namedtuple(
        'LaudannaDirection',
        (
            'source_genesymbol',
            'target_genesymbol',
        ),
    )

    url = urls.urls['laudanna']['sigflow_rescued']
    c = curl.Curl(url, silent = False)
    data = c.result
    data = data.split('\n')[1:]
    directions = []

    for l in data:

        if l:

            directions.append(
                LaudannaDirection(
                    *l.split('=')[0].strip().split(' (pp) ')
                )
            )

    return directions


def laudanna_effects():
    """
    Downloads and processes the SignalingDirection edge attributes
    from Laudanna Lab.
    Returns list of effects.
    """

    LaudannaEffect = collections.namedtuple(
        'LaudannaEffect',
        (
            'source_genesymbol',
            'target_genesymbol',
            'effect',
        ),
    )

    url = urls.urls['laudanna']['sigdir_rescued']
    c = curl.Curl(url, silent = False)
    data = c.result
    data = data.split('\n')[1:]
    effects = []

    for l in data:

        if l:

            l = l.split('=')
            effects.append(
                LaudannaEffect(
                    *(
                        l[0].strip().split(' (pp) ') +
                        [l[1].strip()]
                    )
                )
            )

    return effects
