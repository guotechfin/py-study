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

from authorization_service import authorization_obj


class AuthorizationChange(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS

        self.user_id = self.get_argument("user_id", -1)
        self.right_id = self.get_argument("right_id", -1)

    def check_params(self):
        if (self.user_id == -1 or self.right_id == -1):
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
    @utility.check_right(conf.AUTHORIZATION[4][0][1][0])
    def get(self):
        if not self.check_params():
            return self.response()
        try:
            authorization_obj.change_authorization(
                    self._db_session,
                    user_id=self.user_id,
                    right_id=self.right_id,
                    )
            self._db_session.commit()
        except Exception as e:
            mylog.logger.error("change_authorization error %s" % e)
            self.ret = 1
            self.msg = error_msg.SERVER_ERROR
            self._db_session.rollback()
        return self.response()
