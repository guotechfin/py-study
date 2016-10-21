#!/bin/env python
# -*- coding:utf8 -*-


from group_member_model import GroupMember
from common import utility


class GroupMemberService(object):
    def search_group_member_list(
            self,
            session,
            group_id=-1,
            division_id=-1,
            user_id=-1):
        group_member = session.query(GroupMember)
        if group_id != -1:
            group_member = group_member.filter_by(group_id=group_id)
        if division_id != -1:
            group_member = group_member.filter_by(
                    exchange_division_id=division_id)
        if user_id != -1:
            group_member = group_member.filter_by(
                    user_id=user_id)
        return group_member.all()

    def new_group_member(
            self,
            session,
            group_id=-1,
            division_id=-1,
            user_id=-1,
            remark=""):
        group_member = GroupMember(
                group_id=group_id,
                exchange_division_id=division_id,
                user_id=user_id,
                remark=remark.strip())
        session.add(group_member)

    def modify_group_member(
            self,
            session,
            id,
            group_id=-1,
            division_id=-1,
            remark=""):
        session.query(GroupMember).get(id).update({
            'group_id': group_id,
            'exchange_division_id': division_id,
            'remark': remark
            })

    def del_group_member(
            self,
            session,
            group_id,
            division_id,
            user_id):
        group_member = self.search_group_member_list(
                session=session,
                group_id=group_id,
                division_id=division_id,
                user_id=user_id)
        group_member.delete()


group_member_obj = GroupMemberService()
