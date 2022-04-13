# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 10:46
# @Author  : kl
# @File    : main.py
import unittest
from tools.HTMLTestRunnerNew import HTMLTestRunner

# 通过TestLoader加载到一个TestSuite当中去
s = unittest.TestLoader().discover(r'E:\python projects\lemon\0308\execise')
print(s)

# 运行测试用例
# runner = unittest.TextTestRunner()
# runner.run(s)

#html测试结果
with open('test_login.html',mode='wb') as b:
    runner = HTMLTestRunner(
        b,
        title='测试报告',
        description='测试报告的描述'
    )
    runner.run(s)