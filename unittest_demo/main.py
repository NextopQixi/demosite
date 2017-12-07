#!/bin/python
#coding=utf-8
'''
Created on 2016年8月25日

@author: wujianxin
'''
import os
import smtplib
import email
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase

# 第三方 SMTP 服务
mail_host="smtp.qiye.163.com"  #设置服务器
mail_user="wujianxin@taihe.com"    #用户名
mail_pass="Xiaoxin270"   #口令 


sender = 'wujianxin@taihe.com'
# receivers = ['245608144@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['muchunpeng@taihe.com'] 

def SendEmail(report):
    f = open(report,'rb')
    mail_body = f.read()
    f.close()
    message = MIMEMultipart()
    message.attach(MIMEText(mail_body, 'html', 'utf-8'))
    message['From'] = Header(sender, 'utf-8')
    message['To'] =  Header(receivers[0], 'utf-8')

    subject = '测试'+report+'报告'
    message['Subject'] = Header(subject, 'utf-8')
    
    contype = 'application/octet-stream'  
    maintype, subtype = contype.split('/', 1)  
    ## 读入文件内容并格式化  
    file_msg = MIMEBase(maintype, subtype)  
    file_msg.set_payload(mail_body)  
    encoders.encode_base64(file_msg)  
  
    ## 设置附件头  
    basename = os.path.basename(report)  
    file_msg.add_header('Content-Disposition','attachment', filename = basename)  
    message.attach(file_msg) 
#     # 构造附件1，传送当前目录下的 test.txt 文件
#     att1 = MIMEText(open('UnitTest.html', 'rb').read(), 'base64', 'utf-8')
#     att1["Content-Type"] = 'application/octet-stream'
#     # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#     att1["Content-Disposition"] = 'attachment; filename="UnitTest.html"'
#     message.attach(att1)
    
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return "邮件发送成功"
    except smtplib.SMTPException as e:
        print(e)
        return "Error: 无法发送邮件"

def GenerateReport(path,file):
    os.system('cd'+path)
    filelist = os.listdir(path)
    if file not in filelist:
        return 'file not in path'
    os.system('py.test '+file+' --html=./'+file[0:file.find('.')]+'.html')
    
if __name__ == '__main__':

    path=os.getcwd()
    file='UnitTestDemo.py'
    GenerateReport(path,file)
    report='UnitTest.html'
    print(SendEmail(report))
