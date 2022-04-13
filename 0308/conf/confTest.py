# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 15:39
# @Author  : kl
# @File    : confTest.py
from configparser import ConfigParser
# 1、实例化
conf= ConfigParser()
# 2、将文件中的数据读取
conf.read("log.ini", encoding="utf-8")
# 3、使用get函数获取section下的option值# Log必须要有, name也必须存在
value = conf.get("log", "name")
print(value)