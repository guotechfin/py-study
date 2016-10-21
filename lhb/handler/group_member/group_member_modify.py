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

from group_member_service import group_member_obj


class GroupMemberModify(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS

        input = json.loads(self.request.body)
        self.group_member_id = input.get("group_member_id", -1)
        self.group_id = input.get("group_id", -1)
        self.division_id = input.get("division_id", -1)
        self.remark = input.get("remark", "")

    def check_params(self):
        if (self.group_member_id == -1 or
                self.group_id == -1 or
                self.division_id == -1):
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
            group_member_obj.modify_group_member(
                    self._db_session,
                    id=self.group_member_id,
                    group_id=self.group_id,
                    division_id=self.division_id,
                    remark=self.remark
                    )
            self._db_session.commit()
        except Exception as e:
            mylog.logger.error("modify_group_member error %s" % e)
            self.ret, self.msg = error_msg.SERVER_ERROR
            self._db_session.rollback()
        return self.response()
