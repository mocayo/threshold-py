# -*- coding: utf-8 -*- 
# http://blog.chinaunix.net/uid-25267728-id-4678802.html

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pl

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

# np.random.seed([1])

def fun(x1, x2, p):
	theta1, theta2, theta3 = p
	# return theta1 + theta2*np.sin(x1) + theta3*np.exp(x2)
	return theta1 + theta2*x1 + theta3*x2

preal = np.random.rand(1,3)[0]

x1 = np.linspace(1,2)
x2 = np.linspace(2,3)

yreal = fun(x1, x2, preal)
ytest = [np.random.normal(0, 0.1) + y for y in yreal]

ptest = np.random.rand(1,3)[0]

# print ptest

for j in range(3):
	if j==0:
		ptest = [0,0,0]
	print j
	print ptest
	# 学习率
	alpha = 1

	# print fun(x1,x2,ptest)
	# err = fun(x1,x2,ptest) - yreal

	# t0 = ptest[0] - alpha * sum(err)
	# t1 = ptest[1] - alpha * sum([err[i] *x1[i] for i in range(len(x1))])
	# t2 = ptest[2] - alpha * sum([err[i] *x2[i] for i in range(len(x2))])
	delta = [0,0,0]
	for i in range(len(x1)):
		delta[0] = delta[0] + yreal[i] - alpha * fun(x1[i], x2[i], ptest)
		delta[1] = delta[1] + (yreal[i] - alpha * fun(x1[i], x2[i], ptest)) * x1[i]
		delta[2] = delta[2] + (yreal[i] - alpha * fun(x1[i], x2[i], ptest)) * x2[i]

	ptmp = [ptest[i] + delta[i] for i in range(len(ptest))]
	ptest = ptmp


# pl.plot(yreal, label=u"真实数据")
# pl.plot(ytest, 'o',label=u"带噪声的数据")
# pl.legend()
# pl.show()