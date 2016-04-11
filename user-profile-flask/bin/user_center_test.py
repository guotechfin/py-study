#!/bin/env python
# -*-coding:utf-8-*-

import urllib2
import json

HOST = "http://test-iportal.jpushoa.com/"

def new_user():
    url = "%s/user_profile/v1/user/create_user" % HOST
    data = dict()
    data["name"] = "jpush"
    data["password"] = "jpush"
    req = urllib2.Request(url=url, data="data=" + json.dumps(data))
    resp = urllib2.urlopen(req)
    print resp.read()

def modify_user():
    url = "%s/user_center/v1/user/modify_user" % HOST
    data = dict()
    data["id"] = 1
    data["name"] = "chenbaiheng"
    data["password"] = "chenbaiheng"
    data["phone"] = "chenbaiheng"
    data["wechat"] = "chenbaiheng1"
    data["type"] = 0
    data["group_id_list"] = [3, 2]
    req = urllib2.Request(url=url, data="data=" + json.dumps(data))
    resp = urllib2.urlopen(req)
    print resp.read()

def modify_password():
    url = "%s/user_center/v1/user/modify_password" % HOST
    data = dict()
    data["email"] = "chenbh@jpush.cn"
    data["old_password"] = "123456"
    data["new_password"] = "chenbaiheng"
    req = urllib2.Request(url=url, data="data=" + json.dumps(data))
    resp = urllib2.urlopen(req)
    print resp.read()

def get_user_list():
    url = "%s/user_center/v1/user/get_user_list?" % HOST
    url += "group_id=2"
    req = urllib2.Request(url=url)
    resp = urllib2.urlopen(req)
    print resp.read()

def get_user_info():
    url = "%s/user_center/v1/user/get_user_info?id=1" % HOST
    req = urllib2.Request(url=url)
    resp = urllib2.urlopen(req)
    print resp.read()


if __name__ == "__main__":
    new_user()
    #modify_user()
    #get_user_list()
    #get_user_info()
    #modify_password()
