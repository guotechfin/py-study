#!/bin/env python
# -*- coding:utf8 -*-


import tornado.gen
import tornado.httpclient

from ticket_model import Ticket


class SinaApi(object):
    @tornado.gen.coroutine
    def get_stock_real_time_info(self, code_list):
        single = False
        if not isinstance(code_list, list):
            single = True
            code_list = [code_list]
        code_name_list = list()
        ticket_list = list()
        for code in code_list:
            if code[:1] == '6':
                code_prefix = 'sh'
            else:
                code_prefix = 'sz'
            code_name_list.append("%s%s" % (code_prefix, code))
        http_client = tornado.httpclient.AsyncHTTPClient()
        try:
            url = "http://hq.sinajs.cn/list=%s" % (",".join(code_name_list))
            response = yield http_client.fetch(url)
            resp = response.body.strip().decode('gbk')
            for i in resp.split('\n'):
                ticket_list.append(self.create_ticket(i.strip()))
        except Exception as e:
            print e
        if single:
            raise tornado.gen.Return(ticket_list[0])
        else:
            raise tornado.gen.Return(ticket_list)

    def create_ticket(self, sina_text):
        code = sina_text.split('"')[0][-7:-1]
        info = sina_text.split('"')[1]
        info = info.split(',')
        ticket = Ticket()
        ticket.code = code
        ticket.time = info[31]
        ticket.name = info[0]
        ticket.change_rate = round(
                ((float(info[3]) - float(info[2])) / float(info[2])) * 100, 2)
        ticket.volume = int(info[8])
        ticket.price = float(info[3])
        ticket.transacation_amount = float(info[9]) / 10000
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
        return ticket


sina_obj = SinaApi()
