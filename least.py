# coding=utf-8

import pickle
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.stats import norm
from scipy.optimize import leastsq
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.cross_decomposition import PLSRegression
from sklearn import linear_model

# data = pickle.load(open('C4-A22-PL-01%r2.pkl', 'rb'))
data = pickle.load(open('C4-A09-J-01%r1.pkl', 'rb'))

dt = [data[i][0].strftime('%Y-%m-%d') for i in range(len(data))]
val = [float(data[i][2]) for i in range(len(data))]
wl = [float(data[i][1]) for i in range(len(data))]

scale = 80

dt = dt[scale:]
val = val[scale:]
wl = wl[scale:]

# size = 10

# print dt[0:size]
# print val[0:size]
# print wl[0:size]

size = 8
split = 7
# x = np.array(wl[0:size])
# y = np.array(val[0:size])
'''时间字符串转为时间戳'''
def getTimestampByStr(timestr):
	import time
	return time.mktime(time.strptime(timestr, '%Y-%m-%d'))

x = [[getTimestampByStr(dt[i]), wl[i]] for i in range(0, split)]
y = val[0:split]

print x
print y

train_x = [[getTimestampByStr(dt[i]), wl[i]] for i in range(split, size)]
real_y = val[split:size]

def rmse(y_test, y):
    return sp.sqrt(sp.mean((y_test - y) ** 2))


def R22(y_test, y_true):
    y_mean = np.array(y_true)
    y_mean[:] = y_mean.mean()
    return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)


def R2(y_test, y_true):
    return 1 - ((y_test - y_true)**2).sum() / ((y_true - y_true.mean())**2).sum()

def errrate(y_test, y_true):
	err = (abs(y_test-y_true))/y_true 
	return ("%.4f" % err)


# clf = linear_model.LinearRegression()
# clf = linear_model.Ridge (alpha = .5)
# clf = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
# clf = PLSRegression()
clf = linear_model.Lasso(alpha = 0.6)
# clf = linear_model.LassoLars(alpha=.1)

clf.fit(x, y)

train_y = clf.predict(train_x)

# plt.style.use('fivethirtyeight')
plt.plot(range(0,len(train_y)), train_y, 'go', label='train')
plt.plot(range(0,len(real_y)), real_y, 'ro', label='real')
plt.bar(range(0,len(real_y)), [rmse(train_y[i], real_y[i]) for i in range(0,len(real_y))], label='rmse', alpha=0.4, align='center')
plt.legend(loc='lower center', bbox_to_anchor=(0.6,0.95),ncol=3,fancybox=True,shadow=True)
plt.yticks(range(0, 100, 5))
plt.grid()

print train_y, real_y
print [errrate(train_y[i], real_y[i]) for i in range(0,len(real_y))]

plt.show()