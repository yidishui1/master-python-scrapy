# coding=utf-8
#6.4 百度知道爬虫
#(1)

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk') #改变标准输出的默认编码

import re
import urllib.request
import time
import urllib.error
#模拟成浏览器
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#将opener安装为全局
urllib.request.install_opener(opener)
#设置一个列表listurl存储文章网址列表
listurl=[]
#自定义函数，功能为使用代理服务器
def use_proxy(proxy_addr,url):
    #建立异常处理机制
    try:
        import urllib.request
        proxy= urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('gbk')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #若为URLError异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)
#获取所有文章链接
def getlisturl(key,pagestart,pageend,proxy):
    try:
        page=pagestart
        #编码关键词key
        keycode=urllib.request.quote(key)
        #编码"&page"
        #pagecode1=urllib.request.quote("&_sug_type_=&s_from=input&_sug_=y&type=2&page=")
        #pagecode2=urllib.request.quote("&ie=utf8")
        #循环爬取各页的文章链接
        for page in range(pagestart,pageend+1):
            #分别构建各页的url链接，每次循环构建一次
            #url="http://weixin.sogou.com/weixin?query="+keycode+pagecode1+str(page)+pagecode2 #这个地方貌似有问题
            #url = "http://weixin.sogou.com/weixin?query=" + keycode +"&_sug_type_=&s_from=input&_sug_=y&type=2&page="+ str(page) + "&ie=utf8"  # 这个地方貌似有问题
            page=(page-1)*10
            url="https://zhidao.baidu.com/search?word="+keycode+"&ie=gbk&site=-1&sites=0&date=0&pn="+str(page)
            print(url)

            #用代理服务器爬，解决IP被封杀问题
            data1=use_proxy(proxy,url)
            #print(data1)

            #获取文章链接的正则表达式
            listurlpat='<dl class="dl.*?(http://.*?)"'
            #获取每页的所有文章链接并添加到列表listurl中
            listurl.append(re.compile(listurlpat,re.S).findall(data1))

        #print(listurl)
        print("共获取到"+str(len(listurl))+"页") #便于调试
       
        return listurl

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #若为URLError异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)
#通过文章链接获取对应内容
def getcontent(listurl,proxy):
    i=0
    #设置本地文件中的开始html编码
    html1='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>百度知道</title>
    </head>
    <body>'''
    fh=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 6/zhidao.html","wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    #再次以追加写入的方式打开文件，以写入对应文章内容
    fh=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 6/zhidao.html","ab")
    #此时listurl为二维列表，形如listurl[][],第一维存储的信息跟第几页相关，第二维存的跟该页第几个文章链接相关
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url=listurl[i][j]
                #处理成真实url，读者亦可以观察对应网址的关系自行分析，采集网址比真实网址多了一串amp
                url=url.replace("http","https")
                #使用代理去爬取对应网址的内容
                data=use_proxy(proxy,url)
                #文章标题正则表达式
                titlepat='<span class="ask-title ">(.*?)</span>'
                #文章内容正则表达式
                contentpat='<pre id="best-content.*?>(.*?)</pre>'
                #通过对应正则表达式找到标题并赋给列表title
                title=re.compile(titlepat).findall(data)
                #通过对应正则表达式找到内容并赋给列表content
                content=re.compile(contentpat,re.S).findall(data)
                #初始化标题与内容
                thistitle="此次没有获取到"
                thiscontent="此次没有获取到"
                #如果标题列表不为空，说明找到了标题，取列表第零个元素，即此次标题赋给变量thistitle
                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]
                #将标题与内容汇总赋给变量dataall
                dataall="<p>标题为:"+thistitle+"</p><p>内容为:"+thiscontent+"</p><br>"
                #将该篇文章的标题与内容的总信息写入对应文件
                fh.write(dataall.encode("utf-8"))
                print("第"+str(i)+"个网页第"+str(j)+"次处理") #便于调试
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
                #若为URLError异常，延时10秒执行
                time.sleep(10)
            except Exception as e:
                print("exception:"+str(e))
                #若为Exception异常，延时1秒执行
                time.sleep(1)
    fh.close()
    #设置并写入本地文件的html后面结束部分代码
    html2='''</body>
    </html>
    '''
    fh=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 6/zhidao.html","ab")
    fh.write(html2.encode("utf-8"))
    fh.close()
#设置关键词
key="算法"
#设置代理服务器，该代理服务器有可能失效，读者需要换成新的有效代理服务器
proxy="117.63.78.161:6666"
#可以为getlisturl()与getcontent()设置不同的代理服务器，此处没有启用该项设置
proxy2=""
#起始页
pagestart=1
#抓取到哪页
pageend=10
listurl=getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy)