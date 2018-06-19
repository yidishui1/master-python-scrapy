#(2)
# -*- coding: utf-8 -*-
import scrapy
#导入items文件中的MypjtItem
from mypjt.items import MypjtItem
class MyspdSpider(scrapy.Spider):
    name = "myspd"
    allowed_domains = ["sina.com.cn"]
    start_urls = (
#定义要抓取的起始网址为新浪首页
        'http://www.sina.com.cn/',
    )
    def parse(self, response):
#初始化item
        item=MypjtItem()
#通过Xpath表达式提取该网页中的标题信息
        item["title"]=response.xpath("/html/head/title").extract()
#输出提取到的标题信息
        print(item["title"])