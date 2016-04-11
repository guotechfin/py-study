#!/bin/env python
# -*-coding:utf-8-*-

import sys
sys.path.append("views")
sys.path.append("common")
sys.path.append("models")
sys.path.append("controllers")
sys.path.append("conf")

from flask import Flask
from user_view import user
from token_view import token
from profile_view import profile

app = Flask(__name__)
app.register_blueprint(user, 
        url_prefix="/user_profile/v1/user")
app.register_blueprint(profile, 
        url_prefix="/user_profile/v1/profile")
app.register_blueprint(token, 
        url_prefix="/user_profile/v1/token")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8089, debug=True)
