#(6)
# -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem
class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    allowed_domains = ["sina.com.cn"]
#     start_urls = (
# #设置起始网址为新浪新闻下的某个新闻网页
#         'http://tech.sina.com.cn/d/s/2016-09-17/doc-ifxvyqwa3324638.shtml',
#     )
    start_urls = (
        'http://tech.sina.com.cn/d/s/2016-09-17/doc-ifxvyqwa3324638.shtml',
        "http://sina.com.cn",
    )

    def parse(self, response):
        item=MypjtItem()
#通过Xpath表达式提取网页中的标题信息
        # (4)
        item["title"] = response.xpath("/html/head/title/text()").extract()
        item["key"] = response.xpath("//meta[@name='keywords']/@content").extract()
#直接输出，在Python3.X中，虽然包含中文信息，但直接输出即可
        print(item["title"],item["key"])
        return item