#!/bin/env python
#-*- coding:utf8 -*-

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

from handler.user.user_service import user_obj


class AuthorityLogin(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS

        input = json.loads(self.request.body)
        self.user_name = input.get("user_name", "")
        self.pwd = input.get("pwd", "").upper()

    def check_params(self):
        if (self.user_name == "" or self.pwd == ""):
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
        self.resp_json = json.dumps(resp_dict, ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return
        
    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def post(self):
        if not self.check_params():
            return self.response()
        user = user_obj.check_pwd(
                self._db_session, self.user_name, self.pwd)
        if user != None:
            token_id = utility.create_token(user.id)
            mylog.logger.debug("%s create token_id: %s" % 
                    (user.id, token_id))
            self.set_secure_cookie('%s_token_id' % conf.service_name, 
                    str(token_id))
            self.set_secure_cookie('%s_user_id' % conf.service_name, 
                    str(user.id),
                    expires_days=conf.TOKEN_TIMEOUT)
            self.set_secure_cookie('%s_user_name' % conf.service_name, 
                    str(user.user_name),
                    expires_days=conf.TOKEN_TIMEOUT)
            self.set_secure_cookie('%s_real_name' % conf.service_name, 
                    str(user.real_name),
                    expires_days=conf.TOKEN_TIMEOUT)
        else:
            self.ret, self.msg = 1, error_msg.ACCOUNT_PWD_ERROR
        return self.response()
