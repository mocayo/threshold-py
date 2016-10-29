# -*- coding: utf-8 -*- 

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pl
from scipy.optimize import leastsq

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
	theta1, theta2, theta3 = p
	return theta1 + theta2 * np.sin(x) + theta3 * np.exp(x)

def residuals(p, y, x):
    return y - fun(p, x)

x = np.linspace(1,2)

preal = np.random.rand(1,3)[0]

yreal = fun(preal, x)
ytest = [np.random.normal(0, 0.1) + y for y in yreal]

p0 = np.random.rand(1,3)[0]

plsq = leastsq(residuals, p0, args=(ytest, x))

pl.plot(yreal, label=u"真实数据")
pl.plot(ytest, 'o',label=u"带噪声的数据")
pl.plot(fun(plsq[0],x), label=u"拟合数据")
pl.legend()
pl.show()