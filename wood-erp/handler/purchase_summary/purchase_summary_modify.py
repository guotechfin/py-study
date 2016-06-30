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


class PurchaseSummaryModify(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS

        input = json.loads(self.request.body)
        self.purchase_summary_id = input.get("purchase_summary_id", -1)
        self.buyer_id = int(input.get("buyer_id", -1))
        self.create_date = input.get("create_date", "")
        self.remark = input.get("remark", "")

    def check_params(self):
        if self.buyer_id == -1 or self.purchase_summary_id == -1:
            self.ret, self.msg = 1, error_msg.PARAMS_ERROR
            return False
        return True

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
    @utility.check_right(conf.AUTHORIZATION[0][0][2][0])
    def post(self):
        if not self.check_params():
            return self.response()
        try:
            result = purchase_summary_obj.modify_purchase_summary(
                    self._db_session,
                    purchase_summary_id=self.purchase_summary_id,
                    buyer_id=self.buyer_id,
                    create_date=self.create_date,
                    remark=self.remark
                    )
            self._db_session.commit()
        except Exception as e:
            mylog.logger.error("modify_purchase_summary error %s" % e)
            self.ret = 1
            self.msg = error_msg.SERVER_ERROR
            self._db_session.rollback()
        if not result:
            self.ret = 1
            self.msg = error_msg.CHECKED_ERROR
        return self.response()
