
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

      $ python -m venv /path/to/venv
      $ . /path/to/venv/bin/activate

5. Installing pgraph.

   .. code-block:: shell

      (venv)$ cd /path/to/pgraph
      (venv)$ pip install -e . -e .[development]


6. Running celery worker.

   .. code-block:: shell

      (venv)$ CONFIG_FILE=/path/to/pgraph/development.ini celery -A pgraph.tasks worker --loglevel=info

7. Running pserve from another venv session.

   .. code-block:: shell

      (venv)$ pserve /path/to/pgraph/development.ini

