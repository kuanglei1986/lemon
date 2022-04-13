# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 16:16
# @Author  : kl
# @File    : hand_log.py
"""
自己封装的日志类：
1、具备的功能：能够将日志同时输出到控制台和文件当中。(实例化的时候就具备)
2、debug()、info()、warning()、error()、critical()、exception()

延伸拓展：单例模式
"""
import os
import datetime
import logging
from configparser import ConfigParser
from tools.handle_path import log_conf_path,log_output_dir

class HandleLog(logging.Logger):

    def __init__(self):
        # 直接从配置文件当中读取：日志名字、日志文件路径、日志级别
        # 1、实例化
        conf = ConfigParser()
        # 2、将文件中的数据读取
        conf.read(log_conf_path, encoding="utf-8")
        super().__init__(conf.get("log","name"),
                         conf.get("log","level"))
        # 能够将日志同时输出到控制台和文件当中
        # 设计日志的格式
        fmt = '%(asctime)s %(levelname)s %(filename)s 【行号:%(lineno)d】:%(message)s'
        formatter = logging.Formatter(fmt)

        # ========2、 创建一个控制台输出渠道 ============
        # 实例化一个控制台渠道类
        handle1 = logging.StreamHandler()
        # 设置输出渠道的，日志格式
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        # ========2、 创建一个文件输出渠道 ============
        # 实例化一个文件渠道类, [如果日志当中有中文，要指定编码格式为utf-8]
        # 指定日志文件名称:  文件名_时间.log
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        log_filename = "{}_{}.log".format(conf.get("log", "logfile_name"),now)
        log_full_path = os.path.join(log_output_dir, log_filename)
        handle2 = logging.FileHandler(log_full_path,
                                      encoding="utf-8")
        # 设置输出渠道的，日志格式
        handle2.setFormatter(formatter)
        self.addHandler(handle2)


logger = HandleLog()

if __name__ == '__main__':
    logger = HandleLog()
    logger.info("666")