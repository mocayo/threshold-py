# -*- coding:utf-8 -*-
# 多项式拟合:用python中numpy库自带的polyfit函数即可完成
import numpy as np
# from scipy.optimize import leastsq
# import matplotlib.pyplot as pl
import util
# from flask import Flask
# app = Flask(__name__)

'''
# 测试
test = util.addDay('2017-01-16', -15)
start = util.addDay('2017-01-16', -15)
# end = util.addDay(day, -1)
print start
'''

# @app.route('/<point>&<day>/')
def getPredictData(point = 'C4-A22-PL-01', day = '2017-01-16', delta = -10):
	start = util.addDay(day, delta)
	end = day
	pred = None
	# print start,end
	# 直接取出处理好的数据
	Xi,Yi = util.dataconverse(point, start, end)
	# print("Xi=%s, Yi=%s" % (Xi,Yi))
	# print("len(Xi)=%s" % len(Xi))
	# print Xi.shape
	# print "abc"
	# 判断X，Y都为空的情况
	if len(Xi) < -delta:
		print "Xi，Yi exist NULL"
		return pred
	else:
		# 判断Y有空值的情况
		for y in Yi:
			if y == None:
				print "Yi exist NULL"
				return pred
		# 拟合自由度为3
		z3 = np.polyfit(Xi[:-1], Yi[:-1], 3)
		# 拟合自由度为6
		z6 = np.polyfit(Xi[:-1], Yi[:-1], 6)
		# 生成的多项式对象
		p3 = np.poly1d(z3)
		p6 = np.poly1d(z6)
		predict = p6(Xi[-1])
		'''
		print "=============================="
		print("多项式拟合函数为：")
		print("自由度为3： \n%s" % p3)
		print("自由度为6： \n%s" % p6)
		print("预测值： %s" % predict) 
		print "=============================="
		# 绘制曲线
		pl.figure(figsize=(8,6))
		# 原曲线
		pl.plot(Xi, Yi, 'b-', label='Origin Line')
		# 自由度为3的曲线
		pl.plot(Xi, p3(Xi), 'gv--', label='Poly Fitting Line(deg=3)')
		# 自由度为6的曲线
		pl.plot(Xi, p6(Xi), 'r^-', label='Poly Fitting Line(deg=6)')
		pl.legend()
		# Save figure 必须在pl.show()的前面，否则生成新的空白figure
		pl.savefig('poly.png')
		# pl.show()
		'''
		pred = '%0.4f' % predict
		return pred
	
	
if __name__ == '__main__':
	# app.run()
	print getPredictData(point = "C4-A41-PL-03jx",  day = '2017-01-10', delta = -10)
