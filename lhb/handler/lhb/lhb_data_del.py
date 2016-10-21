#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import tornado.gen
import tornado.httpclient
from tornado.escape import utf8
import json
import re
import datetime

from common import web_handler
from common import mylog
from common import error_msg
from common import conf
from common import utility

from lhb_service import lhb_obj


class LHBDataDel(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS

        self.date = self.get_argument("date",
                datetime.datetime.now().strftime("%Y%m%d"))

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def get(self):
        lhb_obj.del_lhb_data(self._db_session, self.date)
        self._db_session.commit()
        self.response()
