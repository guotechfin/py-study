#!/bin/env python
# -*- coding:utf8 -*-
import os


# 项目名
SERVICE_NAME = "template-user"

# 是否调试
debug = True

# mysql user
MYSQL_USER = "%s" % SERVICE_NAME
MYSQL_PWD = "123456"
MYSQL_DB = "%s_db" % SERVICE_NAME

# 私钥
PRIVATE_KEY = "8434567812345678"
# token 7天有效期
TOKEN_TIMEOUT = 7 * 24 * 60 * 60
