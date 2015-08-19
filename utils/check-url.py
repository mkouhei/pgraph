#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Meckerel custom metric."""
import sys
import time
import requests
from datetime import datetime


def dispatch_app(args):
    """Dispatch heroku app."""
    delta = round(24 / len(args))
    hour = datetime.now().hour
    for i in range(len(args)):
        if delta * i <= hour < delta * (i + 1):
            app = args[i]
            break
        else:
            app = args[-1]
    return app


def check_status(app=None, url=None):
    """Check status."""
    if url is None:
        url = 'http://{0}.herokuapp.com'.format(app)
    else:
        app = 'proxy'
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
    if len(sys.argv) == 1:
        print('[usage] {0} proxy_url target-app [...]'.format(sys.argv[0]))
        sys.exit(1)
    print('# mackerel-agent-plugin')
    rc, reason = check_status(app=dispatch_app(sys.argv[2:]))
    print('{0}\t{1}\t{2}'.format('pgraph.upstream', rc, epoch_now()))
    rc, reason = check_status(url=sys.argv[1])
    print('{0}\t{1}\t{2}'.format('pgraph.proxy', rc, epoch_now()))
    sys.exit(0)


if __name__ == '__main__':
    main()
