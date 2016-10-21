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

from group_service import group_obj


class GroupModify(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS
        self.msg = error_msg.SUCCESS

        input = json.loads(self.request.body)
        self.group_id = input.get("group_id", -1)
        self.name = input.get("name", "")
        self.remark = input.get("remark", "")

    def check_params(self):
        if (self.name == "" or self.group_id == -1):
            self.ret, self.msg = error_msg.PARAMS_ERROR
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
    def post(self):
        if not self.check_params():
            return self.response()
        try:
            group_obj.modify_group(
                    self._db_session,
                    id=self.group_id,
                    name=self.name,
                    remark=self.remark
                    )
            self._db_session.commit()
        except Exception as e:
            mylog.logger.error("modify_group error %s" % e)
            self.ret, self.msg = error_msg.SERVER_ERROR
            self._db_session.rollback()
        return self.response()
