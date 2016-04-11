#!/bin/env python
# -*- coding:utf8 -*-

from datetime import datetime
import time
import conf

from sqlalchemy import Integer, Column, String
from sqlalchemy import create_engine, UniqueConstraint, text
from sqlalchemy import ForeignKey
from sqlalchemy import func, or_, not_
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, MetaData, \
        Integer, String, DateTime, Unicode, Float
from sqlalchemy.dialects.mysql import INTEGER, TIMESTAMP, TINYINT, FLOAT, DOUBLE
from sqlalchemy.pool import NullPool


Base = declarative_base()


class User(Base):
    __tablename__ = 'profile_user'
    user_id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, server_default='')
    password = Column(String(50), nullable=False, server_default='')
    create_time = Column(DateTime, nullable=False)


connect_sql = ("mysql://%s:%s@%s:%s/%s?charset=utf8" % 
        (conf.mysql_user, conf.mysql_pwd,
            conf.host, conf.port, conf.mysql_db))
engine = create_engine(
        connect_sql, encoding='utf-8', echo=True,
        poolclass=NullPool)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, expire_on_commit=False)
