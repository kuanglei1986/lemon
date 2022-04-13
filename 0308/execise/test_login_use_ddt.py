# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 17:46
# @Author  : kl
# @File    : test_login_use_ddt.py
import unittest
import ddt
import os
from login import login_check
from tools.HandleExcel import HandleExcel

# 得到excel文件的路径
file_dir = os.path.dirname(os.path.abspath(__file__))
case_dir = os.path.dirname(file_dir)
excel_path = os.path.join(case_dir, "testdatas\cases.xlsx")
print(excel_path)
# 实例化HandleExcel类
he = HandleExcel(excel_path, 'login')
cases = he.read_all_rows_data()
# print(cases)
#测试类@ddt.ddt
# 1、每一组测试数据,都会识别为一个测试用例
# 2、如果某一组测试数据用例执行失败,并不会影响下一组测试数据用例的执行。

@ddt.ddt
class TestLogin(unittest.TestCase):
    @ddt.data(*cases)
    def test_login_00_success(self, data):
        res = login_check(data["user"],data["password"])
        print(res)
        # print(type(res))
        # print(type(data["expected"]))
        self.assertEqual(eval(data["expected"]),res)

if __name__ == '__main__':
    unittest.main()