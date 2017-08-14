# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from core import auth
from core import db_handler
from core import transaction
from core import accounts
from core import logger
from core.auth import login_required

import json,os,shutil

'''
临时账户数据（id、账户数据、是否登录）
:return: 
'''
user_data_dic = {
    "id": "",
    "user_data": "",
    "is_logined": False
}

def run():
    '''
    处理用户交互的事情
    :return: 
    '''
    flag = True
    while flag:

        if user_data_dic["is_logined"] == False:
            username = input("请输入用户名:").strip()
            password = input("请输入密码:").strip()
            if username == "admin":#做一个临时管理接口
                if password == "123456":
                    manage()
                else:
                    print("密码错!")
            else:
                user_data_dic["id"] = username#载入一个临时的用户数据，id是用户名，是否登录是“否”
                user_data_dic_authed = auth.acc_login(username,password,user_data_dic)#使用验证模块的登录函数尝试登录
                if user_data_dic["is_logined"] == True:
                    interactive(user_data_dic_authed)#让已经验证的用户进入交互功能
                else:
                    continue
        else:
            interactive(user_data_dic)

def interactive(user_data):
    '''
    交互功能，调用六大功能
    :return: 
    '''
    #print("welcome to interactive")
    print("这是interactive里的user_data_dic",user_data)
    func_list_str = ["1、账户信息",
                     "2、存款",
                     "3、取现",
                     "4、转账",
                     "5、账单",
                     "6、登出"]
    for line in func_list_str:
        print(line)
    func_dic = {
        '1': account_info,#账户信息
        '2': deposit,#存款
        '3': withdraw,#取款
        '4': transfer,#转账
        '5': pay_check,#账单查询
        '6': logout,#登出
    }
    choose_input = input(">>>>>>>>>请输入你的选择：").strip()
    if choose_input not in func_dic:
        print("输入的内容有误")
    else:
        func_dic[choose_input](user_data)

def account_info(user_data):
    '''
    账户信息
    :return: 
    '''
    # print("this is account_info")
    now_balance = accounts.load_current_balance(user_data["id"])
    user_data["user_data"]["balance"] = now_balance#在进行操作前先刷新下现在的余额
    print("这是账户查询里的user_date", user_data)
    print("\033[34;1m用户:%s\033[0m"%user_data['id'])
    print("\033[34;1m额度:%s\033[0m"%user_data["user_data"]["balance"])

@login_required
def deposit(user_data):
    '''
    存款模块
    :return:
    '''
    #print("this is deposit")
    now_balance = accounts.load_current_balance(user_data["id"])
    user_data["user_data"]["balance"] = now_balance#在进行操作前先刷新下现在的余额
    print("这是还款里的user_date", user_data)
    input_amount = input("请输入需要存入的金额，最小单位1元：").strip()
    if len(input_amount)>0 and input_amount.isdigit():
        input_amount = int(input_amount)
    else:
        print("请输入整数")
    transaction.make_transaction(input_amount,"deposit",user_data)


@login_required
def withdraw(user_data):
    '''
    取款模块
    :return: 
    '''
    print("this is withdraw")
    now_balance = accounts.load_current_balance(user_data["id"])
    user_data["user_data"]["balance"] = now_balance#在进行操作前先刷新下现在的余额
    print("这是取现里的user_date", user_data)
    input_amount = input("请输入需要提现的金额，最小单位1元：").strip()
    if len(input_amount) > 0 and input_amount.isdigit():
        input_amount = int(input_amount)
    else:
        print("请输入整数")
    transaction.make_transaction(input_amount, "withdraw", user_data)


@login_required
def transfer(user_data):
    '''
    转账模块
    :return: 
    '''

    now_balance = accounts.load_current_balance(user_data["id"])
    user_data["user_data"]["balance"] = now_balance  # 在进行操作前先刷新下现在的余额
    print("这是取现里的user_date", user_data)
    ############################
    #获取转账帐号数据
    db_path = db_handler.db_handler()  # 调用数据库判断模块获取数据库地址
    while True:
        transfer_to = input("请输入转账的ID:").strip()
        receive_user_data = {
            'user_data':''
        }
        db_account = "%s\\accounts\\%s.json" % (db_path, transfer_to)
        if os.path.exists(db_account):
            f = open(db_account, "r")
            receive_user_data['user_data'] = json.loads(f.read())
            f.close()
            break
        else:
            print("账户不存在")

    ###########################
    input_amount = input("请输入需要转账的金额，最小单位1元：").strip()
    if len(input_amount) > 0 and input_amount.isdigit():
        input_amount = int(input_amount)
    else:
        print("请输入整数")

    transaction.make_transaction(input_amount, "transfer_to", user_data)
    now_balance2 = accounts.load_current_balance(user_data["id"])
    if now_balance > now_balance2:#如果钱被成功划走了，那么就在给对方帐号打钱
        transaction.make_transaction(input_amount, "transfer_from", receive_user_data)

