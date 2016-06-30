#!/bin/env python
# -*- coding:utf8 -*-

from warehouse_list import WarehouseList
from warehouse_modify import WarehouseModify
from warehouse_new import WarehouseNew
from warehouse_del import WarehouseDel
from common import conf

url = [
        ("/%s/warehouse/list" % conf.SERVICE_NAME, WarehouseList),
        ("/%s/warehouse/new" % conf.SERVICE_NAME, WarehouseNew),
        ("/%s/warehouse/modify" % conf.SERVICE_NAME, WarehouseModify),
        ("/%s/warehouse/del" % conf.SERVICE_NAME, WarehouseDel),
        ]
