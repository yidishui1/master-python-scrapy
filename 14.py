#��14��Scrapy���������洢
#14.1 Scrapy���������
#(1)
# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
class MypjtItem(scrapy.Item):
    # define the fields for your item here like:
    # ����title�������洢��ҳ������Ϣ
    title=scrapy.Field()
    
#(2)
# -*- coding: utf-8 -*-
import scrapy
#����items�ļ��е�MypjtItem
from mypjt.items import MypjtItem
class MyspdSpider(scrapy.Spider):
    name = "myspd"
    allowed_domains = ["sina.com.cn"]
    start_urls = (
#����Ҫץȡ����ʼ��ַΪ������ҳ
        'http://www.sina.com.cn/',
    )
    def parse(self, response):
#��ʼ��item
        item=MypjtItem()
#ͨ��Xpath���ʽ��ȡ����ҳ�еı�����Ϣ
        item["title"]=response.xpath("/html/head/title").extract()
#�����ȡ���ı�����Ϣ
        print item["title"]

#(3)
# -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem
class MyspdSpider(scrapy.Spider):
    name = "myspd"
    allowed_domains = ["sina.com.cn"]
    start_urls = (
        'http://www.sina.com.cn/',
    )
    def parse(self, response):
        item=MypjtItem()
        item["title"]=response.xpath("/html/head/title").extract()
        #print item["title"]
# item["title"]��һ���б��������ǿ���ͨ��forѭ�����������б��е�Ԫ��
        for i in item["title"]:
#�Ա��������ı�����Ϣ����encode("gbk")����
            print i.encode("gbk")

#(4)
D:\Python35\myweb\part13>scrapy startproject mypjt
New Scrapy project 'mypjt', using template directory 'd:\\python35\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\Python35\myweb\part13\mypjt

You can start your first spider with:
    cd mypjt
    scrapy genspider example example.com

#(5)
# -*- coding: utf-8 -*-
import scrapy
class MypjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()

#(6)
# -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem
class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    allowed_domains = ["sina.com.cn"]
    start_urls = (
#������ʼ��ַΪ���������µ�ĳ��������ҳ
        'http://tech.sina.com.cn/d/s/2016-09-17/doc-ifxvyqwa3324638.shtml',
    )

    def parse(self, response):
        item=MypjtItem()
#ͨ��Xpath���ʽ��ȡ��ҳ�еı�����Ϣ
        item["title"]=response.xpath("/html/head/title/text()")
#ֱ���������Python3.X�У���Ȼ����������Ϣ����ֱ���������
        print(item["title"])

#14.2 Scrapy�����Ĵ洢
#(1)
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#����Ŀ����pipelines�ļ����������MypjtPipeline������������忴��
    'mypjt.pipelines.MypjtPipeline': 300,
}

#(2)
# -*- coding: utf-8 -*-
#����codecsģ�飬ʹ��codecsֱ�ӽ��н���
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#������pipelines������࣬������Ҫ��ղ�settings.py�������õ�������Ӧ����
class MypjtPipeline(object):
#__init__()Ϊ��ĳ�ʼ����������ʼ��ʱ�����
    def __init__(self):
#������д��ķ�ʽ�������һ����ͨ�ļ����ڴ洢ץȡ��������
        self.file = codecs.open("D:/python35/myweb/part13/mydata1.txt", "wb", encoding="utf-8")
#process_item()Ϊpipelines�е���Ҫ��������Ĭ�ϻ��Զ�����
    def process_item(self, item, spider):
#����ÿ��Ҫд������
        l = str(item) + '\n'
#�˴�ͨ��print()������������ĵ���
        print(l)
#����Ӧ��Ϣд���ļ���
        self.file.write(l)
        return item
#close_spider()����һ���ڹر�֩��ʱ����
    def close_spider(self,spider):
#�ر��ļ�����ʼ����
        self.file.close()

#14.3 ������ĵ�json�ļ�
#(1)
# -*- coding: utf-8 -*-
import codecs
#��ΪҪ����JSON�ļ��Ĵ������Ե���jsonģ��
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class MypjtPipeline(object):
    def __init__(self):
#��д��ķ�ʽ�������һ��json��ʽ����׺��Ϊ.json�����ļ�
        self.file = codecs.open("D:/python35/myweb/part13/mydata1.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
#ͨ��dict(item)��itemת����һ���ֵ�
#Ȼ��ͨ��jsonģ���µ�dumps()�����ֵ�����
        i=json.dumps(dict(item))
#�õ������ݺ���ϡ�\n�����з��γ�Ҫд���һ������
        line = i + '\n'
#�ڴ˽���ֱ�������������ԣ�ʵ�ʵ�ʱ�������һ�п���ȥ��
        print(line)
#д�����ݵ�json�ļ���
        self.file.write(line)
        return item
    def close_spider(self,spider):
#�ر��ļ�����ʼ����
        self.file.close()

#(2)
# -*- coding: utf-8 -*-
import codecs
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MypjtPipeline(object):
    def __init__(self):
        self.file = codecs.open("D:/python35/myweb/part13/mydata1.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
#ͨ��jsonģ���µ�dumps()�����ʱ��
#�ڶ���������ensure_ascii����ΪFalse
        i=json.dumps(dict(item), ensure_ascii=False)
        line = i + '\n'
        print(line)
        self.file.write(line)
        return item
    def close_spider(self,spider):
        self.file.close()

#(3)
   start_urls = (
        'http://tech.sina.com.cn/d/s/2016-09-17/doc-ifxvyqwa3324638.shtml',
        "http://sina.com.cn",
    )

#(4)
  item["title"]=response.xpath("/html/head/title/text()").extract()
        item["key"]=response.xpath("//meta[@name='keywords']/@content").extract()



