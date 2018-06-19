#��ʮ����
#12.3 ���ù�������
#(1)
from scrapy.spiders import Spider
 
class FirstSpider(Spider):
    name = "first"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://www.baidu.com",
    ]
 
    def parse(self, response):
        pass

#(2)
>>> ti=sel.xpath("/html/head/title")
>>> print(ti)
[<Selector xpath='/html/head/title' data='<title>�ٶ�һ�£����֪��</title>'>]
>>> 

#(3)
>>> exit()
D:\Python35\myweb\part12>

#12.4 ʵսItems
#(1)
class MyfirstpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urlname=scrapy.Field()
    urlkey=scrapy.Field()
    urlcr=scrapy.Field()
    urladdr=scrapy.Field()

#(2)
>>> import scrapy
>>> class person(scrapy.Item):
	name=scrapy.Field()
	job=scrapy.Field()
	email=scrapy.Field()
#(3)
>>> weisuen=person(name="weiwei",job="teacher",email="qiansyy@iqianyue.com")

#(4)
>>> print(weisuen)
{'email': 'qiansyy@iqianyue.com', 'job': 'teacher', 'name': 'weiwei'}

#(5)
>>> weisuen["job"]
'teacher'

#(6)
>>> weisuen["email"]
'abc@sina.com'

#(7)
>>> weisuen.keys()
dict_keys(['job', 'email', 'name'])

#(8)
>>> weisuen.items()
ItemsView({'email': 'abc@sina.com', 'job': 'teacher', 'name': 'weiwei'})

#12.5 ʵսSpider��
#(1)
# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem

class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    allowed_domains = ["sina.com.cn"]
    start_urls = (
        'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
        'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
        'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',
    )

    def parse(self, response):
        item=MyfirstpjtItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print(item["urlname"])

#(2)
# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem

class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    start_urls = (
        'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
        'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
        'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',
    )
#������������url2
    urls2=("http://www.jd.com",
           "http://sina.com.cn",
           "http://yum.iqianyue.com",
           )
#��д��start_requests()����
    def start_requests(self):
#�ڸ÷����н���ʼ��ַ����Ϊ��������url2�ж�ȡ
        for url in self.urls2:
#����Ĭ��make_requests_from_url()�������ɾ�������ͨ��yield����
            yield self.make_requests_from_url(url)
    def parse(self, response):
        item=MyfirstpjtItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print(item["urlname"])

#12.7 	Spider���������
#(1)
# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem

class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
#��ʱ��Ȼ���ڴ˶�����start_urls���ԣ����������ã���Ϊ�ڹ��췽����������д
    start_urls = (
        'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
        'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
        'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',
    )
#��д��ʼ������__init__()�������ò���myurl
    def __init__(self,myurl=None,*args,**kwargs):
        super(WeisuenSpider,self).__init__(*args,**kwargs)
#���Ҫ������ַ����ӦֵΪ���յ��Ĳ���
        print("Ҫ��ȡ����ַΪ��%s"%myurl)
#���¶���start_urls���ԣ�����ֵΪ�������Ĳ���ֵ
        self.start_urls=["%s"%myurl]
    def parse(self, response):
        item=MyfirstpjtItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print("���½���ʾ��ȡ����ַ�ı���")
        print(item["urlname"])

#(2)
# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem

class WeisuenSpider(scrapy.Spider):
    name = "weisuen"

    start_urls = (
        'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
        'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
        'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',
    )

    def __init__(self,myurl=None,*args,**kwargs):
        super(WeisuenSpider,self).__init__(*args,**kwargs)
#ͨ��split()�����ݽ����Ĳ����ԡ�|��Ϊ�и�����зָ����ָ�������һ���б���ֵ��myurllist����
        myurllist=myurl.split("|")
#ͨ��forѭ���������б�myurllist�����ֱ����������Ҫ��ȡ�ĸ���ַ
        for i in myurllist:
            print("Ҫ��ȡ����ַΪ��%s"%i)
#����ʼ��ַ����Ϊ�������Ĳ����и���ַ��ɵ��б�
        self.start_urls=myurllist
    def parse(self, response):
        item=MyfirstpjtItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print("���½���ʾ��ȡ����ַ�ı���")
        print(item["urlname"])

#12.8 ��XMLFeedSpider������XMLԴ
#(1)
D:\Python35\myweb\part12>scrapy startproject myxml
New Scrapy project 'myxml', using template directory 'd:\\python35\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\Python35\myweb\part12\myxml

