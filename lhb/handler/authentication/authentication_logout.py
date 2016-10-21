#!/bin/env python
#-*- coding:utf8 -*-

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


class AuthenticationLogout(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        self.resp_json = json.dumps(resp_dict, ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return
        
    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def get(self):
        self.clear_cookie("%s_token_id" % conf.SERVICE_NAME)
        return self.response()
