#!/usr/bin/env python
#coding:utf-8

import tornado.web
import os
import importlib

from common import conf


setting = dict(
    static_url_prefix = "/%s/static/" % conf.SERVICE_NAME, 
    template_path = os.path.join(os.path.dirname(__file__),"template"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    autoreload = True,
    cookie_secret=conf.PRIVATE_KEY,
    )

modules = [
    'authentication',
    'authorization',
    'purchase_summary',
    'user',
    'warehouse',
    'wood',
    "buyer",
    "customer"]


handlers = []
for i in modules:
    handlers += importlib.import_module('handler.%s.url' % i).url

application = tornado.web.Application(handlers=handlers, **setting)
