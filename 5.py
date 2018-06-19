# -*- coding: utf-8 -*-

#1 普通字符作为原子
import re
pattern="yue" #普通字符作为原子
string="http://yum.iqianyue.com"
result1=re.search(pattern,string)
print(result1)

#2 非打印字符作为原子
import re
pattern="\n"
string='''http://yum.iqianyue.com
http://baidu.com'''
result1=re.search(pattern,string)
print(result1)

#全局匹配函数
import re
string="hellomypythonhispythonourpythonend"
pattern=re.compile(".python.")#预编译
result=pattern.findall(string)#找出符合模式的所有结果
print(result)

#re.sub()函数
import re
string="hellomypythonhispythonourpythonend"
pattern="python"#预编译
result1=re.sub(pattern,"php",string)#全部替换
result2=re.sub(pattern,"php",string,2)#最多替换两次
print(result1)
print(result2)

#5.6 Cookiejar实战精析 未进行Cookie处理
import urllib.request
import urllib.parse
url="http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LQ6tg"
postdata=urllib.parse.urlencode({
    "username":"yujyue",
    "password":"112358ab"
}).encode('utf-8')#使 用 urlencode编 码 处 理 后 ， 再 设 置 为 utf-8编 码 #
req=urllib.request.Request(url,postdata)#构 建 Request对 象
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
data=urllib.request.urlopen(req).read()#登 录 并 爬 取 对 应 网 页
fhandle=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 5/1.html","wb")
fhandle.write(data)#将 内 容 写 入 对 应 文 件
fhandle.close()
url2="http://bbs.chinaunix.net/"#设 置 要 爬 取 的 该 网 站 下 其 他 网 页 地 址
req2=urllib.request.Request(url2,postdata)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
data2=urllib.request.urlopen(req2).read()#爬 取 该 站 下 的 其 他 网 页
fhandle=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 5/2.html","wb")
fhandle.write(data2)#将 爬 取 到 的 其 他 网 页 写 入 对 应 文 件
fhandle.close()


#5.6 Cookiejar实战精析 进行Cookie处理

import urllib.request
import urllib.parse
import http.cookiejar

url="http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LQ6tg"
postdata=urllib.parse.urlencode({
    "username":"yujyue",
    "password":"112358ab"
}).encode('utf-8')#使 用 urlencode编 码 处 理 后 ， 再 设 置 为 utf-8编 码 #
req=urllib.request.Request(url,postdata)#构 建 Request对 象
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
#使 用 http.cookiejar.CookieJar()创 建 CookieJar对 象
cjar=http.cookiejar.CookieJar()
#使 用 HTTPCookieProcessor创 建 cookie处 理 器 ， 并 以 其 为 参 数 构 建 opener对 象
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#将opener安 装 为 全 局
urllib.request.install_opener(opener)
file=opener.open(req)
data=file.read()
file=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 5/3.html","wb")
file.write(data)
file.close()
url2="http://bbs.chinaunix.net/"#设 置 要 爬 取 的 该 网 站 下 其 他 网 页 地 址
req2=urllib.request.Request(url2,postdata)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
data2=urllib.request.urlopen(req2).read()#爬 取 该 站 下 的 其 他 网 页
#data2=urllib.request.urlopen(url2).read()
fhandle=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 5/4.html","wb")
fhandle.write(data2)
fhandle.close()

#5.6 Cookiejar实战精析 进行Cookie处理 51job拓展失败

import urllib.request
import urllib.parse
import http.cookiejar

url="https://i.51job.com/userset/ajax/whoviewme.php"
postdata=urllib.parse.urlencode({
    "loginname":"yujyue",
    "password":"112358@job"
}).encode('utf-8')#使 用 urlencode编 码 处 理 后 ， 再 设 置 为 utf-8编 码 #
req=urllib.request.Request(url,postdata)#构 建 Request对 象
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
#使 用 http.cookiejar.CookieJar()创 建 CookieJar对 象
cjar=http.cookiejar.CookieJar()
#使 用 HTTPCookieProcessor创 建 cookie处 理 器 ， 并 以 其 为 参 数 构 建 opener对 象
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#将opener安 装 为 全 局
urllib.request.install_opener(opener)
file=opener.open(req)
data=file.read()
file=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 5/5.html","wb")
file.write(data)
file.close()
url2="https://www.51job.com/"#设 置 要 爬 取 的 该 网 站 下 其 他 网 页 地 址
req2=urllib.request.Request(url2,postdata)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
data2=urllib.request.urlopen(req2).read()#爬 取 该 站 下 的 其 他 网 页
#data2=urllib.request.urlopen(url2).read()
fhandle=open("C:/Users/leishen/Documents/anaconda3/scrapy/master python scrapy/chapter 5/6.html","wb")
fhandle.write(data2)
fhandle.close()