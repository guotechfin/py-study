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


class PurchaseSummaryNew(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS
        self.purchase_summary_id = -1

        input = json.loads(self.request.body)
        self.buyer_id = int(input.get("buyer_id", -1))
        self.create_date = input.get("create_date", "")
        self.remark = input.get("remark", "")

    def check_params(self):
        if self.buyer_id == -1:
            self.ret, self.msg = 1, error_msg.PARAMS_ERROR
            return False
        return True

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['purchase_summary_id'] = self.purchase_summary_id
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    @utility.login_requested
    @utility.check_right(conf.AUTHORIZATION[0][0][1][0])
    def post(self):
        if not self.check_params():
            return self.response()
        try:
            self.purchase_summary_id = (purchase_summary_obj.
                    new_purchase_summary(
                        self._db_session,
                        buyer_id=self.buyer_id,
                        user_id=self._user_id,
                        create_date=self.create_date,
                        remark=self.remark)
                    )
            self._db_session.commit()
        except Exception as e:
            mylog.logger.error("new_purchase_summary error %s" % e)
            self.ret = 1
            self.msg = error_msg.SERVER_ERROR
            self._db_session.rollback()
        return self.response()
