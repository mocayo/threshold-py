# -*- coding: UTF-8 -*-

import pickle

from sqlconnect import MSSQL

# 获取所有的测点
def getAllPoints():
	sql = "SELECT DISTINCT DesignCode FROM LCRiver_xwdh_1.dbo.DefInsSort"
	ms = MSSQL()
	resList = ms.ExecQuery(sql)
	return [str(res[0]).strip() for res in resList]

# 获取所有的表名
def getAllTable():
	sql = "SELECT [table] FROM LCRiver_xwdh_1.dbo.DefTableType"
	ms = MSSQL()
	resList = ms.ExecQuery(sql)
	#strip()消除空格
	return [str(res[0]).strip() for res in resList]

# 根据测点返回对应表名	
def getTableByPoint(point='C4-A29-PL-01'):
	sql = "SELECT [table] FROM	LCRiver_xwdh_1.dbo.DefTableType "
	sql += "WHERE [type] IN (SELECT [type] FROM LCRiver_xwdh_1.dbo.DefInsSort "
	sql += "WHERE [DesignCode] = '" + point + "')"
	ms = MSSQL()
	resList =  ms.ExecQuery(sql)
	return str(resList[0][0]).strip()
	#return "".join(resList[0]).strip()

# 根据表名获取分量
def getCompByTable(table='T_ZB_PL'):
	sql = "SELECT R1,R2,R3 FROM LCRiver_xwdh_1.dbo.MonitorItemType "
	sql += "WHERE TABLE_NAME = '" + table.strip() + "'"
	ms = MSSQL()
	resList = ms.ExecQuery(sql)
	return resList[0]

# 获取指定表的所有测点
def getPointsByTable(table='T_ZB_PL'):
	if table=='T_ZB_3DLASER':
		return
	sql = "SELECT DISTINCT(INSTR_NO) FROM LCRiver_xwdh_2.dbo." + table.strip()

	ms = MSSQL()
	resList = ms.ExecQuery(sql)
	return [''.join(res).strip() for res in resList]

# def insert(key, value, types='comps'):
# 	sql = "INSERT INTO LCRiver_xwdh_2.dbo.ThresholdInfo([key],[value],[type]) "
# 	sql += "VALUES ('" + key + "', '" + value + "', '" +  types + "')"

# 	ms = MSSQL()
# 	ms.ExecNonQuery(sql)

# 根据表获取需要计算的分量
def getCalculatedCompByTable(table='T_ZB_PL'):
	sql = "SELECT value FROM LCRiver_xwdh_2.dbo.ThresholdInfo "
	sql += "WHERE [type]='comps' AND [key]='" + table.strip() + "'"
	ms = MSSQL()	
	resList = ms.ExecQuery(sql)
	return ''.join(resList[0]).strip()

# 根据测点获取数据
def getDataByPoint(point='C4-A22-PL-01', start='2016-07-01', end='2016-07-08'):
	dt = []
	val = []
	table = getTableByPoint(point)
	# print table
	comp = getCalculatedCompByTable(table)
	# print comp
	# print u'对应表格' , str(table)
	# print u'需要计算的分量', comp
	sql = "SELECT DT," + comp + " FROM LCRiver_xwdh_2.dbo." + table + " "
	sql += "WHERE INSTR_NO = '" + point + "' "
	sql += "AND DT BETWEEN '" + start + "' AND '" + end + "' "
	sql += "AND datename(Hour, DT)=8 "
	sql += "ORDER BY DT"
	ms = MSSQL()
	# print sql
	resList = ms.ExecQuery(sql)
	# print resList
	for i in range(len(resList)):
		if resList[i][1] is None:
			dt.append(resList[i][0].strftime('%Y-%m-%d'))
			val.append(None)
		else:
			dt.append(resList[i][0].strftime('%Y-%m-%d'))
			val.append(float(resList[i][1]))
	return dt, val

# 获取指定日期测点需要计算分量的实测值
def getDataByDay(point='C4-A22-PL-01', day='2016-07-01'):
	table = getTableByPoint(point)
	comp = getCalculatedCompByTable(table)
	# print u'对应表格' , str(table)
	print u'需要计算的分量', comp
	sql = "SELECT " + comp + " FROM LCRiver_xwdh_2.dbo." + table + " "
	sql += "WHERE INSTR_NO = '" + point + "' "
	sql += "AND CONVERT(VARCHAR(10),DT,120) = '" + day + "'"
	sql += "AND datename(Hour, DT)=8"
	ms = MSSQL()
	# print sql
	resList = ms.ExecQuery(sql)
	return float(resList[0][0])

# 获取水位数据
def getWLByDay(day='2016-07-01'):
	sql = "SELECT UPLEVEL FROM xwplat.dbo.B_HUBENV "
	sql += "WHERE UPLEVELDT = '" + day + "'"
	ms = MSSQL()
	# print sql
	resList = ms.ExecQuery(sql)
	return resList[0][0]

def main():
	# print getCalculatedCompByTable('T_ZB_UP')
	# print getDataByPoint(point='A22-T1005-PJ',start='2016-12-27', end='2017-01-10')
	# print getDataByDay()
	# print getPointsByTable('T_ZB_IP')
	print getTableByPoint("C6B-DCL-Ⅲ'-C-01")
	# print getAllTable()
	# print getWLByDay()b
	# print getAllPoints()

if __name__ == '__main__':
	main()	