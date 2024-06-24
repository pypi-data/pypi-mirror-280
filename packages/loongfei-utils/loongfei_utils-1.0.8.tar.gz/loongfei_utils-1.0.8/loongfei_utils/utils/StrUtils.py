# -*- coding: utf-8 -*-
import datetime
import random
import threading


def init_random_tr(start_str="temp"):
    """
    初始化随机字符串，该方法为线程安全的
    :param start_str: 自定义开头字符串，如果空则默认为“temp”开头
    :return: 返回新的字符串，格式为：开头字符串_时间字符串_1000到9999的随机数
    """
    lock = threading.Lock()
    new_str = start_str
    with lock:
        time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        random_str = str(random.randint(1000, 9999))
        new_str = new_str + "_" + time_str + "_" + random_str
    return new_str
