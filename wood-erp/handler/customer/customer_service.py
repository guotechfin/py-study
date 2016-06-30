#!/bin/env python
# -*- coding:utf8 -*-


from customer_model import Customer
from common import utility


class CustomerService(object):
    def search_customer_list(
            self,
            session,
            customer_id=-1,
            start=-1,
            end=-1,
            flag=0):
        customer = session.query(Customer)
        if customer_id != -1:
            customer = customer.filter_by(id=customer_id)
        if flag != -1:
            customer = customer.filter_by(flag=flag)
        if start == -1 and end == -1:
            return customer.all()
        else:
            return customer[start:end], customer.count()

    def new_customer(self, session, name="", remark=""):
        customer = Customer(
                name=name.strip(),
                remark=remark.strip(),
                flag=0)
        session.add(customer)

    def modify_customer(self, session, customer_id, name="", remark=""):
        data = dict()
        data['name'] = name.strip()
        data['remark'] = remark.strip()
        (session.query(Customer).
                filter_by(id=customer_id).update(data))

    def del_customer(self, session, customer_id):
        (session.query(Customer).
                filter_by(id=customer_id).
                update({Customer.flag: 1}))


customer_obj = CustomerService()
