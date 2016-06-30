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

from user_service import user_obj


class UserModify(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS

        input = json.loads(self.request.body)
        self.user_id = input.get("user_id", -1)
        self.user_name = input.get("user_name", "")
        self.real_name = input.get("real_name", "")
        self.pwd = input.get("pwd", "")
        self.phone = input.get("phone", "")
        self.email = input.get("email", "")

    def check_params(self):
        if (self.user_name == "" or self.real_name == "" or
                self.user_id == -1):
            self.ret, self.msg = 1, error_msg.PARAMS_ERROR
            return False
        if not re.match('^[0-9a-zA-Z]+$', str(self.user_name)):
            self.ret, self.msg = 1, error_msg.USER_NAME_ERROR
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
    @utility.check_right(conf.AUTHORIZATION[3][0][2][0])
    def post(self):
        if not self.check_params():
            return self.response()
        try:
            user_obj.modify_user(
                    self._db_session,
                    user_id=self.user_id,
                    user_name=self.user_name,
                    real_name=self.real_name,
                    pwd=self.pwd,
                    phone=self.phone,
                    email=self.email
                    )
            self._db_session.commit()
        except Exception as e:
            mylog.logger.error("modify_user error %s" % e)
            self.ret = 1
            self.msg = error_msg.NEW_USER_NAME_ERROR
            self._db_session.rollback()
        return self.response()
