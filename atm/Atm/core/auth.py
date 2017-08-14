# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json,os
from core import db_handler
from core import main
from conf import settings

def login_required(func):
    "验证用户是否登录"

    def wrapper(*args,**kwargs):
        #print('--wrapper--->',args,kwargs)
        if args[0].get('is_logined'):
            return func(*args,**kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper


def acc_login(username,password,user_data_dic):
    '''
    
    :param username: 
    :param password: 
    :return: auth,是否分录变ture，id=账户
    '''
    if isfrozen(username):
        print("用户已经冻结！")
        return
    else:
        user_data_dic_authed = acc_auth(username,password,user_data_dic)#发给验证模块验证
    return user_data_dic_authed

def acc_auth(username,password,user_data_dic):

    db_path = db_handler.db_handler()#调用数据库判断模块获取数据库地址
    db_account = "%s\\accounts\\%s.json"%(db_path,username)#使用数据库地址调取数据库中相应的账户数据


    print("该用户数据文件路径，%s"%db_account)
    if os.path.exists(db_account):
    # with open(db_account,"r") as f:
    #     print(f.read())
        f = open(db_account, "r")
        account_data_dic = json.loads(f.read())#这是账户数据，以json读取的字典形式呈现
        print("该用户数据文件内容",account_data_dic)
        print("这是临时用户数据," ,user_data_dic)

        if account_data_dic["username"] == username and account_data_dic["password"] == password:
            print("登录成功")
            user_data_dic["is_logined"] = True
            user_data_dic["user_data"] = account_data_dic
            print("acc_auth登录成功后的user_data_dic",user_data_dic)
            return user_data_dic

        else:
            print("错误的用户名或密码")
    else:
        print("错误的用户名或密码")

def isfrozen(username):
    '''
    判断是否是冻结账户
    :param username:
    :return:
    '''
    db_path = db_handler.db_handler()  # 调用数据库判断模块获取数据库地址
    db_frozen_account = "%s\\accounts\\frozen\\%s.json" % (db_path, username)  # 使用数据库地址调取数据库中相应的账户数据
    if os.path.exists(db_frozen_account):
        return True
    else:
        return False
