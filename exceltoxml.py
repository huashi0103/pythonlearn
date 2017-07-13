import xlrd
import xlwt
import xml
from xml.dom import minidom
import os


#简单的IO操作保存txt
def createtxt():
    ls=os.linesep
    #get filename
    while True:
        fname=input('Enter filename:')
        if os.path.exists(fname):
            print("error:'%s' already exists"%fname)
        else:
             break;

    #get file content(text)lines
    all=[]
    print("\nEnter lines('.'by itself to quit).\n")

    #loop until user terminates input
    while True:
        entry=input('>')
        if entry=='.':
            break
        else:
            all.append(entry)

    #write ines to file with proper line-ending

    fobj=open(fname,'w')
    fobj.writelines(['%s%s'%(x,ls) for x in all])
    fobj.close()
    print('DONE!')
    f=open(fname,'r')
    for l in f.readlines():
        print(l,end='')
    

#读写excel
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

#读写xml
def xml():
    #import xml.dom.minidom
    impl = minidom.getDOMImplementation()#创建xml对象
    dom = impl.createDocument(None, 'Root', None)  #创建dom
    root = dom.documentElement#根节点
    root.setAttribute('attr','root')#属性
    for i in range(1,3):
        employee=dom.createElement('employee')#添加子节点
        employee.setAttribute('attr','child')#添加属性
        value=dom.createTextNode('value')
        employee.appendChild(value)#添加值
        
        root.appendChild(employee)
    #保存
    file=r'C:\Users\huach\Desktop\test.xml'
    if os.path.exists(file):os.remove(file)#有就删除了
    f=open(file,'a')
    dom.writexml(f, addindent='  ', newl='\n')
    f.close()
    print('xml写入成功')
    #读取
    dom = minidom.parse(file)
    root = dom.documentElement
    ems=root.getElementsByTagName('employee')
    for em in ems:
        attr=em.getAttribute("attr")#属性
        print('em.attr=%s'%attr)
        print('em.attr=%s'%em.firstChild.data)#值

#访问mssql，引用pymssql，这里是别人的简单封装，可以直接用，简单的查询增删查改没问题·
import pymssql

class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启
    用法：
    """
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():
## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    ms = MSSQL(host="localhost",user="sa",pwd="sa",db="MWDatabase")
    resList = ms.ExecQuery("select * from Fiducial_Anchor_Cable")
    for li in resList:
        print(li)      

#本地数据sqlite
import sqlite3

def insert():
    conn=sqlite3.connect('test.db')
    cursor=conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
    cursor.execute('insert into user(id,name) values (\'1\',\'Michael\')')
    cursor.rowcount
    cursor.close
    conn.commit()
    conn.close()

def select():
    conn=sqlite3.connect('test.db')
    cursor=conn.cursor()
    cursor.execute('select * from user where id=?',('1',))
    values=cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()



if __name__=='__main__':
    xml()

