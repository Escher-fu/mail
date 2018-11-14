# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:57:02 2018

@author: CCC
"""

'''
[配置文件介绍]：
user.ini: 存放发件人的邮箱和密码
customers.ini: 存放收件人列表的邮箱号
'''

import configparser

#填写配置文件所对应的目录
the_path = "E:/18_learn/Project/stock/new_email/"

# 读取配置文件
# 获取发件邮箱得用户名与密码
def get_config(section, key, file_name):
    config = configparser.ConfigParser()
    path = the_path+file_name
    config.read(path)
    return config.get(section, key)

get_config("get_user", "user_mail", "user.ini")

# 获取收件人邮箱列表
def get_client(option, file_name):
    config = configparser.ConfigParser()
    path = the_path+file_name
    config.read(path)
    options = config.options(option)
    client_list = []
    for i in options:
        mail = config.get(option, i)
        client_list.append(mail)
    return(client_list)

get_client("get_customers", "customers.ini")
