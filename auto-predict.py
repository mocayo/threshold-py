# -*- coding:utf-8 -*-
# 自动预测：自动读取所有测点并输出其预测值
import getdata
import poly

addpoints = []
# points = getdata.getAllPoints()

'''
for table in tables:
	addpoints = getdata.getPointsByTable(table)
	# print addpoints
	if(addpoints is None):
		pass
	else:
		points.extend(addpoints)

tables = getdata.getAllTable()
'''

def autoPredictByTable(table = 'T_ZB_PL', day = '2017-01-10', delta = -10):
	points = getdata.getPointsByTable(table)
	if(points is None):
		print "表%s为空！"
	else:
		for point in points:
			print point
			predict = poly.getPredictData(point, day, delta)
			print "%s : %s\n------------------------" % (point, predict)

if __name__ == '__main__':
	autoPredictByTable('T_ZB_EA')