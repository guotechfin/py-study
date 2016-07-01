#!/bin/env python
# -*- coding:utf8 -*-

from common.conf import LARGE_VOLUMNS


class Ticket(object):
    g_price = 0
    g_volumns = 0

    def __init__(self):
        self.name = ""
        self.code = ""
        self.time = ""
        self.volumns = 0
        self.price = 0
        # 买1 量
        self.b1_v = 0
        # 买1 价
        self.b1_p = 0
        self.b2_v = 0
        self.b2_p = 0
        self.b3_v = 0
        self.b3_p = 0
        self.b4_v = 0
        self.b4_p = 0
        self.b5_v = 0
        self.b5_p = 0

        # 卖1 量
        self.a1_v = 0
        # 卖1 价
        self.a1_p = 0
        self.a2_v = 0
        self.a2_p = 0
        self.a3_v = 0
        self.a3_p = 0
        self.a4_v = 0
        self.a4_p = 0
        self.a5_v = 0
        self.a5_p = 0

    def __str__(self):
        s = ((u"卖5：%s %s\n"
                u"卖4：%s %s\n"
                u"卖3：%s %s\n"
                u"卖2：%s %s\n"
                u"卖1：%s %s\n"
                u"----------\n"
                u"成交：%s %s %s\n"
                u"----------\n"
                u"买1：%s %s\n"
                u"买2：%s %s\n"
                u"买3：%s %s\n"
                u"买4：%s %s\n"
                u"买5：%s %s\n") % (
                    self.a5_p, self.a5_v/100, 
                    self.a4_p, self.a4_v/100,
                    self.a3_p, self.a3_v/100,
                    self.a2_p, self.a2_v/100,
                    self.a1_p, self.a1_v/100,
                    self.time, self.code, self.name,
                    self.b1_p, self.b1_v/100,
                    self.b2_p, self.b2_v/100,
                    self.b3_p, self.b3_v/100,
                    self.b4_p, self.b4_v/100,
                    self.b5_p, self.b5_v/100,
                        ))
        return s.encode('utf8')

    def large_volumns(self):
        if (self.a5_v >= LARGE_VOLUMNS
                or self.a4_v >= LARGE_VOLUMNS
                or self.a3_v >= LARGE_VOLUMNS
                or self.a2_v >= LARGE_VOLUMNS
                or self.a1_v >= LARGE_VOLUMNS
                or self.b1_v >= LARGE_VOLUMNS
                or self.b2_v >= LARGE_VOLUMNS
                or self.b3_v >= LARGE_VOLUMNS
                or self.b4_v >= LARGE_VOLUMNS
                or self.b5_v >= LARGE_VOLUMNS):
            if (self.a5_v != 0
                    and self.a4_v != 0
                    and self.a3_v != 0
                    and self.a2_v != 0
                    and self.a1_v != 0
                    and self.b1_v != 0
                    and self.b2_v != 0
                    and self.b3_v != 0
                    and self.b4_v != 0
                    and self.b5_v != 0
                    ):
                return True
        else:
            return False
