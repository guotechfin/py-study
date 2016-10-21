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

from user_service import user_obj


class UserList(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS
        self.user_list = list()
        self.total = 0

        self.start = int(self.get_argument("start", -1))
        self.end = int(self.get_argument("end", -1))

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['user_list'] = utility.to_obj(
                self.user_list, without_fields=['pwd'])
        resp_dict['total'] = int(self.total)
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def get(self):
        self.user_list, self.total = user_obj.search_user_list(
               self._db_session,
               start=self.start,
               end=self.end)
        self._db_session.commit()
        return self.response()
