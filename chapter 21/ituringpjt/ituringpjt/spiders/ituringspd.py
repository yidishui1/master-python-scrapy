# -*- coding: utf-8 -*-
import scrapy
from ituringpjt.items import IturingpjtItem
from scrapy.http import Request
import urllib.request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re
import io
import sys
import time
import socket
import urllib.error
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

class IturingspdSpider(scrapy.Spider):
    name = "ituringspd"
    allowed_domains = ["ituring.com.cn"]
    # 通过start_requests方法编写首次的爬取行为
    def start_requests(self):
        # 首次爬取模拟成浏览器进行
        #yield Request("http://www.ituring.com.cn/book?tab=book&sort=new&page=36", headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})
        yield Request("http://www.ituring.com.cn/book?tab=book&sort=new&page=9")
    def parse(self, response):
        socket.setdefaulttimeout(20)
        item = IturingpjtItem()
        item["url0"] = response.xpath('//div[@class="book-img"]/a/@href').extract()
        # try:
        #     item["url0"]= response.xpath('//div[@class="book-img"]/a/@href').extract()
        # except:
        #     time.sleep(10)
        #     item["url0"] = response.xpath('//div[@class="book-img"]/a/@href').extract()
        '''
        # #伪装浏览器
        headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        # 将opener安装为全局
        urllib.request.install_opener(opener)
        '''
        for m in range(0, len(item["url0"])):
            newurl="http://www.ituring.com.cn"+item["url0"][m]
            item["url1"]=[newurl]
            try:
                data = urllib.request.urlopen(newurl).read().decode('utf-8')

                pname='<h2>(.*?)</h2>'
                item["name"] = re.compile(pname, re.S).findall(str(data))
                try:
                    item["name"][0]
                except:
                    item["name"]= [" ",]

                item["recommend"] = [" ", ]
                item["reader"] = [" ", ]
                item["author"] = [" ", ]

                ptranslator='<div class="book-author">.*?</span>.*?<span>(.*?)</span>.*?</div>'
                item["translator"] = re.compile(ptranslator, re.S).findall(str(data))
                try:
                    item["translator"][0]
                except:
                    item["translator"]= [" ",]

                item["label"] = [" ", ]
                item["introduction"] = [" ", ]
                item["date"] = [" ", ]
                item["price"] = [" ", ]
                item["pages"] = [" ", ]
                item["printing"] = [" ", ]
                item["state"] = [" ", ]
                item["otitle"] = [" ", ]
                item["characteristic"] = [" ", ]
                item["authorintroduction"] = [" ", ]
                yield item
                # pname='<h2>(.*?)</h2>'
                # item["name"] = re.compile(pname, re.S).findall(str(data))
                # try:
                #     item["name"][0]
                # except:
                #     item["name"]= [" ",]
                #
                # preader='<div class="item article-vote"><span class="number">(.*?)</span>'
                # item["reader"] = re.compile(preader, re.S).findall(str(data))
                # try:
                #     item["reader"][0]
                # except:
                #     item["reader"]= [" ",]
                #
                # precommend='<span class="number">(.*?)</span><span class="text ">推荐</span>'
                # item["recommend"] = re.compile(precommend, re.S).findall(str(data))
                # try:
                #     item["recommend"][0]
                # except:
                #     item["recommend"]= [" ",]
                #
                # pauthor='<div class="book-author">.*?<span>(.*?)</span>'
                # item["author"] = re.compile(pauthor, re.S).findall(str(data))
                # try:
                #     item["author"][0]
                # except:
                #     item["author"]= [" ",]
                #
                # ptranslator='<div class="book-author">.*?</span>.*?<span>(.*?)</span>.*?</div>'
                # item["translator"] = re.compile(ptranslator, re.S).findall(str(data))
                # try:
                #     item["translator"][0]
                # except:
                #     item["translator"]= [" ",]
                #
                # plabel='class="post-tag">(.*?)</a>'
                # item["label"] = re.compile(plabel, re.S).findall(str(data))
                # try:
                #     item["label"][0]
                # except:
                #     item["label"]= [" ",]
                #
                # item["introduction"] = [" ", ]
                # '''
                # pintroduction='<div class="book-intro readmore">(.*?)</div>'
                # item["introduction"] = re.compile(pintroduction, re.S).findall(str(data))
                # try:
                #     item["introduction"][0]
                # except:
                #     item["introduction"]= [" ",]
                # '''
                #
                # pdate ='<strong>出版日期</strong>(.*?)</li>'
                # item["date"] = re.compile(pdate, re.S).findall(str(data))
                # try:
                #     item["date"][0]
                # except:
                #     item["date"] = [" ",]
                #
                # pprice='<strong>定　　价</strong>(.*?)</li>'
                # item["price"] = re.compile(pprice, re.S).findall(str(data))
                # try:
                #     item["price"][0]
                # except:
                #     item["price"]= [" ",]
                #
                # ppages='<strong>页　　数</strong>(.*?)</li>'
                # item["pages"] = re.compile(ppages, re.S).findall(str(data))
                # try:
                #     item["pages"][0]
                # except:
                #     item["pages"]= [" ",]
                #
                # pprinting='<strong>印刷方式</strong>(.*?)</li>'
                # item["printing"] = re.compile(pprinting, re.S).findall(str(data))
                # try:
                #     item["printing"][0]
                # except:
                #     item["printing"]= [" ",]
                #
                # pstate='<strong>出版状态</strong>(.*?)</li>'
                # item["state"] = re.compile(pstate, re.S).findall(str(data))
                # try:
                #     item["state"][0]
                # except:
                #     item["state"]= [" ",]
                #
                # potitle = '<strong>原书名</strong>(.*?)</li>'
                # item["otitle"] = re.compile(potitle, re.S).findall(str(data))
                # try:
                #     item["otitle"][0]
                # except:
                #     item["otitle"] = [" ",]
                #
                # item["characteristic"] = [" ", ]
                # '''
                # pcharacteristic='<h3>本书特色</h3>.*?<div class="intro">(.*?)</div>'
                # item["characteristic"] = re.compile(pcharacteristic, re.S).findall(str(data))
                # try:
                #     item["characteristic"][0]
                # except:
                #     item["characteristic"]= [" ",]
                # '''
                #
                # item["authorintroduction"] = [" ", ]
                # '''
                # pauthorintroduction='<h3>作者介绍</h3>.*?<div class="intro">(.*?)</div>'
                # item["authorintroduction"] = re.compile(pauthorintroduction, re.S).findall(str(data))
                # try:
                #     item["authorintroduction"][0]
                # except:
                #     item["authorintroduction"]= [" ",]
                # '''
                # yield item

            except:
                item["url1"] = [" ", ]
                item["name"] = [" ", ]
                item["recommend"] = [" ", ]
                item["reader"] = [" ", ]
                item["author"] = [" ", ]
                item["translator"] = [" ", ]
                item["label"] = [" ", ]
                item["introduction"] = [" ", ]
                item["date"] = [" ", ]
                item["price"] = [" ", ]
                item["pages"] = [" ", ]
                item["printing"] = [" ", ]
                item["state"] = [" ", ]
                item["otitle"] = [" ", ]
                item["characteristic"] = [" ", ]
                item["authorintroduction"] = [" ", ]
                yield item

        ''''''
        for i in range(10,57):
            # 通过上面总结的网址格式构造要爬取的网址
            nexturl = "http://www.ituring.com.cn/book?tab=book&sort=new&page="+str(i)
            # print(nexturl)
            # 通过yield返回Request，并指定要爬取的网址和回调函数
            # 实现自动爬取
            yield Request(nexturl, callback=self.parse)

