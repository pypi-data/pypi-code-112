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


def phosphopoint_interactions():

    PhosphopointInteraction = collections.namedtuple(
        'PhosphopointInteraction',
        (
            'source_genesymbol',
            'source_entrez',
            'target_genesymbol',
            'target_entrez',
            'category',
        ),
    )

    url = urls.urls['phosphopoint']['url']
    c = curl.Curl(url, silent = False, large = True)
    _ = next(c.result)

    return [
        PhosphopointInteraction(*l.strip().split(';'))
        for l in c.result
    ]


def phosphopoint_directions():

    return [
        (l[0], l[2])
        for l in phosphopoint_interactions()
    ]
