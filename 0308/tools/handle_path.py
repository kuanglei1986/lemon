# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 17:35
# @Author  : kl
# @File    : handle_path.py

import os

# basedir
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(basedir)
conf_path = os.path.join(basedir, "conf")
# print(conf_path)

# 日志配置文件_path
log_conf_path = os.path.join(basedir, "conf", "log.ini")
# 日志输出路径配置
log_output_dir = os.path.join(basedir,"outputs", "logs")

# 测试数据dir
testdatas_dir = os.path.join(basedir, "testdatas")
# print(testdatas_dir)