@login_required
def pay_check(user_data):
    '''
    账单模块
    :return: 
    '''
    print("this is pay_check")
    db_path = db_handler.db_handler()
    username = user_data["user_data"]['username']
    account_log = "%s\\logs\\%s.txt" % (db_path, username)
    if os.path.exists(account_log):
        with open(account_log, "r", encoding="utf-8") as f_r:
            for line in f_r:
                print(line)
    else:
        print("暂无交易信息")


def logout(user_data):
    exit()

def manage():
    '''
    管理员接口
    :return:
    '''
    while True:
        func_list_str = ["1、添加账户",
                         "2、用户额度管理",
                         "3、冻结账户管理",
                         "4、登出",
                         ]
        for line in func_list_str:
            print(line)
        func_dic = {
            '1': account_add,  # 账户add
            '2': limit,  # 额度管理
            '3': account_frozen,  # 账户冻结
            '4': exit,  # 转账

        }
        choose_input = input(">>>>>>>>>请输入你的选择：").strip()
        if choose_input not in func_dic:
            print("输入的内容有误")
        else:
            func_dic[choose_input]()

def account_add():
    add_username = input("请输入需要添加的用户名：").strip()
    add_password = input("请输入用户的密码:").strip()
    add_password_again = input("请重复一次输入密码:").strip()
    if len(add_username) > 0 and len(add_password) > 0 :
        if add_password == add_password_again:
            db_path = db_handler.db_handler()  # 调用数据库判断模块获取数据库地址

            db_account_add = "%s\\accounts\\%s.json" % (db_path, add_username)  # 使用数据库地址调取数据库中相应的账户数据
            if os.path.exists(db_account_add):
                # with open(db_account,"r") as f:
                #     print(f.read())
                print("账户已存在")
            else:
                add_money = input("请输入金额，最小单位1元：")
                if add_money.isdigit():

                    add_money = int(add_money)
                    add_user_info = {
                        "username":add_username,
                        "password":add_password,
                        "balance":add_money
                    }
                    f = open(db_account_add, "w")
                    f.write(json.dumps(add_user_info))
                    f.close()
                else:
                    print("输入金额必须是最小单位1元的数字！")
        else:
            print("两次密码输入不一致")
    else:
        print("用户名和密码不为空")

def limit():
    username = input("请输入你要调整的用户名：")

    db_path = db_handler.db_handler()
    db_account = "%s\\accounts\\%s.json" % (db_path, username)
    if os.path.exists(db_account):
        new_limit = input("请输入你想调整的额度:")
        if new_limit.isdigit():
            new_limit = int(new_limit)
            f_r = open(db_account,"r")
            user_data = json.loads(f_r.read())
            user_data["balance"] = new_limit
            f_r.close()
            f_w = open(db_account,"w")
            f_w.write(json.dumps(user_data))
            f_w.close()
            print("调整完成！")
        else:
            print("请输入整数！")
    else:
        print("输入的用户名不存在！")

def account_frozen():
    while True:
        func_list_str = ["1、冻结账户",
                         "2、解冻",
                         "3、返回上一级",
                         ]
        for line in func_list_str:
            print(line)
        func_dic = {
            '1': accounts.freeze,  # 账户add
            '2': accounts.unfreeze,  # 额度管理
            '3': manage  # 账户冻结

        }
        choose_input = input(">>>>>>>>>请输入你的选择：").strip()
        if choose_input not in func_dic:
            print("输入的内容有误")
        else:
            func_dic[choose_input]()

def custom(money,mall_name):
    '''
    处理从商城来的用户交互的事情
    :return:
    '''
    #print("this is custom")

    username = input("请输入用户名:").strip()
    password = input("请输入密码:").strip()
    user_data_dic["id"] = username#载入一个临时的用户数据，id是用户名，是否登录是“否”
    user_data_dic_authed = auth.acc_login(username,password,user_data_dic)#使用验证模块的登录函数尝试登录
    if user_data_dic["is_logined"] == True:
        pay_success = mall_transfer(user_data_dic_authed,money,mall_name)#让已经验证的用户进入交互功能
        return pay_success





def mall_transfer(user_data,money,mall_name):
    print(user_data,money,mall_name)
    now_balance = accounts.load_current_balance(user_data["id"])
    user_data["user_data"]["balance"] = now_balance  # 在进行操作前先刷新下现在的余额
    print("这是mall里的user_date", user_data)

    db_path = db_handler.db_handler()  # 调用数据库判断模块获取数据库地址
    receive_user_data = {
        'user_data': ''
    }
    db_account = "%s\\accounts\\%s.json" % (db_path, mall_name)
    if os.path.exists(db_account):
        f = open(db_account, "r")
        receive_user_data['user_data'] = json.loads(f.read())
        f.close()


    transaction.make_transaction(money, "transfer_to_mall", user_data)
    now_balance2 = accounts.load_current_balance(user_data["id"])
    if now_balance > now_balance2:  # 如果钱被成功划走了，那么就在给对方帐号打钱
        transaction.make_transaction(money, "transfer_from", receive_user_data)

        return True
    else:
        return False


