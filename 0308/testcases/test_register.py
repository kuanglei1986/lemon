# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 17:05
# @Author  : kl
# @File    : test_register.py
import os
import ddt
import unittest
import requests
from tools.HandleExcel import HandleExcel
from tools.handle_path import testdatas_dir
from tools.handle_requests import HandleRequests
from tools.hand_log import HandleLog

excel_path = os.path.join(testdatas_dir, "cases.xlsx")
he = HandleExcel(excel_path,"注册")
datas = he.read_all_rows_data()
print(datas)
logger = HandleLog()

@ddt.ddt
class TestRegister(unittest.TestCase):
    name = "注册"

    @classmethod
    def setUpClass(cls) -> None:
        logger.info(f"============= {cls.name} 接口测试开始！ ==============")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info(f"============= {cls.name} 接口测试结束！ ==============")

    @ddt.data(*datas)
    def test_register_success(self, case):
        logger.info(f"********* {case.get('title')} 用例 ********")
        hr = HandleRequests()
        resp = hr.send_req(case["method"], case["url"], eval(case['req_data']))
        res_dict = resp.json()
        print(res_dict)

if __name__ == '__main__':
    unittest.main()