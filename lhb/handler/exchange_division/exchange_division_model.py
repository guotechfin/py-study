#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table, drop_table
from common import conf


class ExchangeDivision(Base):
    # 交易席位
    __tablename__ = 'exchange_division'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False, server_default='')
    

if conf.DEBUG:
    create_table("exchange_division")
