#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table
from common import conf

class Wood(Base):
    __tablename__ = 'wood'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, server_default='')
    # 等级
    grade = Column(String(100), nullable=False, server_default='')
    # 长 单位CM
    length = Column(INTEGER, nullable=False, server_default='0')
    # 宽 单位CM
    width = Column(INTEGER, nullable=False, server_default='0')
    # 高(厚度) 单位CM
    heigth = Column(INTEGER, nullable=False, server_default='0')
    # 规格(长度*宽度*高)
    size = Column(String(100), nullable=False, server_default='')
    # 条数
    number = Column(INTEGER, nullable=False, server_default='1')
    # 单扎平方米
    volumn = Column(NUMERIC(10, 2), nullable=False, server_default='0')
    # 剩余平方米
    remain = Column(NUMERIC(10, 2), nullable=False, server_default='0')
    # 0 存在
    # 1 删除
    flag = Column(INTEGER, nullable=False, server_default='0')

if conf.DEBUG:
    create_table("wood")
