#(2)
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MysqlpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #建立name存储网页标题
    name=scrapy.Field()
    #建立keywd存储网页关键词
    keywd=scrapy.Field()