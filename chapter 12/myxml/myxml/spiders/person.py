#(5)
# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem
class PersonSpider(XMLFeedSpider):
    name = 'person'
    allowed_domains = ['iqianyue.com']
#设置XML网址
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/test.xml']
    iterator = 'iternodes' # you can change this; see the docs
#设置开始迭代的节点
    itertag = 'person' # change it accordingly

    def parse_node(self, response, selector):
        i = MyxmlItem()
#提取邮件信息
        i['link'] = selector.xpath('/person/email/text()').extract()
#输出提取到的邮件信息
        print(i['link'])
        return i