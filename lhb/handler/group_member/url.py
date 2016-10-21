#!/bin/env python
# -*- coding:utf8 -*-

from group_member_list import GroupMemberList
from group_member_modify import GroupMemberModify
from group_member_new import GroupMemberNew
from group_member_del import GroupMemberDel
from common import conf

url = [
        ("/%s/group_member/list" % conf.SERVICE_NAME, GroupMemberList),
        ("/%s/group_member/new" % conf.SERVICE_NAME, GroupMemberNew),
        ("/%s/group_member/modify" % conf.SERVICE_NAME, GroupMemberModify),
        ("/%s/group_member/del" % conf.SERVICE_NAME, GroupMemberDel),
        ]
