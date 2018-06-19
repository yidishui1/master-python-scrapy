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
        self.file = codecs.open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 21/mydata.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        #item=dict(item)
        #print(len(item["name"]))
#每一页中包含多个商品信息，所以可以通过循环，每一次处理一个商品
#其中len(item["name"])为当前页中商品的总数，依次遍历

#将当前页的第j个商品的名称赋值给变量name
        name1=item["name1"][0]
        #price1=item["price1"][0]
        dz1=item["dz1"][0]
        link1=item["link1"][0]
        tel1= item["tel1"][0]
        lptd1 = item["lptd1"][0]
        ckjg1 = item["ckjg1"][0]
        wylx1 = item["wylx1"][0]
        kfs1 = item["kfs1"][0]
        qywz1 = item["qywz1"][0]
        lpdz1 = item["lpdz1"][0]
        zdsf1 = item["zdsf1"][0]
        lphx1 = item["lphx1"][0]
        zxkp1 = item["zxkp1"][0]
        jfsj1 = item["jfsj1"][0]
        slcdz1 = item["slcdz1"][0]
        ysxkz1 = item["ysxkz1"][0]
        jzlx1 = item["jzlx1"][0]
        cqnx1 = item["cqnx1"][0]
        rjl1 = item["rjl1"][0]
        lhl1 = item["lhl1"][0]
        ghhs1 = item["ghhs1"][0]
        lczk1 = item["lczk1"][0]
        gcjd1 = item["gcjd1"][0]
        wyglf1 = item["wyglf1"][0]
        wygs1 = item["wygs1"][0]
        cws1 = item["cws1"][0]
        cwb1 = item["cwb1"][0]

        #将当前页下第j个商品的name、price、dz、link等信息处理一下
#重新组合成一个字典
        goods={"name1":name1,"dz1":dz1,"link1":link1,"tel1":tel1,"lptd1":lptd1,"ckjg1":ckjg1,"wylx1":wylx1,"kfs1":kfs1,"qywz1":qywz1,"lpdz1":lpdz1,"zdsf1":zdsf1,"lphx1":lphx1,"zxkp1":zxkp1,"jfsj1":jfsj1,"slcdz1":slcdz1,"ysxkz1":ysxkz1,"jzlx1":jzlx1,"cqnx1":cqnx1,"rjl1":rjl1,"lhl1":lhl1,"ghhs1":ghhs1,"lczk1":lczk1,"gcjd1":gcjd1,"wyglf1":wyglf1,"wygs1":wygs1,"cws1":cws1,"cwb1":cwb1}
        # goods = {"name1": name1, "dz1": dz1, "link1": link1, "tel1": tel1}
        #goods = {"name1": name1, "price1": price1, "dz1": dz1, "link1": link1, "tel1": tel1}
        #goods={"name1":name1,"price1":price1,"dz1":dz1,"link1":link1,"tel1":tel1,"starttime1":starttime1,"givetime1":givetime1}
        #将组合后的当前页中第j个商品的数据写入json文件
        i=json.dumps(dict(goods), ensure_ascii=False)
        line = i + '\n'
        self.file.write(line)
#返回item
        return item
    def close_spider(self,spider):
        self.file.close()

