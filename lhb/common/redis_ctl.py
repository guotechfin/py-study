#!/bin/env python
#-*- coding: UTF-8 -*-

import redis
import mylog

class Redis_db():
    def __init__(self, host='localhost', port=6379, db=0, socket_timeout=1):
        '''
        http://redis-py.readthedocs.org/en/latest/
        '''
        self.host = host
        self.port = port
        self.which_db = db
        self.socket_timeout = socket_timeout
        self.db = None
        self.connect_db()

    def connect_db(self):
        self.db = None
        try:
            self.db = redis.StrictRedis(
                host=self.host, 
                port=int(self.port),
                db = self.which_db,
                socket_timeout=self.socket_timeout,
                charset='utf-8'
            )
            mylog.logger.info("redis connected!")
            return True
        except Exception as err:
            mylog.logger.error("connect redis error: %s" % err)
            return False

    def is_db_connected(self):
        try:
            if self.db.ping() == True:
                return True
            else:
                return False
        except Exception as err:
            mylog.logger.error("redis is disconnect, err info: %s" % err)
        return False

    def check_connect(self):
        if not self.is_db_connected():
            if not self.connect_db():
                mylog.logger.error("redis is disconnect !!")
                return False
        return True

redis_db = Redis_db()

if __name__ == '__main__':
    if redis_db.check_connect():
        value = redis_db.db.get('test')
        mylog.logger.debug("result %s" % value)
