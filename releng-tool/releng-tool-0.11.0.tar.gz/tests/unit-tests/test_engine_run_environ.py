# -*- coding: utf-8 -*-
# Copyright 2021 releng-tool

from tests import prepare_testenv
from tests import prepare_workdir
import os
import unittest

class TestEngineRunEnviron(unittest.TestCase):

    def run(self, result=None):
        old_env = dict(os.environ)
        try:
            super(TestEngineRunEnviron, self).run(result)
        finally:
            os.environ.clear()
            os.environ.update(old_env)

    def test_engine_run_environ_assets_dir(self):
        with prepare_workdir() as assets_dir:
            os.environ['RELENG_ASSETS_DIR'] = assets_dir

            with prepare_testenv() as engine:
                expected_cache_dir = os.path.join(assets_dir, 'cache')
                expected_dl_dir = os.path.join(assets_dir, 'dl')
                self.assertEqual(engine.opts.cache_dir, expected_cache_dir)
                self.assertEqual(engine.opts.dl_dir, expected_dl_dir)

    def test_engine_run_environ_cache_dir(self):
        with prepare_workdir() as cache_dir:
            os.environ['RELENG_CACHE_DIR'] = cache_dir

            with prepare_testenv() as engine:
                self.assertEqual(engine.opts.cache_dir, cache_dir)

    def test_engine_run_environ_dl_dir(self):
        with prepare_workdir() as dl_dir:
            os.environ['RELENG_DL_DIR'] = dl_dir

            with prepare_testenv() as engine:
                self.assertEqual(engine.opts.dl_dir, dl_dir)
