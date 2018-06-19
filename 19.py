#��19��ǧͼ��ͼƬ������Ŀ
#
#��1��
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QtpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#����picurl�洢ͼƬ����ַ
    picurl=scrapy.Field()
#����picid�洢ͼƬ��ַ�е�ͼƬ�����Է��㹹�챾���ļ���
    picid=scrapy.Field()

#��2��
# -*- coding: utf-8 -*-
import urllib.request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QtpjtPipeline(object):
    def process_item(self, item, spider):
#һ��ͼƬ�б�ҳ���ж���ͼƬ��ͨ��forѭ�����ν�ͼƬ�洢������
        for i in range(0,len(item["picurl"])):
            thispic=item["picurl"][i]
#���������ܽ�Ĺ��ɹ����ԭͼƬ��URL��ַ
            trueurl=thispic+"_1024.jpg"
#�����ͼƬ�ڱ��ش洢�ĵ�ַ
            localpath = "D:/Python35/myweb/part19/pic/" + item["picid"][i] + ".jpg"
#ͨ��urllib.request.urlretrieve()��ԭͼƬ���ص�����
            urllib.request.urlretrieve(trueurl, filename=localpath)
        return item

#��3��
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'qtpjt.pipelines.QtpjtPipeline': 300,
}


#��4��
# -*- coding: utf-8 -*-
import scrapy
import re
from qtpjt.items import QtpjtItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = "qtspd"
    allowed_domains = ["58pic.com"]
    start_urls = (
        'http://www.58pic.com/tb/',
    )

    def parse(self, response):
        item=QtpjtItem()
#������ȡ����ͼ��ַ��������ʽ
        paturl="(http://pic.qiantucdn.com/58pic/.*?).jpg"
        #��ȡ��ӦͼƬ��ַ
item["picurl"]=re.compile(paturl).findall(str(response.body))
#�������ȡͼƬ����������ʽ���Է��㹹������ص��ļ���
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
#��ȡ�������е�ͼƬ��
        item["picid"] = re.compile(patlocal).findall(str(response.body))
        yield item
#ͨ��forѭ�����α���1��200ҳͼƬ�б�ҳ
        for i in range(1,201):
#�������һҳͼƬ�б�ҳ����ַ
            nexturl="http://www.58pic.com/tb/id-"+str(i)+".html"
            yield Request(nexturl, callback=self.parse)





