#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table
from common import conf

class WoodWarehouse(Base):
    __tablename__ = 'wood_warehouse'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    wood_id = Column(INTEGER, nullable=False, server_default='0')
    warehouse_id = Column(INTEGER, nullable=False, server_default='0')
    purchase_summary_id = Column(INTEGER, nullable=False, server_default='0')
    purchase_detail_id = Column(INTEGER, nullable=False, server_default='0')
    # 剩余平方米
    remain = Column(NUMERIC(10, 2), nullable=False, server_default='0')
    # 0 没有销售卖出过(没有脏)
    # 1 销售卖出过，以后不能撤回
    dirty = Column(INTEGER, nullable=False, server_default='0')
    create_date = Column(DateTime, nullable=False, server_default=text('NOW()'))

if conf.DEBUG:
    create_table("wood_warehouse")
