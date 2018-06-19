'''
#15.2 实战pipelines编写
#(1)
# -*- coding: utf-8 -*-
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AnjukepjtPipeline(object):
    def __init__(self):
#打开mydata.json文件
        self.file = codecs.open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 15/mydata.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        i=json.dumps(dict(item), ensure_ascii=False)
#每条数据后加上换行
        line = i + '\n'
#写入数据到mydata.json文件中
        self.file.write(line)
        return item
    def close_spider(self,spider):
#关闭mydata.json文件
        self.file.close()
'''

#（2）
# -*- coding: utf-8 -*-
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AnjukepjtPipeline(object):
    def __init__(self):
#此时存储到的文件是mydata2.json，不与之前存储的文件mydata.json冲突
        self.file = codecs.open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 15/mydata3.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        #item=dict(item)
        #print(len(item["name"]))
#每一页中包含多个商品信息，所以可以通过循环，每一次处理一个商品
#其中len(item["name"])为当前页中商品的总数，依次遍历
        for j in range(0,len(item["name"])):
#将当前页的第j个商品的名称赋值给变量name
            name=item["name"][j]
            price=item["price"][j]
            comnum=item["comnum"][j]
            link=item["link"][j]
#将当前页下第j个商品的name、price、comnum、link等信息处理一下
#重新组合成一个字典
            goods={"name":name,"price":price,"comnum":comnum,"link":link}
            #将组合后的当前页中第j个商品的数据写入json文件
            i=json.dumps(dict(goods), ensure_ascii=False)
            line = i + '\n'
            self.file.write(line)
#返回item
        return item
    def close_spider(self,spider):
        self.file.close()