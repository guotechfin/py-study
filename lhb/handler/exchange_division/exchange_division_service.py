#!/bin/env python
# -*- coding:utf8 -*-


from exchange_division_model import ExchangeDivision
from common import utility


class ExchangeDivisionService(object):
    def new_exchange_division(self, session, name=""):
        exchange_division = ExchangeDivision(name=name.strip())
        session.add(exchange_division)

    def get_exchange_division_id(self, session, name=''):
        division = (session.query(ExchangeDivision).
                filter_by(name=name).first())
        if division:
            return division.id
        division = ExchangeDivision(name=name.strip())
        session.add(division)
        session.flush()
        return division.id

    def get_exchange_division(self, session, id):
        return session.query(ExchangeDivision).get(id)


division_obj = ExchangeDivisionService()
