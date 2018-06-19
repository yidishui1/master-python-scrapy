''''''
#(2)
# -*- coding: utf-8 -*-
#导入codecs模块，使用codecs直接进行解码
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#定义了pipelines里面的类，类名需要与刚才settings.py里面设置的类名对应起来
class MypjtPipeline(object):
#__init__()为类的初始化方法，开始的时候调用
    def __init__(self):
#首先以写入的方式创建或打开一个普通文件用于存储抓取到的数据
        self.file = codecs.open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 14/mydata1.txt", "wb", encoding="utf-8")
        #self.file.write('ailoveyou')
        #self.file.write('yujyue')
#process_item()为pipelines中的主要处理方法，默认会自动调用
    def process_item(self, item, spider): #函数成功运行的前提时运行的爬虫文件中parse函数下要求rutern item。
#设置每行要写的内容
        data = str(item) + '\n'
#此处通过print()输出，方便程序的调试
        print(data)
#将对应信息写入文件中
        self.file.write(data)
        return item
#close_spider()方法一般在关闭蜘蛛时调用
    def close_spider(self,spider):
#关闭文件，有始有终
        self.file.close()



'''#14.3 输出中文到json文件
#(1)
# -*- coding: utf-8 -*-
import codecs
#因为要进行JSON文件的处理，所以导入json模块
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class MypjtPipeline(object):
    def __init__(self):
#以写入的方式创建或打开一个json格式（后缀名为.json）的文件
        self.file = codecs.open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 14/mydata1.json", "wb", encoding="utf-8")
        #self.file.write("天堂")
    def process_item(self, item, spider):
#通过dict(item)将item转化成一个字典
#然后通过json模块下的dumps()处理字典数据
#第二个参数将ensure_ascii设置为False
        i=json.dumps(dict(item), ensure_ascii=False)
#得到的数据后加上”\n”换行符形成要写入的一行数据
        line = i + '\n'
#在此进行直接输出，方便调试，实际的时候输出这一行可以去掉
        print(line)
#写入数据到json文件中
        self.file.write(line)
        return item
    def close_spider(self,spider):
#关闭文件，有始有终
        self.file.close()

'''
