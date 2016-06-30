#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table
from common import conf

class PurchaseSummary(Base):
    __tablename__ = 'purchase_summary'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    buyer_id = Column(INTEGER, nullable=False, server_default='0')
    user_id = Column(INTEGER, nullable=False, server_default='0')
    create_date = Column(DateTime, nullable=False, server_default=text('NOW()'))
    # 购买费用
    purchase_charge = Column(NUMERIC(10, 2), nullable=False, server_default='0')
    # 卖出收入
    sale_charge = Column(NUMERIC(10, 2), nullable=False, server_default='0')
    remark = Column(String(200), nullable=False, server_default='')
    # 0 存在
    # 1 删除
    flag = Column(INTEGER, nullable=False, server_default='0')
    # 0 未审核
    # 1 审核通过
    review = Column(INTEGER, nullable=False, server_default='0')

if conf.DEBUG:
    create_table("purchase_summary")
