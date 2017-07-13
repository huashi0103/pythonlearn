from mssql import MSSQL
import xlrd

ms = MSSQL(host='DESKTOP-9SCR28N\SQLEXPRESS12', user='sa', pwd='123', db='MWDatabase')
def step1():
    excelpath=r'D:\Desktop\仪器类型.xlsx'
    workbook=xlrd.open_workbook(excelpath)
    sheet=workbook.sheet_by_index(0)
    nr=sheet.nrows
    instruments=ms.ExecQuery("select * from InstrumentTypeTable")
    #for l in li:print(l)
    reslist=ms.ExecQuery("select Fiducial_Table,Instrument_Name from InstrumentTable")
    for l in reslist:
        if(not CheckTable(l[0])):continue
        for item in instruments:
            if item[4]!=l[1]:continue
            sql="update %s set SubProject_Name='%s',Point_Code='%s' where ItemProject_Name='%s'"%(l[0],item[1],item[6],item[2])
            fres=ms.ExecNonQuery(sql)
            #print(sql)

def step3():
    reslist=GetTableName()
    prolist=[]
    protable=[]
    alllist=dict()
    for l in reslist:
        if (not CheckTable(l[0])): continue
        res=ms.ExecQuery("select name from syscolumns where id = object_id('%s')"%l[0])
        alllist[l[0]]=res

    for key in alllist:
        for l in alllist[key]:
            #if l.upper() not in prolist:
            flag=True
            for v in alllist.values():
                if l not in v:
                    flag=False
                    #prolist.append(l[0].upper())
                    #protable.append(key)
            if flag:prolist.append(l[0])
    for p in prolist:print(p)
    #print(len(prolist))
    res=ms.ExecQuery("select * from FieldName_Chinese_English")
    oldplist=[]
    for r in res:oldplist.append(r[2].upper())
    count=0
    for i in range(len(prolist)):
        if prolist[i] not in oldplist:
            count+=1
            print("%s %s"%(protable[i],prolist[i]))
    print(count)




def GetTableName():
    reslist=ms.ExecQuery("select Fiducial_Table,Instrument_Name from InstrumentTable")
    tables=[]
    for l in reslist:
        if (not CheckTable(l[0])): continue
        tables.append(l)
    return tables

def CheckTable(table):
    reslist = ms.ExecQuery("select count(1) from sys.objects where name = '%s'"%table)
    return reslist[0][0]==1


if __name__=='__main__':
    step3()
