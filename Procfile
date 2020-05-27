web: newrelic-admin run-program python runapp.py
worker: CONFIG_FILE=heroku.ini newrelic-admin run-program celery worker -c 1 --app=pgraph.tasks --loglevel=info
