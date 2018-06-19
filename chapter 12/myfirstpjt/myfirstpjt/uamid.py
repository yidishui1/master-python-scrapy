# -*- coding: utf-8 -*-
#(6)
#uamid下载中间件
import random
from myfirstpjt.settings import UAPOOL
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
    def __init__(self,ua=''):
        self.ua=ua
    def process_request(self,request,spider):
        thisua=random.choice(UAPOOL)
        print("当前使用的user-agent是："+thisua)
        request.headers.setdefault('User-Agent',thisua)
