# -*- coding: utf-8 -*-
import threading
import time

from loongfei_utils.utils import StrUtils
from loongfei_utils.MultiThreading import ExecuteList
from copy import deepcopy
from Crypto.Cipher import AES

import shutil
import requests as rq
import re
import os


class TSCrawlingToMp4:
    """
    非加密ts文件抓取抓取
    """

    def __init__(self, url, path, zh_file_name, logger):
        """
        :param url: 视频对应的m3u8地址
        :param path: 要存放的路径，不能是中文
        :param zh_file_name: 将合并后采用英文名字的视频转移并命名为中文名字
        :param logger: 传入日志句柄，用于日志输出
        """
        self.error_retry_counts = 3
        self.count = 10
        self.url = url
        self.path = path
        self.zh_file_name = zh_file_name
        self.__init_file_path()
        self.logger = logger

        # 需要抓取的链接列表对应的名字列表，用于创建本地m3u8文件，并按次顺序合并TS文件
        self.ts_name_list = []
        # 需要抓取的链接列表
        self.crawling_url_list = []
        # 因个别网站文件名字超长，导致windows系统无法保存，因此采用映射关系保存
        self.name_and_name_rel = {}
        # 生成随机字符串使用
        self.default_ts_count = 100000
        # 下载错误的链接
        self.error_download_list = {}
        # 是否继续下载错误链接
        self.if_continue_download_error_url = True

    def __init_file_path(self):
        # 获得一个随机值，用来设置临时文件夹名称及临时mp4命名
        m3u8_str = StrUtils.init_random_tr("m3u8")
        # 存放的路径上创建新的文件夹，存放TS文件及m3u8文件，视频生成后将被删除
        if not self.path.endswith("/"):
            self.path = self.path + "/"
        self.save_ts_file_dir = self.path + m3u8_str + "/"
        # TS视频合并后的英文名字，用于ffmpeg处理，ffmpeg不支持中文路径
        self.en_file_name = m3u8_str
        # 判断存储TS的临时文件是否存在，不存在则创建
        if not os.path.exists(self.save_ts_file_dir):
            os.makedirs(self.save_ts_file_dir)
        # m3u8文件路径
        self.m3u8_file_path = self.save_ts_file_dir + self.en_file_name + ".txt"
        # 合并后的 mp4 英文路径
        self.en_mp4_view_path = self.save_ts_file_dir + self.en_file_name + ".mp4"
        # 合并后的 mp4 中文路径
        self.zh_mp4_view_path = self.path + self.zh_file_name + ".mp4"

    def __init_new_file_name(self):
        lock = threading.Lock()
        with lock:
            self.default_ts_count += 1
            new_ts_name = "ts_movie_" + str(self.default_ts_count) + ".ts"
        return new_ts_name

    def __init_crawling_ts_list(self):
        crawling_data = rq.get(self.url)
        self.data_body = crawling_data.text
        pattern = r"\S+\.ts"
        ts_item = ""
        ts_item_list = re.findall(pattern, self.data_body)
        if len(ts_item_list) > 0:
            ts_item = ts_item_list[0]
        if ts_item.startswith("http") or ts_item.startswith("HTTP"):
            self.crawling_url_list = deepcopy(ts_item_list)
            for url in ts_item_list:
                ts_name = url.split('/')[-1]
                new_ts_name = self.__init_new_file_name()
                self.name_and_name_rel[ts_name] = new_ts_name
                self.ts_name_list.append(new_ts_name)
        else:
            # self.ts_name_list = deepcopy(ts_item_list)
            for ts_name in ts_item_list:
                if not ts_name.startswith("/"):
                    crawling_url = re.sub("(?<=/)[^/]*.m3u8$", ts_name, self.url)
                    self.crawling_url_list.append(crawling_url)
                    new_ts_name = self.__init_new_file_name()
                    self.name_and_name_rel[ts_name] = new_ts_name
                    self.ts_name_list.append(new_ts_name)
        self.__init_decode_object()

    def __init_decode_object(self):
        # 获取加密算法类型
        encryption_key_str = ""
        encryption_key_str_list = re.findall("(?<=METHOD=)[^,]*(?=,)", self.data_body)
        if len(encryption_key_str_list) > 0:
            encryption_key_str = encryption_key_str_list[0]
        if encryption_key_str == "" or encryption_key_str is None:
            self.if_encryption = False
        else:
            self.if_encryption = True
            # 获得IV偏移量
            iv_temp_list = re.findall("(?<=IV=).*", self.data_body)
            if len(iv_temp_list) == 0:
                self.IV = ""
            else:
                self.IV = iv_temp_list[0].replace("0x", "")[:16].encode()
            # 获取TS解密key
            encryption_key_uri = ""
            encryption_key_uri_list = re.findall("(?<=URI=\")[^\"]*(?=\")", self.data_body)
            if len(encryption_key_uri_list) > 0:
                encryption_key_uri = encryption_key_uri_list[0]
            if encryption_key_uri.startswith("http") or encryption_key_uri.startswith("HTTP"):
                encryption_key_url = encryption_key_uri
            else:
                encryption_key_url = re.sub("(?<=/)[^/]*.m3u8$", encryption_key_uri, self.url)
            self.encryption_key = rq.get(encryption_key_url).content
            # 根据加密算法初始化解密对象
            if encryption_key_str == "AES-128":
                decode_obj = AES.new(self.encryption_key, AES.MODE_CBC, self.IV)
                self.decode_obj = decode_obj

    def __download_ts_video(self, crawling_url):
        if_success = True
        ts_name = crawling_url.split('/')[-1]
        new_ts_name = self.name_and_name_rel[ts_name]
        save_ts_path = self.save_ts_file_dir + new_ts_name
        try:
            with open(save_ts_path, 'wb+') as f:
                if self.if_encryption:
                    f.write(self.decode_obj.decrypt(rq.get(crawling_url, timeout=(60, 600)).content))
                else:
                    f.write(rq.get(crawling_url, timeout=(60, 600)).content)
        except BaseException as e:
            self.logger.error("---> 下载文件出错，错误信息为：{}".format(e))
            if_success = False
        return if_success

    def __create_ts_info_file(self):
        for error_download_item in self.error_download_list:
            ts_name = error_download_item.split('/')[-1]
            # self.logger.info("~~~~~ts_name: {}".format(ts_name))
            new_ts_name = self.name_and_name_rel[ts_name]
            # self.logger.info("~~~~~new_ts_name: {}".format(new_ts_name))
            # self.logger.info("~~~~~self.ts_name_list: {}".format(self.ts_name_list))
            self.ts_name_list.remove(new_ts_name)
        # self.logger.info("~~~after remove error items , self.ts_file_list:" + str(self.ts_name_list))
        with open(self.m3u8_file_path, 'w+') as f:
            for ts_name_temp in self.ts_name_list:
                f.write(f"file \'{ts_name_temp}\'" + "\n")

    def __hebing_ts(self):
        self.logger.info("---> m3u8文件地址：" + self.m3u8_file_path)
        self.logger.info("---> 英文视频地址：" + self.en_mp4_view_path)
        os.system("ffmpeg -f concat -i " + self.m3u8_file_path + " -c copy " + self.en_mp4_view_path)
        self.logger.info("---> 视频合并完成，开始转移视频，并重命名，新的文件地址为：" + self.zh_mp4_view_path)
        shutil.move(self.en_mp4_view_path, self.zh_mp4_view_path)
        self.logger.info("---> 转移完成，开始删除原始视频TS文件~~~")
        shutil.rmtree(self.save_ts_file_dir)

    def __retry_download_error_ts_video(self):
        time.sleep(3)
        if self.if_continue_download_error_url:
            if self.error_retry_counts <= 0 or len(self.error_download_list) <= 0:
                self.if_continue_download_error_url = False
        while self.if_continue_download_error_url:
            self.logger.info(f"---> 倒数第 {self.error_retry_counts} 次尝试,需重新下载 {len(self.error_download_list)} 个错误链接：" + str(self.error_download_list))
            # 初始化多线程类
            execute_list_temp = ExecuteList(self.__download_ts_video, self.error_download_list, self.count, self.logger)
            # 开启多线程
            execute_list_temp.start_thread()
            self.error_download_list.clear()
            self.error_download_list = deepcopy(set(execute_list_temp.getting_error_list()))
            self.error_retry_counts -= 1
            if self.error_retry_counts > 0 and len(self.error_download_list) > 0:
                self.__retry_download_error_ts_video()
            else:
                self.if_continue_download_error_url = False

    def do_crawling(self, count, error_retry_counts=3):
        """
        执行爬取
        :param count: 开启线程数
        :param error_retry_counts: 如果抓取错误，对于错误的请求，重新抓取次数，默认3次
        """
        # 基于m3u8地址获取TS对应的m3u8文件并整理成TS名字序列
        self.__init_crawling_ts_list()
        self.count = count
        self.error_retry_counts = error_retry_counts
        # 基于TS名字序列生产保存路径序列
        self.logger.info(self.ts_name_list)
        # self.logger.info(self.savePathList)
        self.logger.info(self.crawling_url_list)
        # 初始化多线程类
        execute_list = ExecuteList(self.__download_ts_video, self.crawling_url_list, self.count, self.logger)
        # 开启多线程
        execute_list.start_thread()
        if len(execute_list.getting_error_list()) > 0:
            self.error_download_list.clear()
            self.error_download_list = deepcopy(set(execute_list.getting_error_list()))
            self.__retry_download_error_ts_video()
        # 在本地生成txt，用来保存ts的合并顺序
        self.__create_ts_info_file()
        # 合并TS文件生成英文名称的mp4，转移正式mp4文件并以中文名命名同时删除ts临时文件
        self.__hebing_ts()
        self.logger.info(f"---> {self.zh_file_name} ，下载完成~~~~")
