#��ʮ���� ����ƪ ʵս��Ŀ����
#18.3 ��Ѷ����������Ŀ��дʵս
#��1��
Create database hexun;

#(2)
Use hexun;
Create table myhexun(id int(10) auto_increment primary key not null,name varchar(30),url varchar(100),hits int(15),comment int(15));

#(3)
D:\Python35\myweb\part18>scrapy startproject hexunpjt
New Scrapy project 'hexunpjt', using template directory 'd:\\python35\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\Python35\myweb\part18\hexunpjt
You can start your first spider with:
    cd hexunpjt
    scrapy genspider example example.com

#(4)
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HexunpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#����name�洢������
    name= scrapy.Field()
#����url�洢����url��ַ
    url= scrapy.Field()
#����hits�洢�����Ķ���
    hits= scrapy.Field()
#����comment�洢����������
    comment= scrapy.Field()

#(5)
# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HexunpjtPipeline(object):

    def __init__(self):
        #�տ�ʼʱ���Ӷ�Ӧ���ݿ�
        self.conn=pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="hexun")

    def process_item(self, item, spider):
        #ÿһ�������б�ҳ�а�����ƪ���ĵ���Ϣ�����ǿ���ͨ��forѭ��һ�δ�������ĵ���Ϣ
        for j in range(0, len(item["name"])):
            # ����ȡ����name��url��hits��comment�ֱ𸳸�������
            name=item["name"][j]
            url=item["url"][j]
            hits=item["hits"][j]
            comment=item["comment"][j]
            #�����Ӧ��sql��䣬ʵ�ֽ���ȡ���Ķ�Ӧ���ݲ������ݿ���
            sql="insert into myhexun(name,url,hits,comment) VALUES('"+name+"','"+url+"','"+hits+"','"+comment+"')"
            #ͨ��queryʵ��ִ�ж�Ӧ��sql���
            self.conn.query(sql)
        return item


    def close_spider(self,spider):
        # ���ر����ݿ�����
        self.conn.close()

#(6)

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'hexunpjt.pipelines.HexunpjtPipeline': 300,
}

#(7)
# Disable cookies (enabled by default)
COOKIES_ENABLED = False

#(8)
# Disable cookies (enabled by default)
COOKIES_ENABLED = False

#(9)
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#(10)
# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from hexunpjt.items import HexunpjtItem
from scrapy.http import Request

class MyhexunspdSpider(scrapy.Spider):
    name = "myhexunspd"
    allowed_domains = ["hexun.com"]
    #����Ҫ��ȡ���û���uid��Ϊ����������ȡ��ַ��׼��
    uid = "19940007"
    #ͨ��start_requests������д�״ε���ȡ��Ϊ
    def start_requests(self):
        #�״���ȡģ������������
        yield Request("http://"+str(self.uid)+".blog.hexun.com/p1/default.html",headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})


    def parse(self, response):
        item = HexunpjtItem()
        item['name']=response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()
        item["url"]=response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()
        #��������Ҫʹ��urllib��reģ���ȡ���ĵ����������Ķ���
        #������ȡ�洢�������͵������ַ��������ʽ
        pat1='<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        #hcurlΪ�洢�������͵��������ַ
        hcurl=re.compile(pat1).findall(str(response.body))[0]
        # ģ��������
        headers2 = ("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers2]
        # ��opener��װΪȫ��
        urllib.request.install_opener(opener)
        #dataΪ��Ӧ�����б�ҳ�����в��ĵĵ����������������
        data=urllib.request.urlopen(hcurl).read()
        #pat2Ϊ��ȡ�����Ķ�����������ʽ
        pat2="click\d*?','(\d*?)'"
        #pat3Ϊ��ȡ������������������ʽ
        pat3="comment\d*?','(\d*?)'"
        #��ȡ�Ķ��������������ݲ��ֱ�ֵ��item�µ�hits��comment
        item["hits"]=re.compile(pat2).findall(str(data))
        item["comment"]=re.compile(pat3).findall(str(data))
        yield item
        #��ȡ�����б�ҳ����ҳ��
        pat4="blog.hexun.com/p(.*?)/"
        #ͨ��������ʽ��ȡ��������Ϊһ���б������ڶ���Ԫ��Ϊ��ҳ��
        data2=re.compile(pat4).findall(str(response.body))
        if(len(data2)>=2):
            totalurl=data2[-2]
        else:
            totalurl=1
        #��ʵ�������У���һ��print�Ĵ������ע�͵����ڵ��Թ����У����Կ�����һ��print�Ĵ���
        #print("һ��"+str(totalurl)+"ҳ")
        #����forѭ����������ȡ�������б�ҳ�Ĳ�������
        for i in range(2,int(totalurl)+1):
            #������һ��Ҫ��ȡ��url����ȡһ��ҳ�����б�ҳ�е�����
            nexturl="http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"/default.html"
            #������һ����ȡ����һ����ȡ��Ȼģ������������
            yield Request(nexturl,callback=self.parse,headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})
    













