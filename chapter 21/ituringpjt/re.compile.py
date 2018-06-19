# -*- coding: utf-8 -*-
# import scrapy
import re
import urllib.request
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import io
import sys
import urllib.error

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

item='http://www.ituring.com.cn/book/2556'
# #伪装浏览器
headers = {"Accept-Encoding":"utf-8,gb2312","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 将opener安装为全局
urllib.request.install_opener(opener)

data = urllib.request.urlopen(item).read().decode('utf-8')
# pat3='<div class="des">(.*?)</div>'
print(data)
#item["starttime1"]=data.xpath("div[2]/div[1]/div[1]/div[2]/div[2]/ul/li/div[2]/text()").extract()
# pat3 ='<h3>作者介绍</h3>.*?<div class="intro">(.*?)</div>'
# pat4 = '<div class="des">(.*?)</div>'
# pat3 = '<div class="name">最新开盘</div>.*?class="des">(.*?)</div>'
# pat4 = '<div class="name">交房时间</div>.*?class="des">(.*?)</div>'
# pat3 = '<div class="name">(.*?)</div>'
# pat4 = '<div class="des">(.*?)</div>'
# starttime1 = re.compile(pat3, re.S).findall(str(data))
# try:
#     starttime1[0]
# except:
#     starttime1=[" ",]
# if starttime1==None:
#     starttime1 == ['1',]
# givetime1 = re.compile(pat4, re.S).findall(str(data))
# item["givetime1"] = re.compile(pat4).findall(str(data))


# picid=re.compile(patlocal).findall(str(item))[0]
# picid=re.compile(pat1).findall(str(item))[0]
#picid=re.compile(patlocal).findall(item)[0]
# print(picid)
# print(starttime1)
# print(starttime1[0].replace(' ', '')[:200])
# print(givetime1)
'''
data= '"lptd1": "\n                                                                    <a target=\"_blank\" class=\"can-tag\"\n                                       href=\"https://nc.fang.anjuke.com/jia/Z17707/\"\n                                       soj=\"canshu_left_tips\">品牌开发商</a>\n                                                                    <a target=\"_blank\" class=\"can-tag\"\n                                       href=\"https://nc.fang.anjuke.com/jia/Z17671/\"\n                                       soj=\"canshu_left_tips\">改善房</a>\n                                                                    <a target=\"_blank\" class=\"can-tag\"\n                                       href=\"https://nc.fang.anjuke.com/jia/Z17700/\"\n                                       soj=\"canshu_left_tips\">人车分流</a>\n                                                                    <a target=\"_blank\" class=\"can-tag\"\n                                       href=\"https://nc.fang.anjuke.com/jia/Z17695/\"\n                                       soj=\"canshu_left_tips\">车位充足</a>\n                                                                    <a target=\"_blank\" class=\"can-tag\"\n                                       href=\"https://nc.fang.anjuke.com/jia/Z17679/\"\n                                       soj=\"canshu_left_tips\">自然湖</a>\n'
pat='soj=\"canshu_left_tips\">(.*?)</a>'
lptd1s = re.compile(pat, re.S).findall(str(data))
lptd1=''
for i in range(0, len(lptd1s)):
    lptd1=lptd1+lptd1s[i]+','

print(lptd1)
'''
'''
data='30.00%                                <a target="_blank" class="space gray"                                    href="https://nc.fang.anjuke.com/loupan/infodesc-416488-lvhua.html"                                    soj="canshu_left_lvhualv">[查看详情]</a>'
pat='(.*?%)'
lhl1s = re.compile(pat, re.S).findall(str(data))
lhl11=lhl1s[0]
print(lhl11)
'''
'''
data='\n                                                                                                                                    住宅                                                                            <span class=\"can-spe can-big space2 \">\n                                        10000                                        </span>元/㎡                                                                                                                                                                            <a target=\"_blank\" class=\"space\"\n                                   href=\"https://nc.fang.anjuke.com/loupan/jiage-416621.html?from=loupan_tab\"\n                                   soj=\"canshu_left_danjia\">[价格走势]</a>\n                                                    '
pat='\n\s+(\S+)\s+'
ckjg1s = re.compile(pat, re.S).findall(str(data))
ckjg1=''
for i in range(0, len(ckjg1s)):
    ckjg1=ckjg1+ckjg1s[i]+','

print(lptd1)
'''
'''
data= '                            <a target=\"_blank\" href=\"https://nc.fang.anjuke.com/loupan/xihu/\"\n                               soj=\"canshu_left_quyu\">西湖</a>-\n                            <a target=\"_blank\" href=\"https://nc.fang.anjuke.com/loupan/xihu_12157/\"\n                               soj=\"canshu_left_quyu\">朝阳新城</a>\n                        '
pat='soj=\"canshu_left_quyu\">(.*?)</a>'
qyw1s = re.compile(pat, re.S).findall(str(data))
qyw1=''
for i in range(0, len(qyw1s)):
    qyw1=qyw1+qyw1s[i]+','

print(qyw1)
'''
'''
qywz1='                                                             <a target="_blank" soj="canshu_left_kfs" href="https://nc.fang.anjuke.com/loupan/kfs-78903.html">中航集团中航里城南昌分公司</a>                                                    '
pat = '(href.*?)</a>'
qywz1s = re.compile(pat, re.S).findall(str(qywz1))
try:
    qywz1s[0]
except:
    qywz1s = [" ", ]
qywz1 = ''
for i in range(0, len(qywz1s)):
    qywz1 = qywz1 + qywz1s[i] + ','

print(qywz1)
'''

# #data='住宅：70年　别墅：70年                                <a target=\"_blank\" class=\"space gray\"\n                                   href=\"https://nc.fang.anjuke.com/loupan/infodesc-416667-chanquan.html\"\n                                   soj=\"canshu_left_nianxian\">[查看详情]</a>'
# data='123'
# print(data[:20])
