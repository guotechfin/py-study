#!/bin/env python
# -*-coding:utf-8-*-

import json

from flask import Blueprint, request, Response
from flask import render_template
from user_controller import user_obj
from user_profile_controller import user_profile_obj
from my_log import logger
import utility
from flask import redirect


profile = Blueprint("profile", __name__)


@profile.route('/index.html', methods=['GET'])
def index():
    user_id = request.cookies.get('user_id')
    user_name = request.cookies.get('user_name')
    user_token = request.cookies.get('user_token')
    if user_id == "" or user_token == "":
        return redirect("/user_profile/v1/token/login")
    if not utility.check_token(user_id, user_token):
        return redirect("/user_profile/v1/token/login")
    type = request.args.get("type", "")
    content = request.args.get("content", "")
    if type and content:
        if type == "mac":
            content = content.upper()
        infoJson, geoJson = user_profile_obj.get_user_profile(type, content)
    return render_template('index.html', **locals())
