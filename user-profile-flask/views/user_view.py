#!/bin/env python
# -*-coding:utf-8-*-

import json

from flask import Blueprint, request, Response
from user_controller import user_obj
from my_log import logger


user = Blueprint("user", __name__)


@user.route('/create_user', methods=['POST'])
def create_user():
    input = request.form.get("data", {})
    ret, msg = 0, ""
    if input == {}:
        ret, msg = 1, u"参数错误"
    else:
        input = json.loads(input)
        result = user_obj.new_user(
                name=input.get('name', ''),
                password=input.get('password', ''))
        if not result:
            ret, msg = 1, u"用户注册失败"
        else:
            ret, msg = 0, ""
    resp_dict = dict()
    resp_dict['ret'] = ret
    resp_dict['msg'] = msg
    return Response(json.dumps(resp_dict))


@user.route('/modify_user', methods=['POST'])
def modify_user():
    input = request.form.get("data", {})
    ret, msg = 0, ""
    if input == {}:
        ret, msg = 1, u"参数错误"
    else:
        input = json.loads(input)
        result = user_obj.modify_user(
                id=input.get("id", ""),
                name=input.get('name', ''),
                password=input.get('password', ''))
        if not result:
            ret, msg = 1, u"用户修改失败"
        else:
            ret, msg = 0, ""
    resp_dict = dict()
    resp_dict['ret'] = ret
    resp_dict['msg'] = msg
    return Response(json.dumps(resp_dict))


@user.route('/modify_password', methods=['POST'])
def modify_password():
    input = request.form.get("data", {})
    ret, msg = 0, ""
    if input == {}:
        ret, msg = 1, u"资料不能为空！"
    else:
        input = json.loads(input)
        result = user_obj.modify_password(
                name=input.get("user_name", ""),
                old_password=input.get('old_pwd', ''),
                new_password=input.get('new_pwd', ''))
        if result:
            ret, msg = 0, ""
        else:
            ret, msg = 1, u"旧密码错误"
    resp_dict = dict()
    resp_dict['ret'] = ret
    resp_dict['msg'] = msg
    return Response(json.dumps(resp_dict))


@user.route('/get_user_list', methods=['GET'])
def get_user_list():
    resp_dict = dict()
    resp_dict['ret'] = 0
    resp_dict['msg'] = ""
    user_list = list()
    users = user_obj.get_user_list()
    for i in users:
        data = dict()
        data['user_id'] = i.user_id
        data['name'] = i.name
        data['create_time'] = i.create_time.strftime("%Y%m%d %H:%M:%S")
        user_list.append(data)
    resp_dict['data'] = user_list
    resp_dict['total'] = len(user_list)
    return Response(json.dumps(resp_dict))
