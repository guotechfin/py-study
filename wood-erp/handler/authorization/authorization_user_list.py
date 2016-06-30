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


class AuthorizationUserList(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS
        self.authorization_list = list()

        self.user_id = self.get_argument("user_id", -1)

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['authorization_user_list'] = utility.to_obj(
                self.authorization_user_list)
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    @utility.login_requested
    @utility.check_right(conf.AUTHORIZATION[4][0][0][0])
    def get(self):
        if self.user_id == -1:
            self.user_id = self._user_id
        self.authorization_user_list = (authorization_obj.
                search_authorization_user_list(
                    self._db_session,
                    user_id=self.user_id))
        self._db_session.commit()
        return self.response()
