# -*- coding:utf-8 -*-
# 正弦函数拟合（sin）：使用scipy.optimize提供的curve_fit()函数
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import util

### 取数据
# 直接取出处理好的数据，类型为np.array
# 默认为测点‘C4-A22-PL-01’的2017-01-01到2017-01-08的数据
Xi,Yi = util.dataconverse()
#print Xi,Yi

# 定义正弦函数： y = a*sinx+c
def func(x, a, c):
	return a * np.sin(x) + c

### main
popt, pcov = curve_fit(func, Xi, Yi)
print popt,pcov

### 绘制曲线
plt.figure(figsize=(8,6))
# 原曲线
plt.plot(Xi, Yi, 'b-', label='Origin Line')
# 指数拟合的曲线
plt.plot(Xi, func(Xi, popt[0], popt[1]), 'r^-', label='Sin Fitting Line')
plt.legend()
# Save figure 必须在plt.show()的前面，否则生成新的空白figure
plt.savefig('sin.png')
plt.show()