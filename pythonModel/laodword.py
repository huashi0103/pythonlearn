import win32com
from win32com.client import Dispatch, constants
import win32com.client
import os
import sys
import re
import string
import copy
from mssql import MSSQL

import pypyodbc

ms = MSSQL(host='DESKTOP-9SCR28N\SQLEXPRESS12', user='sa', pwd='123', db='MWDatabase')


# ms = MSSQL(host='XJ', user='sa', pwd='123', db='MWDatabase')
def loadaccess():
    print("从mdb中读取数据")
    rootpath=r"D:\Desktop\BGKDB.MDB"
    conn = pypyodbc.connect(u'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + rootpath)
    sql='select b.MName,b.MCP1,a.* from Sensor as a left join MCU as b on a.MID=b.MID'
    cur=conn.cursor()
    cur.execute(sql)
    list = cur.fetchall()

    print("开始更新或者插入数据")
    sqlformat="update Auto_System_AllPiont set MCU_Station='%s',MCU_Number='%s',IP_Address='%s' where Survey_Point_Number='%s'"

    checksql="select * from Auto_System_AllPiont where Survey_Point_Number='%s'"
    insertsql="	insert Into Auto_System_AllPiont (ID,Survey_Point_Number,MCU_Station,MCU_Number,IP_Address,Instrument_Name) values (%s,'%s','%s','%s','%s','%s')"
    idsql='select max(id) from Auto_System_AllPiont'
    for l in list:
        try:
            if l[0] is None:continue
            checkres=ms.ExecQuery(checksql%l[3])
            if len(checkres) != 0: #表里边有的测点
                sql=sqlformat%(l[0].split('-')[0],l[0],l[1],l[3])
                #print(sql)
                res=ms.ExecNonQuery(sql)
                if res == 0: print(sql)
            else:#表里边没有的测点
                if l[6] == '位移计':#位移计单独处理
                    name=l[3][:-2]
                    mres = ms.ExecQuery("select * from Fiducial_Multi_Displacement where Survey_point_Number='%s'"%name)
                    if len(mres) != 0:#判断是否是多点位移计
                        sname=mres[int(l[3][-1:])-1][2]
                        checkres = ms.ExecQuery(checksql % sname)
                        if len(checkres) != 0:#多点用转换后的测点再查一次，有就更新
                            sql = sqlformat % (l[0].split('-')[0], l[0], l[1], sname)
                            res = ms.ExecNonQuery(sql)
                            if res == 0: print(sql)
                        else:#没有插入
                            id = ms.ExecQuery(idsql)[0][0]
                            id = int(id) + 1
                            sql = insertsql % (id, sname, l[0].split('-')[0], l[0], l[1],'多点位移计')
                            ms.ExecNonQuery(sql)
                    else:#单点位移计直接添加
                        id = ms.ExecQuery(idsql)[0][0]
                        id = int(id) + 1
                        sql = insertsql % (id, l[3], l[0].split('-')[0], l[0], l[1],'单点位移计')
                        ms.ExecNonQuery(sql)
                elif l[6] == '锚索计':
                    name = l[3][:-2]
                    #print(name)
                    checkres = ms.ExecQuery(checksql%name)
                    if len(checkres) != 0:  # 表里边有的测点
                        sql = sqlformat % (l[0].split('-')[0], l[0], l[1],name)
                        # print(sql)
                        res = ms.ExecNonQuery(sql)
                        if res == 0: print(sql)
                    else:
                        id = ms.ExecQuery(idsql)[0][0]
                        id = int(id) + 1
                        sql = insertsql % (id,name, l[0].split('-')[0], l[0], l[1],'锚索测力计')
                        ms.ExecNonQuery(sql)
                else:#其他直接插入
                    print(l[3])
                    id = ms.ExecQuery(idsql)[0][0]
                    id = int(id) + 1
                    sql=insertsql%(id,l[3],l[0].split('-')[0],l[0],l[1],l[6])
                    ms.ExecNonQuery(sql)
        except Exception as e:
            print(e)
            print(sql)
            break
    print('over')




def deleteerror():
    print("从mdb中读取数据")
    rootpath=r"D:\Desktop\BGKDB.MDB"
    conn = pypyodbc.connect(u'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + rootpath)
    sql='select b.MName,b.MCP1,a.* from Sensor as a left join MCU as b on b.MID=a.MID'
    #sql='select * from Sensor'
    cur=conn.cursor()
    cur.execute(sql)
    list = cur.fetchall()
    for l in list:
        if l[6] == '锚索计':
            print(l)








if __name__=='__main__':
    loadaccess()
