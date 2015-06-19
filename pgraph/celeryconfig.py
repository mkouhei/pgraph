# -*- coding: utf-8 -*-
"""pgraph celery configuration for Heroku."""
import os

BROKER_URL = os.environ.get('CLOUDAMQP_URL')
BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_TIMEOUT = 30
BROKER_HEARTBEAT = 30
CELERY_SEND_EVENTS = False
CELERY_EVENT_QUEUE_EXPIRES = 60
CELERY_RESULT_BACKEND = 'amqp'
