#!/bin/env python
# -*- coding:utf8 -*-

from purchase_summary_list import PurchaseSummaryList
from purchase_summary_modify import PurchaseSummaryModify
from purchase_summary_new import PurchaseSummaryNew
from purchase_summary_del import PurchaseSummaryDel
from purchase_summary_change_review import PurchaseSummaryChangeReview
from common import conf

url = [
        ("/%s/purchase_summary/list" % conf.SERVICE_NAME, PurchaseSummaryList),
        ("/%s/purchase_summary/new" % conf.SERVICE_NAME, PurchaseSummaryNew),
        ("/%s/purchase_summary/modify" % conf.SERVICE_NAME, PurchaseSummaryModify),
        ("/%s/purchase_summary/del" % conf.SERVICE_NAME, PurchaseSummaryDel),
        ("/%s/purchase_summary/change_review" % conf.SERVICE_NAME, PurchaseSummaryChangeReview),
        ]
