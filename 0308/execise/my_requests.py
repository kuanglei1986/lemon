# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 17:38
# @Author  : kl
# @File    : my_requests.py
import requests


class MyRequests:

    # 初始化方法
    def __init__(self):
        # 请求头
        self.headers = {"X-Lemonban-Media-Type": "lemonban.v2"}

    # 属性
    # 方法 post/put.. json=XXX , get..  params=XXX
    def send_requests(self,method,url, data,token=None):
        # 处理请求头
        self.__deal_header(token)
        # 调用requests的方法去发起一个请求。并得到响应结果
        if method.upper() == "GET":
            resp = requests.request(method, url, params=data, headers=self.headers)
        else:
            resp = requests.request(method, url, json=data, headers=self.headers)
        return resp

    def __deal_header(self,token=None):
        if token:
            self.headers["Authorization"] = "Bearer {}".format(token)

if __name__ == '__main__':
    mr = MyRequests()
    url = "http://api.lemonban.com/futureloan/member/register"
    req_data = {
        "mobile_phone": "18610100022",
        "pwd": "123456789",
        "reg_name": "py37小简"
    }
    method = "post"
    resp = mr.send_requests(method,url,req_data)
    print(resp.json())

    # url地址
    url = "http://api.lemonban.com/futureloan/member/login"
    # 请求类型：post

    # 请求体
    req_data = {
        "mobile_phone": "13418538457",
        "pwd": "123456789"
    }
    method = "post"
    resp = mr.send_requests(method,url,  req_data)
    print(resp.json())

    # 提取出来，给到下一接口去作为请求
    json_res = resp.json()
    token = json_res["data"]["token_info"]["token"]
    member_id = json_res["data"]["id"]

    url = "http://api.lemonban.com/futureloan/member/recharge"
    # 请求数据
    req_data = {
        "member_id": member_id,
        "amount": 10
    }
    method = "post"
    resp = mr.send_requests(method,url,  req_data,token=token)
    print(resp.json())
