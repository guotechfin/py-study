#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table
from common import conf

class Authorization(Base):
    __tablename__ = 'authorization'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, nullable=False, server_default='0')
    right_id = Column(INTEGER, nullable=False, server_default='0')

if conf.DEBUG:
    create_table("authorization")
