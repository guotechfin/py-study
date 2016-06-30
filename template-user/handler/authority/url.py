#!/bin/env python
# -*- coding:utf8 -*-

from authority_login import AuthorityLogin
from authority_logout import AuthorityLogout
from authority_verify_code import AuthorityVerifyCode
from common import conf

authority_url = [
        ("/%s/authority/login" % conf.SERVICE_NAME,
            AuthorityLogin),
        ("/%s/authority/logout" % conf.SERVICE_NAME,
            AuthorityLogout),
        ("/%s/authority/verify_code" % conf.SERVICE_NAME,
            AuthorityVerifyCode),
        ]
