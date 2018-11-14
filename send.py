# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:02:52 2018

@author: CCC
"""


import smtplib
import sys

# 添加文件所在的地址的文件夹，以加载模块
sys.path.append("E:/18_learn/Project/stock/new_email")
import config
import message

# 发送邮件
def send_mail():
    msg = message.get_mail_message()
    smtpserver = 'smtp.qq.com'
    sender = config.get_config("get_user", "user_mail", "user.ini")
    username = sender
    password = config.get_config("get_user", "user_pwd", "user.ini")
    receiver = config.get_client("get_customers", "customers.ini")
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    for i in receiver:
        smtp.sendmail(sender, i, msg.as_string())
    smtp.quit()

send_mail()
