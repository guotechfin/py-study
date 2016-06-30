#!/bin/env python
# -*- coding:utf8 -*-

from wood_warehouse_list import WoodWarehouseList
from wood_warehouse_modify import WoodWarehouseModify
from wood_warehouse_new import WoodWarehouseNew
from wood_warehouse_del import WoodWarehouseDel
from common import conf

url = [
        ("/%s/wood_warehouse/list" % conf.SERVICE_NAME, WoodWarehouseList),
        ("/%s/wood_warehouse/new" % conf.SERVICE_NAME, WoodWarehouseNew),
        ("/%s/wood_warehouse/modify" % conf.SERVICE_NAME, WoodWarehouseModify),
        ("/%s/wood_warehouse/del" % conf.SERVICE_NAME, WoodWarehouseDel),
        ]
