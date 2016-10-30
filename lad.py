# -*- coding: utf-8 -*- 

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pl
from scipy.optimize import leastsq
import getdata
from qhutil import *

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
	# return theta1 + theta2 * np.exp(theta3 * np.array(x))
	return theta1 + theta2 * np.array(x) + theta3 * np.array(x) **2

def residuals(p, y, x):
    return y - fun(p, x)

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
	# real = getdata.getDataByDay(point=point, day=day)
	print '===================='
	print 'day: ', day
	print 'predict:', '%.4f' % predict
	# print 'realval:', real
	# print 'aberror:', '%.4f' % np.abs(predict-real)
	# print 'errrate:', '%.4f' % errrate(predict, real)
	print '===================='
	ytest = fun(plsq[0],x[:-1])
	# print errrate(ytest, yreal)

	# pl.plot(yreal, 'o', label=u"真实数据")
	# pl.plot(ytest, label=u"拟合数据")
	# pl.legend(loc=0)
	# pl.show()

	return predict

def fitday(day = '2016-04-01', point='C4-A22-IP-01', period=50):
	res = []
	dt,val = getdata.getDataByPoint(point=point, start=day, end=addDay(day,period))
	for i in range(period):
		res.append(fit(point=point ,day=addDay(day, i)))
	pl.plot(val,label=u"真实数据")
	pl.plot(res,label=u"拟合数据")
	pl.xticks(range(len(dt)), dt)
	pl.legend(loc=0)
	pl.show()

if __name__ == '__main__':
	# print fit(point='C4-A22-IP-01',day='2016-08-16')
	# d1 = datetime.datetime.strptime('2016-07-16', '%Y-%m-%d')
	# print d1
	# d2 = d1 + datetime.timedelta(days=-15)
	# print d2
	# print d2.strftime('%Y-%m-%d')
	# print addDay()
	fitday(period=10)
	