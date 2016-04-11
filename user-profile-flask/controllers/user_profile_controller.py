#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import thriftpy
from conf import DATA_HOST, DATA_PORT
from my_log import logger
import json

from thriftpy.protocol import TCyBinaryProtocolFactory
from thriftpy.transport import TCyBufferedTransportFactory
from thriftpy.rpc import make_client


pkg_path = os.path.abspath(os.path.dirname(__file__))
thrift_path = os.path.join(pkg_path, 'user_profile.thrift')


class UserProfileController(object):
    def connect_data_source(self):
        user_profile_thrift = thriftpy.load(
                thrift_path,
                module_name="user_profile_thrift")
        return make_client(
            user_profile_thrift.UserProfileServiceV2,
            DATA_HOST,
            DATA_PORT,
            proto_factory=TCyBinaryProtocolFactory(),
            trans_factory=TCyBufferedTransportFactory())

    def query_profile(self, type, key):
        data = dict()
        try:
            connect = self.connect_data_source()
            data = connect.queryProfile(type, key, None)
        except Exception as e:
            logger.error("访问后端查询个人资料数据接口出错 %s" % e)
        return data

    def query_trace(self, type, key):
        data = dict()
        try:
            connect = self.connect_data_source()
            data = connect.queryTrace('lbs', type, key,
                    1420004411000, 1514698811000)
        except Exception as e:
            logger.error("访问后端查询地点数据接口出错 %s" % e)
        return data

    def get_user_profile(self, type, content):
        li_lbs, dic, data, loc = [], {}, [], []
        datas = self.query_profile(type, content)
        locs = self.query_trace(type, content)
        if locs:
            for item in locs:
                loc = json.loads(locs[item]) if locs[item] else []
                break
        for sub in datas:
            dic["imei"] = sub
            data = datas[sub]
            break
        if data: 
            dic["phone"] = json.loads(data["phone"]) if data.has_key('phone') else '-'
            dic["uid"] = json.loads(data["uid"]) if data.has_key('uid') else ['-'] 
            dic["appkey"] = ['-'] 
            dic["device"] = json.loads(data["device_info"]).get("model") if data.has_key('device_info') and json.loads(data["device_info"]).has_key("model") else '-' 
            dic["app"] = json.loads(data["app_list"]) if data.has_key('app_list') else ['-'] 
            dic["category"] = json.loads(data["app_tags"]).get("class_one") if data.has_key('app_tags') and json.loads(data["app_tags"]).has_key("class_one") else ['-']
            dic["usergroup"] = json.loads(data["app_tags"]).get("user_group").replace("|"," | ") if data.has_key('app_tags') and json.loads(data["app_tags"]).has_key("user_group") else '-'
            dic["homeaddr"] = json.loads(data["home_address"]) if data.has_key('home_address') else ['-']
            dic["workaddr"] = json.loads(data["work_address"]) if data.has_key('work_address') else ['-']
            dic["gender"] = data["gender"] if data.has_key('gender') else ['-']
        else:
            dic = {"imei":"-","phone":["-"],"uid":["-"],"appkey":["-"],"device":"-","app":["-"],"category":["-"],"usergroup":"-","gender":"-"}
        return json.dumps(dic), json.dumps(loc)


user_profile_obj = UserProfileController()


def main():
    type = "ukey"
    tag = "lbs"
    key = "356195060335906"
    columns = None
    result = user_profile_obj.query_profile(type, key)
    print result
    result = user_profile_obj.query_trace(tag, type, key)
    print result


if __name__ == '__main__':
    main()
