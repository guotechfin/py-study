#!/bin/env python
# -*- coding:utf8 -*-


from group_model import Group
from common import utility


class GroupService(object):
    def search_group_list(self, session, user_id=-1, start=-1, end=-1):
        group = session.query(Group)
        if user_id != -1:
            group = group.filter_by(user_id=user_id)
        if start == -1 and end == -1:
            return group.all(), group.count()
        else:
            return group[start:end], group.count()

    def get_group(self, session, id):
        return session.query(Group).get(id)

    def new_group(self, session, user_id=-1, name="", remark=""):
        group = Group(
                user_id=user_id,
                name=name.strip(),
                remark=remark.strip())
        session.add(group)

    def modify_group(self, session, id, name="", remark=""):
        session.query(Group).get(id).update({
            'name': name,
            'remark': remark})

    def del_group(self, session, id):
        session.query(Group).get(id).delete()


group_obj = GroupService()
