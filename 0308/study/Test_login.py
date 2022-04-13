# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 17:02
# @Author  : kl
# @File    : Test_login.py
import unittest
import os
from login import login_check

# 得到excel文件的路径
file_dir = os.path.dirname(os.path.abspath(__file__))
case_dir = os.path.dirname(file_dir)
excel_path = os.path.join(case_dir,"testdatas\cases.xlsx")
print(excel_path)
# 实例化HandleExcel类
he = HandleExcel(excel_path,'注册')
cases = he.read_all_rows_data()
print(cases)

# 测试类
class TestLogin(unittest.TestCase):
    def setUp(self):
        print("-----每一个测试用例运行之前,会执行我")

    def tearDown(self) -> None:
        print("----每一个测试用例运行之后,会执行我 我是后置清理工--")

    @classmethod
    def setUpClass(cls) -> None:
        print("********测试类的第一个用例运行之前,会执行我")

    @classmethod
    def tearDownClass(cls) -> None:
        print("******测试类的最后一个用例运行之前,会执行我 我是后置清理工")

    # 测试用例，test_开头
    def test_login_success(self):
        res = login_check("python43", "lemonban")
        expected_res = {"code": 0, "msg": "登录成功"}
        self.assertEqual(expected_res,res)
        self.assertIn("a",["a","b","c"])

    def test_login_null(self):
        res = login_check("python43")
        expected_res = {"code": 1, "msg": "所有的参数不能为空"}
        self.assertEqual(expected_res,res)

    def test_login_fail(self):
        res = login_check("python43", "lemonban1")
        expected_res = {"code": 1, "msg": "账号或密码不正确"}
        self.assertEqual(expected_res,res)

if __name__ == '__main__':
    unittest.main()
