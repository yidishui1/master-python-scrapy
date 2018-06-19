# -*- coding: utf-8 -*-
import scrapy
from anjukepjt.items import AnjukepjtItem
from scrapy.http import Request
import urllib.request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

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
        #item["price"]=response.xpath("//div[2]/div[2]/div[1]/div[3]/div/a[2]/p[2]/span/text()").extract()
        item["link"]=response.xpath("//div[2]/div[1]/div[3]/div/div/a[1]/@href").extract()
        item["dz"]=response.xpath("//div[2]/div[1]/div[3]/div/div/a[2]/span/text()").extract()
        #item["tel"]=response.xpath("//p[@class='tel']/text()").extract()
        # #伪装浏览器
        headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        # 将opener安装为全局
        urllib.request.install_opener(opener)
        for m in range(0, len(item["link"])):
            item["name1"]=re.compile('(.*)').findall(item["name"][m])
            item["link1"]=re.compile('(.*)').findall(item["link"][m])
            item["dz1"]=re.compile('(.*)').findall(item["dz"][m])

            pat1 = '(https://.*?/.*?/).*?html'
            pat2 = 'https://.*?/.*?/(.*?html)'
            newurl = re.compile(pat1).findall(item["link"][m])[0] + "canshu-" + re.compile(pat2).findall(item["link"][m])[0] + "?from=loupan_tab"
            # data为对应博客列表页的所有博文的点击数与评论数数据
            # data = urllib.request.urlopen(item["link"][m]).read().decode('gb2312')
            data = urllib.request.urlopen(newurl).read().decode('utf-8')

            tel='lp-icons lp-icons-tel"></i><span.*?>(.*?)</span>'
            item["tel1"] = re.compile(tel, re.S).findall(str(data))
            try:
                item["tel1"][0]
            except:
                item["tel1"]= [" ", ]



            lptd='<div class="name">楼盘特点</div>.*?class="des">(.*?)</div>'
            item["lptd1"] = re.compile(lptd, re.S).findall(str(data))
            try:
                item["lptd1"][0]
            except:
                item["lptd1"]= [" ", ]
            ckjg='<div class="name">参考单价</div>.*?class="des">(.*?)</div>'
            item["ckjg1"] = re.compile(ckjg, re.S).findall(str(data))
            try:
                item["ckjg1"][0]
            except:
                item["ckjg1"]= [" ", ]
            wylx='<div class="name">物业类型</div>.*?class="des">(.*?)</div>'
            item["wylx1"] = re.compile(wylx, re.S).findall(str(data))
            try:
                item["wylx1"][0]
            except:
                item["wylx1"]= [" ", ]
            kfs = '<div class="name">开发商</div>.*?class="des">(.*?)</div>'
            item["kfs1"] = re.compile(kfs, re.S).findall(str(data))
            try:
                item["kfs1"][0]
            except:
                item["kfs1"]= [" ", ]
            qywz = '<div class="name">区域位置</div>.*?class="des">(.*?)</div>'
            item["qywz1"] = re.compile(qywz, re.S).findall(str(data))
            try:
                item["qywz1"][0]
            except:
                item["qywz1"]= [" ", ]
            lpdz = '<div class="name">楼盘地址</div>.*?class="des">(.*?)</div>'
            item["lpdz1"] = re.compile(lpdz, re.S).findall(str(data))
            try:
                item["lpdz1"][0]
            except:
                item["lpdz1"]= [" ", ]
            zdsf = '<div class="name">最低首付</div>.*?class="des">(.*?)</div>'
            item["zdsf1"] = re.compile(zdsf, re.S).findall(str(data))
            try:
                item["zdsf1"][0]
            except:
                item["zdsf1"]= [" ", ]
            lphx = '<div class="name">楼盘户型</div>.*?class="des">(.*?)</div>'
            item["lphx1"] = re.compile(lphx, re.S).findall(str(data))
            try:
                item["lphx1"][0]
            except:
                item["lphx1"]= [" ", ]
            zxkp = '<div class="name">最新开盘</div>.*?class="des">(.*?)</div>'
            item["zxkp1"] = re.compile(zxkp, re.S).findall(str(data))
            try:
                item["zxkp1"][0]
            except:
                item["zxkp1"]= [" ", ]
            jfsj = '<div class="name">交房时间</div>.*?class="des">(.*?)</div>'
            item["jfsj1"] = re.compile(jfsj, re.S).findall(str(data))
            try:
                item["jfsj1"][0]
            except:
                item["jfsj1"]= [" ", ]
            slcdz = '<div class="name">售楼处地址</div>.*?class="des">(.*?)</div>'
            item["slcdz1"] = re.compile(slcdz, re.S).findall(str(data))
            try:
                item["slcdz1"][0]
            except:
                item["slcdz1"]= [" ", ]
            ysxkz = '<div class="name">预售许可证</div>.*?class="des licence">(.*?)</div>'
            item["ysxkz1"] = re.compile(ysxkz, re.S).findall(str(data))
            try:
                item["ysxkz1"][0]
            except:
                item["ysxkz1"]= [" ", ]
            jzlx = '<div class="name">建筑类型</div>.*?class="des">(.*?)</div>'
            item["jzlx1"] = re.compile(jzlx, re.S).findall(str(data))
            try:
                item["jzlx1"][0]
            except:
                item["jzlx1"]= [" ", ]
            cqnx = '<div class="name">产权年限</div>.*?class="des">(.*?)</div>'
            item["cqnx1"] = re.compile(cqnx, re.S).findall(str(data))
            try:
                item["cqnx1"][0]
            except:
                item["cqnx1"]= [" ", ]
            rjl = '<div class="name">容积率</div>.*?class="des">(.*?)</div>'
            item["rjl1"] = re.compile(rjl, re.S).findall(str(data))
            try:
                item["rjl1"][0]
            except:
                item["rjl1"]= [" ", ]
            lhl = '<div class="name">绿化率</div>.*?class="des">(.*?)</div>'
            item["lhl1"] = re.compile(lhl, re.S).findall(str(data))
            try:
                item["lhl1"][0]
            except:
                item["lhl1"]= [" ", ]
            ghhs = '<div class="name">规划户数</div>.*?class="des">(.*?)</div>'
            item["ghhs1"] = re.compile(ghhs, re.S).findall(str(data))
            try:
                item["ghhs1"][0]
            except:
                item["ghhs1"]= [" ", ]
            lczk = '<div class="name">楼层状况</div>.*?class="des">(.*?)</div>'
            item["lczk1"] = re.compile(lczk, re.S).findall(str(data))
            try:
                item["lczk1"][0]
            except:
                item["lczk1"]= [" ", ]
            gcjd = '<div class="name">工程进度</div>.*?class="des">(.*?)</div>'
            item["gcjd1"] = re.compile(gcjd, re.S).findall(str(data))
            try:
                item["gcjd1"][0]
            except:
                item["gcjd1"]= [" ", ]
            wyglf = '<div class="name">物业管理费</div>.*?class="des">(.*?)</div>'
            item["wyglf1"] = re.compile(wyglf, re.S).findall(str(data))
            try:
                item["wyglf1"][0]
            except:
                item["wyglf1"]= [" ", ]
            wygs = '<div class="name">物业公司</div>.*?class="des">(.*?)</div>'
            item["wygs1"] = re.compile(wygs, re.S).findall(str(data))
            try:
                item["wygs1"][0]
            except:
                item["wygs1"]= [" ", ]
            cws = '<div class="name">车位数</div>.*?class="des">(.*?)</div>'
            item["cws1"] = re.compile(cws, re.S).findall(str(data))
            try:
                item["cws1"][0]
            except:
                item["cws1"]= [" ", ]
            cwb = '<div class="name">车位比</div>.*?class="des">(.*?)</div>'
            item["cwb1"] = re.compile(cwb, re.S).findall(str(data))
            try:
                item["cwb1"][0]
            except:
                item["cwb1"]= [" ", ]

            yield item
        yield item
#提取完后返回item
#接下来很关键，通过循环自动爬取75页的数据
        for i in range(2,15):
#通过上面总结的网址格式构造要爬取的网址
            url="https://nc.fang.anjuke.com/loupan/all/p"+str(i)+"/"
#通过yield返回Request，并指定要爬取的网址和回调函数
#实现自动爬取
            yield Request(url, callback=self.parse)