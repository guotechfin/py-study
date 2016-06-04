#!/bin/env python
# -*- coding:utf8 -*-


from user_model import User
from common import utility

class UserService(object):
    def get_user_list(
            self,
            session,
            start=-1,
            end=-1,
            flag=0):
        user = session.query(User)
        if start == -1 and end == -1:
            return user.all()
        else:
            user = user.filter_by(flag=flag)
            user_list = user[start:end]
            return user_list, user.count()

    def new_user(
            self,
            session,
            user_name,
            real_name="",
            pwd="",
            phone="",
            email=""):
        user = User(user_name=user_name,
                real_name=real_name,
                pwd=utility.make_pwd(pwd),
                phone=phone,
                email=email)
        session.add(user)

    def modify_user(
            self,
            session,
            user_id,
            user_name="",
            real_name="",
            pwd="",
            phone="",
            email="",
            flag=0):
        data = dict()
        data['user_name'] = str(user_name).strip()
        data['real_name'] = str(real_name).strip()
        data['phone'] = str(phone).strip()
        data['email'] = str(email).strip()
        data['flag'] = flag
        if pwd:
            data['pwd'] = utility.make_pwd(pwd)
        session.query(User).filter_by(id=user_id).update(data)

    def check_pwd(self, session, user_name, pwd):
        user = (session.query(User).
                filter_by(user_name=user_name).
                filter_by(pwd=utility.make_pwd(pwd)).
                first())
        return user


user_obj = UserService()
