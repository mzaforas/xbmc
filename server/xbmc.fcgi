#!/usr/bin/python
import sys
sys.path.insert(0, '/home/pi/xbmc/')

from flup.server.fcgi import WSGIServer
from xbmc import app

if __name__ == '__main__':
    WSGIServer(app).run()
