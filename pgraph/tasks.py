# -*- coding: utf-8 -*-
"""pgraph.tasks module."""
from celery import Celery
from py_deps import Package


APP = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')


@APP.task
def gen_dependency(pkg_name):
    """Generate dependencies."""
    return Package(pkg_name)


@APP.task
def search(pkg_name):
    """Search package."""
    return Package.search(pkg_name)
