#14.1 Scrapy的中文输出
#(1)
# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
class MypjtItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义title，用来存储网页标题信息
    title=scrapy.Field()
    key=scrapy.Field()