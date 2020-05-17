# -*- coding: utf-8 -*-
"""pgraph.views module."""
import sys
import pkg_resources
from pyramid.renderers import get_renderer
from pyramid.view import view_config, notfound_view_config
from py_deps.exceptions import InvalidMetadata, BackendFailure
from pgraph import __project__, __version__, __author__, __repo__, READTHEDOCS
from pgraph import tasks


def get_ver(pkg_name):
    """Get package version."""
    version = pkg_resources.get_distribution(pkg_name).version
    return version


class GraphViews:
    """Graph view class."""

    def __init__(self, request):
        """Initialize."""
        self.request = request
        renderer = get_renderer('templates/layout.pt')
        self.layout = renderer.implementation().macros['layout']
        self.meta = dict(project=__project__,
                         depver={'python': sys.version.split()[0],
                                 'py_deps': get_ver('py-deps'),
                                 'pylibmc': get_ver('pylibmc'),
                                 'celery': get_ver('celery'),
                                 'pyramid': get_ver('pyramid')},
                         version=__version__,
                         author=__author__,
                         repo=__repo__,
                         docs=READTHEDOCS)

    # pylint: disable=unused-argument
    @view_config(route_name='index', renderer='templates/index.pt')
    def index(self):
        """Index view."""
        return self.meta

    @view_config(route_name='config', renderer='templates/config.pt')
    def config(self):
        """Configure for Linkdraw."""
        self.request.response.content_type = 'application/javascript'
        pkg_name = self.request.matchdict['pkg']
        self.meta['pkg_name'] = pkg_name
        self.meta['version'] = self.request.matchdict['version']
        return self.meta

    @view_config(route_name='linkdraw', renderer='json')
    def linkdraw(self):
        """Linkdraw data."""
        pkg_name = self.request.matchdict['pkg']
        version = self.request.matchdict['version']
        task_id = self.request.GET.get('task')
        self.meta['pkg_name'] = pkg_name
        data = tasks.read_cache(pkg_name, version)
        if data:
            result = data.draw('linkdraw', link_prefix='/graph')
            result['status'] = 200
        else:
            if task_id:
                job = tasks.result(task_id)
            else:
                job = tasks.gen_dependency.delay(pkg_name, version)
            if job.ready() is False:
                result = {'status': 202,
                          'descr': 'Accepted',
                          'task': job.task_id}
            else:
                if job.successful():
                    try:
                        result = job.result
                        result['status'] = 200
                    except InvalidMetadata:
                        result = {'status': 500,
                                  'descr': 'Invalid package metadata.',
                                  'task': job.task_id}
                        job.revoke()
                else:
                    result = {'status': 404,
                              'descr': 'Failed parsing dependencies.',
                              'task': job.task_id}
                    job.revoke()
        return result

    @view_config(route_name='graph', renderer='templates/graph.pt')
    def graph(self):
        """Drawing graph."""
        pkg_name = self.request.matchdict['pkg']
        version = self.request.matchdict['version']
        link = 'https://pypi.python.org/pypi/{0}/{1}'.format(pkg_name, version)
        self.meta['pkg_name'] = pkg_name
        self.meta['base_pkg'] = dict(version=version,
                                     link=link)
        return self.meta

    @view_config(route_name='graph_latest', renderer='templates/graph.pt')
    def graph_latest(self):
        """Drawing latest version graph."""
        pkg_name = self.request.matchdict['pkg']
        version = tasks.latest_version(pkg_name)
        link = 'https://pypi.python.org/pypi/{0}/{1}'.format(pkg_name, version)
        self.meta['pkg_name'] = pkg_name
        self.meta['base_pkg'] = dict(version=version,
                                     link=link)
        return self.meta

    @view_config(route_name='search', renderer='templates/search.pt')
    def search(self):
        """Search package."""
        pkg_name = self.request.GET.get('pkg_name')
        self.meta['pkg_name'] = pkg_name
        self.meta['results'] = tasks.search(pkg_name)
        return self.meta

    @view_config(context=BackendFailure, renderer='templates/error.pt')
    def failed_backend(self):
        """Backend failure error page."""
        self.request.response.status = '500 Internal Server Error'
        self.meta['title'] = self.request.response.status
        self.meta['reason'] = 'PyPI: {}'.format(
            self.request.exception.args[0].strerror)
        return self.meta

    @notfound_view_config(renderer='templates/error.pt')
    def notfound(self):
        """Not found error page."""
        self.request.response.status = '404 Not Found'
        self.meta['title'] = self.request.response.status
        self.meta['reason'] = "The resource '{}' could not be found.".format(
            self.request.exception.args[0])
        return self.meta
