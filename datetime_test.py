#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import datetime
import calendar

# 计算上一个时间
last_friday = datetime.date.today()
oneday = datetime.timedelta(days=1)

while last_friday.weekday() != calendar.FRIDAY:
    last_friday -= oneday

print(last_friday.strftime('%A, %d-%b-%Y'))

# 借助模运算寻找上一个周五
today = datetime.date.today()
target_day = calendar.FRIDAY

thid_day = today.weekday()
delta_to_target = (thid_day - target_day) % 7

last_friday = today - datetime.timedelta(days=delta_to_target)

print(last_friday.strftime('%A, %d-%b-%Y'))

