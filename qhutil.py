# -*- coding: utf-8 -*- 

import datetime
import time

# 时间字符串转为时间戳
def getTimestampByStr(timestr):
	return time.mktime(time.strptime(timestr, '%Y-%m-%d'))

# 归一化
def norm(x):
	maxv = max(x)
	minv = min(x)
	return [(xx-minv)/float(maxv-minv) for xx in x]

# 相对误差
def errrate(y_test, y_true):
	err = (abs(y_test-y_true))/y_true 
	return err	

# 日期加减天操作
def addDay(day='2016-07-16', delta=-15):
	d1 = datetime.datetime.strptime(day, '%Y-%m-%d')
	return (d1 + datetime.timedelta(days=delta)).strftime('%Y-%m-%d')