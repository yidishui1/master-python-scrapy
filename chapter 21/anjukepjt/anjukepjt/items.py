#(2)
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukepjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#定义主页面元素
#定义好name用来存储商品名
    name=scrapy.Field()
#定义好price用来存储商品价格
    #price=scrapy.Field()
#定义好link用来存储商品链接
    link=scrapy.Field()
#定义好dz用来存储商品评论数
    dz=scrapy.Field()


#定义详情页面元素
# 定义好name1用来存储商品名
    name1=scrapy.Field()
#定义好price1用来存储商品价格
    #price1=scrapy.Field()
#定义好link1用来存储商品链接
    link1=scrapy.Field()
#定义好dz1用来存储商品评论数
    dz1 = scrapy.Field()
#定义tel1用来存储售楼处电话
    tel1=scrapy.Field()

    lptd1=scrapy.Field()
    ckjg1=scrapy.Field()
    wylx1=scrapy.Field()
    kfs1=scrapy.Field()
    qywz1=scrapy.Field()
    lpdz1=scrapy.Field()
    zdsf1=scrapy.Field()
    lphx1=scrapy.Field()
    zxkp1=scrapy.Field()
    jfsj1=scrapy.Field()
    slcdz1=scrapy.Field()
    ysxkz1=scrapy.Field()
    jzlx1=scrapy.Field()
    cqnx1=scrapy.Field()
    rjl1=scrapy.Field()
    lhl1=scrapy.Field()
    ghhs1=scrapy.Field()
    lczk1=scrapy.Field()
    gcjd1=scrapy.Field()
    wyglf1=scrapy.Field()
    wygs1=scrapy.Field()
    cws1=scrapy.Field()
    cwb1=scrapy.Field()