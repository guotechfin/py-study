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


class LHBDateList(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS
        self.lhb_date_list = list()

        self.code = self.get_argument("code", "")

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['lhb_date_list'] = utility.to_obj(
                self.lhb_date_list,
                need_fields=["date"]
                )
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    @utility.login_requested
    def get(self):
        self.lhb_date_list = lhb_obj.search_lhb_list(
                self._db_session,
                code=self.code,
                distinct_date=1)
        self._db_session.commit()
        return self.response()
