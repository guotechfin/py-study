#!/bin/env python
# -*- coding:utf8 -*-


from authorization_model import Authorization
from common import conf


class AuthorizationService(object):
    def search_authorization_user_list(
            self,
            session,
            user_id):
        return (session.query(Authorization).
                filter_by(user_id=user_id).all())

    def change_authorization(self, session, user_id=-1, right_id=-1):
        if self.check_authorization(session, user_id, right_id):
            (session.query(Authorization).
                    filter_by(user_id=user_id).
                    filter_by(right_id=right_id).
                    delete())
        else:
            authorization = Authorization(
                    user_id=user_id,
                    right_id=right_id)
            session.add(authorization)

    def check_authorization(self, session, user_id=-1, right_id=-1):
        if user_id in conf.SUPPER_USER:
            return True
        right = (session.query(Authorization).
                filter_by(user_id=user_id).
                filter_by(right_id=right_id).
                first())
        if right:
            return True
        else:
            return False
        

authorization_obj = AuthorizationService()
