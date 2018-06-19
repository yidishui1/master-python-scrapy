# coding=utf-8
import threading
import queue
import re
import urllib.request
import time
import urllib.error
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk') #改变标准输出的默认编码

urlqueue=queue.Queue()
#模拟成浏览器
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#将opener安装为全局
urllib.request.install_opener(opener)
listurl=[]
 #使用代理服务器的函数
def use_proxy(proxy_addr,url):
    try:
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
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)
#线程1，专门获取对应网址并处理为真实网址
class geturl(threading.Thread):
    def __init__(self,key,pagestart,pageend,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.pagestart=pagestart
        self.pageend=pageend
        self.proxy=proxy
        self.urlqueue=urlqueue
        self.key=key
    def run(self):
        page=self.pagestart
        #编码关键词key
        keycode=urllib.request.quote(key)
        #编码"&page"
        #pagecode=urllib.request.quote("&page")
        for page in range(self.pagestart,self.pageend+1):
            page=(page-1)*10
            url="https://zhidao.baidu.com/search?word="+keycode+"&ie=gbk&site=-1&sites=0&date=0&pn="+str(page)
            #用代理服务器爬，解决IP被封杀问题
            data1=use_proxy(self.proxy,url)
            #列表页url正则
            listurlpat='<dl class="dl.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        #便于调试
        print("获取到"+str(len(listurl))+"页")
        for i in range(0,len(listurl)):
            #等一等线程2，合理分配资源
            time.sleep(7)
            for j in range(0,len(listurl[i])):
                try:
                    url=listurl[i][j]
                    #处理成真实url，读者亦可以观察对应网址的关系自行分析，采集网址比真实网址多了一串amp
                    url=url.replace("http","https")
                    print("第"+str(i)+"i"+str(j)+"j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
                except urllib.error.URLError as e:
                    if hasattr(e,"code"):
                        print(e.code)
                    if hasattr(e,"reason"):
                        print(e.reason)
                    time.sleep(10)
                except Exception as e:
                    print("exception:"+str(e))
                    time.sleep(1)
#线程2，与线程1并行执行，从线程1提供的文章网址中依次爬取对应文章信息并处理
class getcontent(threading.Thread):
    def __init__(self,urlqueue,proxy):
        threading.Thread.__init__(self)
        self.urlqueue=urlqueue
        self.proxy=proxy
    def run(self):
        html1='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>百度知道</title>
        </head>
        <body>'''
        fh=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 6/zhidao1.html","wb")
        fh.write(html1.encode("utf-8"))
        fh.close()
        fh=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 6/zhidao1.html","ab")
        i=1
        while(True):
            try:
                url=self.urlqueue.get()
                data=use_proxy(self.proxy,url)
                titlepat='<span class="ask-title ">(.*?)</span>'
                contentpat='<pre id="best-content.*?>(.*?)</pre>'
                title=re.compile(titlepat).findall(data)
                content=re.compile(contentpat,re.S).findall(data)
                thistitle="此次没有获取到"
                thiscontent="此次没有获取到"
                if(title!=[]):
                     thistitle=title[0]
                if(content!=[]):
                      thiscontent=content[0]
                dataall="<p>标题为:"+thistitle+"</p><p>内容为:"+thiscontent+"</p><br>"
                fh.write(dataall.encode("utf-8"))
                print("第"+str(i)+"个网页处理") #便于调试
                i+=1
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
                time.sleep(10)
            except Exception as e:
                print("exception:"+str(e))
                time.sleep(1)
        fh.close()
        html2='''</body>
        </html>
        '''
        fh=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 6/zhidao1.html","ab")
        fh.write(html2.encode("utf-8"))
        fh.close()
#并行控制程序，若60秒未响应，并且存url的队列已空，则判断为执行成功
class conrl(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue=urlqueue
    def run(self):
        while(True):
            print("程序执行中")
            time.sleep(60)
            if(self.urlqueue.empty()):
                print("程序执行完毕！")
                exit()
key="算法"
proxy="117.63.78.161:6666"
proxy2=""
pagestart=1#起始页
pageend=10#抓取到哪页
#创建线程1对象，随后启动线程1
t1=geturl(key,pagestart,pageend,proxy,urlqueue)
t1.start()
#创建线程2对象，随后启动线程2
t2=getcontent(urlqueue,proxy)
t2.start()
#创建线程3对象，随后启动线程3
t3=conrl(urlqueue)
t3.start()



