#!/bin/env python
# -*-coding:utf-8-*- 

import hashlib
import time
from M2Crypto.EVP import Cipher
import base64
import conf


def make_pwd(pwd):
    m = hashlib.md5()
    m.update(pwd.strip())
    return m.hexdigest()

def check_pwd(md5_old_pwd, new_pwd):
    if md5_old_pwd == make_pwd(new_pwd):
        return True
    else:
        return False

def create_token(user_id):
    plain_token = ("%s_%s_jpush_user_center" %
            (int(time.time()), user_id))
    return Encrypt(plain_token)

def check_token(user_id, token):
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
