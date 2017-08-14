# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
dir_path = os.path.dirname

BASE_DIR = (dir_path(dir_path(os.path.abspath(__file__))))
#print(BASE_DIR)

sys.path.append(BASE_DIR)

from core import main

main.run()