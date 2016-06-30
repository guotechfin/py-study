#!/bin/env python
# -*- coding:utf8 -*-

from authentication_login import AuthenticationLogin
from authentication_logout import AuthenticationLogout
from authentication_verify_code import AuthenticationVerifyCode
from common import conf

url = [
        ("/%s/authentication/login" % conf.SERVICE_NAME,
            AuthenticationLogin),
        ("/%s/authentication/logout" % conf.SERVICE_NAME,
            AuthenticationLogout),
        ("/%s/authentication/verify_code" % conf.SERVICE_NAME,
            AuthenticationVerifyCode),
        ]
