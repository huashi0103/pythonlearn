import xml.dom.minidom
import os
def writecs():
    path= r"D:\WORK\Project\苗尾\typelist.xml"
    dom = xml.dom.minidom.parse(path)
    root = dom.documentElement
    instruments = root.getElementsByTagName('Instrument')
    dics = dict()
    if os.path.exists('f.txt'):
        os.remove('f.txt')
    f = open('f.txt', 'a')
    i=0
    for ins in instruments:
        if ins.getAttribute('Fiducial_Table')=='':continue
        f.write('/// <summary>')
        f.write('\n')
        f.write('/// %s'%ins.getAttribute('Instrument_Name'))
        f.write('\n')
        f.write('/// </summary>')
        f.write('\n')
        f.write('[Description("%s")]'%ins.getAttribute('Instrument_Name'))
        f.write('\n')
        f.write('%s,'%ins.getAttribute('Fiducial_Table'))
        f.write('\n')
        i+=1
    print(i)
        #dics[ins.getAttribute('Instrument_Name')] = [ins.getAttribute('Fiducial_Table'), ins.getAttribute('Monitor_Name')]
    for ins in instruments:
        if ins.getAttribute('Fiducial_Table')=='':continue
        classname=ins.getAttribute('Fiducial_Table')
        s='''
            /// <summary>
            /// %s
            /// </summary>
            public class %s:BaseInstrument
            {
               public %s()
               {
                   base.InsType=InstrumentType.%s;
               }
               public override double DifBlock(ParamData data, params double[] expand)
               {
                   return base.DifBlock(data, expand);
               }
               public override double ShakeString(ParamData data, params double[] expand)
               {
                   return base.ShakeString(data, expand);
               }
               public override double AutoDefined(ParamData data, string expression)
               {
                   return base.AutoDefined(data, expression);
               }
            }
        '''
        f.write(s%(ins.getAttribute('Instrument_Name'),classname,classname,classname))

import xml.dom.minidom
def writexml():
    pro='苗尾'
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'ProConfig', None)
    root = dom.documentElement
    root.setAttribute('ProjectName', str(pro))
    ent=dom.createElement('DataRoot')
    dataroot = dom.createTextNode(r'D:\WORK\Project\苗尾\昆明院苗尾监测资料\内观资料')
    ent.appendChild(dataroot)
    root.appendChild(ent)
    inss=dom.createElement('Instruments')
    path=r'D:\WORK\Project\苗尾\苗尾考证表'
    list=os.listdir(path)
    for file in list:
        employee = dom.createElement('Ins')
        insname=dom.createTextNode(file[:file.find('.')])
        employee.appendChild(insname)
        inss.appendChild(employee)
    root.appendChild(inss)

    f = open(r'D:\WORK\Project\苗尾\Config.xml', 'w', encoding='utf-8')
    dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
    f.close()
    print('xml写入成功')



import xlrd
def writeexcel():
    path=r"D:\WORK\Project\白鹤滩\数字边坡数据下红岩渗压计.xlsx"
    book=xlrd.open_workbook(path)
    sheet=book.sheet_by_index(0)
    nr=sheet.nrows
    for i in range(nr):
        print(sheet.row_values(i))

def writetable():
    path = r"D:\WORK\Project\苗尾\typelist.xml"
    dom = xml.dom.minidom.parse(path)
    root = dom.documentElement
    instruments = root.getElementsByTagName('Instrument')

    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'TableConfig', None)
    root = dom.documentElement
    for ins in instruments:
        ent=dom.createElement('Instrument')
        ent.setAttribute('Instrument_Name',ins.getAttribute('Instrument_Name'))
        ent.setAttribute('Fiducial_Table', ins.getAttribute('Fiducial_Table'))
        ent.setAttribute('Instrument_Name', ins.getAttribute('Instrument_Name'))
        root.appendChild(ent)
    inss=dom.createElement('Instruments')


