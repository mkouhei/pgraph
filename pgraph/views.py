# -*- coding: utf-8 -*-
"""pgraph.views module."""
import time
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
        return self.meta

    @view_config(route_name='linkdraw', renderer='json')
    def linkdraw(self):
        """Linkdraw data."""
        pkg_name = self.request.matchdict['pkg']
        self.meta['pkg_name'] = pkg_name
        job = tasks.gen_dependency.delay(pkg_name)
        while job.ready() is False:
            time.sleep(1)
        if job.successful():
            result = job.result.draw('linkdraw',
                                     decode_type='json',
                                     disable_time=True,
                                     disable_descr=True)
            return result

    @view_config(route_name='graph', renderer='templates/graph.pt')
    def graph(self):
        """drawing graph."""
        pkg_name = self.request.matchdict['pkg']
        self.meta['pkg_name'] = pkg_name
        job = tasks.gen_dependency.delay(pkg_name)
        while job.ready() is False:
            time.sleep(1)
        if job.successful():
            self.meta['linkdraw'] = job.result.draw('linkdraw',
                                                    decode_type='json')
            self.meta['base_pkg'] = self.meta['linkdraw']['nodes'][0]
        else:
            self.meta['linkdraw'] = False
            self.meta['base_pkg'] = {'link': None, 'version': None}
        return self.meta

    @view_config(route_name='search', renderer='templates/search.pt')
    def search(self):
        """search package."""
        pkg_name = self.request.GET.get('pkg_name')
        self.meta['pkg_name'] = pkg_name
        job = tasks.search.delay(pkg_name)
        while job.ready() is False:
            time.sleep(1)
        if job.successful():
            self.meta['results'] = list(set([pkg.get('name')
                                             for pkg in job.result]))
        else:
            self.meta['results'] = False
        return self.meta
