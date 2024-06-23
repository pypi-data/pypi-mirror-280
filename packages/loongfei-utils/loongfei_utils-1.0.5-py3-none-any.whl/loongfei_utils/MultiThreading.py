# -*- coding: utf-8 -*-
import threading
import time
from types import FunctionType


class ExecuteList:

    __function__ = None  # 处理序列数据的方法
    __need_execute_list__ = []  # 需要处理的数据序列
    __executing_list__ = []  # 正在处理中的数据序列
    __execute_error_list__ = []  # 处理错误的数据序列
    __thread_list__ = []  # 正在执行的线程列表
    __thread_num__ = 0  # 启用的线程数
    lock = threading.Lock()

    """
    fun：实际的处理过程，引入外部函数；需要返回处理结果:True or False
    need_execute_list：需要多线程处理的序列；
    thread_num：启用的线程数；
    logger：日志输出
    """

    def __init__(self, func:FunctionType, need_execute_list:list, thread_num:int, logger:object):
        """
        :param fun: 处理数据的函数
        :param need_execute_list: 需要被处理的数据
        :param thread_num:  启动的线程数
        :param logger:  打印日志logger
        """
        self.__function__ = func
        self.__need_execute_list__ = need_execute_list
        self.__thread_num__ = thread_num
        self.logger = logger

    def start_thread(self):
        for i in range(self.__thread_num__):
            thread_name = "loongfei-thread-" + str(i)
            self.__thread_list__.append(thread_name)
            threading.Thread(target=self.__executing_list_item__, args=(thread_name,)).start()
        if_continue = True
        while if_continue:
            if len(self.__thread_list__) > 0:
                self.logger.info("---> 剩余线程：" + str(self.__thread_list__))
                time.sleep(10)
            else:
                if_continue = False
                self.logger.info("---> 多线程执行完毕，准备结束~~~")

    def __getting_executing_data__(self, execute_type, execute_list_item):
        """
        :param execute_type: 处理类型，1：取；2：销毁；3：添加至错误队列
        :param execute_list_item:
        :return:
        """
        with self.lock:
            if execute_type == "1":
                if len(self.__need_execute_list__) > 0:
                    execute_list_item = self.__need_execute_list__.pop()
                    self.__executing_list__.append(execute_list_item)
                else:
                    execute_list_item = ""
            elif execute_type == "2":
                self.__executing_list__.remove(execute_list_item)
            else:
                self.__executing_list__.remove(execute_list_item)
                self.__execute_error_list__.append(execute_list_item)
        return execute_list_item

    def __executing_list_item__(self, thread_name):
        continue_do = True
        while continue_do:
            execute_list_item = self.__getting_executing_data__("1", "")
            if execute_list_item != "":
                self.logger.info("---> 线程：“" + thread_name + "” ，获取数据 “" + str(execute_list_item) + "” 并开始处理~~~")
                execute_result = None
                try:
                    execute_result = self.__function__(execute_list_item)
                except BaseException as e:
                    self.__getting_executing_data__("3", execute_list_item)
                    self.logger.info("---> 线程：“" + thread_name + "” ，处理数据 “" + str(execute_list_item) + "” 失败，错误信息{0}~~~".format(e))
                else:
                    if not execute_result:
                        self.__getting_executing_data__("3", execute_list_item)
                        self.logger.info("---> 线程：“" + thread_name + "” ，处理数据 “" + str(execute_list_item) + "” 后，处理方法返回错误，请排查处理方法~~~")
                    else:
                        self.__getting_executing_data__("2", execute_list_item)
                        self.logger.info("---> 线程：“" + thread_name + "” ，处理数据 “" + str(execute_list_item) + "” 完毕~~~")

            else:
                continue_do = False
                self.logger.info("---> 线程：“" + thread_name + "” ，执行完毕，即将关闭~~~")
                self.__thread_list__.remove(thread_name)

    def getting_error_list(self):
        return self.__execute_error_list__
