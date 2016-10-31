# -*- coding: utf-8 -*- 

import datetime
import time
import numpy as np

# 时间字符串转为时间戳
def getTimestampByStr(timestr):
	return time.mktime(time.strptime(timestr, '%Y-%m-%d'))

# 归一化
def norm(x):
	maxv = max(x)
	minv = min(x)
	if maxv == minv:
		maxv += 0.0001
	return [(xx-minv)/float(maxv-minv) for xx in x]

# 相对误差
def errrate(y_test, y_true):
	err = (abs(y_test-y_true))/y_true 
	return err	

# 日期加减天操作
def addDay(day='2016-07-16', delta=-15):
	d1 = datetime.datetime.strptime(day, '%Y-%m-%d')
	return (d1 + datetime.timedelta(days=delta)).strftime('%Y-%m-%d')

def rmse(y_test, y_true):
    return np.sqrt(np.mean((y_test - y_true) ** 2))

def R22(y_test, y_true):
    y_mean = np.array(y_true)
    y_mean[:] = y_mean.mean()
    return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)

def R2(y_test, y_true):
    return 1 - ((y_test - y_true)**2).sum() / ((y_true - y_true.mean())**2).sum()