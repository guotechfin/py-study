#!/bin/env python
# -*- coding:utf8 -*-


from purchase_summary_model import PurchaseSummary
from common import utility
import datetime


class PurchaseSummaryService(object):
    def get_purchase_summary_list(
            self,
            session,
            start=-1,
            end=-1,
            start_date="",
            end_date="",
            buyer_id=-1,
            review=-1,
            flag=0):
        purchase_summary = (session.query(PurchaseSummary).
                filter_by(flag=flag))
        if start_date != "" and end_date != "":
            purchase_summary = (purchase_summary.
                    filter_by(create_date >= start_date).
                    filter_by(create_date <= end_date))
        if buyer_id != -1:
            purchase_summary = (purchase_summary.
                    filter_by(buyer_id=buyer_id))
        if review != -1:
            purchase_summary = (purchase_summary.
                    filter_by(review=review))
        if start == -1 and end == -1:
            return purchase_summary.all()
        else:
            return purchase_summary[start:end], purchase_summary.count()

    def new_purchase_summary(
            self,
            session,
            buyer_id=-1,
            user_id=-1,
            create_date="",
            remark=""):
        if create_date == "":
            create_date = datetime.datetime.now()
        purchase_summary = PurchaseSummary(
                buyer_id=buyer_id,
                user_id=user_id,
                create_date=create_date,
                remark=remark.strip(),
                purchase_charge=0,
                sale_charge=0,
                flag=0,
                review=0)
        session.add(purchase_summary)
        session.flush()
        return purchase_summary.id

    def modify_purchase_summary(
            self,
            session,
            purchase_summary_id=-1,
            buyer_id=-1,
            create_date="",
            remark=""):
        if self.check_purchase_summary(session, purchase_summary_id):
            return False
        if create_date == "":
            create_date = datetime.datetime.now()
        data = dict()
        data['buyer_id'] = buyer_id
        data['create_date'] = create_date
        data['remark'] = remark.strip()
        (session.query(PurchaseSummary).
                filter_by(id=purchase_summary_id).update(data))
        return True

    def del_purchase_summary(self, session, purchase_summary_id):
        if self.check_purchase_summary(session, purchase_summary_id):
            return False
        (session.query(PurchaseSummary).
                filter_by(id=purchase_summary_id).
                update({PurchaseSummary.flag: 1}))
        return True

    def check_purchase_summary(self, session, purchase_summary_id):
        p = (session.query(PurchaseSummary).
                filter_by(id=purchase_summary_id).first())
        if p.review == 1:
            return True
        else:
            return False

    def change_purchase_review(self, session, purchase_summary_id):
        data = dict()
        if self.check_purchase_summary(session, purchase_summary_id):
            data['review'] = 0
        else:
            data['review'] = 1
        (session.query(PurchaseSummary).
                filter_by(id=purchase_summary_id).update(data))
            

    def update_purchase_charge(
            self,
            session,
            purchase_summary_id=-1,
            purchase_charge=-1,
            sale_charge=-1):
        if self.check_purchase_summary(session, purchase_summary_id):
            return False
        data = dict()
        if purchase_charge != -1:
            data['purchase_charge'] = purchase_charge
        if sale_charge != -1:
            data['sale_charge'] = sale_charge
        (session.query(PurchaseSummary).
                filter_by(id=purchase_summary_id).update(data))
        return True


purchase_summary_obj = PurchaseSummaryService()
