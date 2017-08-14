# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json,shutil,os
from core import db_handler




def dump_account(account_data):
    print("这是account_data里的account_data",account_data)
    db_path = db_handler.db_handler()
    username = account_data['username']
    db_account = "%s\\accounts\\%s.json" % (db_path, username)
    f = open(db_account,"w")
    f.write(json.dumps(account_data))
    f.close()

def load_current_balance(id):
    db_path = db_handler.db_handler()
    db_account = "%s\\accounts\\%s.json" % (db_path, id)
    f = open(db_account, "r")
    account_dic = json.loads(f.read())
    now_balance = account_dic["balance"]
    f.close()
    return now_balance

def freeze():
    freeze_username = input("输入你要冻结的账户:").strip()
    db_path = db_handler.db_handler()
    db_account = "%s\\accounts\\%s.json" % (db_path, freeze_username)
    db_frozen_account = "%s\\accounts\\frozen\\%s.json" % (db_path, freeze_username)
    if os.path.exists(db_account):
        shutil.move(db_account,db_frozen_account)
    else:
        print("账户不存在")

def unfreeze():
    freeze_username = input("输入你要冻结的账户:").strip()
    db_path = db_handler.db_handler()
    db_account = "%s\\accounts\\%s.json" % (db_path, freeze_username)
    db_frozen_account = "%s\\accounts\\frozen\\%s.json" % (db_path, freeze_username)
    if os.path.exists(db_frozen_account):
        shutil.move(db_frozen_account,db_account)
    else:
        print("账户不存在")


