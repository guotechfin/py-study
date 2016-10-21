#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table, drop_table
from common import conf


class LHB(Base):
    __tablename__ = 'lhb'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False, server_default=text('NOW()'))
    # 上榜理由
    reason = Column(String(500), nullable=False, server_default='')
    code = Column(String(50), nullable=False, server_default='')
    ticket_name = Column(String(50), nullable=False, server_default='')
    # 收盘价
    ticket_end_price = Column(NUMERIC(10, 2), nullable=False, server_default='0')
    # 收盘涨跌幅
    ticket_change_rate = Column(NUMERIC(10, 2), nullable=False, server_default='0')
    # 成交金额 单位万
    ticket_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    # 成交量 单位手
    ticket_transaction_volume = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    # 卖
    a_1_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    # 单位万
    a_1_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_1_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_2_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    a_2_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_2_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_3_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    a_3_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_3_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_4_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    a_4_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_4_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_5_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    a_5_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    a_5_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    # 买
    b_1_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    b_1_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_1_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_2_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    b_2_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_2_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_3_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    b_3_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_3_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_4_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    b_4_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_4_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_5_exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    b_5_buy_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')
    b_5_sale_transaction_amount = Column(NUMERIC(14, 2), nullable=False, server_default='0')


if conf.DEBUG:
    create_table("lhb")
