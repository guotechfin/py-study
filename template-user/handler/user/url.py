#!/bin/env python
# -*- coding:utf8 -*-

from user_list import UserList
from user_modify import UserModify
from user_new import UserNew
from common import conf

user_url = [
        ("/%s/user/list" % conf.service_name, UserList),
        ("/%s/user/new" % conf.service_name, UserNew),
        ("/%s/user/modify" % conf.service_name, UserModify),
        ]
