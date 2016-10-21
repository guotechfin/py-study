#!/bin/env python
# -*- coding:utf8 -*-


from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER,\
        TIMESTAMP, TINYINT, FLOAT, DOUBLE, NUMERIC

from common import Base, create_table, drop_table
from common import conf


class GroupMember(Base):
    # 帮派成员
    __tablename__ = 'group_member'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    exchange_division_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    user_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    group_id = Column(INTEGER(unsigned=True), nullable=False, server_default='0')
    remark = Column(String(500), nullable=False, server_default='')


if conf.DEBUG:
    create_table("group_member")
