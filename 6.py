#������
#6.1 ��Python�����ʵ��
#(1)
<img width="220" height="220" data-img="1" data-lazy-img="//img12.360buyimg.com/n7/jfs/t2437/118/775474476/74776/4087862f/562616d9Nc17cd80a.jpg">
ͼƬ2��Ӧ���룺
<img width="220" height="220" data-img="1" data-lazy-img="//img10.360buyimg.com/n7/jfs/t2230/83/2893465811/162158/80a547ef/56fa0f30N7794db4a.jpg">

#(2)
import re
import urllib.request
def craw(url,page):
    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    pat1='<div id="plist".+? <div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]
    pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imagelist:
        imagename="D:/Python35/myweb/part6/img1/"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1

#6.2 ץȡҳ������ʵս
#(1)
#ץȡҳ������
import re
import urllib.request
def getlink(url):
    #ģ��������
    headers=("User-Agent"," Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #��opener��װΪȫ��
    urllib.request.install_opener(opener)
    file=urllib.request.urlopen(url)
    data=str(file.read())
    #�������󹹽������ӱ��ʽ
    pat='(https?://[^\s)";]+\.(\w|/)*)' 
    link=re.compile(pat).findall(data)
    #ȥ���ظ�Ԫ��
    link=list(set(link))
    return link
#Ҫ��ȡ����ҳ����
url="http://blog.csdn.net/"
#��ȡ��Ӧ��ҳ�а��������ӵ�ַ
linklist=getlink(url)
#ͨ��forѭ���ֱ���������ȡ�������ӵ�ַ����Ļ��
for link in linklist:
    print(link[0])
    
#(2)
import urllib.request
import re
def getcontent(url,page):
    #ģ��������
    headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #��opener��װΪȫ��
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    #������Ӧ�û���ȡ��������ʽ
    userpat='target="_blank" title="(.*?)">'
    #��������������ȡ��������ʽ
    contentpat='<div class="content">(.*?)</div>'
    #Ѱ�ҳ����е��û�
    userlist=re.compile(userpat,re.S).findall(data)
    #Ѱ�ҳ����е�����
    contentlist=re.compile(contentpat,re.S).findall(data)
    x=1
    #ͨ��forѭ�������������ݲ������ݷֱ𸳸���Ӧ�ı���
    for content in contentlist:
        content=content.replace("\n","")
        #���ַ�����Ϊ���������Ƚ���Ӧ�ַ�������һ������
        name="content"+str(x)
         #ͨ��exec()����ʵ�����ַ�����Ϊ����������ֵ
        exec(name+'=content')
        x+=1
    y=1
    #ͨ��forѭ�������û�����������û���Ӧ������
    for user in userlist:
        name="content"+str(y)
        print("�û�"+str(page)+str(y)+"��:"+user)
        print("������:")
        exec("print("+name+")")
        print("\n")
        y+=1
#�ֱ��ȡ��ҳ�Ķ��ӣ�ͨ��forѭ�����Ի�ȡ��ҳ
for i in range(1,30):
    url="http://www.qiushibaike.com/8hr/page/"+str(i)
    getcontent(url,i)

#6.4 ΢������ʵս
#(1)
import re
import urllib.request
import time
import urllib.error
#ģ��������
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#��opener��װΪȫ��
urllib.request.install_opener(opener)
#����һ���б�listurl�洢������ַ�б�
listurl=[]
#�Զ��庯��������Ϊʹ�ô��������
def use_proxy(proxy_addr,url):
    #�����쳣�������
    try:
        import urllib.request
        proxy= urllib.request.ProxyHandler({'http':proxy_addr})  
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #��ΪURLError�쳣����ʱ10��ִ��
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #��ΪException�쳣����ʱ1��ִ��
        time.sleep(1)
#��ȡ������������
def getlisturl(key,pagestart,pageend,proxy):
    try:
        page=pagestart
        #����ؼ���key
        keycode=urllib.request.quote(key)
        #����"&page"
        pagecode=urllib.request.quote("&page")
        #ѭ����ȡ��ҳ����������
        for page in range(pagestart,pageend+1):
            #�ֱ𹹽���ҳ��url���ӣ�ÿ��ѭ������һ��
            url="http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            #�ô���������������IP����ɱ����
            data1=use_proxy(proxy,url)
            #��ȡ�������ӵ�������ʽ
            listurlpat='<div class="txt-box">.*?(http://.*?)"'
            #��ȡÿҳ�������������Ӳ���ӵ��б�listurl��
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print("����ȡ��"+str(len(listurl))+"ҳ") #���ڵ���
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #��ΪURLError�쳣����ʱ10��ִ��
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #��ΪException�쳣����ʱ1��ִ��
        time.sleep(1)
#ͨ���������ӻ�ȡ��Ӧ����
def getcontent(listurl,proxy):
    i=0
    #���ñ����ļ��еĿ�ʼhtml����
    html1='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>΢������ҳ��</title>
    </head>
    <body>'''
    fh=open("D:/Python35/myweb/part6/1.html","wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    #�ٴ���׷��д��ķ�ʽ���ļ�����д���Ӧ��������
    fh=open("D:/Python35/myweb/part6/1.html","ab")
    #��ʱlisturlΪ��ά�б�����listurl[][],��һά�洢����Ϣ���ڼ�ҳ��أ��ڶ�ά��ĸ���ҳ�ڼ��������������
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url=listurl[i][j]
                #�������ʵurl����������Թ۲��Ӧ��ַ�Ĺ�ϵ���з������ɼ���ַ����ʵ��ַ����һ��amp
                url=url.replace("amp;","")
                #ʹ�ô���ȥ��ȡ��Ӧ��ַ������
                data=use_proxy(proxy,url)
                #���±���������ʽ
                titlepat="<title>(.*?)</title>"
                #��������������ʽ
                contentpat='id="js_content">(.*?)id="js_sg_bar"'
                #ͨ����Ӧ������ʽ�ҵ����Ⲣ�����б�title
                title=re.compile(titlepat).findall(data)
                #ͨ����Ӧ������ʽ�ҵ����ݲ������б�content
                content=re.compile(contentpat,re.S).findall(data)
                #��ʼ������������
                thistitle="�˴�û�л�ȡ��"
                thiscontent="�˴�û�л�ȡ��"
                #��������б�Ϊ�գ�˵���ҵ��˱��⣬ȡ�б�����Ԫ�أ����˴α��⸳������thistitle
                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]
                #�����������ݻ��ܸ�������dataall
                dataall="<p>����Ϊ:"+thistitle+"</p><p>����Ϊ:"+thiscontent+"</p><br>"
                #����ƪ���µı��������ݵ�����Ϣд���Ӧ�ļ�
                fh.write(dataall.encode("utf-8"))
                print("��"+str(i)+"����ҳ��"+str(j)+"�δ���") #���ڵ���
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
                #��ΪURLError�쳣����ʱ10��ִ��
                time.sleep(10)
            except Exception as e:
                print("exception:"+str(e))
                #��ΪException�쳣����ʱ1��ִ��
                time.sleep(1)
    fh.close()
    #���ò�д�뱾���ļ���html����������ִ���
    html2='''</body>
    </html>
    '''
    fh=open("D:/Python35/myweb/part6/1.html","ab")
    fh.write(html2.encode("utf-8"))
    fh.close()
#���ùؼ���            
key="������"
#���ô�����������ô���������п���ʧЧ��������Ҫ�����µ���Ч���������
proxy="119.6.136.122:80"
#����Ϊgetlisturl()��getcontent()���ò�ͬ�Ĵ�����������˴�û�����ø�������
proxy2=""
#��ʼҳ
pagestart=1
#ץȡ����ҳ
pageend=2
listurl=getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy)

#6.6 ���߳�����ʵս
#(1)
#���̻߳���
import threading
class A(threading.Thread):
    def __init__(self):
        #��ʼ�����߳�
        threading.Thread.__init__(self)
    def run(self):
        #���߳�Ҫִ�еĳ�������
        for i in range(10):
            print("�����߳�A")
class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("�����߳�B")
#ʵ�����߳�AΪt1
t1=A()
#�����߳�t1
t1.start()
#ʵ�����߳�BΪt2
t2=B()
#�����߳�t2����ʱ��t1ͬʱִ��
t2.start()

#(2)
import threading
import queue
import re
import urllib.request
import time
import urllib.error

urlqueue=queue.Queue()
#ģ��������
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#��opener��װΪȫ��
urllib.request.install_opener(opener)
listurl=[]
 #ʹ�ô���������ĺ���
def use_proxy(proxy_addr,url): 
    try:
        proxy= urllib.request.ProxyHandler({'http':proxy_addr})  
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
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
#�߳�1��ר�Ż�ȡ��Ӧ��ַ������Ϊ��ʵ��ַ
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
        #����ؼ���key
        keycode=urllib.request.quote(key)
        #����"&page"
        pagecode=urllib.request.quote("&page")
        for page in range(self.pagestart,self.pageend+1):
            url="http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            #�ô���������������IP����ɱ����
            data1=use_proxy(self.proxy,url)
            #�б�ҳurl����
            listurlpat='<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        #���ڵ���
        print("��ȡ��"+str(len(listurl))+"ҳ") 
        for i in range(0,len(listurl)):
            #��һ���߳�2�����������Դ
            time.sleep(7)
            for j in range(0,len(listurl[i])):
                try:
                    url=listurl[i][j]
                    #�������ʵurl����������Թ۲��Ӧ��ַ�Ĺ�ϵ���з������ɼ���ַ����ʵ��ַ����һ��amp
                    url=url.replace("amp;","")
                    print("��"+str(i)+"i"+str(j)+"j�����")
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
#�߳�2�����߳�1����ִ�У����߳�1�ṩ��������ַ��������ȡ��Ӧ������Ϣ������
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
        <title>΢������ҳ��</title>
        </head>
        <body>'''
        fh=open("D:/Python35/myweb/part6/2.html","wb")
        fh.write(html1.encode("utf-8"))
        fh.close()
        fh=open("D:/Python35/myweb/part6/2.html","ab")
        i=1
        while(True):
            try:
                url=self.urlqueue.get()
                data=use_proxy(self.proxy,url)
                titlepat="<title>(.*?)</title>"
                contentpat='id="js_content">(.*?)id="js_sg_bar"'
                title=re.compile(titlepat).findall(data)
                content=re.compile(contentpat,re.S).findall(data)
                thistitle="�˴�û�л�ȡ��"
                thiscontent="�˴�û�л�ȡ��"
                if(title!=[]):
                     thistitle=title[0]
                if(content!=[]):
                      thiscontent=content[0]
                dataall="<p>����Ϊ:"+thistitle+"</p><p>����Ϊ:"+thiscontent+"</p><br>"
                fh.write(dataall.encode("utf-8"))
                print("��"+str(i)+"����ҳ����") #���ڵ���
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
        fh=open("D:/Python35/myweb/part6/2.html","ab")
        fh.write(html2.encode("utf-8"))
        fh.close()
#���п��Ƴ�����60��δ��Ӧ�����Ҵ�url�Ķ����ѿգ����ж�Ϊִ�гɹ�
class conrl(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue=urlqueue
    def run(self):
        while(True):
            print("����ִ����")
            time.sleep(60)
            if(self.urlqueue.empty()):
                print("����ִ����ϣ�")
                exit()
key="�˹�����"
proxy="119.6.136.122:80"
proxy2=""
pagestart=1#��ʼҳ
pageend=2#ץȡ����ҳ
#�����߳�1������������߳�1
t1=geturl(key,pagestart,pageend,proxy,urlqueue)
t1.start()
#�����߳�2������������߳�2
t2=getcontent(urlqueue,proxy)
t2.start()
#�����߳�3������������߳�3
t3=conrl(urlqueue)
t3.start()



for i in range(1,79):
    url="http://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)

#(3)
