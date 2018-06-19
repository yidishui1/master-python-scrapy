# coding=utf-8
#(2)关键字为中文时解码操作
import urllib.request
key="算法"
key_code=urllib.request.quote(key)
print(key_code)