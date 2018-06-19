#（4）
# -*- coding: utf-8 -*-
import scrapy
import re
from qtpjt.items import QtpjtItem
from scrapy.http import Request
import urllib.request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import os


class QtspdSpider(scrapy.Spider):
    name = "qtspd"
    allowed_domains = ["58pic.com"]
    # start_urls = (
    #     'http://www.58pic.com/tb/',
    # )
    # 通过start_requests方法编写首次的爬取行为
    def start_requests(self):
        # 首次爬取模拟成浏览器进行
        yield Request("http://www.58pic.com/tb/", headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})

    def parse(self, response):
        item=QtpjtItem()
        item["picfolder"]=response.xpath("//em[@class='text-green-b']/text()").extract()
        folder = os.path.exists(
            'C:\\Users\\leishen\\Documents\\anaconda3\\scrapy\\master python scrapy\\chapter 19\\pic' + '\\' + item["picfolder"][0])
        if not folder:
            os.mkdir('C:\\Users\\leishen\\Documents\\anaconda3\\scrapy\\master python scrapy\\chapter 19\\pic' + '\\' + item["picfolder"][0])
        item["link"]=response.xpath("//a[@class='thumb-box']/@href").extract() #经过测试，成功
        # headers = {"Accept-Encoding":"utf-8,gb2312","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}
        headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        # 将opener安装为全局
        urllib.request.install_opener(opener)
        for m in range(0, len(item["link"])):
            data = urllib.request.urlopen(item["link"][m]).read()
            paturl = '<img src="(http.*?)".*?show-area-pic'
            item["picurl"] = re.compile(paturl).findall(str(data))
            yield item
            # data为对应博客列表页的所有博文的点击数与评论数数据
            # data = urllib.request.urlopen(item["link"][m]).read().decode('gb2312')
            # for k in range(0, len(item["picurl"])):
            #     patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
            #     item["picid"][k]=re.compile(patlocal).findall(str(item["picurl"][k]))[0]+"-"+str(k)
            # item["picid"]=tupianm
            # picid = 'id="show-area-pic".*?alt="(.*?)"'
            # item["picid"] = re.compile(picid).findall(str(data))

#通过for循环依次遍历1到200页图片列表页
        for i in range(2,3):
#构造出下一页图片列表页的网址
            nexturl="http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-"+str(i)+".html"
            yield Request(nexturl, callback=self.parse)

        '''
#构建提取缩略图网址的正则表达式
        paturl="(http://pic.qiantucdn.com/58pic/.*?).jpg"
        #提取对应图片网址
        item["picurl"]=re.compile(paturl).findall(str(response.body))
#构造出提取图片名的正则表达式，以方便构造出本地的文件名
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
#提取互联网中的图片名
        item["picid"] = re.compile(patlocal).findall(str(response.body))
        '''