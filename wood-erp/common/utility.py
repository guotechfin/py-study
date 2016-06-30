#!/bin/env python
#-*- coding: UTF-8 -*-

import mmhash
import datetime
import time
from M2Crypto.EVP import Cipher
import base64
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from decimal import Decimal

from common import mylog
from common import conf
from common import error_msg

from handler.authorization.authorization_service import authorization_obj


def login_requested(func):
    def _login_requested(*args, **kwargs):
        self = args[0]
        if check_token(self._user_id, self._token_id):
            return func(*args, **kwargs)
        else:
            self.ret = 2
            self.msg = error_msg.TOKEN_TIMEOUT_ERROR
            return self.response()
    return _login_requested

def check_right(right_id):
    def _check_right(func):
        def __check_right(*args, **kwargs):
            self = args[0]
            if authorization_obj.check_authorization(
                    self._db_session, self._user_id, right_id):
                return func(*args, **kwargs)
            else:
                self.ret = 3
                self.msg = error_msg.AUTHORIZATION_ERROR
                return self.response()
        return __check_right
    return _check_right

def make_pwd(pwd):
    return mmhash.get_unsigned_hash(pwd)

def check_pwd(old_pwd, raw_pwd):
    pwd = make_pwd(raw_pwd)
    if old_pwd == pwd:
        return True
    else:
        return False

def create_token(user_id):
    plain_token = ("%s_%s_%s" %
            (int(time.time()),
                user_id,
                conf.SERVICE_NAME))
    return Encrypt(plain_token)

def check_token(user_id, token):
    if not user_id or not token:
        return False
    try:
        plain_token = Decrypt(token)
        plain_token_list = plain_token.split("_")
        create_time = plain_token_list[0]
        plain_user_id = plain_token_list[1]
        if int(time.time()) - int(create_time) > conf.TOKEN_TIMEOUT:
            return False
        if str(plain_user_id) == str(user_id):
            return True
        return False
    except Exception as e:
        return False

def Encrypt(data):
    # '使用aes_128_ecb算法对数据加密'
    # 加密操作
    ENCRYPT_OP = 1
    # 初始化变量，对于aes_128_ecb算法无用
    iv = '\0' * 16
    cipher = Cipher(alg='aes_128_ecb',
            key=conf.PRIVATE_KEY,
            iv=iv,
            op=ENCRYPT_OP)
    buf = cipher.update(data)
    buf = buf + cipher.final()
    del cipher
    return base64.b64encode(buf)

def Decrypt(data):
    # '使用aes_128_ecb算法对数据解密'
    # 解密操作
    DECRYPT_OP = 0
    # 初始化变量，对于aes_128_ecb算法无用
    iv = '\0' * 16
    data = base64.b64decode(data)
    cipher = Cipher(alg='aes_128_ecb',
            key=conf.PRIVATE_KEY,
            iv=iv,
            op=DECRYPT_OP)
    buf = cipher.update(data)
    buf = buf + cipher.final()
    del cipher
    return buf 

def to_obj(orm_obj, without_fields=[]):
    if orm_obj == None:
        return None
    elif isinstance(orm_obj.__class__, DeclarativeMeta):
        fields = {}
        for field in [x for x in dir(orm_obj)
                if not x.startswith('_') and x != 'metadata' and x not in without_fields]:
            data = orm_obj.__getattribute__(field)
            if isinstance(data, datetime.datetime):
                fields[field] = data.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(data, datetime.date):
                fields[field] = data.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(data, datetime.timedelta):
                fields[field] = ((datetime.datetime.min + data).time().
                        strftime("%Y-%m-%d %H:%M:%S"))
            elif isinstance(data, Decimal):
                fields[field] = float(data)
            else:
                fields[field] = data
        return fields
    elif isinstance(orm_obj, list):
        obj_list = list()
        for i in orm_obj:
            obj_list.append(to_obj(i, without_fields))
        return obj_list
