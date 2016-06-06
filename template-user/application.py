#!/usr/bin/env python
#coding:utf-8

import tornado.web
import os

from common import conf

from handler.user.url import user_url
from handler.authority.url import authority_url

setting = dict(
    static_url_prefix = "/%s/static/" % conf.service_name, 
    template_path = os.path.join(os.path.dirname(__file__),"template"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    autoreload = True,
    cookie_secret=conf.PRIVATE_KEY,
    )

handlers = []
handlers += user_url
handlers += authority_url

application = tornado.web.Application(handlers=handlers, **setting)
