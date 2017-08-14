# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from core import db_handler
import os
from conf import settings

def logger(amount, tran_type, account_data):
    log_info = []
    print("this is logger:",amount, tran_type, account_data)
    db_path = db_handler.db_handler()
    username = account_data['username']
    balance = str(account_data['balance'])
    action = settings.TRANSACTION_TYPE[tran_type]['action']
    account_log = "%s\\logs\\%s.txt" % (db_path,username)
    log_info_now = "%s    %s   余额：%s\n"%(action,amount,balance)
    if os.path.exists(account_log):
        with open(account_log, "r", encoding="utf-8") as f_r:
            for line in f_r:
                log_info.append(line)
    log_info.append(log_info_now)
    with open(account_log,"w",encoding="utf-8") as f_w:
        for line in log_info:
            f_w.write(line)