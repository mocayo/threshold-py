# -*- coding: utf-8 -*- 

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pl
from scipy.optimize import leastsq
import datetime
import time
import getdata

# 绘图设置
# 设置字体
mpl.rcParams['font.sans-serif'] = ['SimHei']  
# 用来正常显示负号
mpl.rcParams['axes.unicode_minus'] = False  
# 设置坐标轴刻度显示大小
mpl.rc('xtick', labelsize=16)  
mpl.rc('ytick', labelsize=16)
# 设置绘图风格
pl.style.use('fivethirtyeight')

def fun(p, x):
	theta1, theta2, theta3 = p
	# return theta1 + theta2 * np.sin(x) + theta3 * np.exp(x)
	return theta1 + theta2 * np.exp(theta3 * np.array(x))

def residuals(p, y, x):
    return y - fun(p, x)

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


def fit(point = 'C4-A22-PL-01', day = '2016-07-16', delta = -15):
	# x = np.linspace(1,20,100)
	# point = 'C4-A22-PL-01'
	start = addDay(day=day, delta=delta)
	end = day

	dt,val = getdata.getDataByPoint(point=point, start=start, end=end)
	dt.append(day)
	x = [getTimestampByStr(d) for d in dt]
	x = np.array(norm(x))
	
	yreal = val
	p0 = np.random.rand(1,3)[0]
	plsq = leastsq(residuals, p0, args=(yreal, x[:-1]))
	predict = fun(plsq[0],x[-1])
	real = getdata.getDataByDay(point=point, day=day)
	print '===================='
	print 'day: ', day
	print 'predict:', '%.4f' % predict
	print 'realval:', real
	print 'aberror:', '%.4f' % np.abs(predict-real)
	print 'errrate:', '%.4f' % errrate(predict, real)
	print '===================='
	ytest = fun(plsq[0],x[:-1])
	print errrate(ytest, yreal)

	pl.plot(yreal, 'o', label=u"真实数据")
	pl.plot(ytest, label=u"拟合数据")
	pl.legend(loc=0)
	pl.show()

if __name__ == '__main__':
	fit(point='C4-A22-IP-01',day='2016-08-16')
	# d1 = datetime.datetime.strptime('2016-07-16', '%Y-%m-%d')
	# print d1
	# d2 = d1 + datetime.timedelta(days=-15)
	# print d2
	# print d2.strftime('%Y-%m-%d')
	# print addDay()