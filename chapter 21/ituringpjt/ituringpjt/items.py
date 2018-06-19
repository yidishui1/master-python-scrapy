# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IturingpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url0 = scrapy.Field()
    url1 = scrapy.Field()
    # picture = scrapy.Field()
    name = scrapy.Field()
    recommend = scrapy.Field()
    reader = scrapy.Field()
    author = scrapy.Field()
    translator = scrapy.Field()
    label = scrapy.Field()
    introduction = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
    pages = scrapy.Field()
    printing = scrapy.Field()
    state = scrapy.Field()
    otitle = scrapy.Field()
    characteristic = scrapy.Field()
    authorintroduction = scrapy.Field()

