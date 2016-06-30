#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import tornado.gen
import tornado.httpclient
from tornado.escape import utf8
import json
import re

from common import web_handler
from common import mylog
from common import error_msg
from common import conf
from common import utility

from authorization_service import authorization_obj


class AuthorizationList(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.authorization_list = list()
        self.ret = 0
        self.msg = error_msg.SUCCESS

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['authorization_list'] = self.authorization_list
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    @utility.login_requested
    @utility.check_right(conf.AUTHORIZATION[4][0][0][0])
    def get(self):
        self.authorization_list = conf.AUTHORIZATION
        return self.response()
