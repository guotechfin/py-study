#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import tornado.gen
import tornado.httpclient
from tornado.escape import utf8
import json
import re
import datetime

from common import web_handler
from common import mylog
from common import error_msg
from common import conf
from common import utility

from lhb_service import lhb_obj
from handler.exchange_division.exchange_division_service import division_obj
from handler.group_member.group_member_service import group_member_obj


class LHBDetail(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret, self.msg = error_msg.SUCCESS
        self.lhb_detail = list()

        self.code = self.get_argument("code", "")
        self.date = self.get_argument("date",
                datetime.datetime.now().strftime("%Y%m%d"))

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['lhb_detail'] = utility.to_obj(self.lhb_detail)
        self.resp_json = json.dumps(
                resp_dict,
                ensure_ascii=False)
        self.write(self.resp_json)
        self.finish()
        return

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    @utility.login_requested
    def get(self):
        self.lhb_detail = lhb_obj.search_lhb_list(
                self._db_session,
                code=self.code,
                date=self.date)
        for i in self.lhb_detail:
            for j in dir(i):
                if j.endswith("division_id"):
                    setattr(i, j.replace("id", "name"), "")
                    setattr(i, j.replace("exchange_division", "group_list"), [])
                    division = division_obj.get_exchange_division(
                            self._db_session, getattr(i, j))
                    if division:
                        setattr(i, j.replace("id", "name"), division.name)
                        group_member = group_member_obj.search_group_member_list(
                                self._db_session,
                                division_id=getattr(i, j),
                                user_id=self._user_id)
                        if group_member:
                            setattr(i,
                                j.replace("exchange_division", "group_list"),
                                group_member)
        self._db_session.commit()
        return self.response()
