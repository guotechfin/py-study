#!/bin/env python
# -*- coding:utf8 -*-


from wood_warehouse_model import WoodWarehouse
from common import utility
import datetime


class WoodWarehouseService(object):
    def search_wood_warehouse_list(
            self,
            session,
            wood_id=-1,
            wood_warehouse_id=-1
            warehouse_id=-1,
            purchase_summary_id=-1,
            purchase_detail_id=-1,
            finish=-1):
        wood_warehouse = session.query(WoodWarehouse)
        if wood_warehouse_id != -1:
            wood_warehouse = wood_warehouse.filter_by(
                    wood_warehouse_id=wood_warehouse_id)
        if wood_id != -1:
            wood_warehouse = wood_warehouse.filter_by(
                    wood_id=wood_id)
        if warehouse_id != -1:
            wood_warehouse = wood_warehouse.filter_by(
                    warehouse_id=warehouse_id)
        if purchase_summary_id != -1:
            wood_warehouse = wood_warehouse.filter_by(
                    purchase_summary_id=purchase_summary_id)
        if purchase_detail_id != -1:
            wood_warehouse = wood_warehouse.filter_by(
                    purchase_detail_id=purchase_detail_id)
        if finish != -1:
            wood_warehouse = wood_warehouse.filter(
                    WoodWarehouse.remain!=0)
        return wood_warehouse.all()

    def new_wood_warehouse(
            self,
            session,
            wood_id=-1,
            warehouse_id=-1,
            purchase_summary_id=-1,
            purchase_detail_id=-1,
            remain=0,
            create_date=""):
        if create_date == "":
            create_date = datetime.datetime.now()
        wood_warehouse = WoodWarehouse(
                wood_id=wood_id,
                warehouse_id=warehouse_id,
                purchase_summary_id=purchase_summary_id,
                purchase_detail_id=purchase_detail_id,
                remain=remain,
                dirty=0,
                create_date=create_date)
        session.add(wood_warehouse)

    def modify_wood_warehouse(
            self,
            session,
            purchase_summary_id=-1,
            purchase_detail_id=-1,
            create_date="",
            remain=0):
        if not self.check_purchase_summary(
                session,
                purchase_summary_id=purchase_summary_id,
                purchase_detail_id=purchase_detail_id):
            return False
        data = dict()
        if create_date != "":
            data['create_date'] = create_date
        if remain != 0:
            data['remain'] = remain
        wood_warehouse = session.query(WoodWarehouse)
        if purchase_summary_id != -1:
            wood_warehouse = wood_warehouse.filter_by(purchase_summary_id=purchase_summary_id)
        if purchase_detail_id != -1:
            wood_warehouse = wood_warehouse.filter_by(purchase_detail_id=purchase_detail_id)
        wood_warehouse.update(data)
        return True

    def update_wood_warehouse_remain(
            self,
            session,
            wood_warehouse_id=-1,
            wood_id=-1,
            warehouse_id=-1,
            purchase_detail_id=-1,
            wastage):
        wood_warehouse = session.query(WoodWarehouse)
        if wood_warehouse_id != -1:
            wood_warehouse = wood_warehouse.filter_by(id=wood_warehouse_id)
        elif wood_id != -1 and warehouse_id != -1:
            wood_warehouse = (wood_warehouse.
                    filter_by(wood_id=wood_id).
                    filter_by(warehouse_id=warehouse_id))
        elif purchase_detail_id != -1:
            wood_warehouse = wood_warehouse.filter_by(purchase_detail_id=purchase_detail_id)
        else:
            return False
        if wood_warehouse.first().remain >= wastage:
            wood_warehouse.update({WoodWarehouse.remain: WoodWarehouse.remain - remain})
            return True
        else:
            return False

    def del_wood_warehouse(
            self,
            session,
            purchase_summary_id=-1,
            purchase_detail_id=-1)
        if not self.check_purchase_summary(
                session,
                purchase_summary_id=purchase_summary_id,
                purchase_detail_id=purchase_detail_id):
            return False
        wood_warehouse = session.query(WoodWarehouse)
        if purchase_summary_id != -1:
            wood_warehouse = wood_warehouse.filter_by(
                    purchase_summary_id=purchase_summary_id)
        if purchase_detail_id != -1:
            wood_warehouse = wood_warehouse.filter_by(
                    purchase_detail_id=purchase_detail_id)
        wood_warehouse.delete()
        return True

    def check_wood_warehouse_dirty(
            self,
            session,
            wood_warehouse_id=-1,
            purchase_summary_id=-1,
            purchase_detail_id=-1):
        wood_warehouse_list = self.search_wood_warehouse_list(
                wood_warehouse_id=wood_warehouse_id,
                purchase_summary_id=purchase_summary_id,
                purchase_detail_id=purchase_detail_id)
        for i in wood_warehouse_list:
            if i.dirty == 1:
                return False
        return True
            

wood_warehouse_obj = WoodWarehouseService()
