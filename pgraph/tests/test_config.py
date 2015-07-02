# -*- coding: utf-8 -*-
"""pgraph.tests.test_config module."""
import sys
import unittest
from pgraph import config
if sys.version_info < (3, 0):
    # pylint: disable=no-name-in-module,import-error
    from test.test_support import EnvironmentVarGuard
else:
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
