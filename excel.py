import xlrd
import xlwt
import os
import re


def createexcel():
    workbook=xlwt.Workbook()
    return workbook;

def saveexcel(workbook,filename):
    workbook.save(filename)
    print('创建excel文件完成！')

def addsheet(workbook,sheetname):
    sheet=workbook.add_sheet(sheetname,cell_overwrite_ok=True)
    return sheet



def test():
    filepath=r'D:\WORK\Project\三峡\三峡工程自动化文件\XIN三峡枢纽考证表格式.xls'
    data=xlrd.open_workbook(filepath)
    #sheet=data.sheet_by_index(0)
    sheet=data.sheet_by_name('Fiducial_MeasureWater_Weir')
    mergecell=sheet.merged_cells # 获取合并单元格#(row,row_range,col,col_range),
    print(len(mergecell))
    rowcount=sheet.nrows
    colcount=sheet.ncols
    newwork=createexcel()
    newsheet=addsheet(newwork,'sheet1')
    newsheet.write(0,0,sheet.cell(0,0).value)
    newsheet.write(0,1,sheet.cell(0,1).value)
    '''
    for i in range(1,rowcount):
        print('%s:%s'%(int(sheet.cell(i,0).value),sheet.cell(i,1).value))
        newsheet.write(i,0,sheet.cell(i,0).value)
        newsheet.write(i,1,sheet.cell(i,1).value)
    saveexcel(newwork,r'D:\WORK\Project\三峡\三峡工程自动化文件\ptest.xls')
    '''
    for i in range(rowcount):
        print(sheet.row_values(i))
    pass

def CreateSum():
    file=r'D:\WORK\Project\苗尾\考证表格式.xls'
    data=xlrd.open_workbook(file)
    count=len(data.sheets())
    newworkbook=createexcel()
    for i in range(count):
        #print(data.sheet_by_index(i).name)
        oldsheet=data.sheet_by_index(i)
        newsheet=addsheet(newworkbook,oldsheet.name)
        nc=oldsheet.ncols
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        contents=oldsheet.cell(0,0).value
        index=0;
        if(zhPattern.search(contents)):index=2
        for j in range(nc):
            newsheet.write(0,j,oldsheet.cell(index,j).value)
    saveexcel(newworkbook,r'D:\WORK\Project\苗尾\合集.xls')  

def rwexcel():
    path=r'C:\Users\huach\Desktop\右岸交通洞-渗压计.xlsx'
    file=xlrd.open_workbook(path)#打开文件
    sheet=file.sheet_by_index(0)#根据索引获取第一个sheet
    #sheet=file.sheet_by_name('Pe1-1')
    nc=sheet.ncols#获取sheet的列数
    nr=sheet.nrows#sheet 行数

    newbook=xlwt.Workbook()#新建一个excel对象
    nsheet=newbook.add_sheet('testsheet',cell_overwrite_ok=True)#添加一个sheet
    for i in range(20):
        row=sheet.row_values(i)#获取第i行，这是个数组
        for j in range(nc):
            print(row[j],end='')
            nsheet.write(i,j,row[j])#写到新的sheet里边
        print()
    newfile=r'C:\Users\huach\Desktop\test.xls'
    if os.path.exists(newfile):os.remove(newfile)#有就删除了
    newbook.save(newfile)#把新创建的excel对象保存

    
if __name__=='__main__':
    rwexcel()




