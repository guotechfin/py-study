#!/bin/env python
# -*- coding:utf8 -*-


import tornado.gen
import tornado.httpclient
import json
from sqlalchemy import distinct

from lhb_model import LHB
from common import utility
from common import mylog
from common import conf
from lhb_service import lhb_obj
from handler.exchange_division.exchange_division_service import division_obj


class LHBDataSourceService(object):
    @tornado.gen.coroutine
    def get_lhb_list_from_qq(self, session, date):
        http_client = tornado.httpclient.AsyncHTTPClient()
        url = (('http://stock.finance.qq.com'
                '/cgi-bin/sstock/q_lhb_js?'
                't=2&c=&b=%s&e=%s') % (date, date))
        response = yield http_client.fetch(url)
        b = response.body.find('[[')
        e = response.body.find(']]')
        if b == -1 or e == -1:
            mylog.logger.error("query qq lhb error url: %s" % url)
            raise tornado.gen.Return(False)
        data = json.loads(response.body[b:e+2].decode('gbk'))
        for i in data:
            if i[1][:2] not in ('00', '60', '30'):
                continue
            lhb_item = yield self.get_ticket_info_from_qq(session, i[1], date, i[4])
            if not lhb_item:
                raise tornado.gen.Return(False)
            lhb_item.date = i[0]
            lhb_item.reason = i[3]
            session.add(lhb_item)
        raise tornado.gen.Return(True)

    @tornado.gen.coroutine
    def get_ticket_info_from_qq(self, session, code, date, tx_l):
        http_client = tornado.httpclient.AsyncHTTPClient()
        url = (('http://stock.finance.qq.com'
                '/cgi-bin/sstock/q_lhb_xx_js?'
                'c=%s&b=%s&l=%s') % (code, date, tx_l))
        response = yield http_client.fetch(url)
        b = response.body.find('[[')
        e = response.body.find(']]')
        if b == -1 or e == -1:
            mylog.logger.error("query qq lhb detail error url: %s" % url)
            raise tornado.gen.Return(None)
        data = response.body[16:-2].decode('gbk')
        data = data.replace('_zrsp', '"_zrsp"')
        data = data.replace('_zdf', '"_zdf"')
        data = data.replace('_cjl', '"_cjl"')
        data = data.replace('_cje', '"_cje"')
        data = data.replace('_datas', '"_datas"')
        data = data.replace('_o', '"_o"')
        data = json.loads(data)
        lhb_item = LHB(code=code)
        lhb_item.ticket_name = data["_datas"][0][1]
        if data["_zdf"] == "" or data["_zdf"] == "--":
            data["_zdf"] = 0
        lhb_item.ticket_change_rate = float(data["_zdf"])
        if data["_zrsp"] == "" or data["_zrsp"] == "--":
            data["_zrsp"] = 0
        lhb_item.ticket_end_price = round(
                float(data["_zrsp"]) * (1 + lhb_item.ticket_change_rate / 100), 2)
        if data["_cje"] == "" or data["_cje"] == "--":
            data["_cje"] = 1
        lhb_item.ticket_transaction_amount = round(float(data["_cje"]) / 10000, 2)
        if data["_cjl"] == "" or data["_cjl"] == "--":
            data["_cjl"] = 1
        lhb_item.ticket_transaction_volume = float(data["_cjl"])
        for i in data["_datas"]:
            if i[5].find(u"机构") != -1:
                i[5] = "机构专用"
            if i[6] == '--':
                i[6] = 0
            if i[7] == '--':
                i[7] = 0
            if i[2] == 'B':
                if i[3] == '1':
                    lhb_item.b_1_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.b_1_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.b_1_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
                if i[3] == '2':
                    lhb_item.b_2_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.b_2_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.b_2_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
                if i[3] == '3':
                    lhb_item.b_3_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.b_3_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.b_3_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
                if i[3] == '4':
                    lhb_item.b_4_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.b_4_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.b_4_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
                if i[3] == '5':
                    lhb_item.b_5_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.b_5_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.b_5_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
            if i[2] == 'S':
                if i[3] == '1':
                    lhb_item.a_1_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.a_1_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.a_1_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
                if i[3] == '2':
                    lhb_item.a_2_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.a_2_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.a_2_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
                if i[3] == '3':
                    lhb_item.a_3_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.a_3_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.a_3_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
                if i[3] == '4':
                    lhb_item.a_4_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.a_4_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.a_4_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
                if i[3] == '5':
                    lhb_item.a_5_buy_transaction_amount = float(i[6]) / 10000
                    lhb_item.a_5_sale_transaction_amount = float(i[7]) / 10000
                    lhb_item.a_5_exchange_division_id = (
                            division_obj.get_exchange_division_id(session, i[5]))
        raise tornado.gen.Return(lhb_item)

    @tornado.gen.coroutine
    def get_lhb_list_from_jys(self, session, date):
        yield [self.get_lhb_list_from_sz(session, date),
                self.get_lhb_list_from_sh(session, date)]


    @tornado.gen.coroutine
    def get_lhb_list_from_sz(self, session, date):
        # 深交所龙虎榜数据
        http_client = tornado.httpclient.AsyncHTTPClient()
        # 深圳证券市场中小企业板交易公开信息
        url = ('http://www.szse.cn/szseWeb/common/szse/'
                'files/text/smeTxt/gk/sme_jy%s.txt' % date[2:])
        # 深圳证券市场创业板交易公开信息 
        url = ('http://www.szse.cn/szseWeb/common/szse/'
                'files/text/nmTxt/gk/nm_jy%s.txt' % date[2:])
        # 深圳证券市场主板A股交易公开信息
        url = ('http://www.szse.cn/szseWeb/common/szse'
                '/files/text/jy/jy%s.txt' % date[2:])
        response = yield http_client.fetch(url)
        print response.body.decode("gbk")

    def analyse_lhb_from_sz(self, session, date, content):
        s = content.find(u'证券代码')
        e = content[s:].find(u'--------------')
        ticket_list = list()
        for i in content[s:s+e].split('\r\n')[1:]:
            tmp = list()
            for j in i.split(' '):
                if j:
                    tmp.append(j)
            ticket_list.append(tmp)

            

            
    @tornado.gen.coroutine
    def get_lhb_list_from_sh(self, session, date):
        # 上交所龙虎榜数据
        http_client = tornado.httpclient.AsyncHTTPClient()
        url = ('http://query.sse.com.cn/infodisplay/showTradePublicFile.do?'
                'isPagination=false&dateTx=%s-%s-%s' % 
                (date[:4], date[4:6], date[6:8]))
        headers = dict()
        headers['Referer'] = 'http://www.sse.com.cn/disclosure/diclosure/public/'
        headers['User-Agent'] = conf.USER_AGENT
        response = yield http_client.fetch(url, headers=headers)
        #print response.body

lhb_data_source_obj = LHBDataSourceService()
