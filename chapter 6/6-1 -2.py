# coding=utf-8
#第六章
#6.1 简单Python爬虫的实现，爬取图片
import re
import os
import urllib.request
import urllib.error
import time #为了设置延时，避免过快收集导致主机拒绝访问
import socket


#第一道过滤
def craw(url,page1,page2):
    socket.setdefaulttimeout(20)
    #header=("User-Agent"," Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
    # print(url)
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    #print(html1)
    pat1 = '<div class="thread-box">.+?<div id="postlist" class="pl cl thread-box p20 mt">'#第一道过滤
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    #print(result1)

    pat2='"http://(.+?\.jpg)"'#初步提取图片code
    imagelist = re.compile(pat2).findall(result1)
    # print(imagelist)

    x=1
    for imageurl in imagelist:
        imagename = "C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 6/img1-2/"+str(page1)+"/"+str(page2)+"-"+str(x)+".jpg"
        imageurl = "http://" + imageurl
        #request=urllib.request.Request(imageurl,headers=header)
        try:
            #response=urllib.request.urlopen(request)
            urllib.request.urlretrieve(imageurl, filename=imagename)
            #response.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
        time.sleep(0.1)


for i in range(18062,18350):
    folder = os.path.exists('C:\\Users\\leishen\\Documents\\anaconda3\\scrapy\\master python scrapy\\chapter 6\\img1-2'+'\\'+str(i))
    if not folder:
        os.mkdir('C:\\Users\\leishen\\Documents\\anaconda3\\scrapy\\master python scrapy\\chapter 6\\img1-2' + '\\' + str(i))
    for j in range(1,6):
        url="http://www.lesmao.me/thread-"+str(i)+"-"+str(j)+"-1.html"
        craw(url,i,j)


'''测试存储图片功能模块
imagename="C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 6/img1/1.jpg"
imageurl="http:"+"//img11.360buyimg.com/n7/jfs/t18100/103/2653814757/84497/3eaae60e/5b0375d9N6ff9ee7e.jpg"
try:
    urllib.request.urlretrieve(imageurl,filename=imagename)
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
'''