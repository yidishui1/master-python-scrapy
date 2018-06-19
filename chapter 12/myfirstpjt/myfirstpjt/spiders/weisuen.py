'''
# -*- coding: utf-8 -*-
import scrapy


class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    allowed_domains = ["iqianyue.com"]
    start_urls = (
        'http://www.iqianyue.com/',
    )

    def parse(self, response):
        pass

'''

''''''
#12.5 实战Spider类
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


'''
#(2)#重写了start_requests()方法，将起始网址设置为从新属性url2中读取
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
#定义了新属性url2
    urls2=("http://www.jd.com",
           "http://sina.com.cn",
           "http://yum.iqianyue.com",
           )
#重写了start_requests()方法
    def start_requests(self):
#在该方法中将起始网址设置为从新属性url2中读取
        for url in self.urls2:
#调用默认make_requests_from_url()方法生成具体请求并通过yield返回
            yield self.make_requests_from_url(url)
    def parse(self, response):
        item=MyfirstpjtItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print(item["urlname"])
'''

'''
#12.7 	Spider类参数传递，通过传递参数的方式爬取单个网址
#(1)
# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem

class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
#此时虽然还在此定义了start_urls属性，但不起作用，因为在构造方法进行了重写
    start_urls = (
        'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
        'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
        'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',
    )
#重写初始化方法__init__()，并设置参数myurl
    def __init__(self,myurl=None,*args,**kwargs):
        super(WeisuenSpider,self).__init__(*args,**kwargs)
#输出要爬的网址，对应值为接收到的参数
        print("要爬取的网址为：%s"%myurl)
#重新定义start_urls属性，属性值为传进来的参数值
        self.start_urls=["%s"%myurl]
    def parse(self, response):
        item=MyfirstpjtItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print("以下将显示爬取的网址的标题")
        print(item["urlname"])
'''

'''
#(2) 通过传递参数的方式爬取多个网址
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
#通过split()将传递进来的参数以“|”为切割符进行分隔，分隔后生成一个列表并赋值给myurllist变量
        myurllist=myurl.split("|")
#通过for循环遍历该列表myurllist，并分别输出传进来要爬取的各网址
        for i in myurllist:
            print("要爬取的网址为：%s"%i)
#将起始网址设置为传进来的参数中各网址组成的列表
        self.start_urls=myurllist
    def parse(self, response):
        item=MyfirstpjtItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print("以下将显示爬取的网址的标题")
        print(item["urlname"])

'''