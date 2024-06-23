import re

from loongfei_utils.MultiThreading import ExecuteList
from loongfei_utils.utils import LoggerUtils
from loongfei_utils.utils import StrUtils
from loongfei_utils.M3u8Crawer import TSCrawlingToMp4

a = ['1s','2s','3','4','5','6','7','8']
logger = LoggerUtils.config_only_kzt_logger("info")
def do_a(item):
    logger.info(item)
    return True

# aa = ExecuteList(do_a, a, 3, logger)
# aa.start_thread()
# print(str(aa.getting_error_list()))
#
# print(type(do_a))
# print(StrUtils.init_random_tr("sss"))

cd = TSCrawlingToMp4(url="https://sbfree1.cdnx-video.com/202207/t2251/m3u8/index.m3u8",
                             path="D:/Downloads/view/",
                             zh_file_name="赤裸特工未删减版",
                             logger=logger)
cd.do_crawling(100)

# str = """
#       适合m3u8格式为：
# #EXTM3U
# #EXT-X-VERSION:3
# #EXT-X-TARGETDURATION:20
# #EXT-X-MEDIA-SEQUENCE:0
# #EXT-X-KEY:METHOD=AES-128,URI="enc.key",IV=0x00000000000000000000000000000000
# #EXTINF:20.333333,
# https://p.jisuts.com:999/hls/232/20240211/2326858/plist0.ts
# #EXTINF:1.125000,
#       """


