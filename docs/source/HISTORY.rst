History
=======

0.5.0 (2015-10-09)
------------------

* Supports Python 3.5.
* Adds showing version of running environments.
* Adjust svg_width for PC web brawser.
* Fixes unit test graph_not_found.

0.4.8 (2015-08-19)
------------------

* Changes custom 404 not found pages.
* Closes #4, #5 error handlings 503 errors.
* Fixes INTERNALERROR occurs when run the tox.
* Changes mackerel-agent-plugin script for proxy.

0.4.7 (2015-08-15)
------------------

* Changes setting SVG size from window InnerWidth, InnerHeight.
* Changes Sphinx theme to sphinx_rtd_theme.
* Adds mackerel metric plugin.

0.4.6 (2015-07-27)
------------------

* Uses static_path instead of static_url.
* Changes example pathname.

0.4.5 (2015-07-22)
------------------

* Adds latest_version method, display latest version package.
* Applies override node link with link_prefix.

0.4.4 (2015-07-19)
------------------

* Adds invalid metadata handler.

0.4.3 (2015-07-16)
------------------

* Change the color of the nodes to give gradation by the dependency depth (py-deps>=0.5.2)

0.4.2 (2015-07-12)
------------------

* Changes pgraph.tasks.search (py-deps>=0.5.1).
* Fixes `None` redundant second argument of `dict.get()`.
* Fixes old-style string formatting.

0.4.1 (2015-07-03)
------------------

* Adds unit tests for backend_config, config modules.
* Changes example to redirect to the graph of latest version of pgraph.
* Fixes responsive navbar, search form.
* Chagnes Demo site URL.

0.4.0 (2015-06-29)
------------------

* Revokes when tasks.gen_depenency failed.
* Fixes extras_requires for Heroku.
* Changes Celery backend for Heroku to PostgreSQL in default.
* Changes install requires pyramid_celery to celery.

0.3.1 (2015-06-24)
------------------

* Applies GPLv3 and adds LICENSE file.

0.3.0 (2015-06-24)
------------------

* Supports cache backend using memcached.
* Adds side bar into layout.
* Changes for Heroku.

  * Updates setup configuration.
  * Applies New Relic.
  * Fixes Procfile and run.

0.2.0 (2015-06-19)
------------------

* Integrates configurations locally and Heroku.
* Changes not use job queue if Package data exists in the cache.
* Enable to change Celery configuration using CELERY_CONFIG variable and ``.ini`` file.
* Specify package version.
* Adds linkdraw configuration link.
* Adds search form at navigation bar.
* Changes searched view.
* Coverage >= 90%.
* Supports running on Heroku.

0.1.0 (2015-06-08)
------------------

* Initial release.

