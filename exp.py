#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as pl


def hyperbola_residuals(p, y, x):
    '''计算双曲线模型的误差并返回。'''
    return y - x / (p[0] * x + p[1])


def exponent_residuals(p, y, x):
    '''计算指数模型的误差并返回。'''
    return y - p[0] * np.exp(p[1] / x)


def hyper_value(x, p):
    '''根据变量和参数计算双曲线函数的值。'''
    return  x / (p[0] * x + p[1])


def exp_value(x, p):
    '''根据变量和参数计算指数函数的值。'''
    return p[0] * np.exp(p[1] / x)


# 猜测的初始参数值
p0 = [1, 1]

# 数值
x = np.arange(1, 17, 1)
y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])

# 拟合，调用参数分别为误差residuals，猜测初始值，需要拟合的实验数据
hyper_plsq = leastsq(hyperbola_residuals, p0, args=(np.reciprocal(y), np.reciprocal(x)))
exp_plsq = leastsq(exponent_residuals, p0, args=(y, x))

# 分别输出两组结果
print u'双曲线函数参数：', hyper_plsq[0]
print u'指数函数参数:', exp_plsq[0]

# 绘制原曲线和拟合后的曲线
pl.plot(x, y, 'b^-', label='Origin Line')
pl.plot(x, hyper_value(x, hyper_plsq[0]), 'gv--', label='Hyperbola Fitting Line')
pl.plot(x, exp_value(x, exp_plsq[0]), 'r*', label='Exponent Fitting Line')
pl.axis([0, 18, 0, 18])
pl.legend()
# Save figure 保存图像
pl.savefig('scipy01.png', dpi=96)
pl.show()