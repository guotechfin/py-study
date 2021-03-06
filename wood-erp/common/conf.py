#!/bin/env python
# -*- coding:utf8 -*-
import os


# 项目名
SERVICE_NAME = "wood_erp"

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

# 权限列表
AUTHORIZATION = (
        ((
            (0, u"查看"),
            (1, u"新建"),
            (2, u"修改"),
            (3, u"删除"),
            (4, u"审核"),
        ), u"采购开单"),
        ((
            (10, u"查看"),
            (11, u"新建"),
            (12, u"修改"),
            (13, u"删除"),
            (14, u"审核"),
        ), u"销售开单"),
        ((
            (20, u"查看"),
            (21, u"新建"),
            (22, u"修改"),
            (23, u"删除"),
            (24, u"审核"),
        ), u"客户收款"),
        ((
            (30, u"查看"),
            (31, u"新建"),
            (32, u"修改"),
        ), u"用户"),
        ((
            (40, u"查看"),
            (41, u"修改"),
        ), u"权限配置"),
        ((
            (50, u"查看"),
            (51, u"新建"),
            (52, u"修改"),
            (53, u"删除"),
        ), u"木材"),
        ((
            (60, u"查看"),
            (61, u"新建"),
            (62, u"修改"),
            (63, u"删除"),
        ), u"仓库"),
        ((
            (70, u"查看"),
            (71, u"新建"),
            (72, u"修改"),
            (73, u"删除"),
        ), u"采购商"),
        ((
            (80, u"查看"),
            (81, u"新建"),
            (82, u"修改"),
            (83, u"删除"),
        ), u"客户"),
)
