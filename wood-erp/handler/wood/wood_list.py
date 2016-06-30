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

from wood_service import wood_obj


class WoodList(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS
        self.wood_list = list()
        self.total = 0

        self.start = int(self.get_argument("start", -1))
        self.end = int(self.get_argument("end", -1))

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['wood_list'] = utility.to_obj(self.wood_list)
        resp_dict['total'] = int(self.total)
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    @utility.login_requested
    @utility.check_right(conf.AUTHORIZATION[5][0][0][0])
    def get(self):
        self.wood_list, self.total = wood_obj.search_wood_list(
               self._db_session,
               start=self.start,
               end=self.end)
        self._db_session.commit()
        return self.response()
