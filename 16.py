#��16��CrawlSpider
#16.1 ��ʶCrawSpider
#��1��
D:\Python35\myweb\part16>scrapy startproject mycwpjt
New Scrapy project 'mycwpjt', using template directory 'd:\\python35\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\Python35\myweb\part16\mycwpjt
You can start your first spider with:
    cd mycwpjt
    scrapy genspider example example.com

#��2��
D:\Python35\myweb\part16\mycwpjt>scrapy genspider -t crawl weisuen sohu.com
Created spider 'weisuen' using template 'crawl' in module:
  Mycwpjt.spiders.weisuen

#16.2 ������ȡ��
#��1��
rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

#��2��
 rules = (
        Rule(LinkExtractor(allow=('.shtml')), callback='parse_item', follow=True),
    )

#��3��
rules = (
        Rule(LinkExtractor(allow=('.shtml'),allow_domains=(sohu.com)), callback='parse_item', follow=True),
    )

#16.3 ʵսCrawSpiderʵ��
#��1��
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MycwpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    link=scrapy.Field()

#��2��
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MycwpjtPipeline(object):
    def process_item(self, item, spider):
        print(item["name"])
        print(item["link"])
        print("-------------------")
        return item

#��3��
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'mycwpjt.pipelines.MycwpjtPipeline': 300,
}

#��4��
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mycwpjt.items import MycwpjtItem


class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
#������ҳ��url��ַ�����ڣ�
#��http://news.sohu.com/20160926/n469167364.shtml��
#���Կ��Եõ���ȡ��������ʽΪ'.*?/n.*?shtml��
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'),allow_domains=('sohu.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MycwpjtItem()
#����Xpath���ʽ��ȡ������ҳ�еı���
        i["name"]=response.xpath("/html/head/title/text()").extract()
#����Xpath���ʽ��ȡ��ǰ������ҳ������
        i["link"]=response.xpath("//link[@rel='canonical']/@href").extract()
        return i

#��5��
 rules = (
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'),allow_domains=('sohu.com')), callback='parse_item', follow=False),
    )




