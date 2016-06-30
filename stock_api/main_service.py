#!/bin/env python
# -*- coding:utf8 -*-


from apscheduler.schedulers.blocking import BlockingScheduler
from service.sina_stock_service import sina_obj

if __name__ == "__main__":
    sina_obj.get_stock_real_time_info('002560')
