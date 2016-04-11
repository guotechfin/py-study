#!/bin/env python
# -*-coding:utf-8-*-

import json

from flask import Blueprint, request, Response
from user_controller import user_obj
from my_log import logger
import utility
from flask import render_template
from flask import redirect
from flask import make_response


token = Blueprint("token", __name__)


@token.route('/login', methods=['POST', 'GET'])
def login():
    user_name = request.form.get("user_name", "")
    password = request.form.get("password", "")
    if user_name == "" or password == "":
        return render_template('login.html', **locals())
    else:
        user_info = user_obj.get_user_by_name(user_name)
        if not user_info:
            msg = u"不存在用户名"
            return render_template('login.html', **locals())
        elif not utility.check_pwd(user_info.password, password):
            msg = u"密码错误"
            return render_template('login.html', **locals())
        else:
            user_id = user_info.user_id
            user_token = utility.create_token(user_id)
            resp = make_response(redirect("/user_profile/v1/profile/index.html"))
            resp.set_cookie('user_name', str(user_name))
            resp.set_cookie('user_id', str(user_id))
            resp.set_cookie('user_token', str(user_token))
            return resp


@token.route('/logout', methods=['GET'])
def logout():
    resp = make_response(redirect("/user_profile/v1/token/login"))
    resp.set_cookie('user_name', "", expires=0)
    resp.set_cookie('user_id', "", expires=0)
    resp.set_cookie('user_token', "", expires=0)
    return resp


@token.route('/check_token', methods=['GET'])
def check_token():
    user_id = request.args.get("user_id", "")
    user_token = request.args.get("token", "")
    ret, msg = 0, ""
    if user_id == "" or user_token == "":
        ret, msg = 1, u"参数错误"
    else:
        if not utility.check_token(user_id, user_token):
            ret, msg = 2, u"token失效"
        else:
            ret, msg = 0, ""
    resp_dict = dict()
    resp_dict['ret'] = ret
    resp_dict['msg'] = msg
    return Response(json.dumps(resp_dict))
