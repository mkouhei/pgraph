"""run app script for Heroku."""
import os
from paste.deploy import loadapp
from wsgiref.simple_server import make_server

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    wsgi_app = loadapp('config:heroku.ini', relative_to='.')
    httpd = make_server('0.0.0.0', port, wsgi_app)
    httpd.serve_forever()
