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

import pypath.share.curl as curl
import pypath.resources.urls as urls


def pazar_interactions():

    PazarInteraction = collections.namedtuple(
        'PazarInteraction',
        ('tf', 'target', 'pmid'),
    )

    url = urls.urls['pazar']['url_rescued']
    c = curl.Curl(url, silent = False)
    data = c.result

    return [
        PazarInteraction(*map(x.split('\t').__getitem__, (1, 4, 10)))
        for x in ''.join(data.values()).split('\n')
        if len(x) > 0
    ]
