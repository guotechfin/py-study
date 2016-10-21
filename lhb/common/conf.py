#!/bin/env python
# -*- coding:utf8 -*-
import os


# 项目名
SERVICE_NAME = "lhb"
PORT = 8094

# 是否调试
DEBUG = True

# mysql user
MYSQL_USER = "%s" % SERVICE_NAME
MYSQL_PWD = "123456"
MYSQL_DB = "%s_db" % SERVICE_NAME
# sqlalchemy 连接池 连接过期时间2小时 单位秒
MYSQL_CONNECT_TIMEOUT = 2 * 60 * 60

# 私钥
PRIVATE_KEY = "8434567812345678"
# token 7天有效期
TOKEN_TIMEOUT = 7 * 24 * 60 * 60

# supper user id
SUPPER_USER = [1, 2]

# 1w手
LARGE_VOLUME = 1000000
# 100w
LARGE_PRICE = 1000000


def get_code_list():
    def load_ticket(path, exclude_list=[]):
        code_list = list()
        with open(path, 'r') as f:
            for i in f.readlines():
                code = i.strip()
                if code not in exclude_list:
                    code_list.append(code)
        return code_list
    black_code_list = load_ticket('common/b50.txt')
    code_list = load_ticket('common/s50.txt', black_code_list)
    return code_list
TICKET_LIST = get_code_list()
QUERY_NUM = 20


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'
PROXY_HOST = "121.40.103.93"
PROXY_PORT = 8001
