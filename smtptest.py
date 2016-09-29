from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication  

import getpass

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

'''
smtp服务器地址
smtp.126.com
smtp.qq.com
'''
'''
from_addr=input('From:')
to_addr=input('to:')
smtp_server=input('smtp server:')
'''

from_addr='huachengming@126.com'
to_addr='464623826@qq.com'
smtp_server='smtp.126.com'
password=""

def SendMsg(msg):
    server=smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg)
    server.quit()


def SendMail(msgtext,msg_type):
    msg=MIMEText(msgtext,msg_type,'utf-8')
    msg['From']=_format_addr('pythonrtest:%s'%from_addr)
    msg['To']=_format_addr('huashi%s'%to_addr)
    msg['Subject']=Header('come from huashi mail...','utf-8').encode()
    server=smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()



def SendTextMail(msgtext):
    SendMail(msgtext,'plain')
    
def SendHTML(msgtext):
    SendMail(msgtext,'html')

def SendAccessory(msgtext,path,file,ext,filetype):
    # 邮件对象:
    msg = MIMEMultipart()
    msg['From']=_format_addr('pythonrtest:%s'%from_addr)
    msg['To']=_format_addr('huashi%s'%to_addr)
    msg['Subject']=Header('come from huashi mail...','utf-8').encode()
    # 邮件正文是MIMEText: 
    msg.attach(MIMEText(msgtext,'plain','utf-8') )
    print(msg.as_string())
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(path, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase(filetype,ext,filename=file)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=file)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    SendMsg(msg.as_string())
    pass
    


if __name__=="__main__":
    #password=input('password:')
    password="hua0103shi"#getpass.getpass('password:')
    #SendTextMail('这是一封测试邮件，来自huashi')
    SendAccessory(r"this is test mail","D:\\Desktop\\psb.jpg","psb.jpg",'jpg','image')
    
