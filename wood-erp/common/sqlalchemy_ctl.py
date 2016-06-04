#!/bin/env python
# -*- coding:utf8 -*-

from datetime import datetime
import time
import conf

from sqlalchemy import Integer, Column, String, create_engine, UniqueConstraint, text
from sqlalchemy import ForeignKey
from sqlalchemy import func, or_, not_
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, MetaData, \
        Integer, String, DateTime, Unicode, Float
from sqlalchemy.dialects.mysql import INTEGER, TIMESTAMP, TINYINT, FLOAT, DOUBLE
from sqlalchemy.pool import NullPool
from common.mylog import logger

if conf.debug:
    # 执行赋mysql权限
    connect_sql = ("mysql://%s:%s@127.0.0.1:3306/%s?charset=utf8" % 
            ('root', '', ''))
    engine = create_engine(connect_sql, encoding='utf-8', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    sql = text('create database if not exists %s;' % conf.mysql_db)
    data = session.execute(sql)
    sql = text('select * from mysql.user where User = :user;')
    data = session.execute(sql, {"user": conf.mysql_user})
    if data.rowcount == 0:
        sql = ('grant all on %s.* to %s@127.0.0.1;' % 
                (conf.mysql_db, conf.mysql_user))
        data = session.execute(text(sql))
        sql = text('set password for %s@127.0.0.1=password("%s");' % 
                (conf.mysql_user, conf.mysql_pwd))
        data = session.execute(sql)
        sql = text('FLUSH PRIVILEGES')
        data = session.execute(sql)

        #sql = text('drop user %s@127.0.0.1;' % conf.mysql_user)
        #data = session.execute(sql)
        #sql = text('drop database if exists %s;' % conf.mysql_db)
        #data = session.execute(sql)
    session.close_all()

Base = declarative_base()
connect_sql = ("mysql://%s:%s@127.0.0.1:3306/%s?charset=utf8" % 
        (conf.mysql_user, conf.mysql_pwd, conf.mysql_db))
if conf.debug:
    engine = create_engine(
            connect_sql,
            encoding='utf-8',
            echo="debug",
            echo_pool="debug")
else:
    engine = create_engine(
            connect_sql,
            encoding='utf-8')
DBSession = sessionmaker(bind=engine)
