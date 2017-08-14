# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json,os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def db_handler():
    '''
    判断数据库引擎，暂时没有这个功能
    :return: 
    '''
    db_path = file_db()
    print(db_path)
    return db_path



def file_db():
    '''
    返回数据库的路径
    :return:db_path
    '''
    db_path = "%s\db"%BASE_DIR
    #f=open()
    return db_path

db_handler()