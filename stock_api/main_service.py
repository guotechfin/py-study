#!/bin/env python
# -*- coding:utf8 -*-

import gevent
from gevent import monkey
monkey.patch_socket()


from service.sina_stock_service import sina_obj
from apscheduler.schedulers.blocking import BlockingScheduler
from common import mylog
from common import conf
import time
import signal



def track_job():
    def task(code):
        ticket = sina_obj.get_stock_real_time_info(code)
        if ticket and ticket.large_volumns():
            print ticket
    t = time.time()
    threads = [gevent.spawn(task, i) for i in conf.TICKET_LIST]
    gevent.joinall(threads)
    print time.time() - t

if __name__ == "__main__":
    gevent.signal(signal.SIGQUIT, gevent.kill)
    sched = BlockingScheduler()
    #sched.add_job(track_job, 'interval', seconds=2)
    #sched.start()
    track_job()
