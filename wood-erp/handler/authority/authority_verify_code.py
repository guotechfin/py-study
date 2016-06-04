#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import tornado.gen
import tornado.httpclient
from tornado.escape import utf8
import json
import re
import time
import random

from common import web_handler
from common import mylog
from common import error_msg
from common import conf
from common import utility
import gen_img

class AuthorityVerifyCode(web_handler.WebHandler):
    def get(self):
        verify_id = ("%s_verify_%s" % 
                (conf.service_name, int(time.time())))
        verify_content = ""
        for i in xrange(0, 4):
            verify_content += (
                    "%s" % gen_img.init_chars[
                        random.randint(
                            0, gen_img.init_chars_len-1)])
        redis_ctl.redis_db.db.setex(verify_id, 
                conf.verify_timeout, verify_content)
        self.set_cookie('%s_verify_id' % conf.service_name, 
                str(verify_id))
        data = gen_img.gen_img(verify_content)
        mylog.logger.debug("gen verify_id: %s verify_content: %s" % 
                (verify_id, verify_content))
        self.add_header('Content-Type', 'image/jpg')
        self.add_header('Cache-Control', 'no-cache')
        self.write(data)
        self.finish()
        return
