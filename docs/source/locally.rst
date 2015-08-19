
How to run things locally
=========================

1. Installing RabbitMQ.

   .. code-block:: shell

      $ sudo apt-get install rabbitmq-server

2. Setup RabbitMQ.

   .. code-block:: shell

      $ sudo rabbitmqctl add_vhost /pgraph
      $ sudo rabbitmqctl add_user pgraph passw0rd
      $ sudo rabbitmqctl set_permissions -p /pgraph pgraph ".*" ".*" ".*"
      $ sudo rabbitmqctl delete_user guest

3. Cloning repository.
         
   .. code-block:: shell

      $ git clone https://github.com/mkouhei/pgraph
      $ cd pgraph
      $ git submodule init
      $ git submodule update

4. Createing virtual environment.

   .. code-block:: shell

      $ pyvenv /path/to/venv
      $ . /path/to/venv/bin/activate

5. Installing pgraph.

   .. code-block:: shell

      (venv)$ cd /path/to/pgraph
      (venv)$ python setup.py develop

   or

   .. code-block:: shell

      (venv)$ pip install --no-use-wheel pgraph

   .. warning::
      Not use ``pip install pgraph``. See also "`Known issue with the packages that depends on py-deps <http://py-deps.readthedocs.org/en/latest/README.html#known-issue-with-the-packages-that-depends-on-py-deps>`_".


6. Running celery worker.

   .. code-block:: shell

      (venv)$ CONFIG_FILE=/path/to/pgraph/development.ini celery -A pgraph.tasks worker --loglevel=info

7. Running pserve from another venv session.

   .. code-block:: shell

      (venv)$ pserve /path/to/pgraph/development.ini

