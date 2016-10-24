# -*- coding: UTF-8 -*-

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import seaborn as sns
import getdata
import time

# 时间字符串转为时间戳
def getTimestampByStr(timestr):
	return time.mktime(time.strptime(timestr, '%Y-%m-%d'))

# 相对误差
def errrate(y_test, y_true):
	err = (abs(y_test-y_true))/y_true 
	return ("%.4f" % err)

def f(x):
	return x**2 + 10*np.sin(x)

def f2(x, a, b):
	return a + b*np.sin(x)
  			
# xdata = np.linspace(-10, 10, num=20)
# ydata = f(xdata) + np.random.randn(xdata.size)
x, y = getdata.getDataByPoint(table='T_ZB_IP', point='C4-A22-IP-03')
xdata = [getTimestampByStr(x[i]) for i in range(len(x))]
ydata = y

guess = [2, 2]
params, params_covariance = optimize.curve_fit(f2, xdata, ydata, guess)
train_y = f2(xdata,params[0],params[1])

err = []
for i in range(len(ydata)):
	err.append(errrate(train_y[i], ydata[i]))
print params
print err

test_x = getTimestampByStr('2016-07-08')
real_data = getdata.getDataByPoint(table='T_ZB_IP', point='C4-A22-IP-03', start='2016-07-08',end='2016-07-09')
real_y = real_data[1][0]
test_y = f2(test_x,params[0],params[1])
print errrate(real_y,test_y)

plt.plot(xdata, ydata, label='raw data')
plt.plot(xdata,f2(xdata,params[0],params[1]), label='curve_fit data')
plt.legend()
plt.show()