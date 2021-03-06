# -*- coding: utf-8 -*-
"""pgraph.tests.test_config module."""
import unittest
from test.support import EnvironmentVarGuard


class BackednConfigTests(unittest.TestCase):

    """Backend config unit tests."""

    def test_heroku_config(self):
        """Load configuration for Heroku."""
        with EnvironmentVarGuard() as env:
            env.set('CONFIG_FILE', 'heroku.ini')
            from pgraph import backend_config as bconfig  # pylint: disable=import-outside-toplevel
            self.assertTrue(hasattr(bconfig, 'CELERY_RESULT_BACKEND'))
            self.assertTrue(hasattr(bconfig, 'BROKER_URL'))
            self.assertTrue(hasattr(bconfig, 'CELERY_SEND_EVENTS'))
            self.assertTrue(hasattr(bconfig,
                                    'CELERY_EVENT_QUEUE_EXPIRES'))
            self.assertTrue(hasattr(bconfig, 'BROKER_POOL_LIMIT'))
            self.assertTrue(hasattr(bconfig,
                                    'BROKER_CONNECTION_TIMEOUT'))
            self.assertTrue(hasattr(bconfig, 'BROKER_HEARTBEAT'))
            self.assertTrue(hasattr(bconfig, 'MEMCACHED_SERVERS'))
            self.assertTrue(hasattr(bconfig, 'MEMCACHED_USERNAME'))
            self.assertTrue(hasattr(bconfig, 'MEMCACHED_PASSWORD'))
            self.assertTrue(hasattr(bconfig, 'CACHE_NAME'))
