# -*- coding: utf-8 -*-
import scrapy
from anjukepjt.items import AnjukepjtItem
from scrapy.http import Request

class aujukespdSpider(scrapy.Spider):
    name = "anjukespd"
    allowed_domains = ["anjuke.com"]
    start_urls = (
        'https://nc.fang.anjuke.com/loupan/all/p1/',
    )

    def parse(self, response):
        item=AnjukepjtItem()
#通过各Xpath表达式分别提取商品的名称、价格、链接、评论数等信息
        # item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        # item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        # item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        #item["comnum"]=response.xpath("//a[@name='P_pl']/text()").extract()

        # item["name"]=response.xpath("//*[@id="container"]/div[2]/div[1]/div[3]/div/div/a[1]/h3/span/text()").extract()
        # item["price"]=response.xpath("//*[@id="container"]/div[2]/div[1]/div[3]/div/div/a[3]/span[3]/text()").extract()
        # item["link"]=response.xpath("//*[@id="container"]/div[2]/div[1]/div[3]/div/div/a[1]/@href").extract()
        # item["comnum"]=response.xpath("//*[@id="container"]/div[2]/div[1]/div[3]/div/div/a[2]/span/text()").extract()
        item["name"]=response.xpath("//div[2]/div[1]/div[3]/div/div/a[1]/h3/span/text()").extract()
        item["price"]=response.xpath("//div[2]/div[2]/div[1]/div[3]/div/a[2]/p[2]/span/text()").extract()
        item["link"]=response.xpath("//div[2]/div[1]/div[3]/div/div/a[1]/@href").extract()
        item["comnum"]=response.xpath("//div[2]/div[1]/div[3]/div/div/a[2]/span/text()").extract()
#提取完后返回item
        yield item
#接下来很关键，通过循环自动爬取75页的数据
        for i in range(1,3):
#通过上面总结的网址格式构造要爬取的网址
            url="https://nc.fang.anjuke.com/loupan/all/p"+str(i)+"/"
#通过yield返回Request，并指定要爬取的网址和回调函数
#实现自动爬取
            yield Request(url, callback=self.parse)