#�ھ���
#9.3 ����ץȡʵս
#��1��
import urllib.request
import http.cookiejar
import re
#��Ƶ���
vid="1472528692"
#�տ�ʼʱ�������ID
comid="6173403130078248384"
url= "http://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&reqnum=20"
headers={ "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Encoding":" gb2312,utf-8",
                        "Accept-Language":" zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
                        "Connection": "keep-alive",
                        "referer":"qq.com"}
cjar=http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
#����һ���Զ��庯��craw(vid,comid),ʵ���Զ�ץȡ��Ӧ������ҳ������ץȡ����
def craw(vid,comid):
    url= "http://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&reqnum=20"
    data=urllib.request.urlopen(url).read().decode("utf-8")
    return data
idpat='"id":"(.*?)"'
userpat='"nick":"(.*?)",'
conpat='"content":"(.*?)",'
#��һ��ѭ��������ץȡ����ҳ��ÿһ�����ѭ��ץȡһҳ
for i in range(1,10):
    print("------------------------------------")
    print("��"+str(i)+"ҳ��������")
    data=craw(vid,comid)
    #�ڶ���ѭ��������ץȡ�Ľ����ȡ������ÿ�����۵���Ϣ��һҳ20������
    for j in range(0,20):
        idlist=re.compile(idpat,re.S).findall(data)
        userlist=re.compile(userpat,re.S).findall(data)
        conlist=re.compile(conpat,re.S).findall(data)
        print("�û����� :"+eval('u"'+userlist[j]+'"'))
        print("����������:"+eval('u"'+conlist[j]+'"'))
        print("\n")
    #��comid�ı�Ϊ��ҳ�����һ������id��ʵ�ֲ����Զ�����
    comid=idlist[19]


