web: ./run 
worker: CELERY_CONFIG=heroku.ini celery worker -c 1 --app=pgraph.tasks --loglevel=info
