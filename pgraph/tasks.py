# -*- coding: utf-8 -*-
"""pgraph.tasks module."""
import os
import sys
from celery import Celery
from py_deps import Package
if sys.version_info < (3, 0):
    # pylint: disable=import-error
    import ConfigParser as configparser
else:
    import configparser


def celery_config():
    """Load Celery configuration."""
    if os.environ.get('CELERY_CONFIG') is None:
        sys.stderr.write("Missing env variable CELERY_CONFIG")
        sys.exit(2)

    config_file = os.path.abspath(os.environ['CELERY_CONFIG'])
    if not os.path.isfile(config_file):
        sys.stderr.write("Can't read file: %s\n\n" % config_file)
        sys.exit(2)

    config = configparser.SafeConfigParser()
    config.read(config_file)
    return config


CONF = celery_config()
APP = Celery('tasks',
             backend=CONF.get('celery', 'backend'),
             broker=CONF.get('celery', 'broker'))


@APP.task
def gen_dependency(pkg_name):
    """Generate dependencies."""
    return Package(pkg_name)


@APP.task
def search(pkg_name):
    """Search package."""
    return Package.search(pkg_name)
