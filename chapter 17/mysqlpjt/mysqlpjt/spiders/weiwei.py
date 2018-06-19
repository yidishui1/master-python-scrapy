#(6)
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mysqlpjt.items import MysqlpjtItem


class WeiweiSpider(CrawlSpider):
    name = 'weiwei'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'),allow_domains=('sina.com.cn')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MysqlpjtItem()
        #通过xpath表达式提取网页标题
        i["name"]=response.xpath("/html/head/title/text()").extract()
        #通过xpath表达式提取网页的关键词
        i["keywd"]=response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        return i
