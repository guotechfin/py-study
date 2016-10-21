#!/bin/env python
# -*- coding:utf8 -*-

from lhb_list import LHBList
from lhb_data import LHBData
from lhb_detail import LHBDetail
from lhb_date_list import LHBDateList
from lhb_data_del import LHBDataDel
from common import conf

url = [
        ("/%s/lhb/list" % conf.SERVICE_NAME, LHBList),
        ("/%s/lhb/data" % conf.SERVICE_NAME, LHBData),
        ("/%s/lhb/detail" % conf.SERVICE_NAME, LHBDetail),
        ("/%s/lhb/date_list" % conf.SERVICE_NAME, LHBDateList),
        ("/%s/lhb/data_del" % conf.SERVICE_NAME, LHBDataDel),
        ]
