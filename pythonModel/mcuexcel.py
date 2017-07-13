import xlrd
import xlwt
import os
import pypyodbc

rootpath="D:\\Desktop\\"
#read inner sensor
# filename='内观IP配置表-1.xls'
# innerwork=xlrd.open_workbook(rootpath+filename)
# sheet=innerwork.sheet_by_index(0)
# for row in sheet.get_rows():
#     for cell in row:
#         print(cell.value)

# read mdbdi
sensordic=dict()
#sensors
filename='sensor.xlsx'
innerwork=xlrd.open_workbook(rootpath+filename)
sheet=innerwork.sheet_by_index(0)
for row in sheet.get_rows():
    sensordic[row[1].value.upper()] = row[2].value
#mcu
mcudic=dict()
filename='MCU.xlsx'
mcuwork=xlrd.open_workbook(rootpath+filename)
sheet=mcuwork.sheet_by_index(0)
for row in sheet.get_rows():
    mcudic[row[0].value] = row


file='auto_system_Allpoints.xlsx'
newfile=xlwt.Workbook()
newsheet=newfile.add_sheet('auto_system_allpoints',cell_overwrite_ok=True)
oldfile=xlrd.open_workbook(rootpath+file)
oldsheet=oldfile.sheet_by_name('Sheet1')
nrow=oldsheet.nrows
ncol=oldsheet.ncols
firstrow=oldsheet.row_values(0)
#write  head
for j in range(ncol):
    k=0
    value = firstrow[j]
    if j == firstrow.index('MCU_Number'):
        value='IP'
    if j == firstrow.index('MCU_Station'):
        value="MCU_Name"
    newsheet.write(0, j, value)

newpoints=list()
keys=sensordic.keys()
for i in range(1,nrow):
    row=oldsheet.row_values(i)
    k = 0
    for j in range(ncol):
        value=row[j]
        #MCU number
        if j==firstrow.index('MCU_Station'):
            if row[1].upper() in keys and sensordic[row[1].upper()] in mcudic.keys() :
                value=mcudic[sensordic[row[1].upper()]][1].value
            else:
                newpoints.append(row[1])
                if isinstance(row[j+1],float):
                    if row[j+1]<10:value=value+'-0'+str(int(row[j+1]))
                    else:value=value+'-'+str(int(row[j+1]))

        # IP
        if j==firstrow.index('MCU_Number'):
            if  row[1].upper() in keys and sensordic[row[1].upper()] in mcudic.keys():
                value=mcudic[sensordic[row[1].upper()]][6].value
            else:
                value = ''
        newsheet.write(i, j,value)

for p in newpoints:
    print(p)
print(len(newpoints))

#newpath=rootpath+'newfile.xls'
#if os.path.exists(newpath):os.remove(newpath)
#newfile.save(newpath)
print('ok')
