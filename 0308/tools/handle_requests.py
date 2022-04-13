# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 16:25
# @Author  : kl
# @File    : handle_requests.py
import os

import requests
from configparser import ConfigParser
from tools.handle_path import conf_path
from tools.hand_log import HandleLog

logger = HandleLog()

class HandleRequests:

    def __init__(self):
        # self.logger = HandleLog()
        # 实例化一个session类
        self.s = requests.Session()
        # 设置全局通用的请求头
        self.s.headers = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
        # 设置全局baseurl
        conf = ConfigParser()
        # print("conf:",conf)
        server_conf = os.path.join(conf_path,"server.ini")
        # print(server_conf)
        s = conf.read(server_conf, encoding="utf-8")
        # print(s)
        self.base_url = conf.get("base","baseurl")
        # print(base_url)

    def send_req(self, method, url, data=None, **kwargs):
        url = self.base_url + url
        logger.info(f"请求url为：{url}")
        logger.info(f"请求method为：{method}")
        logger.info(f"请求headers为：{self.s.headers}")
        logger.info(f"请求datas为：{data}")
        if method.upper() == "GET":
            resp = self.s.get(url, params=data, **kwargs)
        else:
            resp = self.s.request(method, url, data=data, **kwargs)
        logger.info(f"http响应状态码为：{resp.status_code}")
        logger.info(f"响应body为：\n{resp.text}")
        return resp

if __name__ == '__main__':
    h = HandleRequests()


