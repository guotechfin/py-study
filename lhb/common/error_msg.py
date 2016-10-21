#!/bin/env python
# -*- coding:utf8 -*-


SUCCESS = 0, ""
SERVER_ERROR = 1, u"服务器异常"
TOKEN_TIMEOUT_ERROR = 2, u"过期登录"
PARAMS_ERROR = 3, u"参数错误"
USER_NAME_ERROR = 4, u"用户名非法"
ACCOUNT_PWD_ERROR = 5, u"账号或者密码错误"
NEW_USER_NAME_ERROR = 6, u"用户名重复"


VERIFY_CODE_ERROR = u"验证码错误"
CHECKED_ERROR = u"审核通过不能修改,删除"
AUTHORIZATION_ERROR = u"权限不足"
FORBIDDEN_ERROR = u"禁止登陆用户"
