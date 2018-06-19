# -*- coding: utf-8 -*-
# 导入随机模块
import random
# 导入有关IP池有关的模块
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
# 导入有关用户代理有关的模块
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

'''如果要设置IP代理此请开启
class HTTPPROXY(HttpProxyMiddleware):
    # 初始化 注意一定是 ip=''
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        item = random.choice(IPPOOL)
        try:
            print("当前的IP是："+item["ipaddr"])
            request.meta["proxy"] = "http://"+item["ipaddr"]
        except Exception as e:
            print(e)
            pass


#IP池设置

IPPOOL=[
    {"ipaddr": "60.13.187.162:63000"},
    {"ipaddr": "222.185.137.182:6666"},
    {"ipaddr": "58.247.135.174:63000"},
    {"ipaddr": "221.5.54.6:808"},
    {"ipaddr": "122.114.31.177:808"},
    {"ipaddr": "61.135.217.7:80"},
    {"ipaddr": "59.56.252.38:63000"},
    {"ipaddr": "220.191.103.223:6666"},
    {"ipaddr": "113.200.241.202:63000"},
    {"ipaddr": "171.221.202.181:63000"},
    {"ipaddr": "14.118.255.222:6666"},
    {"ipaddr": "14.118.255.138:6666"},
    {"ipaddr": "121.231.155.219:6666"},
    {"ipaddr": "117.86.12.69:18118"},
    {"ipaddr": "117.63.78.4:6666"},
    {"ipaddr": "125.120.203.129:6666"},
    {"ipaddr": "223.145.228.166:6666"},
    {"ipaddr": "110.73.9.160:8123"},
    {"ipaddr": "222.42.136.15:63000"},
    {"ipaddr": "183.167.217.152:63000"},
]
'''
'''如果要设置用户代理池请开启'''


# 用户代理
class USERAGENT(UserAgentMiddleware):
    #初始化 注意一定是 user_agent=''
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        item = random.choice(UAPOOL)
        try:
            print("当前的User-Agent是："+item)
            request.headers.setdefault('User-Agent', item)
        except Exception as e:
            print(e)
            pass


# 设置用户代理池
UAPOOL=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5"
]