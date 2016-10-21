#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table, drop_table
from common import conf


class Group(Base):
    # 龙虎榜组（分帮派）
    __tablename__ = 'lhb_group'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    name = Column(String(500), nullable=False, server_default='')
    remark = Column(String(500), nullable=False, server_default='')
    

if conf.DEBUG:
    create_table("lhb_group")
