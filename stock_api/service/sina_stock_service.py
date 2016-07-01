#!/bin/env python
# -*- coding:utf8 -*-


import requests
from model.ticket import Ticket


class SinaApi(object):
    def get_stock_real_time_info(self, code):
        if code[:1] == '6':
            code_prefix = 'sh'
        else:
            code_prefix = 'sz'
        try:
            resp = requests.get("http://hq.sinajs.cn/list=%s%s" %
                    (code_prefix, code), timeout=1)
            info = resp.text.split('"')[1]
            info = info.split(',')
            ticket = Ticket()
            ticket.code = code
            ticket.time = info[31]
            ticket.volumns = int(info[8])
            ticket.price = float(info[9])
            ticket.b1_v = int(info[10])
            ticket.b1_p = float(info[11])
            ticket.b2_v = int(info[12])
            ticket.b2_p = float(info[13])
            ticket.b3_v = int(info[14])
            ticket.b3_p = float(info[15])
            ticket.b4_v = int(info[16])
            ticket.b4_p = float(info[17])
            ticket.b5_v = int(info[18])
            ticket.b5_p = float(info[19])
            ticket.a1_v = int(info[20])
            ticket.a1_p = float(info[21])
            ticket.a2_v = int(info[22])
            ticket.a2_p = float(info[23])
            ticket.a3_v = int(info[24])
            ticket.a3_p = float(info[25])
            ticket.a4_v = int(info[26])
            ticket.a4_p = float(info[27])
            ticket.a5_v = int(info[28])
            ticket.a5_p = float(info[29])
            ticket.name = info[0]
            return ticket
        except Exception as e:
            print e
            return None


sina_obj = SinaApi()
