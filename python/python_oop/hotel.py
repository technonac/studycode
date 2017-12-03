#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用缺省参数进行实例化
"""


class HotelRoomCalc(object):
    """Hotel room rate calculator"""

    def __init__(self, rt, sales=0.085, rm=0.1):
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        """calculate total,default to daily rate"""
        daily = round(self.roomRate * (1 + self.roomTax + self.salesTax), 2)
        return float(days) * daily


sfo = HotelRoomCalc(299)
print(sfo.calcTotal())
print(sfo.calcTotal(2))

