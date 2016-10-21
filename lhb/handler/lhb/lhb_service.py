#!/bin/env python
# -*- coding:utf8 -*-


import tornado.gen
import tornado.httpclient
import json
from sqlalchemy import distinct

from lhb_model import LHB
from common import utility
from common import mylog


class LHBService(object):
    def search_lhb_list(
            self,
            session,
            date="",
            code="",
            exchange_division_id=-1,
            distinct_code=-1,
            distinct_date=-1,
            start=-1,
            end=-1):
        if distinct_code != -1:
            lhb = session.query(LHB.code).distinct()
        elif distinct_date != -1:
            lhb = session.query(LHB.date).distinct()
        else:
            lhb = session.query(LHB)
        if date != "":
            lhb = lhb.filter_by(date=date)
        if code != "":
            lhb = lhb.filter_by(code=code)
        if exchange_division_id != -1:
            lhb = lhb.filter_by(exchange_division_id=exchange_division_id)
        lhb = lhb.order_by("-id")
        if start == -1 and end == -1:
            return lhb.all()
        else:
            return lhb[start:end], lhb.count()

    def distinct_code(self, lhb_list):
        code_set = set()
        lhb_distinct_list = list()
        for i in lhb_list:
            if i.code not in code_set:
                code_set.add(i.code)
                lhb_distinct_list.append(i)
        return lhb_distinct_list

    def get_lhb_lastest_date(self, session):
        return session.query(LHB).order_by('-date').first().date.strftime("%Y%m%d")

    def del_lhb_data(self, session, date):
        session.query(LHB).filter_by(date=date).delete()
            

lhb_obj = LHBService()
