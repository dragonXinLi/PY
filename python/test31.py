#encoding=utf-8;

import os;
import re
from datetime import datetime , timedelta , timezone
# import datetime

now = datetime.now()

# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
# now = datetime.datetime.now()
print(now)
print(type(now))

dt = datetime(2015,4,19,12,20)
print(dt)

timestamp = dt.timestamp()
print(timestamp)

now2 = datetime.fromtimestamp(timestamp) # 本地时间
print(now2)

print(datetime.utcfromtimestamp(timestamp))  #UTC时间

cday = datetime.strptime('2015-6-1 15:19:59' , '%Y-%m-%d %H:%M:%S')
print(cday)

print(cday.strftime('%a, %b %d %H:%M'))

#时间加减

print(now)
print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=2,hours=10))

#本地时间转换为UTC时间

tz_utc_8 = timezone(timedelta(hours=8))
now3 = datetime.now()
print(now3)


dt = now.replace(tzinfo=tz_utc_8)#强制设置为8时区
print(dt)

#时区转换

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

def to_timestamp(dt_str,tz_str):
    get_time = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    get_utc = re.match(r'^UTC([+|-]\d{1,2}):00$',tz_str)
    print('utc %s' %get_utc)
    get_utc2 = re.match(r'^UTC([+|-]\d{1,2}):00$', tz_str).group(1)
    print('utc22 %s' % int(get_utc2))
    tz_utc = timezone(timedelta(hours=int(get_utc2)))
    dt = get_time.replace(tzinfo=tz_utc)
    return dt.timestamp()

print(to_timestamp('2015-6-1 08:10:30' , 'UTC+7:00'))

