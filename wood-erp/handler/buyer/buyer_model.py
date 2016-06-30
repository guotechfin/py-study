#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table
from common import conf

class Buyer(Base):
    __tablename__ = 'buyer'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, server_default='')
    remark = Column(String(100), nullable=False, server_default='')
    # 0 存在
    # 1 删除
    flag = Column(INTEGER, nullable=False, server_default='0')

if conf.DEBUG:
    create_table("buyer")
