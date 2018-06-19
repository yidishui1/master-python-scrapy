# coding=utf-8
import urllib.request
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk') #改变标准输出的默认编码
#4.6  瞒天过海之代理服务器的设置
#(1)
def use_proxy(proxy_addr,url):
    proxy= urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('gbk')
    return data
proxy_addr="117.66.167.176:8118"
data=use_proxy(proxy_addr,"https://zhidao.baidu.com/question/81775125.html?fr=iks&word=%E7%AE%97%E6%B3%95&ie=gbk")
print(data)
print(len(data))