You can start your first spider with:
    cd myxml
    scrapy genspider example example.com

#(2)
import scrapy
class MyxmlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#�洢���±���
    title=scrapy.Field()
#�洢��Ӧ����
    link=scrapy.Field()
#�洢��Ӧ��������
    author=scrapy.Field()
�����Ҫ�洢�Ľṹ������֮�󣬿��Դ���һ�������ļ����ڷ���XMLԴ��������ʾ��
D:\Python35\myweb\part12>cd myxml\
D:\Python35\myweb\part12\myxml>scrapy genspider -l
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed
D:\Python35\myweb\part12\myxml>scrapy genspider -t xmlfeed myxmlspider sina.com.cn
Created spider 'myxmlspider' using template 'xmlfeed' in module:
  myxml.spiders.myxmlspider

#(3)
# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem
class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
#����Ҫ������XML�ļ���ַ
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
#��ʱ����ʼ�����Ľڵ�����Ϊ��һ���ڵ�rss
    itertag = 'rss' # change it accordingly
    def parse_node(self, response, node):
        i = MyxmlItem()
#����XPath���ʽ����Ӧ��Ϣ��ȡ���������洢����Ӧ��Item��
        i['title'] = node.xpath("/rss/channel/item/title/text()").extract()
        i['link'] = node.xpath("/rss/channel/item/link/text()").extract()
        i['author'] = node.xpath("/rss/channel/item/author/text()").extract()
#ͨ��forѭ���Դ˱�������ȡ��������item�е���Ϣ�����
        for j in range(len(i['title'])):
            print("��"+str(j+1)+"ƪ����")
            print("�����ǣ�")
            print(i['title'][j])
            print("��Ӧ�����ǣ�")
            print(i['link'][j])
            print("��Ӧ�����ǣ�")
            print(i['author'][j])
            print("----------------------")
        return i

#(4)
D:\Python35\myweb\part12\myxml>scrapy genspider -t xmlfeed person iqianyue.com
Created spider 'person' using template 'xmlfeed' in module:
  myxml.spiders.person

#(5)
# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem
class PersonSpider(XMLFeedSpider):
    name = 'person'
    allowed_domains = ['iqianyue.com']
#����XML��ַ
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/test.xml']
    iterator = 'iternodes' # you can change this; see the docs
#���ÿ�ʼ�����Ľڵ�
    itertag = 'person' # change it accordingly

    def parse_node(self, response, selector):
        i = MyxmlItem()
#��ȡ�ʼ���Ϣ
        i['link'] = selector.xpath('/person/email/text()').extract()
#�����ȡ�����ʼ���Ϣ
        print(i['link'])
        return i

#12.9 ѧ��ʹ��CSVFeedSpider
#(1)
D:\Python35\myweb\part12>scrapy startproject mycsv
New Scrapy project 'mycsv', using template directory 'd:\\python35\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\Python35\myweb\part12\mycsv

You can start your first spider with:
    cd mycsv
    scrapy genspider example example.com

#(2)
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
import scrapy
class MycsvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    sex=scrapy.Field()

#(3)
D:\Python35\myweb\part12\mycsv>scrapy genspider -t csvfeed mycsvspider iqianyue.com
Created spider 'mycsvspider' using template 'csvfeed' in module:
  mycsv.spiders.mycsvspider

#(4)
# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem
class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
#����Ҫ�����csv�ļ����ڵ���ַ
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
#����headers
    headers = ['name', 'sex','addr','email']
    #��������
delimiter = ','
    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response
    def parse_row(self, response, row):
        i = MycsvItem()
#��ȡ���е�name��һ�е���Ϣ
        i['name'] = row['name'].encode()
#��ȡ���е�sex��һ�е���Ϣ
        i['sex'] = row['sex'].encode()
#������Ϣ���
        print("�����ǣ�")
        print(i['name'])
        print("�Ա��ǣ�")
        print(i['sex'])
#�����һ����¼�Ķ�Ӧ�е���Ϣ�����һ�����������ʾ��������۲�
        print("--------------------")
        return i
    
#12.10  Scrapy����࿪����
#(1)
D:\Python35\myweb\part12>scrapy startproject mymultispd
New Scrapy project 'mymultispd', using template directory 'd:\\python35\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\Python35\myweb\part12\mymultispd

You can start your first spider with:
    cd mymultispd
    scrapy genspider example example.com

#(2)
D:\Python35\myweb\part12>cd mymultispd

