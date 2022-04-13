# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 16:59
# @Author  : kl
# @File    : HandleExcel.py
import os

from openpyxl import load_workbook

# 类与上面的代码/注释之间隔2行
class HandleExcel:

    # 类内部方法之间，用一行隔开。
    def __init__(self,excel_path: str,sheet_name):
        """
        打开一个excel文件，然后加载进来。
        :param excel_path:
        """
        try:
            self.wb = load_workbook(excel_path)
        except:
            logger.exception("excel文件加载失败！")
            raise

        self.select_sheet_by_name(sheet_name)

    def select_sheet_by_name(self, sheet_name):
        self.sh = self.wb[sheet_name]
        # logger.info("当前正在操作的表单名是:{}".format(sheet_name))

    def read_all_rows_data(self):
        """
        从选定的表单当中，第一行作为key.
        将后面的每一行数据，与第一行拼接成一个字典数据，作为一条测试用例数据。
        将所有测试用例数据，添加到一个列表当中。
        :return: 测试用例数据列表
        """
        sh_all_datas = list(self.sh.values)
        # 每一行数据的keys
        keys = sh_all_datas[0]
        # 列表变量 - 存放表单当中的每一行数据
        all_cases_datas = []
        # 遍历表单表当中，从第2行开始的每一行测试数据，并与第一行的keys拼接成一个字典。
        for values in sh_all_datas[1:]:
            one_case = dict(zip(keys, values))
            # logger.info("用例数据为:\n{}".format(one_case))
            all_cases_datas.append(one_case)
        return all_cases_datas

if __name__ == '__main__':
    # 得到excel文件的路径
    file_dir = os.path.dirname(os.path.abspath(__file__))
    case_dir = os.path.dirname(file_dir)
    excel_path = os.path.join(case_dir,"testdatas\cases.xlsx")
    print(excel_path)
    # 实例化HandleExcel类
    he = HandleExcel(excel_path,'注册')
    cases = he.read_all_rows_data()
    print(cases)