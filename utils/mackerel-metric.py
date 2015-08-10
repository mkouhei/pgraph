#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import requests
from datetime import datetime


def dispatch_app():
    """Dispatch heroku app."""
    hour = datetime.now().hour
    if 0 <= hour < 8:
        app = 'pgraph-a'
    elif 8 <= hour < 16:
        app = 'pgraph-b'
    else:
        app = 'pgraph-c'
    return app


def check_status(app):
    """Check status."""
    url = 'http://{0}.herokuapp.com'.format(app)
    resp = requests.get(url)
    if 200 == resp.status_code:
        rc = 1
    else:
        rc = 0
    return rc, '{0}: {1}'.format(app, resp.reason)


def epoch_now():
    """Get current epoch time."""
    return time.mktime(datetime.now().timetuple())


def main():
    print('# mackerel-agent-plugin')
    rc, reason = check_status(dispatch_app())
    print('{0}\t{1}\t{2}'.format('pgraph', rc, epoch_now()))
    sys.exit(0)


if __name__ == '__main__':
    main()
