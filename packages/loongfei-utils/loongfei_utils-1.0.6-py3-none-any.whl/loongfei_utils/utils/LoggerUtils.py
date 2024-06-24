# -*- coding: utf-8 -*-
import logging
import os

def setup_logger():

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # 设置日志级别为INFO

    if not logger.handlers:

        log_directory = os.path.join(os.path.dirname(__file__), 'logs')
        os.makedirs(log_directory, exist_ok=True)  # 确保日志目录存在
        file_handler = logging.FileHandler(os.path.join(log_directory, 'app.log'))
        file_handler.setLevel(logging.INFO)  # 文件记录INFO及以上级别的日志


        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)  # 控制台输出INFO及以上级别的日志


        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)


        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger

def config_only_kzt_logger(logger_level="critical"):
    """
    初始化控制台输出logger，该方法不会写入本地日志文件
    :param logger_level: 设置日志级别，默认"critical"，其他级别："debug", "info", "warning", "error", "critical"
    :return: 日志句柄，用于打印日志
    """
    logger = logging.getLogger()
    if logger_level == "debug":
        logger.setLevel(logging.DEBUG)
    elif logger_level == "info":
        logger.setLevel(logging.INFO)
    elif logger_level == "warning":
        logger.setLevel(logging.WARNING)
    elif logger_level == "error":
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.CRITICAL)

    formatter = logging.Formatter(fmt='%(asctime)s  %(filename)s  [line:%(lineno)d]  %(levelname)s :%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # 控制台的输出
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    # 将输出的流 添加给logger
    logger.addHandler(ch)
    return logger