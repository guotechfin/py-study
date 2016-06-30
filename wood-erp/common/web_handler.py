#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import traceback
from tornado.escape import utf8
import json

from common import mylog
from common import DBSession
from common import error_msg
from common import conf
from common import utility


class WebHandler(tornado.web.RequestHandler):
    def initialize(self):
        # 每个请求有一个
        self._db_session = DBSession()
        self._user_id = int(self.get_secure_cookie(
                '%s_user_id' % conf.SERVICE_NAME))
        self._user_name = self.get_secure_cookie(
                '%s_user_name' % conf.SERVICE_NAME)
        self._real_name = self.get_secure_cookie(
                '%s_real_name' % conf.SERVICE_NAME)
        self._token_id = self.get_secure_cookie(
                '%s_token_id' % conf.SERVICE_NAME)
        mylog.logger.debug("%s, ip: %s, query input: %s, body: %s,"
                "cookie: uid: %s, user_name: %s, "
                "real_name: %s, token_id: %s" %
                (self.__class__.__name__,
                    self.request.remote_ip,
                    self.request.query_arguments,
                    self.request.body,
                    self._user_id,
                    self._user_name,
                    self._real_name,
                    self._token_id))
        self.set_header('Content-Type', 'application/json')
        self.resp_json = ""

    def on_finish(self):
        mylog.logger.info("%s, query input: %s, body: %s. "
                "resp: %s. info: (%s), (%s), (%s), (%s), (%s)" %
                (self.__class__.__name__,
                    self.request.query_arguments,
                    self.request.body,
                    self.resp_json,
                    self.get_status(),
                    self.request.remote_ip, 
                    (self.request.request_time()*1000), 
                    self.request.full_url(),
                    self.request.method))
        self._db_session.close()

    def write_error(self, status_code, **kwargs):
        self._db_session.rollback()
        if "exc_info" in kwargs:
            mylog.logger.error("%s" % "".join(
                traceback.format_exception(*kwargs["exc_info"])))
        self.set_status("200", "OK")
        self.set_header('Content-Type', 'application/json')
        self.resp_json = json.dumps(
                {"ret": 1, "msg": error_msg.SERVER_ERROR})
        self.write(self.resp_json)
        self.finish()

    def decode_argument(self, value, name=None):
        try:
            return utf8(value)
        except UnicodeDecodeError:
            raise HTTPError(400, "Invalid unicode in %s: %r" %
                            (name or "url", value[:40]))
