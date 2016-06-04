#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE

from common import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_name = Column(String(100), nullable=False, unique=True, server_default='')
    real_name = Column(String(100), nullable=False, server_default='')
    pwd = Column(String(100), nullable=False, server_default='')
    phone = Column(String(100), nullable=False, server_default='')
    email = Column(String(100), nullable=False, server_default='')
    create_date = Column(DateTime, nullable=False, server_default=text('NOW()'))
    # 0 在职
    # 1 离职
    flag = Column(INTEGER, nullable=False, server_default='0')
