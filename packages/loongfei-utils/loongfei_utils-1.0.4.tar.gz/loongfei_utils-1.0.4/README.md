## 工具介绍
```
封装该工具的主要目的是为了方便个人后续的开发过程。
```


## 文件结构
```
python-utils/
│
└── loongfei_utils/
   ├── __init__.py        # 将文件夹变为Python包
   ├── M3u8Crawer.py      # 爬取m3u8形式的网上视频，可以控制线程数，需要解密的目前仅支持AES-128
   ├── MultiThreading.py  # 多线程工具类
   └── utils/             # 辅助工具类包
      ├── __init__.py     # 将文件夹变为Python包
      ├── LoggerUtils.py  # 初始化logger日志句柄，用于日志输出
      └── StrUtils.py     # 字符串工具类
      
```
## 工具使用方法
### 一、多线程工具类 MultiThreading
```
举例：
1、获取logger日志句柄
引入：
from loongfei_utils.utils import LoggerUtils
创建logger日志句柄
logger = LoggerUtils.config_only_kzt_logger("info")

2、准备要处理的数据
a = [1,2,3,4,5,6,7,8,9]
b = []

3、定义一个处理数据的方法，这个方法用来处理数据，处理完要返回True 或者 False，以便让多线程工具那些执行失败了
def edit_data(item):
    ac = True
    try:
        if item == 5:
            ac = False
        else:
            b.append(item*5)

    except BaseException as e:
        ac = False
    return ac

4、创建多线程工具类
"""
  多线程工具类ExecuteList，参数如下：
  func : 传入处理数据的方法
  need_execute_list : 需要被处理的数据
  thread_num: 要开启多少线程
  logger: 传入日志句柄，用于多线程日志输出
"""
execute_class = ExecuteList(edit_data,a,5,logger)
# 启动线程
execute_class.start_thread()
# 打印哪些数据处理失败
logger.info(execute_class.getting_error_list())
# 输出处理后b的结果
logger.info(b)

```
### 二、m3u8视频爬取工具类 M3u8Crawer
```
说明：
1、m3u8视频爬取工具类支持非加密类型ts视频的下载，同时也支持加密类型ts视频的下载（目前加密仅支持AES-128）；
2、指定要下载的m3u8文件地址，并指定保存路径，还需要指定保存后的中文名称；
3、本程序采用多线程下载，也需要指定开启的线程数；
4、需要指定下载完成后的视频名字，程序下载完成后会自动合并为指定名字的mp4文件并删除临时的ts文件；
5、需要安装 ffmpeg 工具，用于后期ts文件的合并；
6、程序可以自动判断是否需要解密ts文件。
注：该工具在不断完善中。。。

举例：
1、获取logger日志句柄
引入：
from loongfei_utils.utils import LoggerUtils
创建logger日志句柄，紧进行控制台输出
logger = LoggerUtils.config_only_kzt_logger("info")

2、下载视频
引入：
from loongfei_utils.M3u8Crawer import TSCrawlingToMp4

实例化下载类：
"""
  m3u8工具类TSCrawlingToMp4，参数如下：
  url : 视频对应的m3u8地址
  path : 本地保存地址
  zh_file_name: 视频的保存名字
  logger: 传入日志句柄，用于多线程日志输出
"""
move_crawling = TSCrawlingToMp4(url="https://v.cdnlz7.com/20240427/18107_f7400038/index.m3u8",
                     path="D:/Downloads/view/",
                     zh_file_name="奔跑吧第八季第1期",
                     logger=logger)
# 启动爬取，100为开启100个线程下载ts文件
move_crawling.do_crawling(100)

```