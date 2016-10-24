#coding=utf-8

import pickle

from sqlconnect import MSSQL

# 获取所有的表名
def  getAllTable():
	sql = "SELECT [table] FROM LCRiver_xwdh_1.dbo.DefTableType"
	ms = MSSQL()
	resList = ms.ExecQuery(sql)
	return [str(res[0]).strip() for res in resList]

# 根据测点返回对应表名	
def getTableByPoint(point='C4-A29-PL-01'):
	sql = "SELECT [table] FROM	LCRiver_xwdh_1.dbo.DefTableType "
	sql += "WHERE [type] IN (SELECT [type] FROM LCRiver_xwdh_1.dbo.DefInsSort "
	sql += "WHERE [DesignCode] = '" + point.strip() + "')"
	ms = MSSQL()
	resList =  ms.ExecQuery(sql)
	return "".join(resList[0]).strip()

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
	return [''.join(res).strip() for res in resList]

# 根据测点获取数据
def getDataByPoint(table='T_ZB_PL', point='C4-A22-PL-01', comp='R2', start='2016-07-01', end='2016-07-07'):
	sql = "SELECT DT," + comp + " FROM LCRiver_xwdh_2.dbo." + table + " "
	sql += "WHERE INSTR_NO = '" + point + "' "
	sql += "AND DT >= '" + start + "' AND DT <= '" + end + "'"
	ms = MSSQL()
	resList = ms.ExecQuery(sql)
	dt = [resList[i][0].strftime('%Y-%m-%d') for i in range(len(resList))]
	val = [float(resList[i][1]) for i in range(len(resList))]
	return dt, val

def main():
	# print getCalculatedCompByTable('T_ZB_UP')
	print getDataByPoint()

if __name__ == '__main__':
	main()