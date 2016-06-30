#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import tornado.gen
import tornado.httpclient
from tornado.escape import utf8
import json
import re

from common import web_handler
from common import mylog
from common import error_msg
from common import conf
from common import utility

from wood_warehouse_service import wood_warehouse_obj
from handle.wood.wood_service import wood_obj
from handle.warehose.warehouse_service import warehouse_obj


class WoodWarehouseList(web_handler.WebHandler):
    def prepare(self):
        self.resp_json = ""
        self.ret = 0
        self.msg = error_msg.SUCCESS
        self.wood_warehouse_list = list()

        self.wood_id = int(self.get_argument("wood_id", -1))
        self.warehouse_id = int(self.get_argument("warehouse_id", -1))

    def response(self):
        resp_dict = dict()
        resp_dict['ret'] = self.ret
        resp_dict['msg'] = self.msg
        resp_dict['wood_warehouse_list'] = utility.to_obj(
                self.wood_warehouse_list)
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
        self.wood_warehouse_list = (wood_warehouse_obj.
                search_wood_warehouse_list(
                    self._db_session,
                    wood_id=self.wood_id,
                    wood_warehouse=self.warehouse_id))
        for i in self.wood_warehouse_list:
            i.wood = wood_obj.search_wood_list(
                    wood_id=i.wood_id,
                    flag=-1)
            i.warehouse = warehouse_obj.search_warehouse_list(
                    warehouse_id=warehouse_id,
                    flag=-1)
        self._db_session.commit()
        return self.response()