'''

''''''
#(3)
#存入mysql数据库
# -*- coding: utf-8 -*-
import pymysql
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AnjukepjtPipeline(object):

    def __init__(self):
        #刚开始时连接对应数据库
        self.conn=pymysql.connect(host="127.0.0.1", user="root", passwd="127r@oot", db="anjuke")

    def process_item(self, item, spider):
        #每一个博文列表页中包含多篇博文的信息，我们可以通过for循环一次处理各博文的信息
            # 将获取到的name、url、hits、comment分别赋给各变量
        name1 = item["name1"][0]
        dz1 = item["dz1"][0]
        link1 = item["link1"][0]
        tel1 = item["tel1"][0].replace('&nbsp;','')
        lptd1 = item["lptd1"][0]
        pat = 'soj=\"canshu_left_tips\">(.*?)</a>'
        lptd1s = re.compile(pat, re.S).findall(str(lptd1))
        try:
            lptd1s[0]
        except:
            lptd1s = [" ", ]
        lptd1 = ''
        for i in range(0, len(lptd1s)):
            lptd1 = lptd1 + lptd1s[i] + ','

        ckjg1 = item["ckjg1"][0]
        pat = 'class=\"can-spe can-big space2 \">\n\s+(\S+)\s+</span>'
        ckjg1s = re.compile(pat, re.S).findall(str(ckjg1))
        try:
            ckjg1s[0]
        except:
            ckjg1s = [" ", ]
        ckjg1 = ''
        for i in range(0, len(ckjg1s)):
            ckjg1 = ckjg1 + ckjg1s[i] + ','

        wylx1 = item["wylx1"][0].replace(' ','').replace('\n','')
        kfs1 = item["kfs1"][0]
        pat = '(href.*?)</a>'
        kfs1s = re.compile(pat, re.S).findall(str(kfs1))
        try:
            kfs1s[0]
        except:
            kfs1s = [" ", ]
        kfs1 = ''
        for i in range(0, len(kfs1s)):
            kfs1 = kfs1 + kfs1s[i] + ','

        qywz1 = item["qywz1"][0]
        pat = 'soj=\"canshu_left_quyu\">(.*?)</a>'
        qywz1s = re.compile(pat, re.S).findall(str(qywz1))
        try:
            qywz1s[0]
        except:
            qywz1s = [" ", ]
        qywz1 = ''
        for i in range(0, len(qywz1s)):
            qywz1 = qywz1 + qywz1s[i] + ','

        lpdz1 = item["lpdz1"][0]
        pat = 'href="(.*?html)'
        lpdz1s = re.compile(pat, re.S).findall(str(lpdz1))
        try:
            lpdz1s[0]
        except:
            lpdz1s = [" ", ]
        lpdz1 = ''
        for i in range(0, len(lpdz1s)):
            lpdz1 = lpdz1 + lpdz1s[i] + ','

        zdsf1 = item["zdsf1"][0]
        pat = '\n\s+(\S.*?%.*?)\n'
        zdsf1s = re.compile(pat).findall(str(zdsf1))
        try:
            zdsf1s[0]
        except:
            zdsf1s = [" ", ]
        zdsf1 = ''
        for i in range(0, len(zdsf1s)):
            zdsf1 = zdsf1 + zdsf1s[i] + ','

        lphx1 = item["lphx1"][0]
        pat = 'soj=\"canshu_left_huxing\">(.*?)</a>'
        lphx1s = re.compile(pat, re.S).findall(str(lphx1))
        try:
            lphx1s[0]
        except:
            lphx1s = [" ", ]
        lphx1 = ''
        for i in range(0, len(lphx1s)):
            lphx1 = lphx1 + lphx1s[i] + ','

        zxkp1 = item["zxkp1"][0].replace(' ','').replace('\n','')
        jfsj1 = item["jfsj1"][0].replace(' ','').replace('\n','')
        slcdz1 = item["slcdz1"][0]
        ysxkz1 = item["ysxkz1"][0]
        ysxkz1=ysxkz1[:20]

        jzlx1 = item["jzlx1"][0]
        jzlx1=jzlx1[:20]

        cqnx1 = item["cqnx1"][0]
        cqnx1=cqnx1[:20]

        rjl1 = item["rjl1"][0]
        pat = '\n\s+(\S+)\s+<a target='
        rjl1s = re.compile(pat, re.S).findall(str(rjl1))
        try:
            rjl1s[0]
        except:
            rjl1s = [" ", ]
        rjl1 = ''
        for i in range(0, len(rjl1s)):
            rjl1 = rjl1 + rjl1s[i] + ','

        lhl1 = item["lhl1"][0]
        pat = '(\S+)\s+<a target='
        lhl1s = re.compile(pat, re.S).findall(str(lhl1))
        try:
            lhl1s[0]
        except:
            lhl1s = [" ", ]
        lhl1 = ''
        for i in range(0, len(lhl1s)):
            lhl1 = lhl1 + lhl1s[i] + ','

        ghhs1 = item["ghhs1"][0]
        pat = '\n\s+(\S+户)\n\s+\n'
        ghhs1s = re.compile(pat, re.S).findall(str(ghhs1))
        try:
            ghhs1s[0]
        except:
            ghhs1s = [" ", ]
        ghhs1 = ''
        for i in range(0, len(ghhs1s)):
            ghhs1 = ghhs1 + ghhs1s[i] + ','

        lczk1 = item["lczk1"][0]
        gcjd1 = item["gcjd1"][0].replace(' ','').replace('\n','')
        wyglf1 = item["wyglf1"][0]
        wygs1 = item["wygs1"][0].replace(' ','')
        cws1 = item["cws1"][0].replace(' ','')
        cwb1 = item["cwb1"][0]
        pat = '\n\s+(\S+)\s+<a target='
        cwb1s = re.compile(pat, re.S).findall(str(cwb1))
        try:
            cwb1s[0]
        except:
            cwb1s = [" ", ]
        cwb1 = ''
        for i in range(0, len(cwb1s)):
            cwb1 = cwb1 + cwb1s[i] + ','

        cs = self.conn.cursor()
        #构造对应的sql语句，实现将获取到的对应数据插入数据库中
        sql="insert into myanjuke(name1,dz1,link1,tel1,lptd1,ckjg1,wylx1,kfs1,qywz1,lpdz1,zdsf1,lphx1,zxkp1,jfsj1,slcdz1,ysxkz1,jzlx1,cqnx1,rjl1,lhl1,ghhs1,lczk1,gcjd1,wyglf1,wygs1,cws1,cwb1) VALUES('"+name1+"','"+dz1+"','"+link1+"','"+tel1+"','"+lptd1+"','"+ckjg1+"','"+wylx1+"','"+kfs1+"','"+qywz1+"','"+lpdz1+"','"+zdsf1+"','"+lphx1+"','"+zxkp1+"','"+jfsj1+"','"+slcdz1+"','"+ysxkz1+"','"+jzlx1+"','"+cqnx1+"','"+rjl1+"','"+lhl1+"','"+ghhs1+"','"+lczk1+"','"+gcjd1+"','"+wyglf1+"','"+wygs1+"','"+cws1+"','"+cwb1+"')"

        # 通过query实现执行对应的sql语句
        cs.execute(sql)
        # 提交SQL
        self.conn.commit()
        return item


    def close_spider(self,spider):
        # 最后关闭数据库连接
        self.conn.close()

