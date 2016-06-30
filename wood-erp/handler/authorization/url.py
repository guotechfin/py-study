#!/bin/env python
# -*- coding:utf8 -*-

from authorization_user_list import AuthorizationUserList
from authorization_list import AuthorizationList
from authorization_change import AuthorizationChange
from common import conf

url = [
        ("/%s/authorization/list" % conf.SERVICE_NAME, AuthorizationList),
        ("/%s/authorization/user_list" % conf.SERVICE_NAME, AuthorizationUserList),
        ("/%s/authorization/change" % conf.SERVICE_NAME, AuthorizationChange),
        ]
