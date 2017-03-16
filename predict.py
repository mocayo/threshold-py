# -*- coding:utf-8 -*-

from sklearn import linear_model
import matplotlib as mpl
import matplotlib.pyplot as pl
import getdata
import numpy as np
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

# 岭回归 根据水位和日期
def fit(point = 'C4-A22-PL-01', day = '2016-07-16', delta = -15):
	start = addDay(day=day, delta=delta)
	end = day

	dt,val = getdata.getDataByPoint(point=point, start=start, end=end)
	print dt
	# 水位数据
	wl = []
	for i in range(-delta):
		wl.append(getdata.getWLByDay(addDay(start,i)))

	dt.append(day)
	x = [getTimestampByStr(d) for d in dt]
	x = np.array(norm(x))
	fitdatas = [[x[i],wl[i]] for i in range(len(wl))]

	clf = linear_model.Lasso(alpha = 0.6)
	clf.fit(fitdatas, val)
	realVal = getdata.getDataByDay(point,day)
	predict = clf.predict(np.array([x[-1],getdata.getWLByDay(day)]).reshape((1,-1)))[0]
	print '======================'
	print 'realVal:', realVal
	print 'predict:', predict
	print 'aberror:', '%.4f' % np.abs(realVal-predict)
	print 'errrate:', '%.4f' % errrate(predict, realVal)
	print '======================'
	return predict

def fitday(day = '2016-04-01', point='C4-A22-IP-01', period=15):
	res = []
	t0 = time.clock()
	try:
		dt,val = getdata.getDataByPoint(point=point, start=day, end=addDay(day,period))
	except:
		return
	for d in dt:
		res.append(fit(point=point ,day=d))
	print u'需要时间','%.4f' % (time.clock() - t0), 's'

	fig = pl.figure(figsize=(25, 20))
	ax = fig.add_subplot(111)
	xticks = range(0,len(dt),len(dt)/10+1)
	xticklabels = [dt[i] for i in xticks]
	ax.set_xticks(xticks)
	ax.set_xticklabels(xticklabels, rotation=15)
	ax.set_xlabel(u'日期')
	ax.set_ylabel(u'测值')
	pl.plot(val,label=u"真实数据")
	pl.plot(res,label=u"拟合数据")
	pl.title(point)
	pl.legend(loc=0)
	pl.show()

if __name__ == '__main__':
	fitday(day='2014-07-01', period=35)