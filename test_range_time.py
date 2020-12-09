#!/usr/bin/env python
# encoding: utf-8

import datetime

nowtime = datetime.datetime.now()
stmp_time = nowtime - datetime.timedelta()
etmp_time = nowtime - datetime.timedelta()

#print(stmp_time, etmp_time)

start_time = stmp_time.strftime('%M') #开始时间
end_time = etmp_time.strftime('%M') #结束时

print(start_time, end_time)
#print(time.time())

