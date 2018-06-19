#（1）
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QtpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#建立每个进入每个子图片链接网址
    link=scrapy.Field()
#建立picurl存储图片的网址
    picurl=scrapy.Field()
# #建立picid存储图片网址中的图片名，以方便构造本地文件名
#     picid=scrapy.Field()
#建立单页文件夹，方便查找
    picfolder=scrapy.Field()