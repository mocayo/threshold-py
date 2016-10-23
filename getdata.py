#coding=utf-8

import pickle

from sqlconnect import MSSQL

# 获取所有的表名
def  getAllTable():
	sql = "SELECT * FROM LCRiver_xwdh_1.dbo.DefTableType"
	ms = MSSQL()
	resList = ms.ExecQuery(sql)
	return [str(res[1]).strip() for res in resList]

# 根据测点返回对应表名	
def getTableByPoint(point='C4-A29-PL-01'):
	sql = "SELECT [table] FROM	LCRiver_xwdh_1.dbo.DefTableType "
	sql += "WHERE [type] IN (SELECT [type] FROM LCRiver_xwdh_1.dbo.DefInsSort "
	sql += "WHERE [DesignCode] = '" + point.strip() + "')"
	ms = MSSQL()
	resList =  ms.ExecQuery(sql)
	return "".join(resList[0]).strip()

def getCompByTable(table='T_ZB_PL'):
	sql = "SELECT R1,R2,R3 FROM LCRiver_xwdh_1.dbo.MonitorItemType "
	sql += "WHERE TABLE_NAME = '" + table.strip() + "'"

	ms = MSSQL()
	resList = ms.ExecQuery(sql)
	return resList[0]

def getRByComp(comps,comp):
	for i in range(len(comps)):
		if comp == comps[i]:
			return 'r' + str(i+1)
	return None

def getRByPoint(point,comp):
	table = getTableByPoint(point)
	comps = getCompByTable(table)
	return getRByComp(comps,comp)

def dumpPointData(table='T_ZB_PL_RES1',point='C4-A22-PL-01',component='r1'):
	sql = "SELECT DISTINCT	DT,	WL,	realVal FROM LCRiver_xwdh_3.dbo." + table
	sql += " WHERE INSTR_NO = '" + point + "' AND component = '" + component + "'"
 	
	ms = MSSQL()
	print sql
	resList =  ms.ExecQuery(sql)

	output = open(point + '%' + component + '.pkl', 'wb')
	pickle.dump(resList, output)
	return resList

def main():
	# dumpPointData(table='T_ZB_JZ_RES1',point='C4-A09-J-01',component='r1')

if __name__ == '__main__':
    main()