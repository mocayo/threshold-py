# -*- coding:utf-8 -*-

from sklearn import linear_model
import getdata
import numpy as np
from qhutil import *

# 岭回归
def fit(point = 'C4-A22-PL-01', day = '2016-07-16', delta = -15):
	start = addDay(day=day, delta=delta)
	end = day

	dt,val = getdata.getDataByPoint(point=point, start=start, end=end)
	dt.append(day)
	x = [getTimestampByStr(d) for d in dt]
	x = np.array(norm(x))

	fitdatas = [[x[i],val[i]] for i in range(len(val))]
	# print fitdatas

	clf = linear_model.Lasso(alpha = 0.6)
	clf.fit(fitdatas)
	print clf.predict(x[-1])

if __name__ == '__main__':
	fit()