#!/usr/bin/python
# coding=utf-8


'''
Learning Python  日期和时间
'''



import time
import calendar

# UNIX 时间戳（1970年1月1日至当前时间的秒数，返回类型为 float）
unixTime = time.time()                  
print "当前Unix 时间戳：", unixTime


# 时间元组 time.localtime()
'''
time.struct_time(tm_year=2017, tm_mon=3, tm_mday=3, tm_hour=10, tm_min=38, tm_sec=18, tm_wday=4, tm_yday=62, tm_isdst=0)
每个元素分别对应 年、月、日、时、分、秒、周、第几天(一年中)、是否是夏令时（0，1，-1 分别表示是、否、未知）
'''
#  Unix 时间戳转换为本地时间元组, localtime(secs)，参数为 Unix 系统时间戳,如果不加参数则是当前时间
localtime = time.localtime(10)
print 'Unix时间戳第10s 时本地时间元组：',localtime
localtime = time.localtime(time.time())
print '当前本地时间元组：',localtime
localtime = time.localtime()
print '当前本地时间元组：',localtime


# Unix 时间戳转换为格林尼治时间元组（UTC时间）, gmtime(secs), 参数为 Unix 系统时间戳,如果不加参数则是当前时间
print '当前 UTC 时间(元组)：', time.gmtime()
print 'Unix第10秒的 UTC 时间（元组）：', time.gmtime(10)
print 'Unix第10秒的 UTC 时间：',time.asctime(time.gmtime(10))


# 时间元组转换为 Unix 时间戳, mktime(tupletime)
timetuple = (2017, 3, 3, 15, 48, 39, 4, 62, 0)
print 'Unix 时间戳: ', time.mktime( timetuple )


# 时间元组格式化为时间字符串,固定格式为" Fri Mar  3 16:14:21 2017", time.asctime(timetuple)
localtime = time.asctime(time.localtime(time.time()))
print '时间格式化：',localtime


# 日期格式化 time.strftime()
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
# 时间元组格式化为时间字符串 strftime('format','timetuple')
timetuple = (2017, 3, 3, 15, 50, 7, 4, 62, -1)
timeStr1 = time.strftime('%Y-%m-%d %H:%M:%S', timetuple) 
timeStr2 = time.strftime('%a %b %d %H:%M:%S %Y', timetuple) 
timeStr3 = time.strftime('%Y 年 %m 月 %d 日 星期%w %H:%M:%S %Z', timetuple) 
print '日期字符串格式化-1：', timeStr1
print '日期字符串格式化-2：', timeStr2
print '日期字符串格式化-3：', timeStr3


# 时间字符串转换为时间元组 strptime('timestring','format')
timeStr = '2017-03-03 15:50:07'
timetuple = time.strptime(timeStr,'%Y-%m-%d %H:%M:%S')
print '时间字符串转换为元组: ', timetuple


# Unix 时间戳转换为本地时区时间字符串 ctime(secs)，默认如果不指定参数，则为当前时间
print '当前本地时间：', time.ctime()
print 'Unix 第10s 的时间：', time.ctime(10)


# 进程挂起 x 秒 time.sleep(secs) 
time.sleep(2)

# 计算语句块占用的 CPU 时间, 比 time.time() 更精确
t0 = time.clock()
for i in range(50000000) :
	pass
t1 = time.clock()
print '循环执行 50000000 次空语句耗时: ', t0, t1


# Time 模块的属性
# 当地时区与 UTC 时间相差的秒数(>0 美洲， <0 大部分欧洲亚洲非洲)
print time.timezone

# 当地时区的名称
print time.tzname



# 获取某月日历 calendar.month(year,month)
cal = calendar.month(2017,3)
print '2017年1月日历\n',cal


