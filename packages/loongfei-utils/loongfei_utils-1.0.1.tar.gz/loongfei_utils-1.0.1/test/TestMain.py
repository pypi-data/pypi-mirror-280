from com.fcfspace.loongfei.MultiThreading import ExecuteList
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(fmt='%(asctime)s  %(filename)s  [line:%(lineno)d]  %(levelname)s :%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
#控制台的输出
ch = logging.StreamHandler()
ch.setFormatter(formatter)
#将输出的流 添加给logger
logger.addHandler(ch)
a = ['1s','2s','3','4','5','6','7','8']

def do_a(item):
    logger.info(item)
    return True

aa = ExecuteList(do_a, a, 3, logger)
aa.start_thread()
print(str(aa.getting_error_list()))

print(type(do_a))