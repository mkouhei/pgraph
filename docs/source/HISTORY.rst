History
=======

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

