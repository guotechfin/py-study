#!/bin/env python
# -*- coding:utf8 -*-
import os


# 项目名
service_name = "template-user"

# 是否调试
debug = True

# mysql user
mysql_user = "%s" % service_name
mysql_pwd = "123456"
mysql_db = "%s_db" % service_name

# 私钥
PRIVATE_KEY = "8434567812345678"
# token 7天有效期
TOKEN_TIMEOUT = 7 * 24 * 60 * 60
