#!/bin/env python
# -*- coding:utf8 -*-


from user_model import User
from common import utility

class UserService(object):
    def search_user_list(
            self,
            session,
            user_id=-1,
            start=-1,
            end=-1,
            flag=0):
        user = session.query(User)
        if user_id != -1:
            user = user.filter_by(id=user_id)
        if flag != -1:
            user = user.filter_by(flag=flag)
        if start == -1 and end == -1:
            return user.all()
        else:
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
        user = User(user_name=user_name.strip(),
                real_name=real_name.strip(),
                pwd=utility.make_pwd(pwd),
                phone=phone.strip(),
                email=email.strip())
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
        data['user_name'] = user_name.strip()
        data['real_name'] = real_name.strip()
        data['phone'] = phone.strip()
        data['email'] = email.strip()
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
