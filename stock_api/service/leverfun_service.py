#!/bin/env python
# -*- coding:utf8 -*-


from model.ticket import Ticket
import datetime
import urllib2
import json


class LeverfunApi(object):
    def get_stock_real_time_info(self, code):
        try:
            resp = urllib2.urlopen(
                    "https://app.leverfun.com/timelyInfo/timelyOrderForm?stockCode=%s" % code,
                    timeout=5)
            resp = json.loads(resp.read())
            ticket = self.create_ticket(code, resp['data'])
            return ticket
        except Exception as e:
            print e

    def create_ticket(self, code, data):
        ticket = Ticket()
        ticket.level2 = True
        ticket.code = code
        ticket.time = datetime.datetime.now().strftime("%H:%M:%S")
        ticket.price = data['match']
        ticket.b1_v = data['buyPankou'][0]['price']
        ticket.b1_p = int(data['buyPankou'][0]['volume'])
        ticket.b2_v = data['buyPankou'][1]['price']
        ticket.b2_p = int(data['buyPankou'][1]['volume'])
        ticket.b3_v = data['buyPankou'][2]['price']
        ticket.b3_p = int(data['buyPankou'][2]['volume'])
        ticket.b4_v = data['buyPankou'][3]['price']
        ticket.b4_p = int(data['buyPankou'][3]['volume'])
        ticket.b5_v = data['buyPankou'][4]['price']
        ticket.b5_p = int(data['buyPankou'][4]['volume'])
        ticket.b6_v = data['buyPankou'][5]['price']
        ticket.b6_p = int(data['buyPankou'][5]['volume'])
        ticket.b7_v = data['buyPankou'][6]['price']
        ticket.b7_p = int(data['buyPankou'][6]['volume'])
        ticket.b8_v = data['buyPankou'][7]['price']
        ticket.b8_p = int(data['buyPankou'][7]['volume'])
        ticket.b9_v = data['buyPankou'][8]['price']
        ticket.b9_p = int(data['buyPankou'][8]['volume'])
        ticket.b10_v = data['buyPankou'][9]['price']
        ticket.b10_p = int(data['buyPankou'][9]['volume'])
        ticket.a1_v = data['sellPankou'][0]['price']
        ticket.a1_p = int(data['sellPankou'][0]['volume'])
        ticket.a2_v = data['sellPankou'][1]['price']
        ticket.a2_p = int(data['sellPankou'][1]['volume'])
        ticket.a3_v = data['sellPankou'][2]['price']
        ticket.a3_p = int(data['sellPankou'][2]['volume'])
        ticket.a4_v = data['sellPankou'][3]['price']
        ticket.a4_p = int(data['sellPankou'][3]['volume'])
        ticket.a5_v = data['sellPankou'][4]['price']
        ticket.a5_p = int(data['sellPankou'][4]['volume'])
        ticket.a6_v = data['sellPankou'][5]['price']
        ticket.a6_p = int(data['sellPankou'][5]['volume'])
        ticket.a7_v = data['sellPankou'][6]['price']
        ticket.a7_p = int(data['sellPankou'][6]['volume'])
        ticket.a8_v = data['sellPankou'][7]['price']
        ticket.a8_p = int(data['sellPankou'][7]['volume'])
        ticket.a9_v = data['sellPankou'][8]['price']
        ticket.a9_p = int(data['sellPankou'][8]['volume'])
        ticket.a10_v = data['sellPankou'][9]['price']
        ticket.a10_p = int(data['sellPankou'][9]['volume'])
        ticket.name = ""
        return ticket


leverfun_obj = LeverfunApi()
