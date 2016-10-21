#!/bin/env python
# -*- coding:utf8 -*-

from common.conf import LARGE_VOLUME, LARGE_PRICE


class Ticket(object):
    g_price = 0
    g_volume = 0

    def __init__(self):
        self.name = ""
        self.code = ""
        self.time = ""
        self.change_rate = 0
        # 当前成交金额 单位W
        self.transacation_amount = 0
        # 当前成交量 单位手
        self.volume = 0
        # 当前成交价
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
        self.b6_v = 0
        self.b6_p = 0
        self.b7_v = 0
        self.b7_p = 0
        self.b8_v = 0
        self.b8_p = 0
        self.b9_v = 0
        self.b9_p = 0
        self.b10_v = 0
        self.b10_p = 0

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
        self.a6_v = 0
        self.a6_p = 0
        self.a7_v = 0
        self.a7_p = 0
        self.a8_v = 0
        self.a8_p = 0
        self.a9_v = 0
        self.a9_p = 0
        self.a10_v = 0
        self.a10_p = 0
        self.level2 = False

    def __str__(self):
        if not self.level2:
            s = ((u"卖5：%s %s\n"
                    u"卖4：%s %s\n"
                    u"卖3：%s %s\n"
                    u"卖2：%s %s\n"
                    u"卖1：%s %s\n"
                    u"----------\n"
                    u"成交：%s %s %s %s%%\n"
                    u"----------\n"
                    u"买1：%s %s\n"
                    u"买2：%s %s\n"
                    u"买3：%s %s\n"
                    u"买4：%s %s\n"
                    u"买5：%s %s\n\n") % (
                        self.a5_p, self.a5_v/100, 
                        self.a4_p, self.a4_v/100,
                        self.a3_p, self.a3_v/100,
                        self.a2_p, self.a2_v/100,
                        self.a1_p, self.a1_v/100,
                        self.time, self.code, self.name, self.change_rate*100,
                        self.b1_p, self.b1_v/100,
                        self.b2_p, self.b2_v/100,
                        self.b3_p, self.b3_v/100,
                        self.b4_p, self.b4_v/100,
                        self.b5_p, self.b5_v/100,
                            ))
        else:
            s = ((u"卖10：%s %s\n"
                    u"卖9：%s %s\n"
                    u"卖8：%s %s\n"
                    u"卖7：%s %s\n"
                    u"卖6：%s %s\n"
                    u"卖5：%s %s\n"
                    u"卖4：%s %s\n"
                    u"卖3：%s %s\n"
                    u"卖2：%s %s\n"
                    u"卖1：%s %s\n"
                    u"----------\n"
                    u"成交：%s %s %s %s%%\n"
                    u"----------\n"
                    u"买1：%s %s\n"
                    u"买2：%s %s\n"
                    u"买3：%s %s\n"
                    u"买4：%s %s\n"
                    u"买5：%s %s\n"
                    u"买6：%s %s\n"
                    u"买7：%s %s\n"
                    u"买8：%s %s\n"
                    u"买9：%s %s\n"
                    u"买10：%s %s\n\n") % (
                        self.a10_p, self.a10_v, 
                        self.a9_p, self.a9_v,
                        self.a8_p, self.a8_v,
                        self.a7_p, self.a7_v,
                        self.a6_p, self.a6_v,
                        self.a5_p, self.a5_v, 
                        self.a4_p, self.a4_v,
                        self.a3_p, self.a3_v,
                        self.a2_p, self.a2_v,
                        self.a1_p, self.a1_v,
                        self.time, self.code, self.name, self.change_rate*100,
                        self.b1_p, self.b1_v,
                        self.b2_p, self.b2_v,
                        self.b3_p, self.b3_v,
                        self.b4_p, self.b4_v,
                        self.b5_p, self.b5_v,
                        self.b6_p, self.b6_v,
                        self.b7_p, self.b7_v,
                        self.b8_p, self.b8_v,
                        self.b9_p, self.b9_v,
                        self.b10_p, self.b10_v,
                            ))
        return s.encode('utf8')

    def large_volume(self):
        if (self.a10_v >= LARGE_VOLUME
                or self.a9_v >= LARGE_VOLUME
                or self.a8_v >= LARGE_VOLUME
                or self.a7_v >= LARGE_VOLUME
                or self.a6_v >= LARGE_VOLUME
                or self.a5_v >= LARGE_VOLUME
                or self.a4_v >= LARGE_VOLUME
                or self.a3_v >= LARGE_VOLUME
                or self.a2_v >= LARGE_VOLUME
                or self.a1_v >= LARGE_VOLUME
                or self.b1_v >= LARGE_VOLUME
                or self.b2_v >= LARGE_VOLUME
                or self.b3_v >= LARGE_VOLUME
                or self.b4_v >= LARGE_VOLUME
                or self.b5_v >= LARGE_VOLUME
                or self.b6_v >= LARGE_VOLUME
                or self.b7_v >= LARGE_VOLUME
                or self.b8_v >= LARGE_VOLUME
                or self.b9_v >= LARGE_VOLUME
                or self.b10_v >= LARGE_VOLUME):
            return True
        else:
            return False

    def no_zero_volume(self):
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

    def large_price(self):
        if self.level2:
            large_price = LARGE_PRICE/100
        else:
            large_price = LARGE_PRICE
        if (self.a10_v * self.a10_p >= large_price
                or self.a9_v * self.a9_p >= large_price
                or self.a8_v * self.a8_p >= large_price
                or self.a7_v * self.a7_p >= large_price
                or self.a6_v * self.a6_p >= large_price
                or self.a5_v * self.a5_p >= large_price
                or self.a4_v * self.a4_p >= large_price
                or self.a3_v * self.a3_p >= large_price
                or self.a2_v * self.a2_p >= large_price
                or self.a1_v * self.a1_p >= large_price
                or self.b1_v * self.b1_p >= large_price
                or self.b2_v * self.b2_p >= large_price
                or self.b3_v * self.b3_p >= large_price
                or self.b4_v * self.b4_p >= large_price
                or self.b5_v * self.b5_p >= large_price
                or self.b6_v * self.b6_p >= large_price
                or self.b7_v * self.b7_p >= large_price
                or self.b8_v * self.b8_p >= large_price
                or self.b9_v * self.b9_p >= large_price
                or self.b10_v * self.b10_p >= large_price
                ):
            return True
        else:
            return False

    def show(self):
        if (self.large_volume()
                and self.no_zero_volume()
                and self.large_price()):
            return True
        else:
            return False
