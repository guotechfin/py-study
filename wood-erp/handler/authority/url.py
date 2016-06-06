#!/bin/env python
# -*- coding:utf8 -*-

from authority_login import AuthorityLogin
from authority_logout import AuthorityLogout
from authority_verify_code import AuthorityVerifyCode
from common import conf

authority_url = [
        ("/%s/authority/login" % conf.service_name,
            AuthorityLogin),
        ("/%s/authority/logout" % conf.service_name,
            AuthorityLogout),
        ("/%s/authority/verify_code" % conf.service_name,
            AuthorityVerifyCode),
        ]
