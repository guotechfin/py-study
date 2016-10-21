#!/bin/env python
# -*- coding:utf8 -*-

from group_list import GroupList
from group_modify import GroupModify
from group_new import GroupNew
from group_del import GroupDel
from common import conf

url = [
        ("/%s/group/list" % conf.SERVICE_NAME, GroupList),
        ("/%s/group/new" % conf.SERVICE_NAME, GroupNew),
        ("/%s/group/modify" % conf.SERVICE_NAME, GroupModify),
        ("/%s/group/del" % conf.SERVICE_NAME, GroupDel),
        ]
