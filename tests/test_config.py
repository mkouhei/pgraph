# -*- coding: utf-8 -*-
"""pgraph.tests.test_config module."""
import unittest
# pylint: disable=wrong-import-order
from pgraph import config
from test.support import EnvironmentVarGuard


class ConfigTests(unittest.TestCase):

    """Config unit tests."""

    def test_missing_envvar(self):
        """missing CONFIG_FILE envvar."""
        with EnvironmentVarGuard() as env:
            env.set('CONFIG_FILE', '')
            env.unset('CONFIG_FILE')
            with self.assertRaises(SystemExit):
                config.load()

    def test_fail_read_config(self):
        """fail read CONFIG_FILE."""
        with EnvironmentVarGuard() as env:
            env.set('CONFIG_FILE', 'foo.ini')
            with self.assertRaises(SystemExit):
                config.load()

    def test_load_config(self):
        """load config."""
        config_file = config.load()[1]
        self.assertTrue('development.ini' in config_file)
