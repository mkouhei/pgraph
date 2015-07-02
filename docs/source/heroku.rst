Deploying app to Heroku
=======================

1. Prepare Heroku.

   See also "`Getting Started with Python on Heroku <https://devcenter.heroku.com/articles/getting-started-with-python#introduction>`_".

2. Cloning repository, and add remote repository.

   .. code-block:: shell

      $ git clone https://github.com/mkouhei/pgraph
      $ cd pgraph
      $ git remote add heroku <Heroku URL>

3. Enabling plugins

   a. Heroku Postgres

      .. code-block:: shell

         $ heroku addons:create heroku-postgresql:hobby-dev

      See also `Heroku Postgres <https://devcenter.heroku.com/articles/heroku-postgresql>`_

      .. note::
         If you will use CloudAMQP instead of Heroku Postgres, execute this.

         .. code-block:: shell

            $ heroku addons:create cloudamqp:lemur

         See also `CloudAMQP <https://devcenter.heroku.com/articles/cloudamqp>`_.

   b. Memcached Cloud

      .. code-block:: shell

         $ heroku addons:create memcachedcloud:30

      See also `Memcached Cloud <https://devcenter.heroku.com/articles/memcachedcloud>`_

   c. New Relic APM

      .. code-block:: shell

         $ heroku addons:create newrelic:wayne

      See also `New Relic APM <https://devcenter.heroku.com/articles/newrelic>`_
   
3. git push to Heroku.

   .. code-block:: shell

      $ git push heroku master

4. Change the scale your app.

   .. code-block:: shell

      $ heroku ps:scale worker=1


Runnig test locally
-------------------

Use PostgreSQL as Celery backend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Installing PostgreSQL, Memcached.

   .. code-block:: shell

      $ sudo apt-get install postgresql memcached
      $ sudo su - postgres
      $ psql
      postgres=# CREATE USER pgraph WITH PASSWORD 'passw0rd';
      postgres=# CREATE DATABASE pgraph OWNER pgraph;
      postgres=# \q

   .. note::
      You can use `yrmcds <http://cybozu.github.io/yrmcds/>`_ instead of memcached.::
   
        $ sudo apt-get install yrmcds

2. Cloning repository, and add remote repository.

   .. code-block:: shell

      $ git clone https://github.com/mkouhei/pgraph
      $ cd pgraph

3. Generate requirements.txt.

   .. code-block:: shell

      $ python setup.py --version
      $ pip install --no-use-wheel -r requirements.txt -r heroku_requirements.txt

4. Running celery worker.

   .. code-block:: shell

      $ DATABSE_URL=postgres://pgraph:passw0rd@locahost:5432/pgraph CONFIG_FILE=heroku.ini newrelic-admin run-program celery worker -c 1 -A pgraph.tasks --loglevel=info

5. Execute `run` script.

   .. code-block:: shell

      $ DATABASE_URL=postgres://pgraph:passw0rd@localhost:5432/pgraph MEMCACHEDCLOUD_SERVERS=127.0.0.1:11211 newrelic-admin run-program sh run


Use RabbigMQ as Celery backend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Installing RabbitMQ, Memcached.

   .. code-block:: shell

      $ sudo apt-get install rabbitmq-server memcached
         
   .. note::
      You can use `yrmcds <http://cybozu.github.io/yrmcds/>`_ instead of memcached.::
   
         $ sudo apt-get install yrmcds

2. Cloning repository, and add remote repository.

   .. code-block:: shell

      $ git clone https://github.com/mkouhei/pgraph
      $ cd pgraph

3. Generate requirements.txt.

   .. code-block:: shell

      $ python setup.py --version
      $ pip install --no-use-wheel -r requirements.txt -r heroku_requirements.txt

4. Running celery worker.

   .. code-block:: shell

      $ CONFIG_FILE=heroku.ini newrelic-admin run-program celery worker -c 1 -A pgraph.tasks --loglevel=info

5. Execute `run` script.

   .. code-block:: shell

      $ MEMCACHEDCLOUD_SERVERS=127.0.0.1:11211 newrelic-admin run-program sh run

