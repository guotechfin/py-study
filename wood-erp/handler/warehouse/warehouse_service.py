#!/bin/env python
# -*- coding:utf8 -*-


from warehouse_model import Warehouse
from common import utility


class WarehouseService(object):
    def search_warehouse_list(
            self,
            session,
            warehouse_id=-1,
            start=-1,
            end=-1,
            flag=0):
        warehouse = session.query(Warehouse)
        if warehouse_id != -1:
            warehouse = warehouse.filter_by(id=warehouse_id)
        if flag != -1:
            warehouse = warehouse.filter_by(flag=flag)
        if start == -1 and end == -1:
            return warehouse.all()
        else:
            return warehouse[start:end], warehouse.count()

    def new_warehouse(self, session, name=""):
        warehouse = Warehouse(name=name.strip(), flag=0)
        session.add(warehouse)

    def modify_warehouse(self, session, warehouse_id, name=""):
        data = dict()
        data['name'] = name.strip()
        (session.query(Warehouse).
                filter_by(id=warehouse_id).update(data))

    def del_warehouse(self, session, warehouse_id):
        (session.query(Warehouse).
                filter_by(id=warehouse_id).
                update({Warehouse.flag: 1}))


warehouse_obj = WarehouseService()
