# -*- coding: utf-8 -*-
"""pgraph.tasks module."""
from celery import Celery
from py_deps import cache, Package, deps
from pgraph.backend_config import (CACHE_NAME,
                                   MEMCACHED_SERVERS,
                                   MEMCACHED_USERNAME,
                                   MEMCACHED_PASSWORD)
from pgraph import celeryconfig

APP = Celery('tasks')
APP.config_from_object(celeryconfig)


@APP.task
def gen_dependency(pkg_name, version):
    """Generate dependencies."""
    return Package(pkg_name,
                   version=version,
                   cache_name=CACHE_NAME,
                   servers=MEMCACHED_SERVERS,
                   username=MEMCACHED_USERNAME,
                   password=MEMCACHED_PASSWORD)


def read_cache(pkg_name, version):
    """Check cache and read data."""
    _cache = cache.backend(cache_name=CACHE_NAME,
                           servers=MEMCACHED_SERVERS,
                           username=MEMCACHED_USERNAME,
                           password=MEMCACHED_PASSWORD)
    if _cache.read_data((pkg_name, version)):
        return Package(pkg_name,
                       version=version,
                       cache_name=CACHE_NAME,
                       servers=MEMCACHED_SERVERS,
                       username=MEMCACHED_USERNAME,
                       password=MEMCACHED_PASSWORD)
    else:
        return


def search(pkg_name):
    """Search package."""
    return deps.search(pkg_name)


def result(task_id):
    """Retrieve the result of task."""
    # pylint: disable=too-many-function-args
    return APP.AsyncResult(task_id)
