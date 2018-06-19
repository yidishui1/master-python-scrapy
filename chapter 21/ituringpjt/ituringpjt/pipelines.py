'''
#(1)
# -*- coding: utf-8 -*-
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IturingpjtPipeline(object):
    def __init__(self):
#打开mydata.json文件
        self.file = codecs.open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 21/ituringpjt/mydata.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        # 将当前页的第j个商品的名称赋值给变量name
        url1 = item["url1"][0]
        name=item["name"][0].replace(' ','').replace('\r','').replace('\n','')
        read= item["read"][0]
        # 将当前页下第j个商品的name、price、dz、link等信息处理一下
        # 重新组合成一个字典
        goods = {"url1": url1, "name": name, "read": read}
        i = json.dumps(dict(goods), ensure_ascii=False)
        line = i + '\n'
        self.file.write(line)
        # 返回item
        return item

    def close_spider(self,spider):
#关闭mydata.json文件
        self.file.close()
'''
'''

#（2）只是窗口打印输出成功
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IturingpjtPipeline(object):
    def process_item(self, item, spider):
        for j in range(0, len(item["url0"])):
            url0=item["url0"][j]
            print(url0)
            print("-------------------")
        return item
'''

#(3)
#存入mysql数据库
# -*- coding: utf-8 -*-
import pymysql
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IturingpjtPipeline(object):

    def __init__(self):
        #刚开始时连接对应数据库
        self.conn=pymysql.connect(host="127.0.0.1", user="root", passwd="127r@oot", db="ituring")

    def process_item(self, item, spider):
        url0 = item["url0"][0]
        url1 = item["url1"][0]
        # print(url1)#方便查看进度
        # picture = item["picture"][0]
        name = item["name"][0].replace(' ', '').replace('\r', '').replace('\n', '')
        recommend = item["recommend"][0]
        reader = item["reader"][0]
        author = item["author"][0].replace(' ', '').replace('\r', '').replace('\n', '')
        translator = item["translator"][0].replace(' ', '')

        label = ''
        for i in range(0, len(item["label"])):
            label = label + item["label"][i] + ','

        introduction = item["introduction"][0].replace(' ', '')[:250]
        date = item["date"][0]
        price = item["price"][0]
        pages = item["pages"][0]
        printing = item["printing"][0]
        state = item["state"][0]
        otitle = item["otitle"][0].replace(' ', '')[:250]
        characteristic = item["characteristic"][0].replace(' ', '')[:250]
        authorintroduction =' '

        cs = self.conn.cursor()
        #构造对应的sql语句，实现将获取到的对应数据插入数据库中
        sql="insert into myituring(url1,name,recommend,reader,author,translator,label,introduction,date,price,pages,printing,state,otitle,characteristic,authorintroduction) VALUES('"+url1+"','"+name+"','"+recommend+"','"+reader+"','"+author+"','"+translator+"','"+label+"','"+introduction+"','"+date+"','"+price+"','"+pages+"','"+printing+"','"+state+"','"+otitle+"','"+characteristic+"','"+authorintroduction+"')"

        # 通过query实现执行对应的sql语句
        cs.execute(sql)
        # 提交SQL
        self.conn.commit()
        return item


    def close_spider(self,spider):
        # 最后关闭数据库连接
        self.conn.close()
