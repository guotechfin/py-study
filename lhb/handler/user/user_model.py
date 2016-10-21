#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE

from common import Base, create_table
from common import conf

class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_name = Column(String(100), nullable=False, unique=True, server_default='')
    pwd = Column(String(100), nullable=False, server_default='')
    phone = Column(String(100), nullable=False, server_default='')
    email = Column(String(100), nullable=False, server_default='')
    create_date = Column(DateTime, nullable=False, server_default=text('NOW()'))
    # 0 正常情况
    # 1 异常被注销
    flag = Column(INTEGER, nullable=False, server_default='0')

if conf.DEBUG:
    create_table("user")
