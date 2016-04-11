#!/bin/env python
# -*-coding:utf-8-*-

import json
import datetime
import urllib2

from user_model import DBSession, User
from my_log import logger
import utility


class UserController(object):
    def new_user(self, name, password):
        session = DBSession()
        ret = True
        try:
            user = User(
                    name=name.strip(),
                    password=utility.make_pwd(password),
                    create_time=datetime.datetime.now())
            session.add(user)
            session.flush()
            session.commit()
        except Exception as e:
            ret = False
            session.rollback()
            logger.error("新建用户出错. %s" % e)
        session.close()
        return ret

    def modify_user(self, id, name, password):
        data = dict()
        data['name'] = name.strip()
        if password != "":
            data['password'] = utility.make_pwd(password)
        ret = True
        try:
            session = DBSession()
            session.query(User).filter_by(user_id=id).update(data)
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error("更新用户出错. %s" % e)
            ret = False
        session.close()
        return ret

    def get_user(self, id):
        session = DBSession()
        user = session.query(User).filter_by(user_id=id).first()
        session.commit()
        session.close()
        return user

    def get_user_by_name(self, name):
        session = DBSession()
        user = session.query(User).filter(User.name==name).first()
        session.commit()
        session.close()
        return user

    def get_user_list(self):
        session = DBSession()
        user_list = session.query(User).order_by(User.user_id.desc()).all()
        session.commit()
        session.close()
        return user_list

    def modify_password(self, name, old_password, new_password):
        session = DBSession()
        user = (session.query(User).
                filter(User.name == name).
                filter(User.password == utility.make_pwd(old_password)).
                first())
        if user != None:
            user.password = utility.make_pwd(new_password)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False


user_obj = UserController()
