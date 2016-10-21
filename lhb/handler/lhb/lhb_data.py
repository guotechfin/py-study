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

from handler.ticket.gushen_stock_service import gushen_obj
from lhb_data_source_service import lhb_data_source_obj


class LHBData(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS

        self.date = self.get_argument("date",
                datetime.datetime.now().strftime("%Y-%m-%d"))

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
        self.date = ''.join(self.date.split('-'))
        result = yield lhb_data_source_obj.get_lhb_list_from_qq(
                self._db_session, self.date)
        if result:
            self._db_session.commit()
        else:
            self._db_session.rollback()
        #yield gushen_obj.get_stock_real_time_info("002724")
        #yield lhb_data_source_obj.get_lhb_list_from_jys(
        #        self._db_session, "20160905")
        self.response()
