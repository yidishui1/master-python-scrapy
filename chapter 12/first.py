# coding=utf-8
# 第十二章
# 12.3 常用工具命令
# (1)
from scrapy.spiders import Spider


class FirstSpider(Spider):
    name = "first"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://www.baidu.com",
    ]

    def parse(self, response):
        pass