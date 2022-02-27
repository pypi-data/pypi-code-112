###############################################################################
# (c) Copyright 2021 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
import json
import os
from pathlib import Path

import pytest
import responses

import apd.cern_sso
from apd.ap_info import cache_ap_info, load_ap_info_from_single_file

DATA_DIR = Path(__file__).parent / "data"
APINFO_PATHS = DATA_DIR / "rds_ap_info.json"
APINFO_MULTIPLEVERSIONS_PATHS = DATA_DIR / "rds_ap_info_2versions.json"


@pytest.fixture
def apinfo():
    """load the requests test data"""
    return load_ap_info_from_single_file(APINFO_PATHS)


@pytest.fixture
def apinfo_multipleversions():
    """load the requests test data"""
    return load_ap_info_from_single_file(APINFO_MULTIPLEVERSIONS_PATHS)


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        with open(APINFO_PATHS) as f:
            data = json.load(f)

        rsps.add(
            responses.GET,
            "https://lbap.app.cern.ch/stable/v1/SL/RDs",
            body=json.dumps(data["info"]),
            status=200,
            content_type="application/json",
        )

        rsps.add(
            responses.GET,
            "https://lbap.app.cern.ch/stable/v1/SL/RDs/tags",
            body=json.dumps(data["tags"]),
            status=200,
            content_type="application/json",
        )

        yield rsps


@pytest.fixture
def apinfo_cache(tmp_path, mocked_responses, monkeypatch):
    """load the requests test data and cache it in a temp dir"""

    def patched_get_sso_token(uri, app, a, b, c):
        return ""

    monkeypatch.setattr(apd.cern_sso, "get_sso_token", patched_get_sso_token)
    cachedir = tmp_path / "cache"
    os.makedirs(cachedir)
    cache_ap_info(cachedir, "SL", "RDs")
    return cachedir


@pytest.fixture
def apd_cache(monkeypatch):
    monkeypatch.setenv(
        "APD_METADATA_CACHE_DIR", str(Path(__file__).parent / "cache-dir")
    )
    yield
