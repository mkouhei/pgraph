# -*- coding: utf-8 -*-
"""pgraph celery configuration for Heroku."""
import os
from pgraph import config

CONF, CONFIG_FILE = config.load()


if os.path.basename(CONFIG_FILE) == 'heroku.ini':
    # Heroku
    if CONF.get('celery', 'celery_result_backend') == 'amqp':
        # CloudAMQP
        CELERY_RESULT_BACKEND = CONF.get('celery', 'celery_result_backend')
        BROKER_URL = os.environ.get(CONF.get('celery', 'broker_url'))
    else:
        # RDB (PostgreSQL, etc.)
        CELERY_RESULT_BACKEND = 'db+{0}'.format(
            os.environ.get(CONF.get('celery', 'celery_result_backend')))
        BROKER_URL = 'sqla+{0}'.format(
            os.environ.get(CONF.get('celery', 'broker_url')))
    CELERY_SEND_EVENTS = CONF.getboolean('celery',
                                         'celery_send_events')
    CELERY_EVENT_QUEUE_EXPIRES = CONF.getint('celery',
                                             'celery_event_queue_expires')
    BROKER_POOL_LIMIT = CONF.getint('celery',
                                    'broker_pool_limit')
    BROKER_CONNECTION_TIMEOUT = CONF.getint('celery',
                                            'broker_connection_timeout')
    BROKER_HEARTBEAT = CONF.getint('celery',
                                   'broker_heartbeat')
    MEMCACHED_SERVERS = ([os.environ.get(CONF.get('cache', 'servers'))]
                         if os.environ.get(CONF.get('cache', 'servers'))
                         else None)
    MEMCACHED_USERNAME = os.environ.get(CONF.get('cache', 'username'))
    MEMCACHED_PASSWORD = os.environ.get(CONF.get('cache', 'password'))

    __all__ = ['CELERY_RESULT_BACKEND',
               'BROKER_URL',
               'CELERY_SEND_EVENTS',
               'CELERY_EVENT_QUEUE_EXPIRES',
               'BROKER_POOL_LIMIT',
               'BROKER_CONNECTION_TIMEOUT',
               'BROKER_HEARTBEAT']

else:
    # General
    CELERY_RESULT_BACKEND = CONF.get('celery', 'celery_result_backend')
    BROKER_URL = CONF.get('celery', 'broker_url')

    MEMCACHED_SERVERS = ([CONF.get('cache', 'servers')]
                         if CONF.get('cache', 'servers') else None)
    MEMCACHED_USERNAME = CONF.get('cache', 'username')
    MEMCACHED_PASSWORD = CONF.get('cache', 'password')

    __all__ = ['CELERY_RESULT_BACKEND',
               'BROKER_URL']

# Pickle instead of Memcached
CACHE_NAME = (CONF.get('cache', 'cache_name')
              if CONF.get('cache', 'cache_name')
              else 'pgraph.cache')
