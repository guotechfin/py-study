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


class PurchaseSummaryDel(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS
        self.purchase_summary_id = self.get_argument("id", -1)

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    @utility.login_requested
    @utility.check_right(conf.AUTHORIZATION[0][0][3][0])
    def get(self):
        try:
            result = purchase_summary_obj.del_purchase_summary(
                    self._db_session,
                    purchase_summary_id=self.purchase_summary_id
                    )
            self._db_session.commit()
        except Exception as e:
            mylog.logger.error("del_purchase_summary error %s" % e)
            self.ret = 1
            self.msg = error_msg.SERVER_ERROR
            self._db_session.rollback()
        if not result:
            self.ret = 1
            self.msg = error_msg.CHECKED_ERROR
        return self.response()
