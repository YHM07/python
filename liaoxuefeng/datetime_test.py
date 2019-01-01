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

from datetime import datetime, timedelta, timezone
import re

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    n  = int(re.match(r'UTC([+-]\d+):00', tz_str).group(1))
    tz = timezone(timedelta(hours=n))
    dt = dt.replace(tzinfo = tz)
    return dt.timestamp()

print(to_timestamp('2015-6-1 08:10:30', 'UTC+7:00'))
print(to_timestamp('2015-5-31 16:10:30', 'UTC-09:00'))
    


