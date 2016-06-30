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

from purchase_summary_service import purchase_summary_obj


class PurchaseSummaryList(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS
        self.purchase_summary_list = list()
        self.total = 0

        self.start = int(self.get_argument("start", -1))
        self.end = int(self.get_argument("end", -1))

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['purchase_summary_list'] = utility.to_obj(
                self.purchase_summary_list)
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
    @utility.check_right(conf.AUTHORIZATION[0][0][0][0])
    def get(self):
        self.purchase_summary_list, self.total = (
                purchase_summary_obj.
                get_purchase_summary_list(
                    self._db_session,
                    start=self.start,
                    end=self.end))
        self._db_session.commit()
        return self.response()
