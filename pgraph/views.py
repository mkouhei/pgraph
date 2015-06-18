# -*- coding: utf-8 -*-
"""pgraph.views module."""
from pyramid.renderers import get_renderer
from pyramid.view import view_config
from pgraph import __project__, __version__, __author__, __repo__, READTHEDOCS
from pgraph import tasks


class GraphViews(object):

    """Graph view class."""

    def __init__(self, request):
        """Initialize."""
        self.request = request
        renderer = get_renderer('templates/layout.pt')
        self.layout = renderer.implementation().macros['layout']
        self.meta = dict(project=__project__,
                         version=__version__,
                         author=__author__,
                         repo=__repo__,
                         docs=READTHEDOCS)

    # pylint: disable=unused-argument
    @view_config(route_name='index', renderer='templates/index.pt')
    def index(self):
        """index view."""
        return self.meta

    @view_config(route_name='config', renderer='templates/config.pt')
    def config(self):
        """Configuration for Linkdraw."""
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
            result = data.draw('linkdraw',
                               decode_type='json',
                               disable_time=True,
                               disable_descr=True)
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
                    result = job.result.draw('linkdraw',
                                             decode_type='json',
                                             disable_time=True,
                                             disable_descr=True)
                    result['status'] = 200
                else:
                    result = {'status': 404,
                              'descr': 'Failed parsing dependencies.',
                              'task': job.task_id}
        return result

    @view_config(route_name='graph', renderer='templates/graph.pt')
    def graph(self):
        """drawing graph."""
        pkg_name = self.request.matchdict['pkg']
        version = self.request.matchdict['version']
        link = 'https://pypi.python.org/pypi/%s/%s' % (pkg_name, version)
        self.meta['pkg_name'] = pkg_name
        self.meta['base_pkg'] = dict(version=version,
                                     link=link)
        return self.meta

    @view_config(route_name='search', renderer='templates/search.pt')
    def search(self):
        """search package."""
        pkg_name = self.request.GET.get('pkg_name')
        self.meta['pkg_name'] = pkg_name
        self.meta['results'] = tasks.search(pkg_name)
        return self.meta