D:\Python35\myweb\part12\mymultispd>scrapy genspider -t basic myspd1 sina.com.cn
Created spider 'myspd1' using template 'basic' in module:
  mymultispd.spiders.myspd1

D:\Python35\myweb\part12\mymultispd>scrapy genspider -t basic myspd2 sina.com.cn
Created spider 'myspd2' using template 'basic' in module:
  mymultispd.spiders.myspd2

D:\Python35\myweb\part12\mymultispd>scrapy genspider -t basic myspd3 sina.com.cn
Created spider 'myspd3' using template 'basic' in module:
  mymultispd.spiders.myspd3

#(3)
import os
from scrapy.commands import ScrapyCommand
from scrapy.utils.conf import arglist_to_dict
from scrapy.utils.python import without_none_values
from scrapy.exceptions import UsageError


class Command(ScrapyCommand):
    requires_project = True
    def syntax(self):
        return "[options] <spider>"
    def short_desc(self):
#����������Ϣ�����Ը��ݸ���ϲ���ʵ��޸�һ��
        return "Run all spider"
    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")
    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        try:
            opts.spargs = arglist_to_dict(opts.spargs)
        except ValueError:
            raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)
        if opts.output:
            if opts.output == '-':
                self.settings.set('FEED_URI', 'stdout:', priority='cmdline')
            else:
                self.settings.set('FEED_URI', opts.output, priority='cmdline')
            feed_exporters = without_none_values(
                self.settings.getwithbase('FEED_EXPORTERS'))
            valid_output_formats = feed_exporters.keys()
            if not opts.output_format:
                opts.output_format = os.path.splitext(opts.output)[1].replace(".", "")
            if opts.output_format not in valid_output_formats:
                raise UsageError("Unrecognized output format '%s', set one"
                                 " using the '-t' switch or as a file extension"
                                 " from the supported list %s" % (opts.output_format,
                                                                  tuple(valid_output_formats)))
            self.settings.set('FEED_FORMAT', opts.output_format, priority='cmdline')
    #��Ҫ�޸�����
    def run(self, args, opts):
        #��ȡ�����б�
        spd_loader_list=self.crawler_process.spider_loader.list()
        #����������
        for spname in spd_loader_list or args:
            self.crawler_process.crawl(spname, **opts.spargs)
            print("��ʱ����������Ϊ��"+spname)
        self.crawler_process.start()

#12.11 ���ⱻban
#(1)
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.7

#(2)
#IP������
IPPOOL=[
    {"ipaddr":"121.33.226.167:3128"},
    {"ipaddr":"118.187.10.11:80"},
    {"ipaddr":"123.56.245.138:808"},
    {"ipaddr":"139.196.108.68:80"},
    {"ipaddr":"36.250.87.88:47800"},
    {"ipaddr":"123.57.190.51:7777"},
    {"ipaddr":"171.39.26.176:8123"}
]

#(3)
#middlewares�����м��
#���������ģ�飬Ŀ���������ѡһ��IP���е�ip
import random
#��settings�ļ���myfirstpjt.settingsΪsettings�ļ��ĵ�ַ���е������úõ�IPPOOL
from myfirstpjt.settings import IPPOOL
#����ٷ��ĵ���HttpProxyMiddleware��Ӧ��ģ��
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
#��ʼ������
    def __init__(self,ip=''):
        self.ip=ip
#process_request()��������Ҫ����������
    def process_request(self,request,spider):
#�����ѡ��һ��IP
        thisip=random.choice(IPPOOL)
#�����ǰѡ���IP�����ڵ��Թ۲�
        print("��ǰʹ�õ�IP�ǣ�"+thisip["ipaddr"])
#����Ӧ��IPʵ�����Ϊ����Ĵ����ø�IP������ȡ
        request.meta["proxy"]="http://"+thisip["ipaddr"]

#(4)
DOWNLOADER_MIDDLEWARES = {
    #'myfirstpjt.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':123,
    'myfirstpjt.middlewares.IPPOOLS':125
}

#(5)
#�û�����user-agent��������
UAPOOL=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5"
]

#(6)
#uamid�����м��
import random
from myfirstpjt.settings import UAPOOL
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
    def __init__(self,ua=''):
        self.ua=ua
    def process_request(self,request,spider):
        thisua=random.choice(UAPOOL)
        print("��ǰʹ�õ�user-agent�ǣ�"+thisua)
        request.headers.setdefault('User-Agent',thisua)

#(7)
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'myfirstpjt.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':2,
    'myfirstpjt.uamid.Uamid':1
}

