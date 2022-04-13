# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 15:09
# @Author  : kl
# @File    : logTest.py

import logging

# Logging当中提供的日志相关的方法: --用以下这几个方法,在业务代码当中埋日志。
# Logging.xxxx(你要输出的信息)
# Logging模块,默认会收集warning及以上级别的日志输出。
logging.info("我是py43期")
logging.debug ("我debug")
logging.warning("友h提示, 警告")
logging.error("我出错啦")
logging.critical("出大事了")
logging.exception("也是error级别,但是error级别的报错,输出详细的traceback报错信息")
