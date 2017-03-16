# -*- coding: utf-8 -*- 

import datetime
import time
import numpy as np
import getdata

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

# def rmse(y_test, y_true):
#     return np.sqrt(np.mean((y_test - y_true) ** 2))

# def R22(y_test, y_true):
#     y_mean = np.array(y_true)
#     y_mean[:] = y_mean.mean()
#     return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)

# def R2(y_test, y_true):
#     return 1 - ((y_test - y_true)**2).sum() / ((y_true - y_true.mean())**2).sum()

# 对根据测点取到的数据进行处理后返回
def dataconverse(point='C4-A22-PL-01', start='2017-01-01', end='2017-01-08'):
	# 根据测点获取数据
	X0 = np.array(getdata.getDataByPoint(point, start, end)[0])
	Yi = np.array(getdata.getDataByPoint(point, start, end)[1])
	# print X0,Yi
	# shape属性用来判断np.array属性为空 
	if(X0.shape == (0L,)):
		return X0,Yi
	else:
		# 将时间字符串转化为时间戳
		X1 = [getTimestampByStr(xx) for xx in X0]
		# 将时间戳数据归一化
		Xi = np.array(norm(X1))
		return Xi,Yi

if __name__ == '__main__':
	# print addDay()
	print dataconverse(point='A22-T1005-PJ', start='2016-12-27', end='2017-01-10')