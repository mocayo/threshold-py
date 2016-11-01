# -*- coding: UTF-8 -*-

import numpy as np
from scipy import optimize
import matplotlib as mpl
import matplotlib.pyplot as plt
import getdata
import time
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
plt.style.use('fivethirtyeight')

# 时间字符串转为时间戳
def getTimestampByStr(timestr):
	return time.mktime(time.strptime(timestr, '%Y-%m-%d'))

def fun(x, theta1, theta2):
	# theta1, theta2 = p
	return theta1 + theta2*np.sin(x)

def fit(point = 'C4-A22-PL-01', day = '2016-07-16', delta = -7):
	start = addDay(day=day, delta=delta)
	end = day

	dt,val = getdata.getDataByPoint(point=point, start=start, end=end)
	dt.append(day)
	x = [getTimestampByStr(d) for d in dt]
	xdata = np.array(norm(x))
	ydata = val

	guess = np.random.rand(1,2)[0]
	params, params_covariance = optimize.curve_fit(fun, xdata[:-1], ydata, guess)
	train_y = fun(xdata[:-1],params[0],params[1])
	# err = errrate(train_y, ydata)
	# print params
	# print err

	# test_x = xdata[-1]
	# real_data = getdata.getDataByDay(point=point, day=day)
	# real_y = real_data
	# test_y = fun(test_x,params[0],params[1])
	predict = fun(xdata[-1], params[0], params[1])
	print '======================'
	print 'day: ', day
	# print 'realVal:', '%.4f' % real_y
	print 'predict:', '%.4f' % predict
	print 'rmse: ', '%.4f' % rmse(train_y, ydata)
	# print 'aberror:', '%.4f' % np.abs(real_y - test_y)
	# print 'errrate:', '%.4f' % errrate(test_y,real_y)
	print '======================'

	# plt.plot(xdata[:-1], ydata, 'o', label='raw data')
	# plt.plot(xdata[:-1],fun(xdata[:-1],params[0],params[1]), label='curve_fit data')
	# plt.legend(loc=0)
	# plt.title(point)
	# plt.show()
	return predict

def fitday(day = '2016-04-01', point='C4-A22-IP-01', period=50):
	res = []
	t0 = time.clock()
	try:
		dt,val = getdata.getDataByPoint(point=point, start=day, end=addDay(day,period))
		for d in dt:
			res.append(fit(point=point ,day=d))
	except:
		return
	print u'需要时间','%.4f' % (time.clock() - t0), 's'

	fig = plt.figure(figsize=(25, 20))
	ax = fig.add_subplot(111)
	xticks = range(0,len(dt),len(dt)/10+1)
	xticklabels = [dt[i] for i in xticks]
	ax.set_xticks(xticks)
	ax.set_xticklabels(xticklabels, rotation=15)
	ax.set_xlabel(u'日期')
	ax.set_ylabel(u'测值')
	plt.plot(val,label=u"真实数据")
	plt.plot(res,label=u"拟合数据")
	plt.title(point)
	plt.legend(loc=0)
	plt.show()

if __name__ == '__main__':
	# fit(point = 'C4-A22-PL-02')
	fitday(day='2016-01-01',point='C4-A04-PL-02', period=20)
	# import sys
	# points = ['C4-A22-PL-02', 'C4-A22-PL-01', 'C4-A22-IP-02', 'C4-A22-IP-01']
	# for arg in sys.argv:
	# 	if arg in points:
	# 		fitday(day='2016-01-01',point=arg, period=60)