=======================================================
 pgraph: drawing graph of Python packages dependencies
=======================================================

The pgraph provides the graph of Python dependencies,
powered by `Linkdraw <https://github.com/mtoshi/linkdraw/wiki>`_, `Pyramid <http://docs.pylonsproject.org/en/latest/docs/pyramid.html>`_, and `py-deps <https://github.com/mkouhei/py-deps>`_.



How to run things locally
=========================

1. Installing RabbitMQ.

::

   $ sudo apt-get install rabbitmq-server

2. Setup RabbitMQ.

::

   $ sudo rabbitmqctl add_vhost /pgraph
   $ sudo rabbitmqctl add_user pgraph passw0rd
   $ sudo rabbitmqctl set_permissions -p /pgraph pgraph ".*" ".*" ".*"
   $ sudo rabbitmqctl delete_user guest

3. Cloning repository.

::

   $ git clone https://github.com/mkouhei/pgraph
   $ cd pgraph
   $ git submodule init
   $ git submodule update


4. Createing virtual environment.

::

   $ pyvenv /path/to/venv
   $ . /path/to/venv/bin/activate

5. Installing pgraph.

::
      
   (venv)$ cd /path/to/pgraph
   (venv)$ python setup.py install
   or
   (venv)$ pip install pgraph

6. Running celery worker.

::

   (venv)$ celery -A pgraph.tasks.worker --loglevel=info

7. Running pserve from another venv session.

::

   (venv)$ pserve /path/to/pgraph/development.ini

