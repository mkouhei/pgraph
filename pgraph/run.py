# -*- coding: utf-8 -*-
"""pgraph packages."""
import os
from pyramid.config import Configurator


# pylint: disable=unused-argument
def main(global_config, **settings):
    """Pyramid WSGI application."""
    os.environ['CONFIG_FILE'] = global_config.get('__file__')
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('config', '/linkdraw/config/{pkg}/{version}')
    config.add_route('linkdraw', '/api/linkdraw/{pkg}/{version}')
    config.add_route('graph', '/graph/{pkg}/{version}')
    config.add_route('graph_latest', '/graph/{pkg}')
    config.add_route('search', '/search')
    config.scan()
    return config.make_wsgi_app()
