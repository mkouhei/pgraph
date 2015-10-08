# -*- coding: utf-8 -*-
"""pgraph.tests module."""
import os
import sys
import unittest
import json
from pyramid import testing
from webtest import TestApp
from mock import patch


class ViewTests(unittest.TestCase):

    """View unit tests."""

    def setUp(self):
        """Initialize."""
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        """Finalize."""
        testing.tearDown()

    def test_index(self):
        """unit test for index view."""
        from pgraph.views import GraphViews

        request = testing.DummyRequest()
        inst = GraphViews(request)
        response = inst.index()
        self.assertEqual(response['project'], 'pgraph')


class GraphFunctionalTests(unittest.TestCase):

    """Graph view functional tests."""

    def setUp(self):
        """Initialize."""
        from pgraph.run import main
        settings = {'__file__': os.environ['CONFIG_FILE']}
        app = main(settings)
        self.testapp = TestApp(app)

    def test_index(self):
        """unit test of index."""
        res = self.testapp.get('/', status=200)
        self.assertIn(b'Welcome', res.body)

    # pylint: disable=unused-argument
    @patch('pgraph.tasks.search')
    def test_search(self, _mock):
        """unit test of search."""
        res = self.testapp.get('/search?pkg_name=foo', status=200)
        self.assertIn(b'Search &quot;foo&quot; on PyPI', res.body)

    def test_graph(self):
        """unit test of graph."""
        res = self.testapp.get('/graph/py-deps/0.4.5', status=200)
        self.assertIn(b'Graph of &quot;py-deps&quot;', res.body)

    def test_path_error(self):
        """unit test of graph."""
        res = self.testapp.get('/graph/foo/bar/baz', status=404)
        self.assertIn(b'404 Not Found', res.body)

    if sys.version_info < (3, 0):
        @patch('xmlrpclib.ServerProxy')
        def test_graph_not_found(self, _mock):
            """unit test of graph.

            But linkdraw do nothing when the config json is null.
            """
            client_mock = _mock.return_value
            client_mock.package_releases.return_value = None
            res = self.testapp.get('/graph/hoge', status=200)
            self.assertIn(b'Graph of &quot;hoge&quot;', res.body)
            self.assertNotIn(b'glyphicon-tag', res.body)

    else:
        @patch('xmlrpc.client.ServerProxy')
        def test_graph_not_found_py3(self, _mock):
            """unit test of graph.

            But linkdraw do nothing when the config json is null.
            """
            client_mock = _mock.return_value
            client_mock.package_releases.return_value = None
            res = self.testapp.get('/graph/hoge', status=200)
            self.assertIn(b'Graph of &quot;hoge&quot;', res.body)
            self.assertNotIn(b'glyphicon-tag', res.body)

    def test_graph_pkg_broken(self):
        """unit test of graph.

        But linkdraw do nothing when the config json is null.
        """
        res = self.testapp.get('/graph/foo/.1', status=200)
        self.assertIn(b'Graph of &quot;foo&quot;', res.body)
        self.assertIn(b'glyphicon-tag', res.body)
        self.assertIn(b'<span>.1</span>', res.body)

    @patch('pgraph.tasks.gen_dependency.delay')
    def test_api(self, _mock):
        """unit test of graph."""
        job_mock = _mock.return_value
        with open('pgraph/tests/data/py-deps.linkdraw') as fobj:
            data = json.loads(fobj.read())
            job_mock.result.draw.return_value = data
        res = self.testapp.get('/api/linkdraw/py-deps/0.2.0', status=200)
        self.assertDictEqual(data, json.loads(res.body.decode('utf-8')))

    def test_config(self):
        """unit test of config."""
        res = self.testapp.get('/linkdraw/config/py-deps/0.2.0', status=200)
        with open('pgraph/tests/data/config.js') as fobj:
            data = fobj.read()
        self.assertEqual(data.encode('utf-8'), res.body)

    @patch('pgraph.tasks.latest_version')
    def test_example(self, _mock):
        """unit test of example redirect."""
        _mock.return_value = 'Graph &quot;pgraph&quot;'
        res = self.testapp.get('/graph/pgraph', status=200)
        self.assertIn(b'Graph of &quot;pgraph&quot;', res.body)
