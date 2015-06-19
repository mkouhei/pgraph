# -*- coding: utf-8 -*-
import sys
import os
from setuptools import setup
from setuptools.command.test import test as TestCommand

from pgraph import (__project__,
                    __author__,
                    __email__,
                    __version__,
                    __repo__)


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        if self.tox_args:
            errno = tox.cmdline(args=shlex.split(self.tox_args))
        else:
            errno = tox.cmdline(self.test_args)
        sys.exit(errno)


classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Framework :: Pyramid",
    "License :: OSI Approved :: "
    "GNU General Public License v3 or later (GPLv3+)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
]


long_description = (
    open('README.rst').read() +
    open('docs/source/HISTORY.rst').read())

requires = ['pyramid',
            'pyramid_chameleon',
            'pyramid_debugtoolbar',
            'waitress',
            'pyramid_celery',
            'webtest',
            'mock',
            'py-deps>=0.4.6']

extras_require = {
    'reST': ['Sphinx'],
    'heroku': ['CherryPy',
               'PasteScript',
               'PasteDeploy']}
if os.environ.get('READTHEDOCS', None):
    extras_require['reST'].append('recommonmark')

with open('requirements.txt', 'w') as fobj:
    fobj.write('\n'.join(requires +
                         extras_require.get('heroku')))
with open('extras_requirement.txt', 'w') as fobj:
    fobj.write('\n'.join(extras_require.get('reST')))

setup(name=__project__,
      version=__version__,
      description='Drawing graph of the dependencies of Python packages',
      long_description=long_description,
      classifiers=classifiers,
      author=__author__,
      author_email=__email__,
      url=__repo__,
      packages=[__project__],
      data_files=[],
      zip_safe=False,
      install_requires=requires,
      include_package_data=True,
      extras_require=extras_require,
      tests_require=['tox'],
      cmdclass={'test': Tox},
      entry_points={
        'paste.app_factory': ['main = pgraph.run:main']},)
