#!/bin/env python
# -*- coding:utf8 -*-


from buyer_model import Buyer
from common import utility


class BuyerService(object):
    def search_buyer_list(
            self,
            session,
            buyer_id=-1,
            start=-1,
            end=-1,
            flag=0):
        buyer = session.query(Buyer)
        if buyer_id != -1:
            buyer = buyer.filter_by(id=buyer_id)
        if flag != -1:
            buyer = buyer.filter_by(flag=flag)
        if start == -1 and end == -1:
            return buyer.all()
        else:
            return buyer[start:end], buyer.count()

    def new_buyer(self, session, name="", remark=""):
        buyer = Buyer(
                name=name.strip(),
                remark=remark.strip(),
                flag=0)
        session.add(buyer)

    def modify_buyer(self, session, buyer_id, name="", remark=""):
        data = dict()
        data['name'] = name.strip()
        data['remark'] = remark.strip()
        (session.query(Buyer).
                filter_by(id=buyer_id).update(data))

    def del_buyer(self, session, buyer_id):
        (session.query(Buyer).
                filter_by(id=buyer_id).
                update({Buyer.flag: 1}))


buyer_obj = BuyerService()
