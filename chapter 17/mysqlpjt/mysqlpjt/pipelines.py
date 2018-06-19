'''写入mysql数据库'''
#(3)
# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlpjtPipeline(object):
    def __init__(self):
        #刚开始时连接对应数据库
        #self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="127r@oot", db="mypydb", charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="127r@oot", db="mypydb")
    def process_item(self, item, spider):
        #将获取到的name和keywd分别赋给变量name和变量key
        name=item["name"][0]
        key=item["keywd"][0]
        cs = self.conn.cursor()
        #构造对应的sql语句
        sql="insert into mytb(title,keywd) VALUES('"+name+"','"+key+"')"
        #通过query实现执行对应的sql语句
        cs.execute(sql)
        # 提交SQL
        self.conn.commit()

        return item
    def close_spider(self,spider):
        self.conn.close()



'''
#（2）只是窗口打印输出成功
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlpjtPipeline(object):
    def process_item(self, item, spider):
        print("boy")
        print(item["name"][0])
        print("girl")
        print(item["keywd"][0])
        print("-------------------")
        return item
'''