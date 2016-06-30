#!/bin/env python
# -*- coding:utf8 -*-

from wood_list import WoodList
from wood_modify import WoodModify
from wood_new import WoodNew
from wood_del import WoodDel
from common import conf

url = [
        ("/%s/wood/list" % conf.SERVICE_NAME, WoodList),
        ("/%s/wood/new" % conf.SERVICE_NAME, WoodNew),
        ("/%s/wood/modify" % conf.SERVICE_NAME, WoodModify),
        ("/%s/wood/del" % conf.SERVICE_NAME, WoodDel),
        ]
