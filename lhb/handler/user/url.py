#!/bin/env python
# -*- coding:utf8 -*-

from user_list import UserList
from user_modify import UserModify
from user_new import UserNew
from common import conf

url = [
        ("/%s/user/list" % conf.SERVICE_NAME, UserList),
        ("/%s/user/new" % conf.SERVICE_NAME, UserNew),
        ("/%s/user/modify" % conf.SERVICE_NAME, UserModify),
        ]
