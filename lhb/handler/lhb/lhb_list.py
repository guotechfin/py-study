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


class LHBList(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS
        self.lhb_list = list()
        self.select_date = datetime.datetime.now().strftime("%Y%m%d")

        self.date = self.get_argument("date", "")

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['lhb_list'] = utility.to_obj(
                self.lhb_list,
                need_fields=["id", "date", "code", "ticket_name", "ticket_change_rate"]
                )
        resp_dict['date'] = self.select_date
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
        if self.date == "":
            self.select_date = lhb_obj.get_lhb_lastest_date(self._db_session)
        else:
            self.select_date = self.date
        self.lhb_list = lhb_obj.search_lhb_list(
                self._db_session,
                date=self.select_date)
        self.lhb_list = lhb_obj.distinct_code(self.lhb_list)
        self._db_session.commit()
        return self.response()
