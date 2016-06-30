#!/bin/env python
# -*- coding:utf8 -*-


import requests

class SinaApi(object):
    def get_stock_real_time_info(self, code):
        if code[:1] == '6':
            code_prefix = 'sh'
        else:
            code_prefix = 'sz'
        headers = dict()
        headers['User-Agent'] = ('Mozilla/5.0 (Windows NT 6.1; WOW64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/51.0.2704.103 Safari/537.36')
        headers['Accept'] = ('text/html,application/xhtml+xml,'
                'application/xml;q=0.9,image/webp,*/*;q=0.8')
        headers['Accept-Encoding'] = 'gzip, deflate, sdch'
        headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
        headers['Upgrade-Insecure-Requests'] = '1'
        resp = requests.get("http://hq.sinajs.cn/list=%s%s" %
                (code_prefix, code), headers=headers)
        print resp


sina_obj = SinaApi()
