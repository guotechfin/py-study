#!/bin/env python
# -*- coding:utf8 -*-

import gevent
from gevent import monkey
monkey.patch_socket()


from service.sina_stock_service import sina_obj
from service.leverfun_service import leverfun_obj
from apscheduler.schedulers.blocking import BlockingScheduler
from common import mylog
from common import conf
import time
import signal



def sina_track_job():
    def task(code):
        ticket_list = sina_obj.get_stock_real_time_info(code)
        for i in ticket_list:
            if i.show():
                print i
    t = time.time()
    threads = list()
    size = len(conf.TICKET_LIST)/conf.QUERY_NUM
    for i in xrange(0, size):
        start = i*conf.QUERY_NUM
        if i == size:
            end = len(conf.TICKET_LIST)
        else:
            end = start + conf.QUERY_NUM
        threads.append(gevent.spawn(task, conf.TICKET_LIST[start:end]))
    gevent.joinall(threads)
    print time.time() - t


def leverfun_track_job():
    def task(code):
        ticket = leverfun_obj.get_stock_real_time_info(code)
        if ticket.show():
            print ticket
    t = time.time()
    threads = list()
    for i in conf.TICKET_LIST:
        task(i)
    print time.time() - t
        


if __name__ == "__main__":
    gevent.signal(signal.SIGQUIT, gevent.kill)
    sched = BlockingScheduler()
    #sched.add_job(sina_track_job, 'interval', seconds=2)
    #sched.start()
    sina_track_job()
    #leverfun_track_job()
