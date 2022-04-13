# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 13:47
# @Author  : kl
# @File    : login.py

def login_check (username=None, password=None):
    """ 登录校验的函数
    : param username:账号
    : param password: 密码
    :return: dict type
    """
    if username!= None and password!= None:
        if username =="python43" and password =="lemonban":
	        return {'code': 0, 'msg': '登录成功'}
        else:
	        return {'code': 1, 'msg': '账号或密码不正确'}
    else:
        return {'code': 1, 'msg': '所有的参数不能为空'}

if __name__ == '__main__':
    res = login_check("python43","lemonban")
    if res == {"code": 0, "msg": "登录成功"}:
        print("success!")
    else:
        print("fail!")