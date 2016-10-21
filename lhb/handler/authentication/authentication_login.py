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


class AuthenticationLogin(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS

        self.user_name = self.get_body_argument("user_name")
        self.pwd = self.get_body_argument("pwd").upper()

    def check_params(self):
        if (self.user_name == "" or self.pwd == ""):
            self.ret, self.msg = error_msg.PARAMS_ERROR
            return False
        if not re.match('^[0-9a-zA-Z]+$', str(self.user_name)):
            self.ret, self.msg = error_msg.USER_NAME_ERROR
            return False
        return True
        
    def post(self):
        if not self.check_params():
            return self.redirect('/#/login')
        user = user_obj.check_pwd(
                self._db_session, self.user_name, self.pwd)
        self._db_session.commit()
        if user != None:
            token_id = utility.create_token(user.id)
            mylog.logger.debug("%s create token_id: %s" % 
                    (user.id, token_id))
            self.set_secure_cookie('%s_token_id' % conf.SERVICE_NAME, 
                    str(token_id))
            self.set_secure_cookie('%s_user_id' % conf.SERVICE_NAME, 
                    str(user.id),
                    expires_days=conf.TOKEN_TIMEOUT)
            self.set_secure_cookie('%s_user_name' % conf.SERVICE_NAME, 
                    str(user.user_name),
                    expires_days=conf.TOKEN_TIMEOUT)
            return self.redirect('/#/pages/lhb_list')
        else:
            return self.redirect('/#/login')
