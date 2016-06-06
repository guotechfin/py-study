#!/usr/bin/env python
#coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define, options

from application import application
from common import create_table, drop_table
from common import conf

define("port", default=8083, help="run on th given port", type=int)
options.logging = "debug"

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/tornado' % options.port
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()


if __name__=="__main__":
    if conf.debug:
        create_table()
    main()
