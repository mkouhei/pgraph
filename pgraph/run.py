# -*- coding: utf-8 -*-
"""pgraph packages."""
from pyramid.config import Configurator


# pylint: disable=unused-argument
def main(global_config, **settings):
    """Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('config', '/linkdraw/config/{pkg}')
    config.add_route('linkdraw', '/api/linkdraw/{pkg}')
    config.add_route('graph', '/graph/{pkg}')
    config.add_route('search', '/search')
    config.scan()
    return config.make_wsgi_app()
