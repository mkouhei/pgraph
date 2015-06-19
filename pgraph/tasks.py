# -*- coding: utf-8 -*-
"""pgraph.tasks module."""
import os
import sys
from celery import Celery
from py_deps import Package, Container
if sys.version_info < (3, 0):
    # pylint: disable=import-error
    import ConfigParser as configparser
    from urlparse import urlparse
else:
    import configparser
    from urllib.parse import urlparse


def celery_config():
    """Load Celery configuration."""
    if os.environ.get('CELERY_CONFIG') is None:
        sys.stderr.write("Missing env variable CELERY_CONFIG\n\n")
        sys.exit(2)

    config_file = os.path.abspath(os.environ['CELERY_CONFIG'])
    if not os.path.isfile(config_file):
        sys.stderr.write("Can't read file: %s\n\n" % config_file)
        sys.exit(2)

    config = configparser.SafeConfigParser()
    config.read(config_file)
    return config, config_file


def broker_url(url):
    """Return broker url."""
    if urlparse(url).scheme and urlparse(url).netloc and urlparse(url).path:
        return url
    elif (urlparse(url).scheme == '' and
          urlparse(url).netloc == '' and
          urlparse(url).path):
        return os.environ.get(urlparse(url).path)

CONF, CONFIG_FILE = celery_config()
if CONFIG_FILE == 'heroku.ini':
    from pgraph import celeryconfig
    APP = Celery('tasks')
    APP.config_from_object(celeryconfig)
else:
    APP = Celery('tasks',
                 backend=CONF.get('celery', 'backend'),
                 broker=broker_url(CONF.get('celery', 'broker')))


@APP.task
def gen_dependency(pkg_name, version):
    """Generate dependencies."""
    return Package(pkg_name, version=version)


def read_cache(pkg_name, version):
    """Check cache and read data."""
    if Container().read_data((pkg_name, version)):
        return Package(pkg_name, version=version)
    else:
        return


def search(pkg_name):
    """Search package."""
    return Package.search(pkg_name)


def result(task_id):
    """Retrieve the result of task."""
    # pylint: disable=too-many-function-args
    return APP.AsyncResult(task_id)
