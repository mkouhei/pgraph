# -*- coding: utf-8 -*-
"""pgraph.tests module."""
import unittest
from pyramid import testing
from webtest import TestApp


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
        settings = {}
        app = main(settings)
        self.testapp = TestApp(app)

    def test_index(self):
        """unit test of index."""
        res = self.testapp.get('/', status=200)
        self.assertIn(b'Welcome', res.body)

    def test_search(self):
        """unit test of search."""
        res = self.testapp.get('/search?pkg_name=foo', status=200)
        self.assertIn(b'Search &quot;foo&quot; on PyPI', res.body)

    def test_graph(self):
        """unit test of graph."""
        res = self.testapp.get('/graph/py-deps', status=200)
        self.assertIn(b'Graph of &quot;py-deps&quot;', res.body)

    def test_graph_fail(self):
        """unit test of graph."""
        res = self.testapp.get('/graph/foo', status=200)
        self.assertIn(b'foo package is broken.', res.body)
