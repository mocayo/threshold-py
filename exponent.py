# -*- coding:utf-8 -*-
# 指数拟合：使用scipy.optimize中的leastsq最小二乘法拟合指数函数
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as pl
import util

# 定义指数函数为： y = a*e^x + b
def func(p,x):
	return p[0]*np.exp(x)+p[1]

# 定义误差函数
def error(p,x,y):
	return func(p,x)-y

def getPredictData(point = 'C4-A22-PL-01', day = '2017-01-16', delta = -15):
	start = util.addDay(day, delta)
	end = day
	# 直接取出处理好的数据
	Xi,Yi = util.dataconverse(point, start, end)
	print Xi,Yi
	# 定义初始参数
	p0 = [2,1]
	# 拟合系数
	coef = leastsq(error, p0, args = (Xi[:-1],Yi[:-1]))
	p = coef[0]
	#print p
	predict = func(p, Xi[-1])
	# 输出拟合函数
	print "=============================="
	print("指数拟合函数为：")
	print("y = %.4fe^x + %.4f" % (p[0], p[1]))
	print("预测值： %s" % predict) 
	print("实测值： %s" % Yi[-1])
	print "=============================="
	# 绘制曲线
	pl.figure(figsize=(8,6))
	# 原曲线
	pl.plot(Xi, Yi, 'b-', label='Origin Line')
	# 指数拟合的曲线
	pl.plot(Xi, func(p,Xi), 'r^-', label='exponent Fitting Line')
	pl.legend()
	# Save figure 必须在pl.show()的前面，否则生成新的空白figure
	pl.savefig('exponent.png')
	pl.show()
	return predict
		
if __name__ == '__main__':
	getPredictData()

