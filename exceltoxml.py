import xlrd
import xlwt
import  xml.dom.minidom


file=r'D:\WORK\Project\苗尾\考证表格式.xls'
data=xlrd.open_workbook(file)
sheet=data.sheet_by_name('InstrumentTable')
nr=sheet.nrows
nc=sheet.ncols

import xml.dom.minidom  
impl = xml.dom.minidom.getDOMImplementation()  
dom = impl.createDocument(None, 'CONFIG_LIST', None)  
root = dom.documentElement
root.setAttribute('Count',str(nr))
firstrow=sheet.row_values(0)
for i in range(1,nr):
    row=sheet.row_values(i)
    print(row)
    employee = dom.createElement('Instrument')
    for i in range(nc):
        employee.setAttribute(str(firstrow[i]),str(row[i]))
    root.appendChild(employee)  
f=open(r'D:\WORK\Project\苗尾\typelist.xml','a')
dom.writexml(f, addindent='  ', newl='\n')
f.close()
