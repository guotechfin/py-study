#!/bin/env python
# -*- coding:utf8 -*-

from authority_login import AuthorityLogin
from authority_logout import AuthorityLogout
from common import conf

authority_url = [
        ("/%s/authority/login" % conf.service_name, AuthorityLogin),
        ("/%s/authority/logout" % conf.service_name, AuthorityLogout),
        ]
