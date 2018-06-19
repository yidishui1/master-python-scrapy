#��15�±�д�Զ���ȡ��ҳ������
#15.1 ʵսitems��д
#��1��
D:\Python35\myweb\part15>scrapy startproject autopjt
New Scrapy project 'autopjt', using template directory 'd:\\python35\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\Python35\myweb\part15\autopjt
You can start your first spider with:
    cd autopjt
    scrapy genspider example example.com

#(2)
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#�����name�����洢��Ʒ��
    name=scrapy.Field()
#�����price�����洢��Ʒ�۸�
    price=scrapy.Field()
#�����link�����洢��Ʒ����
    link=scrapy.Field()
#�����comnum�����洢��Ʒ������
    comnum=scrapy.Field()


#15.2 ʵսpipelines��д
#(1)
# -*- coding: utf-8 -*-
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutopjtPipeline(object):
    def __init__(self):
#��mydata.json�ļ�
        self.file = codecs.open("D:/python35/myweb/part15/mydata.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        i=json.dumps(dict(item), ensure_ascii=False)
#ÿ�����ݺ���ϻ���
        line = i + '\n'
#д�����ݵ�mydata.json�ļ���
        self.file.write(line)
        return item
    def close_spider(self,spider):
#�ر�mydata.json�ļ�
        self.file.close()

#(2)
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'autopjt.pipelines.AutopjtPipeline': 300,
}

#(3)
# Disable cookies (enabled by default)
COOKIES_ENABLED = False

#15.4 �Զ������дʵս
#(1)
D:\Python35\myweb\part15>cd .\autopjt\
D:\Python35\myweb\part15\autopjt>scrapy genspider -t basic autospd dangdang.com
Created spider 'autospd' using template 'basic' in module:
  Autopjt.spiders.autospd

#(2)
# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = "autospd"
    allowed_domains = ["dangdang.com"]
    start_urls = (
        'http://category.dangdang.com/pg1-cid4011029.html',
    )

    def parse(self, response):
        item=AutopjtItem()
#ͨ����Xpath���ʽ�ֱ���ȡ��Ʒ�����ơ��۸����ӡ�����������Ϣ
        item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"]=response.xpath("//a[@name='P_pl']/text()").extract()

        # item["name"]=response.xpath("//li/p[2]/a/@title").extract()
        # item["price"]=response.xpath("//li/p[1]/span/text()").extract()
        # item["link"]=response.xpath("//li/p[2]/a/@href").extract()
        # item["comnum"]=response.xpath("//li/p[4]/a/text()").extract()
#��ȡ��󷵻�item
        yield item
#�������ܹؼ���ͨ��ѭ���Զ���ȡ75ҳ������
        for i in range(1,76):
#ͨ�������ܽ����ַ��ʽ����Ҫ��ȡ����ַ
            url="http://category.dangdang.com/pg"+str(i)+"-cid4002203.html"
#ͨ��yield����Request����ָ��Ҫ��ȡ����ַ�ͻص�����
#ʵ���Զ���ȡ
            yield Request(url, callback=self.parse)

#15.5 ����������
#��1��
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#��2��
# -*- coding: utf-8 -*-
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutopjtPipeline(object):
    def __init__(self):
#��ʱ�洢�����ļ���mydata2.json������֮ǰ�洢���ļ�mydata.json��ͻ
        self.file = codecs.open("D:/python35/myweb/part15/mydata2.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        #item=dict(item)
        #print(len(item["name"]))
#ÿһҳ�а��������Ʒ��Ϣ�����Կ���ͨ��ѭ����ÿһ�δ���һ����Ʒ
#����len(item["name"])Ϊ��ǰҳ����Ʒ�����������α���
        for j in range(0,len(item["name"])):
#����ǰҳ�ĵ�j����Ʒ�����Ƹ�ֵ������name
            name=item["name"][j]
            price=item["price"][j]
            comnum=item["comnum"][j]
            link=item["link"][j]
#����ǰҳ�µ�j����Ʒ��name��price��comnum��link����Ϣ����һ��
#������ϳ�һ���ֵ�
            goods={"name":name,"price":price,"comnum":comnum,"link":link}
            #����Ϻ�ĵ�ǰҳ�е�j����Ʒ������д��json�ļ�
i=json.dumps(dict(goods), ensure_ascii=False)
            line = i + '\n'
            self.file.write(line)
#����item
        return item
    def close_spider(self,spider):
        self.file.close()



