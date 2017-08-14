# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
dir_path = os.path.dirname
BASE_DIR = (dir_path(dir_path(os.path.abspath(__file__))))
print(BASE_DIR)

sys.path.append(BASE_DIR)
from conf import settings
from core import accounts
from core import logger



def make_transaction(amount,tran_type,user_data):
    while True:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        print(user_data)
        old_balance = user_data['user_data']['balance']
        print("这是make_transaction里的interet和old_balance",interest,old_balance)
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount +interest
            user_data['user_data']['balance'] = new_balance
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            user_data['user_data']['balance'] = new_balance
            if new_balance < 0:
                print("\033[31;1m额度不足\033[0m")
                break
        print("这是make_transaction里的interet和new_balance", interest, new_balance)
        account_data = user_data['user_data']
        logger.logger(amount, tran_type, account_data)
        accounts.dump_account(account_data)
        break


    #print(interest)