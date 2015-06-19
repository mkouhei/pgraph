Deploying app to Heroku
=======================

1. Prepare Heroku.

   See also "`Getting Started with Python on Heroku <https://devcenter.heroku.com/articles/getting-started-with-python#introduction>`_".

2. Cloning repository, and add remote repository.

   .. code-block:: shell

      $ git clone https://github.com/mkouhei/pgraph
      $ cd pgraph
      $ git remote add heroku <Heroku URL>

3. Enabling CloudAMQP.

   .. code-block:: shell
                   
      $ heroku addons:create cloudamqp:lemur

   See also `CloudAMQP <https://devcenter.heroku.com/articles/cloudamqp>`_.
   
3. git push to Heroku.

   .. code-block:: shell

      $ git push heroku master

4. Change the scale your app.

   .. code-block:: shell

      $ heroku ps:scale worker=1
