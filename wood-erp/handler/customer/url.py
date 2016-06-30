#!/bin/env python
# -*- coding:utf8 -*-

from customer_list import CustomerList
from customer_modify import CustomerModify
from customer_new import CustomerNew
from customer_del import CustomerDel
from common import conf

url = [
        ("/%s/customer/list" % conf.SERVICE_NAME, CustomerList),
        ("/%s/customer/new" % conf.SERVICE_NAME, CustomerNew),
        ("/%s/customer/modify" % conf.SERVICE_NAME, CustomerModify),
        ("/%s/customer/del" % conf.SERVICE_NAME, CustomerDel),
        ]
