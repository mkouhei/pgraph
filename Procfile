web: newrelic-admin run-python runapp.py
worker: CELERY_CONFIG=heroku.ini newrelic-admin run-program celery worker -c 1 --app=pgraph.tasks --loglevel=info
