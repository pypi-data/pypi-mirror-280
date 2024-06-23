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

cd = TSCrawlingToMp4(url="https://v6.mzxay.com/202309/17/iaFe9v2WnL1/video/2000k_0X1080_64k_25/hls/index.m3u8",
                             path="D:/Downloads/view/",
                             zh_file_name="玉蒲团之偷情宝鉴",
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

# path='D:/Downloads/view/m3u8_20240623002855656747_8959/h5bo97v98l0rb8825afmfwzgg3sqwqgfzrim3wgnk7ex5pi20htskgvz3km7ji4zkkqfnzka0vsqu4e0lq2ari69qwkgpmfnh951txhkxkp6266ldt8pwbc1f1gsf5zrnezz0t4fql3y1kk5zw9q8zizsxfq0l7x8s5ea34khbgaf52j0an1ky7hi32alv98ijjdv7qnwttdbfx0yjpc6xcv6b6wiibrw7rcyqpeesch78gbr6ty0dptou0vzcvjup4faxa0d5736uh8lzfu2f20t08jh67itzz5imek9.ts'
# with open(path,'w+') as f:
#     f.write("1")

# path='D:/Downloads/view/m3u8_20240623002855656747_8959/h5bo97v98l0rb8825afmfwzgg3sqw0t4fql3yky7hi32apuh8lzfu2f20t08jh67itzz5imek9.ts'
# with open(path,'w+') as f:
#     f.write("1")

