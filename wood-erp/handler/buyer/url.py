#!/bin/env python
# -*- coding:utf8 -*-

from buyer_list import BuyerList
from buyer_modify import BuyerModify
from buyer_new import BuyerNew
from buyer_del import BuyerDel
from common import conf

url = [
        ("/%s/buyer/list" % conf.SERVICE_NAME, BuyerList),
        ("/%s/buyer/new" % conf.SERVICE_NAME, BuyerNew),
        ("/%s/buyer/modify" % conf.SERVICE_NAME, BuyerModify),
        ("/%s/buyer/del" % conf.SERVICE_NAME, BuyerDel),
        ]
