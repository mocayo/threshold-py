# -*- coding: utf-8 -*- 
# http://blog.chinaunix.net/uid-25267728-id-4678802.html

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pl
from scipy.optimize import leastsq
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
pl.style.use('ggplot')

def fun(p, x):
	theta1, theta2 = p
	# return theta1 + theta2 * np.sin(x) + theta3 * np.exp(x)
	return theta1 + theta2 * np.exp(x)

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
	return ("%.4f" % err)

# x = np.linspace(1,20,100)
point = 'C4-A22-PL-01'
start = '2016-07-01'
end = '2016-07-16'

dt,val = getdata.getDataByPoint(point=point, start=start, end=end)

x = [getTimestampByStr(d) for d in dt]
x = np.array(norm(x))
# x = np.linspace(0,1,len(dt))

# yreal = fun(preal, x)
yreal = val

print x
print yreal

p0 = np.random.rand(1,2)[0]
print 'p0 = ', p0
plsq = leastsq(residuals, p0, args=(yreal[:-1], x[:-1]))

print plsq[0]

predict = fun(plsq[0],x[-1])
real = yreal[-1]
print '==============='
print 'predict:', predict
print 'real:', real
print 'errrate:', errrate(predict, real)
print '==============='


pl.plot(yreal, 'o', label=u"真实数据")
pl.plot(fun(plsq[0],x), label=u"拟合数据")
pl.legend(loc=0)
pl.show()
