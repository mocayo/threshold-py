# -*- coding:utf-8 -*-

import time
from sklearn import linear_model
import getdata

# 时间字符串转为时间戳
def getTimestampByStr(timestr):
	return time.mktime(time.strptime(timestr, '%Y-%m-%d'))

# 相对误差
def errrate(y_test, y_true):
	err = (abs(y_test-y_true))/y_true 
	return ("%.4f" % err)

# 岭回归
def ridge(x,y,dt='2016-07-08'):
	clf = linear_model.Lasso(alpha = 0.6)
	clf.fit(x, y)
	clf.predict(getTimestampByStr(dt))

def test():
	x, y = getdata.getDataByPoint()
	print [getTimestampByStr(x[i]) for i in range(len(x))]
	# ridge([getTimestampByStr(x[i]) for i in range(len(x))], y)

if __name__ == '__main__':
	test()