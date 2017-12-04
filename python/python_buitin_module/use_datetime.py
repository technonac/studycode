#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
now = datetime.now()
print(now)

print(type(now))

# 获取指定的日期和时间
dt = datetime(2017, 10, 1, 8, 0)
print(dt)

# datetime转换为timestamp
print(dt.timestamp())

# timestamp转换为datetime
t = 1500000000.0
print(datetime.utcfromtimestamp(t))  # utc时间
print(datetime.fromtimestamp(t))  # 本地时间

# str转换为datetime
cday = datetime.strptime('2017-01-01 10:00:00', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
print(now.strftime('%a,%b %d %H:%M'))

# datetime加减
yesterday = now - timedelta(days=1)
print(yesterday)

